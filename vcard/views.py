from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from constance import config as site_config
from .models import Project, ContactInfo, ProjectTag


def get_index_page(request):
    h1 = site_config.h1
    title = site_config.title

    return render(request, 'vcard/index.html', {'h1': h1, 'title': title})


def get_tags(request):
    data = [tag.get_data() for tag in ProjectTag.objects.all()]

    return JsonResponse(data, safe=False)


def get_projects(request, tag_url_name):
    tag = get_object_or_404(ProjectTag, url_name=tag_url_name)
    data = [project.get_data() for project in tag.project_set.all()]

    return JsonResponse(data, safe=False)


def get_project(request, project_url_name):
    project = get_object_or_404(Project, url_name=project_url_name)

    return render(request, 'vcard/project.html', {'project': project})


def get_contacts(request):
    data = [contact_info.get_data() for contact_info in ContactInfo.objects.all()]

    return JsonResponse(data, safe=False)


def get_about_me_text(request):
    return JsonResponse(site_config.about_me, safe=False)
