from rest_framework.serializers import ModelSerializer

from .models import Student, Teacher, Course, GPA

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = (
            ???
        )

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            ???
        )

class GPASerializer(ModelSerializer):
    class Meta:
        model = GPA
        fields = (
            ???
        )

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = (
            ???
        )
