from adminsortable.models import SortableMixin
from django.db import models


class Course(SortableMixin):
    NAME = 'name'
    TEXT_BOOK_TITLE = 'text_book_title'
    SECTION = 'section'

    name = models.CharField(max_length=255)
    text_book_title = models.CharField(max_length=255)
    section = models.CharField(max_length=1)

    class Meta:
        ordering = ('name')

    def __str__(self):
        return self.name


class Teacher(SortableMixin):
    NAME = 'name'
    AGE = 'age'
    COURSES = 'courses'

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    courses = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name')

    def __str__(self):
        return self.name


class Student(SortableMixin):
    NAME = 'name'
    AGE = 'age'
    ROLLNUMBER = 'rollnumber'
    SEMESTER = 'semester'
    COURSES = 'courses'
    CGPA ='cgpa'

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    rollnumber = models.CharField(max_length=9, min_value=9)
    semester = models.IntegerField()
    courses = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    cgpa = models.ForeignKey(GPA, null=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ('rollnumber')

    def __str__(self):
        return self.name


class GPA(SortableMixin):
    STUDENT = 'student'
    COURSE = 'course'
    SEMESTER = 'semester'
    GRADE = 'grade'

    student = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    semester = models.IntegerField()
    grade = models.CharField(max_length=2)
