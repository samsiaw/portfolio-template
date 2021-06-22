from django.test import TestCase
from django.urls import reverse,resolve
import portfolio.views as views

class TestUrls(TestCase):

    # Test url names against their expected view

    def test_projects(self):
        """Test view function for 'projects' path
        """
        url = reverse('projects')
        self.assertEquals(resolve(url).func, views.projects)

    def test_single_project(self):
        """Test view function for 'single_project'
        """
        url = reverse('single_project', args=[1])
        self.assertEquals(resolve(url).func, views.single_project)
    
    def test_home(self):
        """Test view function for 'home'
        """
        url = reverse('home')
        self.assertEquals(resolve(url).func, views.index)

    def test_error(self):
        """Test view function for 'error'
        """
        url = reverse('error')
        self.assertEquals(resolve(url).func, views.error)

