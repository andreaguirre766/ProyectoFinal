from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Zapatilla


def saludar(request):
    saludo = "Bienvenido a mi blog"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_con_hora(request):
    hoy = datetime.now()
    saludo = f"Hola usuario, fecha: {hoy.day}/{hoy.month}"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_a_usuario(request, nombre):
    texto = f"Hola {nombre}"
    pagina_html = HttpResponse(texto)
    return pagina_html

def saludar_con_html(request):
    contexto = {
        "usuario": "Pedro"
    }
    http_responde = render(
        request=request,
        template_name='Blog/base.html',
        context=contexto,
    )
    return http_responde

def inicio(request):
    contexto = {}
    hhtp_responde = render(
        request=request,
        template_name='Blog/index.html',
        context=contexto,
    )
    return hhtp_responde

def crear(request):
    objeto = Zapatilla(nombre="Air force" , descripcion="Buenas", precio=50000,marca="nike")
    objeto.save()
    contexto = {"mensaje":""}
    hhtp_responde = render(
        request=request,
        template_name='Blog/index.html',
        context=contexto,
    )
    return hhtp_responde
