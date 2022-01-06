from rest_framework import serializers
from .models import Ne110MAdmin0Countries

class Ne110MAdmin0CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ne110MAdmin0Countries
        fields = '__all__'
