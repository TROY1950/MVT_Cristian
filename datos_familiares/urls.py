
from django.urls import path, include
from datos_familiares.views import listar

urlpatterns = [
    path('', listar),
]
                               