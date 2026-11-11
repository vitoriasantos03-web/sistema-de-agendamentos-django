from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_agendamentos, name='listar_agendamentos'),
    path('listar_agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('agendar/', views.agendar, name='agendar'),
    path('excluir/<int:id>/', views.excluir_agendamento, name='excluir_agendamento'),
]