from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Project

class ProjectAPITests(APITestCase):
    def setUp(self):
        self.project_data = {
            'title': 'Test Project',
            'description': 'A test project description',
            'technology': 'Python'
        }
        self.project = Project.objects.create(**self.project_data)
        self.url = '/api/projects/'

    def test_create_project(self):
        data = {
            'title': 'New Project',
            'description': 'New description',
            'technology': 'Django'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 2)
        self.assertEqual(Project.objects.latest('id').title, 'New Project')

    def test_get_projects_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_project_detail(self):
        response = self.client.get(f'{self.url}{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.project_data['title'])

    def test_update_project(self):
        updated_data = {
            'title': 'Updated Project',
            'description': 'Updated description',
            'technology': 'React'
        }
        response = self.client.put(f'{self.url}{self.project.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, 'Updated Project')

    def test_delete_project(self):
        response = self.client.delete(f'{self.url}{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Project.objects.count(), 0)
