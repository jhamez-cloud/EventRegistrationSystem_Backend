from config.viewsets import StandardViewset
from user.serializers import UserSerializer
from user.models import User

class UserViewset(StandardViewset):
    queryset = User.objects.all()
    serializer_class = UserSerializer