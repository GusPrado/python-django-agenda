from django.shortcuts import render
from django.template.loader import render_to_string
from core.models import Evento

# Create your views here.

def lista_eventos(request):
    #usuario = request.user
    #eventos = Evento.objects.filter(usuario=usuario)
    eventos = Evento.objects.all()
    dados = {'eventos': eventos}
    print(dados)
    return render(request, 'agenda.html', dados)
