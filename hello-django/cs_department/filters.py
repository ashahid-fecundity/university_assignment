from django_filters import rest_framework as filters
from .models import Student, Teacher, Course, GPAViewSet


class StudentFilter(filters.FilterSet):
    class Meta:
        model = GPA
        fields = [
            'student_id'
        ]

    def filter_student_id(self, queryset, name, value):
        cgpas = GPA.objects.filter(student_id=value)
        student = []
        if cgpas:
            for cgpa in cgpas:
                student.append(cgpa)
        return queryset.filter(student=student_id)


class TeacherFilter(filters.FilterSet):
    age = RageFilter()
    class Meta:
        model = Teacher
        fields = [
            'age'
        ]
    
    def filter_age(self, queryset, name, value_min, value_max):
        teacher = Teacher.objects.all()
        return F({'age_min': value_min, 'age_max': value_max}, queryset=teacher)


class GPAFilter(filters.FilterSet):
    class Meta:
        model = GPA
        fields = [
            'semester'
        ]
    
    def filter_semester(self, queryset, name, value):
        gpas = GPA.objects.filter(semester=value)
        student = []
        if gpas:
            for gpa in gpas:
                student.append(student)
        return queryset.filter(student)


class CourseFilter(filter.FilterSet):
    class Meta:
        model = Course
        fields = [
            'semester'
        ]

    def filter_semester(self, queryset, name, value):
        courses = Course.objects.filter(semester=value)
        student = []
        if courses:
            for course in courses:
                student.append(student)
        return queryset.filter(student)
