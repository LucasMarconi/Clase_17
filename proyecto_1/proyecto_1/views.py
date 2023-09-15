from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo!, esta es mi primera pagina")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a mi pagina")

# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context

def probando_plantilla(request):

    # Abrimos el archivo html
    mi_html = open('./proyecto_1/plantilla.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)