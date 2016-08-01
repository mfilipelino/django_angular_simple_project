from django.conf.urls import include, url
from django.views.generic import TemplateView


urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^manufactures', TemplateView.as_view(template_name='index.html')),

    url(r'^api/1/', include('vehicles.urls')),
]
