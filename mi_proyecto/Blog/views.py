from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Comentario
from .forms import ComentarioForm
from Blog.models import Zapatilla
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def listar_zapatillas(request):
    contexto = {
        "zapatillas": Zapatilla.objects.all(),
        
    }
    http_responde = render(
        request=request,
        template_name='Blog/lista_zapatillas.html',
        context=contexto,
    )
    return http_responde

def info_marca(request):
    return render(request, 'Blog/infomarca.html')


def registro(request):
    return render(request, 'registro.html')

@login_required
def agregar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            if request.user.is_authenticated:
                comentario.creador = request.user
            comentario.save()
            form = ComentarioForm()
    else:
        form = ComentarioForm()

    comentarios = Comentario.objects.all()
    context = {'form': form, 'comentarios': comentarios}
    return render(request, 'blog/comentarios.html', context)





