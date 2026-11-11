from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm

def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos/listar_agendamentos.html', {'agendamentos': agendamentos})

def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamentos/agendar.html', {'form': form})

def editar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'agendamentos/agendar.html', {'form': form})

def excluir_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    agendamento.delete()
    return redirect('listar_agendamentos')