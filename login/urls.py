from django.urls import path
from . import views



urlpatterns = [
    path('', views.login),
    path('login/', views.login),
    path('cadastro/', views.cadastro),
    path('inicio/', views.inicio),
    path('sobre/', views.sobre),
    path('registrar banho/', views.registrar_novo_banho),
    path('meus pets/', views.meus_pets),
    path('cadastrar pet/', views.cadastrar_pet),
    path('banho e tosa/', views.banho_e_tosa),
    path('medicamentos e vacinas/', views.medicamentos_e_vacinas),
    path('registrar medicamento/', views.registrar_medicamento),


]
