from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from vehicles import vehicles_svc
import json


class VehicleManufacturerView(APIView):


    def get(self, request, manufacture_id, *args, **kargs):

        result = vehicles_svc.get_manufacturer(manufacture_id, as_dict=True)
        return Response(data=result, status=status.HTTP_200_OK, content_type='application/json')

    def put():
        pass

    def post():
        pass

    def delete():
        pass


