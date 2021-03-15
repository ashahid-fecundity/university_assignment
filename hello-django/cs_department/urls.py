from django.urls import path
from .views import StudentViewSet, TeacherViewSet, CourseViewSet, GPAViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, re_path


router = DefaultRouter()
router.register(student, StudentViewSet, base_name='student')
router.register(course, CourseViewSet, base_name='course')
router.register(teacher, Teacher, base_name='teacher')
router.register(gpa, GPAViewSet, base_name='gpa')

urlpatterns = [
    re_path('^', include(router.urls)),
]

# urlpatterns = [
#     path("", views.home, name="home"),
# ]