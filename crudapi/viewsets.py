from rest_framework import viewsets
from . import models
from . import serializers

class Ne110MAdmin0CountriesViewset(viewsets.ModelViewSet):
    queryset = models.Ne110MAdmin0Countries.objects.all()
    serializer_class=serializers.Ne110MAdmin0CountriesSerializer