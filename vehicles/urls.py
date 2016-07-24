from django.conf.urls import url
from vehicles.views import VehicleManufacturerView, VehicleManufacturerListView, VehicleModelView

urlpatterns = [
    url(r'^manufactures/(?P<manufacture_id>[0-9])+/$', VehicleManufacturerView.as_view(), name='api_manufactures'),
    url(r'^manufactures/$', VehicleManufacturerListView.as_view(), name='api_list_manufactures'),
    url(r'^manufactures/(?P<vehicles_model_id>[0-9])+/$', VehicleModelView.as_view(), name='api_vehicles_model')
]