from factory import DjangoModelFactory, Faker,

from .models import Student, Teacher, Course, GPA


class StudentFactory(DjangoModelFactory):
    name = Faker('student_name')
    age = Faker('student_age')
    roll_number = Faker('student_roll_number')
    semester = Faker('student_semester')
    courses = Faker('student_courses')
    cgpa = Faker('student_cgpa')

    class Meta:
        model = Student


class TeacherFactory(DjangoModelFactory):
    name = Faker('teacher_name')
    age = Faker('teacher_age')
    joining_date = Faker('teacher_joining_date')
    courses = Faker('teacher_courses')

    class Meta:
        model = Teacher


class CourseFactory(DjangoModelFactory):
    name = Faker('course_name')
    text_book_title = Faker('course_text_book')
    section = Faker('course_section')

    class Meta:
        model = Course


class GPAFactory(DjangoModelFactory):
    student = Faker('student')
    course = Faker('course')
    semester = Faker('semester')
    grade = Faker('grade')

    class Meta:
        model = GPA
