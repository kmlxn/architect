from django.shortcuts import get_object_or_404, render
from .models import Project, ContactInfo, TextOnSite
from django.http import HttpResponse
from django.core import serializers


def get_index_page(request):
    h1 = get_object_or_404(TextOnSite, name='h1')

    return render(request, 'vcard/index.html', {'h1': h1})


def get_projects(request):
    list_ = Project.objects.all()
    json = serializers.serialize('json', list_)

    return HttpResponse(json, content_type='application/json')


def get_contacts(request):
    list_ = ContactInfo.objects.all()
    json = serializers.serialize('json', list_)

    return HttpResponse(json, content_type='application/json')


def get_about_me_text(request):
    elem = get_object_or_404(TextOnSite, name='about me')
    json = serializers.serialize('json', [elem])

    return HttpResponse(json, content_type='application/json')
