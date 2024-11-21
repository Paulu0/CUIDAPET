
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('cadastro/', include('login.urls')),
    path('inicio/', include('login.urls')),
    path('sobre/', include('login.urls')),
    path('registrar banho/', include('login.urls')),
    path('meus pets/', include('login.urls')),
    path('cadastrar pet/', include('login.urls')),
    path('banho e tosa/', include('login.urls')),
    path('medicamentos e vacinas/', include('login.urls')),
    path('registrar medicamento/', include('login.urls')),


]


