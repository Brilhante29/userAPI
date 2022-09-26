from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Users
from .serializers import UsersSerializer
# Create your views here.

class UsersListCreateAPIView(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    
class UsersRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
