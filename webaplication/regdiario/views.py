from multiprocessing import context
from django.shortcuts import render, HttpResponse

from .models import Pacient, Phase

# Create your views here.
def pacients_list(request):
    #return HttpResponse('Aplicación registro diario')
    pacients_list = Pacient.objects.all()
    context = {'pacients': pacients_list}
    return render(request, 'regdiario/pacients_list.html', context)

def phases_list(request, pacient_id):
    pacient = Pacient.objects.get(pk=pacient_id)
    context = {'pacient': pacient}
    return render(request, 'regdiario/phases_list.html', context)

