from . import views
from django.urls import path

urlpatterns = [
    path('new/', views.asistencia_view, name='asistencia_new'),
    path('success/', views.asistencia_success_view, name='asistencia_success'),
]