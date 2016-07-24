from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from vehicles import views
import vehicles


urlpatterns = [
    # Examples:
    # url(r'^$', 'djangular3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/1/', include('vehicles.urls'))
]

