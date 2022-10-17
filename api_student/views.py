from rest_framework.viewsets import ModelViewSet

from api_student.models import Student
from api_student.serializers import StudentSerializer


class StudentView(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
