from django.conf.urls import url
from vehicles.views import VehicleManufacturerView, VehicleManufacturerListView

urlpatterns = [
    url(r'^manufactures/(?P<manufacture_id>[0-9])+/$', VehicleManufacturerView.as_view(), name='api_manufactures'),
    url(r'^manufactures/$', VehicleManufacturerListView.as_view(), name='api_list_manufactures')
]