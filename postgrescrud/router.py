from crudapi.viewsets import Ne110MAdmin0CountriesViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('countries',Ne110MAdmin0CountriesViewset)