from rest_framework import viewsets
import uuid
from datetime import datetime,timezone

class StandardViewset(viewsets.ModelViewSet):
    use_standard_viewset = True

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)

        if not getattr(self,'use_standard_viewset',False):
            return response
        
        if self._is_already_wrapped(response.data):
            return response
        
        if 200 <= response.status_code < 300:
            if isinstance(response.data,(dict,list)):
                response.data = {
                    "status": "success",
                    "data": response.data,
                    "meta":{
                        "request_id": str(uuid.uuid4()),
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "version": "1.0.0"
                    }
                }
        elif response.status_code >= 400:
            error_data = response.data

            if response.status_code == 400:
                response.data = {
                    "status": "error",
                    "error": "VALIDATION ERROR",
                    "errors": [{
                        "message": "Request Validation Failed",
                        "details": error_data
                    }]
                }
            if response.status_code == 401:
                response.data = {
                    "status": "error",
                    "error": "UNAUTHENTICATED",
                    "errors": [{
                        "message": "Missing or Invalid Token",
                        "details": error_data
                    }]
                }
            if response.status_code == 403:
                response.data = {
                    "status": "error",
                    "error": "FORBIDDEN",
                    "errors": [{
                        "message": "Authnticated But Insufficient Role",
                        "details": error_data
                    }]
                }
            if response.status_code == 404:
                response.data = {
                    "status": "error",
                    "error": "NOT FOUND",
                    "errors": [{
                        "message": "Resource Not Found",
                        "details": error_data
                    }]
                }
            if response.status_code == 500:
                response.data = {
                    "status": "error",
                    "error": "SERVER ERROR",
                    "errors": [{
                        "message": "Internal Server Error",
                        "details": error_data
                    }]
                }
        else:
            response.data = {
                "status": "error",
                "error": {"code":"NOT_FOUND","message":"Resource not found"},
            }
        
        return response
    
    def _is_already_wrapped(self,data):
        if isinstance(data,dict):
            return "status" in data and "data" in data and "meta" in data
        return False