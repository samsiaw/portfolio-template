from django.contrib import admin
from .models import Owner, Tool, Project, Concept

# Register your models here.
admin.site.register(Owner)
admin.site.register(Tool)
admin.site.register(Project)
admin.site.register(Concept)
