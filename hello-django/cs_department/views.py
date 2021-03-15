# from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import Student, Teacher, Course, GPA
from .serializers import (
    StudentSerializer, TeacherSerializer, CourseSerializer, GPASerializer
)
from .filters import StudentFilter, TeacherFilter, GPAFilter, CourseFilter


class StudentViewSet(GenericViewSet,
                     CreateModelMixin,
                     ListModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filterset_class = StudentFilter

class TeacherViewSet(GenericViewSet,
                     CreateModelMixin,
                     ListModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    filterset_class = TeacherFilter

class CourseViewSet(GenericViewSet,
                     CreateModelMixin,
                     ListModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filterset_class = CourseFilter

class GPAViewSet(GenericViewSet,
                     CreateModelMixin,
                     ListModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin):
    serializer_class = GPASerializer
    queryset = GPA.objects.all()
    filterset_class = GPAFilter

# def home(request):
#     return HttpResponse("Hello, Django!")
