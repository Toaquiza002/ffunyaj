from django.urls import path
from . import views
from .views import enviar_formulario
from .views import index, dashboard


urlpatterns=[
    
#VistaPrevia
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('enviar-formulario/', enviar_formulario, name='enviar_formulario'),
    #Funyaj
    path('funyaj/',views.funyaj, name='funyaj'),
    path('becarios/',views.becarios, name='becarios'),
    path('separte/',views.separte, name='separte'),
    path('registroseparte/',views.registroseparte, name='registroseparte'),
#perfiles
#UTC
    path('perfilToaquiza/',views.perfilToaquiza, name='perfilToaquiza'),
    path('perfilTania/',views.perfilTania, name='perfilTania'),
    path('perfilMartha/',views.perfilMartha, name='perfilMartha'),
    path('perfilFranklin/',views.perfilFranklin, name='perfilFranklin'),
    path('perfilJenny/',views.perfilJenny, name='perfilJenny'),
    path('perfilFanny/',views.perfilFanny, name='perfilFanny'),
    path('perfilWilmer/',views.perfilWilmer, name='perfilWilmer'),
    path('perfilSonia/',views.perfilSonia, name='perfilSonia'),
    path('perfilJonathan/',views.perfilJonathan, name='perfilJonathan'),
#Central
    path('perfilLiliana/',views.perfilLiliana, name='perfilLiliana'),
    path('perfilRosa/',views.perfilRosa, name='perfilRosa'),
    path('perfilAlexI/',views.perfilAlexI, name='perfilAlexI'),
    path('perfilJhonny/',views.perfilJhonny, name='perfilJhonny'),
#ESPE
    path('perfilKimberly/',views.perfilKimberly, name='perfilKimberly'),
    path('perfilWillian/',views.perfilWillian, name='perfilWillian'),
#UNACH
    path('perfilIsmael/',views.perfilIsmael, name='perfilIsmael'),
    path('perfilOscar/',views.perfilOscar, name='perfilOscar'),
#Graduados
    path('perfilAna/',views.perfilAna, name='perfilAna'),
#Deportes
    path('deporte/',views.deporte, name='deporte'),
#Musica
    path('musica/',views.musica, name='musica'),
#Salud
    path('salud/',views.salud, name='salud'),
#Turismo
    path('turismo/',views.turismo, name='turismo'),
#Ayuda
    path('ayuda/',views.ayuda, name='ayuda'),
#Donacion
    path('donacion/',views.donacion, name='donacion'),
#Contactos
    path('contactos/',views.contactos, name='contactos'),
#Login
    path('login/',views.login, name='login'),
#Admin
    path('administrador/',views.administrador, name='administrador'),
# todo el formularios

    #POSTULANTES
    path('registrobeca/',views.registrobeca, name='registrobeca'),
    path('listpostulantes/',views.listpostulantes, name='listpostulantes'),
    path('guardarpostulacion/',views.guardarpostulacion),
    path('eliminarPostulantes/<id>',views.eliminarPostulantes),

    #UNIVERSIDAD
    path('listuniversidad/',views.listuniversidad, name='listuniversidad'),
    path('agregaruniversidad/',views.agregaruniversidad),
    path('eliminarUniversidad/<id>',views.eliminarUniversidad),
    path('editaruniversidad/<int:id>/', views.editar_universidad, name='editaruniversidad'),

    #ESTUDIANTES
    path('listestudientes/',views.listestudientes, name='listestudientes'),
    path('agregarestudiante/',views.agregarestudiante),
    path('eliminarEstudiante/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    path('editar_estudiante/<int:id>/', views.editar_estudiante, name='editar_estudiante'),

    #ACADEMICO
    path('historialacademico/',views.historialacademico, name='historialacademico'),
    path('agregarhistorial/',views.agregarhistorial),
    path('eliminarHistorial/<int:id>/', views.eliminarHistorial, name='eliminarHistorial'),
    path('editar_historial/<int:id>/', views.editar_historial, name='editar_historial'),
    #PAGOS
    path('pagos/',views.pagos, name='pagos'),
    path('agregarpagos/',views.agregarpagos),
    path('eliminarPagos/<int:id>/', views.eliminarPagos, name='eliminarPagos'),
    path('editar_pago/<int:id>/', views.editar_pago, name='editar_pago'),
    #SOCIO
    path('listsocio/',views.listsocio, name='listsocio'),
    path('agregarsocio/',views.agregarsocio),
    path('eliminarSocio/<id>',views.eliminarSocio),
    path('editarSocio/<int:id>/', views.editar_socio, name='editar_socio'),
    #COOPERANTE
    path('listcooperante/',views.listcooperante, name='listcooperante'),
    path('agregarcooperante/',views.agregarcooperante),
    path('eliminarCooperante/<id>',views.eliminarCooperante),
    path('editar_cooperante/<int:id>/', views.editar_cooperante, name='editar_cooperante'),
    #VOLUNTARIO
    path('voluntariado/',views.voluntariado, name='voluntariado'),
    path('agregarvoluntariado/',views.agregarvoluntariado),
    path('eliminarVoluntario/<id>',views.eliminarVoluntario),
    path('editar_voluntariado/<int:id>/', views.editar_voluntariado, name='editar_voluntariado'),


    #ADMINISTRADOR
    path('listadmin/',views.listadmin, name='listadmin'),

    path('dashboard/', views.dashboard, name='dashboard'),

]
