from django.shortcuts import render
from .forms import AsistenciaForm
from .models import Asistencia

# Create your views here.

def asistencia_view(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = AsistenciaForm()
    return render(request, 'asistencia_form.html', {'form': form})

def asistencia_success_view(request):
    return render(request, 'success.html') 
