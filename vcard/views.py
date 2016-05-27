from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from constance import config as site_config
from .models import Project, ContactInfo, ProjectTag


def get_index_page(request):
    h1 = site_config.h1

    return render(request, 'vcard/index.html', {'h1': h1})


def get_tags(request):
    tags = ProjectTag.objects.all()
    json = serializers.serialize('json', tags)

    return HttpResponse(json, content_type='application/json')


def get_projects(request, tag_alias):
    tag = get_object_or_404(ProjectTag, alias=tag_alias)
    projects = tag.project_set.all()
    json = serializers.serialize('json', projects)

    return HttpResponse(json, content_type='application/json')


def get_contacts(request):
    list_ = ContactInfo.objects.all()
    json = serializers.serialize('json', list_)

    return HttpResponse(json, content_type='application/json')


def get_about_me_text(request):
    return JsonResponse({'about_me': site_config.about_me})
