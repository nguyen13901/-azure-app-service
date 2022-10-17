from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_student import views

router = DefaultRouter()
router.register(r'students', views.StudentView, basename='students')

urlpatterns = [
    path('', include(router.urls)),
]
