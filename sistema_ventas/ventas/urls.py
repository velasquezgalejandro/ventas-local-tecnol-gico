from django.urls import path
from .views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),  # Ruta para la página de inicio
]
