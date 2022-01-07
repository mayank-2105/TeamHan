from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from crudapi.models import Ne110MAdmin0Countries
from crudapi.serializers import Ne110MAdmin0CountriesSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def countriesApi(request,id=0):
    if request.method=='GET':
        countries = Ne110MAdmin0Countries.objects.all()
        countries_serializer=Ne110MAdmin0CountriesSerializer(countries,many=True)
        return JsonResponse(countries_serializer.data,safe=False)
    elif request.method=='POST':
        countries_data=JSONParser().parse(request)
        countries_serializer=Ne110MAdmin0CountriesSerializer(data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        countries_data=JSONParser().parse(request)
        countries=Ne110MAdmin0Countries.objects.get(ogc_fid=countries_data['ogc_fid'])
        countries_serializer=Ne110MAdmin0CountriesSerializer(countries,data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        countries=Ne110MAdmin0Countries.objects.get(ogc_fid=id)
        countries.delete()
        return JsonResponse("Deleted Successfully",safe=False)