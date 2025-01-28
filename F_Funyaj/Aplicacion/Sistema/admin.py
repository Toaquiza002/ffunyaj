from django.contrib import admin
from .models import Socio, Cooperante, Administrador, Universidad, Estudiante, Beca, HistorialAcademico, Pago, ActividadDeVoluntariado, PostulacionBeca


# Register your models here.
admin.site.register(Socio)
admin.site.register(Cooperante)
admin.site.register(Administrador)
admin.site.register(Universidad)
admin.site.register(Estudiante)
admin.site.register(Beca)
admin.site.register(HistorialAcademico)
admin.site.register(Pago)
admin.site.register(ActividadDeVoluntariado)
admin.site.register(PostulacionBeca)
