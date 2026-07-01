from config.viewsets import StandardViewset
from rest_framework.permissions import AllowAny
from user.serializers import UserSerializer
from user.models import User

class UserViewset(StandardViewset):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]