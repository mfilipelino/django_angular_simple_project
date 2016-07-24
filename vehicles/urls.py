from django.conf.urls import url
from vehicles.views import VehicleManufacturerView

urlpatterns = [
    url(r'^manufactures/(?P<manufacture_id>[0-9]+)/$', VehicleManufacturerView.as_view(), name='api_manufactures')
]