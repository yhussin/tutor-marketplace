from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from main_app import views
from main_app.models import Student, Teacher, Lesson, Language

class HomeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create 4 languages
        languages = ['English', 'French', 'Chinese', 'Spanish']
        for language in languages:
            Language.objects.create(name=language)

        # create 4 teachers in each language
        names = ['Amanda A', 'Billy B', 'Cathy C', 'Derek D']
        for name in names:
            user = User.objects.create(username=name[0:3], password=name[0:3])
            user.teacher_set.create(full_name=name)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class StudentProfileViewTest(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create(username='test', password='test')
        user.student_set.create(full_name='Harry Potter')
        student = user.student_set.first()
        user.save()

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='test', password='test')
        response = self.client.get('/students/profile/1/')
        # check user is logged in
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='test', password='test')
        response = self.client.get(reverse('student_profile', kwargs={'student_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/students/profile/1/')

    def test_view_uses_correct_template(self):
        login = self.client.login(username='test', password='test')
        response = self.client.get(reverse('student_profile', kwargs={'student_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/profile.html')
            
    def test_view_redirects_to_login(self):
        response = self.client.get(reverse('student_profile', kwargs={'student_id': 1}))
        self.assertEqual(response.status_code, 302)

