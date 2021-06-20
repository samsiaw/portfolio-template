from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_GET
from .models import Owner, Project

# Constants
USERNAME = "testuser" # Username to which projects are registered.
# This would typically be the user name for the superuser created

@require_GET
def index(request):
    """
    Renders the home / landing page of the website

    Args:
        request (HttpRequest)

    Returns:
        [HttpResponse]
    """
    context = {}
    try:
        user = Owner.objects.get(username=USERNAME)
        context = user.get_owner_info()
        
    except Exception as e:
        if "error" in request.session:
            del request.session["error"]

        request.session["error"] = {'code': 500, 'message': "Internal Server Error"}
        return HttpResponseRedirect(reverse("error"))


    return render(request, "portfolio/index.html", context={"user": context})


# Projects Page [Projects Listing]
@require_GET
def projects(request):
    """
    Renders the projects page (listing all projects)

    Args:
        request (HttpRequest)

    Returns:
        [HttpResponse]
    """
    response = {}

    
    try:
        user = Owner.objects.get(username=USERNAME)
        # Get all projects of current user
        allProjects = user.projects.all()
        print("Got all projects")
        response["projects"] = []
        response["featured"] = []

        for project in allProjects:
            if project.show:
                if project.featured:
                    response["featured"].append(project.get_project_info())

                else:
                    response["projects"].append(project.get_project_info()) # Other projects [non-featured]

    except Exception as e:
        if 'error' in request.session:
            del request.session['error']

        request.session["error"] = {'code': 500, 'message': "Internal Server Error"}
        return HttpResponseRedirect(reverse("error"))
    
    #return JsonResponse(response)
    return render(request, "portfolio/projects.html", context=response)


@require_GET
def single_project(request, project_id):
    """
    Renders the single_project page with the project_id provided

    Args:
        request ([HttpRequest])
        project_id ([int])

    Returns:
        [HttpResponse]
    """

    response = {}

    try:
        project = Project.objects.get(id=project_id)
        response["project"] = project.get_project_info_v()

    except Exception as e:
        if 'error' in request.session:
            del request.session['error']
            
        return HttpResponseRedirect(reverse("error"))


    #return JsonResponse(response)
    return render(request, "portfolio/single_project.html", context=response)


def error(request):
    """
    Display the error page.
    Error messages are stored in the request's session.

    request.session['error'] returns a dictionary of the form {'code': <int>, 'message': <str>}
    """
    code=404

    if 'error' in request.session:
        if request.session["error"]["code"] != 500: # Not internal server error

            request.session["error"] = {'code': 404, 'message': f"PAGE NOT FOUND"}
        else: code = 500 

    else:
        request.session["error"] = {'code': 404, 'message': f"PAGE NOT FOUND"}

    return render(request, "portfolio/error.html", status=code)

# About Me Page
# Moved about me to home page

# def about(request):
#     """
#     Returns a JsonRepsonse of the user/owner's 'about' information

#     Args:
#         request ([HttpRequest]) 

#     Returns:
#         [JsonResponse]
#     """
#     response = {}
#     if request.method == "GET":
#         try:   
#             user = Owner.objects.get(username=USERNAME)
#             response = user.get_about_info()
#         except:
#             response["error"] = f"Username [{USERNAME}] doesn't exist"
#     else:
#         response["error"] = "Invalid Request Method [Only GET supported]"

#     #return JsonResponse(response)
#     return render(request, "portfolio/about.html", context=response)

