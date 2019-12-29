from django.urls import path, include
from course import views

urlpatterns = [
    path('', views.do),
]