from django.urls import path
from .views import Login, RegisterUser, logoutUser

urlpatterns = [
    path('login', Login.as_view(),  name='login'),
    path('register', RegisterUser, name='register'),
    path('logout', logoutUser, name='logout'),
]