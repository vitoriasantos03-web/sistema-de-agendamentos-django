from django import forms
from .models import Agendamento
class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome_cliente', 'data', 'horario', 'servico']
        labels = {
            'nome_cliente': 'Nome do Cliente',
            'servico': 'Serviço',
            'data': 'Data',
            'horario': 'Horário'
        }
        widgets = {
            'nome_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'servico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Corte de Cabelo, Barba, etc...'}),
            'data': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'horario': forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time'
        })
    }
