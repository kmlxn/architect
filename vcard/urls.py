from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_index_page, name='get_index_page'),
    url(r'^get_projects/(?P<tag_alias>\w+)/$', views.get_projects, name='get_projects'),
    url(r'^get_project/(?P<project_url_name>\w+)/$', views.get_project, name='get_project'),
    url(r'^get_contacts/$', views.get_contacts, name='get_contacts'),
    url(r'^get_tags/$', views.get_tags, name='get_tags'),
    url(r'^get_about_me_text/$', views.get_about_me_text, name='get_about_me_text'),
]
