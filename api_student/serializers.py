from rest_framework.serializers import ModelSerializer
from api_student.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
