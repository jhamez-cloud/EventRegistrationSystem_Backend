from rest_framework.routers import DefaultRouter
from .api.viewsets import UserViewset
from .models import User

routers = DefaultRouter()
routers.register(r"user",UserViewset,basename='user')

urlpatterns = routers.urls