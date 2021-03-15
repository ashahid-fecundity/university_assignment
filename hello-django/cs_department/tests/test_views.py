from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .factories import (
    UserFactory, StudentFactory, TeacherFactory, CourseFactory, GPAFactory
)


class StudentViewSetTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(email='testuser@example.com')
        self.user.set_password('testpassword')
        self.user.save()
        self.client.login(email=self.user.email, password='testpassword')
        self.list_url = reverse('student-list')

    def get_detail_url(self, student_id):
        return reverse(self.student-detail, kwargs={'student_id': student_id})

    def test_get_list(self):
        students = [StudentFactory() for i in range(0, 3)]

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(student['student_id'] for student in response.data['results']),
            set(student.id for student in students)
        )

    def test_get_detail(self):
        student = StudentFactory()
        response = self.client.get(self.get_detail_url(student.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], student.name)

    def test_post(self):
        data = {
            'name': 'New name',
            'age': 'New age',
            'roll_number': 'L-07-0117',
            'semester': 1,
            'courses': 'courses',
            'cgpa': 4.0,
        }
        self.assertEqual(Student.objects.count(), 0)
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        student = Student.objects.all().first()
        for field_name in data.keys():
            self.assertEqual(getattr(student, field_name), data[field_name])

    def test_put(self):
        student = StudentFactory()
        data = {
            'name': 'New name',
            'age': 'New age',
            'roll_number': 'L-07-0117',
            'semester': 1,
            'courses': 'courses',
            'cgpa': 4.0,
        }
        response = self.client.put(
            self.get_detail_url(student.id),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        student.refresh_from_db()
        for field_name in data.keys():
              self.assertEqual(getattr(student, field_name), data[field_name])

    def test_patch(self):
        student = StudentFactory()
        data = {'name': 'New name'}
        response = self.client.patch(
            self.get_detail_url(student.id),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        student.refresh_from_db()
        self.assertEqual(student.name, data['name'])

    def test_delete(self):
        student = StudentFactory()
        response = self.client.delete(self.get_detail_url(student.id))
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED
                        )


class TeacherViewSetTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(email='testuser@example.com')
        self.user.set_password('testpassword')
        self.user.save()
        self.client.login(email=self.user.email, password='testpassword')
        self.list_url = reverse('teacher-list')

    def get_detail_url(self, teacher_id):
        return reverse(self.teacher-detail, kwargs={'teacher_id': teacher_id})

    def test_get_list(self):
        teachers = [TeacherFactor() for i in range(0, 3)]

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(teacher['teacher_id'] for teacher in response.data['results']),
            set(teacher.id for teacher in teachers)
        )

    def test_get_detail(self):
        teacher = TeacherFactory()
        response = self.client.get(self.get_detail_url(teacher.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], teacher.name)

    def test_post(self):
        data = {
            'name': 'New name',
            'age': 'New age',
            'joining_date': 14/2/2021,
            'courses': 'courses',
        }
        self.assertEqual(Teacher.objects.count(), 0)
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Teacher.objects.count(), 1)
        teacher = Teacher.objects.all().first()
        for field_name in data.keys():
            self.assertEqual(getattr(teacher, field_name), data[field_name])

    def test_put(self):
        teacher = TeacherFactory()
        data = { 
            'name': 'New name',
            'age': 'New age',
            'joining_date': 14/2/2021,
            'courses': 'courses',
        }
        response = self.client.put(
            self.get_detail_url(teacher.id),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        teacher.refresh_from_db()
        for field_name in data.keys():
              self.assertEqual(getattr(teacher, field_name), data[field_name])

    def test_patch(self):
        teacher = TeacherFactory()
        data = {'name': 'New name'}
        response = self.client.patch(
            self.get_detail_url(teacher.id),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        teacher.refresh_from_db()
        self.assertEqual(teacher.name, data['name'])

    def test_delete(self):
        teacher = TeacherFactory()
        response = self.client.delete(self.get_detail_url(teacher.id))
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED
                        )


class CourseViewSetTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(email='testuser@example.com')
        self.user.set_password('testpassword')
        self.user.save()
        self.client.login(email=self.user.email, password='testpassword')
        self.list_url = reverse('course-list')

    def get_detail_url(self, course_id):
        return reverse(self.course-detail, kwargs={'course_id': course_id})

    def test_get_list(self):
        courses = [CourseFactory() for i in range(0, 3)]

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(course['course_id'] for course in response.data['results']),
            set(course.id for course in courses)
        )

    def test_get_detail(self):
        course = CourseFactory()
        response = self.client.get(self.get_detail_url(course.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], course.name)

    def test_post(self):
        data = {
            'name': 'New name',
            'text_book_title': 'New title',
            'section': 'A',
        }
        self.assertEqual(Course.objects.count(), 0)
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        course = Course.objects.all().first()
        for field_name in data.keys():
            self.assertEqual(getattr(course, field_name), data[field_name])

    def test_put(self):
        course = CourseFactory()
        data = {
            'name': 'New name',
            'text_book_title': 'New title',
            'section': 'A',
        }
        response = self.client.put(
            self.get_detail_url(course.id),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        course.refresh_from_db()
        for field_name in data.keys():
              self.assertEqual(getattr(course, field_name), data[field_name])

    def test_patch(self):
        course = CourseFactory()
        data = {'name': 'New name'}
        response = self.client.patch(
            self.get_detail_url(course.id),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        course.refresh_from_db()
        self.assertEqual(course.name, data['name'])

    def test_delete(self):
        course = CourseFactory()
        response = self.client.delete(self.get_detail_url(course.id))
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED
                        )


class GPAViewSetTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(email='testuser@example.com')
        self.user.set_password('testpassword')
        self.user.save()
        self.client.login(email=self.user.email, password='testpassword')
        self.list_url = reverse('gpa-list')

    def get_detail_url(self, gpa_id):
        return reverse(self.gpa-detail, kwargs={'gpa_id': gpa_id})

    def test_get_list(self):
        gpas = [GPAFactory() for i in range(0, 3)]

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(gpa['gpa_id'] for gpa in response.data['results']),
            set(gpa.id for gpa in gpas)
        )

    def test_get_detail(self):
        gpa = GPAFactory()
        response = self.client.get(self.get_detail_url(gpa.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], gpa.name)

    def test_post(self):
        data = {
            'name': 'New name',
            'course': 'New course',
            'semester': 1,
            'grade': 4.0,
        }
        self.assertEqual(gpa.objects.count(), 0)
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(gpa.objects.count(), 1)
        gpa = gpa.objects.all().first()
        for field_name in data.keys():
            self.assertEqual(getattr(gpa, field_name), data[field_name])

    def test_put(self):
        gpa = GPAFactory()
        data = {
            'name': 'New name',
            'course': 'New course',
            'semester': 1,
            'grade': 4.0,
        }
        response = self.client.put(
            self.get_detail_url(gpa.id),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        gpa.refresh_from_db()
        for field_name in data.keys():
              self.assertEqual(getattr(gpa, field_name), data[field_name])

    def test_patch(self):
        gpa = GPAFactory()
        data = {'name': 'New name'}
        response = self.client.patch(
            self.get_detail_url(gpa.id),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        gpa.refresh_from_db()
        self.assertEqual(gpa.name, data['name'])

    def test_delete(self):
        gpa = GPAFactory()
        response = self.client.delete(self.get_detail_url(gpa.id))
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED
                        )
