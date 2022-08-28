from django.http import HttpResponse
from django.template import Template, Context, loader
from datos_familiares.models import Datos


def listar(request):
    queryset = Datos.objects.all()
    diccionario = {"datos_familiares" : queryset}
    plantilla = loader.get_template("datos_familiares_list.html")
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)


# Create your views here.
