from django.urls import path
from .views import LoginAPI, RegisterApi

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('register/', RegisterApi.as_view()),
]