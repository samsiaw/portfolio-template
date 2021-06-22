from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class Owner(AbstractUser):
    """
    Owner For Projects. 
    Whiles it's possible to have multiple users and multiple projects linked
    to different users, it's advisable to keep only one user in the database.

    The porfolio website is built with the assumption of only one user in the db.

    :short_descr - Information about user shown on the homepage
    
    """
    username = models.CharField(max_length=20, blank=False, unique=True, null=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, unique=False, blank=False, null=False)
    last_name = models.CharField(max_length=50, unique=False, blank=True, null=False)
    about = models.TextField(blank=True, unique=False, null=False)
    short_descr = models.TextField(blank=True, unique=False, null=False)
    img_src = models.URLField(blank=True, unique=False)

    # Social Media Links
    github_link = models.URLField(unique=True, blank=True)
    linkedin_link = models.URLField(unique=True, blank=True)
    instagram_link = models.URLField(unique=True, blank=True)
    twitter_link = models.URLField(unique=True, blank=True)
    facebook_link = models.URLField(unique=True, blank=True)

    def get_owner_info(self):
        return {
            "username" : self.username,
            "email" : self.email,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "short_descr" : self.short_descr,
            "about" : self.about,
            
            "github_link" : self.github_link,
            "linkedin_link" : self.linkedin_link,
            "instagram_link" : self.instagram_link,
            "twitter_link" : self.twitter_link,
            "facebook_link" : self.facebook_link,
            
        }

    # def get_about_info(self):
    #     return {
    #         "about" : self.about,
    #         "img_src": self.img_src
    #     }
        
class Tool(models.Model):
    """
    Progamming Languages / Tools Used In The Project
    """

    name = models.CharField(max_length=20, blank=False, unique=True, null=False)
    #icon_src = models.URLField(blank=True, unique=False)
    
    def get_li(self):
        """
        Get the li HTML element string form of the tool.
        Used in templates fields that have been autoescaped (or which uses the <pre> tag)
        """
        return f"<li> {self.name.capitalize()} </li>"

    def __str__(self):
        return self.name.capitalize()
    

class Concept(models.Model):
    """
    Concepts involved in the project
    """
    name = models.CharField( max_length=100, blank=False, unique=True, null=False)

    def get_li(self):
        """
        Get the li HTML element string form of the Concept.
        Used in templates fields that have been autoescaped (or which uses the <pre> tag)
        """
        return f"<li> {self.name.capitalize()} </li>"

    def __str__(self):
        return self.name.capitalize()


class Project(models.Model):
    """
    Stores project information

    :show - determines whether to display the current project or not
        [Typically useful when user is not done with project documentation]
    
    Note:
        If using the default django templates/front-end provided, the Text fields for the project have 
    been enclosed in <pre> tags. Hence, user can insert html code as part of the string and have it 
    formatted. <pre> tags are also sensitive to line breaks in the text provided. 
    """
    name = models.CharField(max_length=60, blank=False, null=False)

    github_link = models.URLField(unique=False, blank=True)
    external_link = models.URLField(unique=False, blank=True) # Any external link for the project

    short_descr = models.TextField(max_length=100, blank=True)
    long_descr = models.TextField(blank=True)
    reflection = models.TextField(blank=True)

    owner = models.ForeignKey(Owner, null=False, on_delete=models.CASCADE, related_name="projects")
    languages = models.ManyToManyField(Tool, blank=True)
    concepts = models.ManyToManyField(Concept, blank=True)

    featured = models.BooleanField(default=False)
    show    = models.BooleanField(default=False)

    def __str__(self):
        return "Project: "+self.name

    def get_absolute_url(self):
        return reverse("projects", kwargs={"project_id": self.id})
    
    def get_project_info_v(self): # Get project info [verbose]
        all_langs = [lang.name for lang in self.languages.all()]
        concepts = [c.name for c in self.concepts.all()]
        return {
            "id" : self.id,
            "name" : self.name,
            "short_descr" : self.short_descr,
            "long_descr" : self.long_descr,
            "github_link" : self.github_link,
            "external_link" : self.external_link,
            "languages" : all_langs,
            "concepts"  : concepts,
            "reflection" : self.reflection,
            "featured" : self.featured,
            "show"      : self.show
        }


    def get_project_info(self): # Get project info [shortened version]
        all_langs = [lang.name for lang in self.languages.all()]
        return {
            "id" : self.id,
            "name" : self.name,
            "short_descr" : self.short_descr,
            "github_link" : self.github_link,
            "external_link" : self.external_link,
            "languages" : all_langs,
            "featured" : self.featured,
            "show"      : self.show
        }

