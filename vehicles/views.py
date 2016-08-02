from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from vehicles import vehicles_svc
import json


class VehicleManufacturerView(APIView):
    def get(self, request, manufacture_id=None, *args, **kargs):
        result = vehicles_svc.get_manufacturer(manufacture_id, as_dict=True)
        return Response(data=result, status=status.HTTP_200_OK, content_type='application/json')

    def delete(self, request, manufacture_id=None, *args, **kargs):
        result = vehicles_svc.delete_manufacturer(manufacture_id)
        return Response(data=result, status=status.HTTP_200_OK, content_type='application/json')

    def post(self, request, manufacture_id=None, *args, **kargs):
        result = vehicles_svc.save_manufacturer(request.data)
        return Response(data=result, status=status.HTTP_200_OK, content_type='application/json')


class VehicleManufacturerListView(APIView):
    def get(self, request, *args, **kargs):
        filters = request.query_params.get('filters', '{}')
        filters = json.loads(filters)
        result = vehicles_svc.list_manufacturer(filters=filters, as_dict=True)
        return Response(data=result, status=status.HTTP_200_OK, content_type='application/json')

    def post(self, request, *args, **kargs):
        manufacture_dict = request.data.get('manufacture_dict')
        result = vehicles_svc.save_manufacturer(manufacture_dict)
        return Response(data=result.to_dict(), status=status.HTTP_200_OK, content_type='application/json')


class VehicleModelView(APIView):
    def get(self, request, vehicles_model_id, *args, **kargs):
        result = vehicles_svc.get_vehicle_model(vehicles_model_id, as_dict=True)
        return Response(data=result, status=status.HTTP_200_OK, content_type='application/json')

    def delete(self, request, vehicles_model_id=None, *args, **kargs):
        result = vehicles_svc.delete_vehicle_model(vehicles_model_id)
        return Response(data=result, status=status.HTTP_200_OK, content_type='application/json')


class VehicleModelListView(APIView):
    def get(self, request, *args, **kargs):
        filters = request.query_params.get('filters', '{}')
        filters = json.loads(filters)
        result = vehicles_svc.list_vehicle_model(filters=filters, as_dict=True)
        return Response(data=result, status=status.HTTP_200_OK, content_type='application/json')

    def post(self, request, *args, **kargs):
        vehiclemodel_dict = request.data.get('vehiclemodel_dict')
        result = vehicles_svc.save_vehiclemodel(vehiclemodel_dict)
        return Response(data=result.to_dict(), status=status.HTTP_200_OK, content_type='application/json')


class VehicleView(APIView):
    def get(self, request, vehicles_id=None, *args, **kargs):
        result = vehicles_svc.get_vehicle(vehicles_id, as_dict=True)
        return Response(data=result, status=status.HTTP_200_OK, content_type='application/json')


class VehiclesView(APIView):
    def get(self, request, *args, **kargs):
        filters = request.query_params.get('filters', '{}')
        filters = json.loads(filters)
        result = vehicles_svc.list_vehicles(filters=filters, as_dict=True)
        return Response(data=result, status=status.HTTP_200_OK, content_type='application/json')
