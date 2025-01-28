from django import forms
from .models import Universidad, Estudiante, HistorialAcademico, Pago, Cooperante, Socio, ActividadDeVoluntariado

class UniversidadForm(forms.ModelForm):
    class Meta:
        model = Universidad
        fields = ['nombre', 'direccion']


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombres', 'apellidos', 'cedula', 'direccion', 'telefono', 'email', 'universidad', 'carrera', 'año_de_ingreso', 'estado']

class HistorialAcademicoForm(forms.ModelForm):
    class Meta:
        model = HistorialAcademico
        fields = ['estudiante', 'universidad', 'semestre', 'campus', 'residencia']

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['estudiante', 'beca', 'fecha_de_pago', 'monto']

class CooperanteForm(forms.ModelForm):
    class Meta:
        model = Cooperante
        fields = ['nombre', 'direccion', 'telefono', 'email']

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'apellidos', 'direccion', 'telefono', 'email']

class ActividadDeVoluntariadoForm(forms.ModelForm):
    class Meta:
        model = ActividadDeVoluntariado
        fields = ['estudiante', 'actividad', 'fecha', 'horas']
