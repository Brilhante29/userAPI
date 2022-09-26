from django.urls import path
from .views import UsersListCreateAPIView, UsersRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api', UsersListCreateAPIView.as_view()),
    path('api/<int:pk>', UsersRetrieveUpdateDestroyAPIView.as_view()),
]
