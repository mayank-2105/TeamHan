from django.conf.urls import url
from crudapi import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^country$',views.countriesApi),
    url(r'^country/([0-9]+)$',views.countriesApi)
]