from django.test import Client, TestCase
from django.urls import reverse, resolve
from portfolio.models import *
import portfolio.views as views

class TestViews(TestCase):
    """
    Test views behaviour for the portfolio app

    This class tests:
        Status of responses
        HTML template rendered for the request

    """

    testUserName = views.USERNAME
    

    def setUp(self):
        self.client = Client()
        self.projects_url = reverse('projects')
        self.home_url = reverse('home')
        self.error_url = reverse('error')
        self.create_dummy_projects()

    @classmethod
    def create_dummy_projects(cls):

        owner = Owner.objects.create(username=cls.testUserName, first_name="dj", last_name="test")
        owner.save()

        p = Project.objects.create(name="test_project", owner=owner, featured=True, show=True)
        p.save()
        
    def test_GET_home(self):

        response = self.client.get(self.home_url)
       
        self.assertEquals(response.status_code, 200) # Success
        self.assertTemplateUsed(response, "portfolio/index.html")
        

    def test_GET_all_projects(self):
        
        response = self.client.get(self.projects_url)

        self.assertEquals(response.status_code, 200) # Success
        self.assertTemplateUsed(response, "portfolio/projects.html")


    def test_GET_error(self):
        response = self.client.get(self.error_url)

        self.assertEquals(response.status_code, 404) # A not found status

        self.assertTemplateUsed(response, "portfolio/error.html")


    def test_PUT_all_projects(self):

        response = self.client.put(self.projects_url, {"dummy": True})

        self.assertNotEquals(response.status_code, 200) # Should not be succesful
        # self.assertTemplateUsed(response, "portfolio/error.html")
        