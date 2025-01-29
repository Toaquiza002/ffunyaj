from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Socio, Cooperante, Administrador, Universidad, Estudiante, Beca, HistorialAcademico, Pago, ActividadDeVoluntariado, PostulacionBeca
from .forms import UniversidadForm, EstudianteForm, HistorialAcademicoForm, PagoForm, CooperanteForm, SocioForm, ActividadDeVoluntariadoForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Asegúrate de importar csrf_exempt
from django.core.mail import send_mail
from django.db import IntegrityError
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@csrf_exempt
def enviar_formulario(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        print(f"Nombre: {first_name}, Apellidos: {last_name}, Email: {email}, Teléfono: {phone_number}, Fecha de nacimiento: {birth_date}, Género: {gender}, Ciudad: {city}")
        message = f"""
        Nombre: {first_name} {last_name}
        Correo electrónico: {email}
        Número de teléfono: {phone_number}
        Fecha de nacimiento: {birth_date}
        Género: {gender}
        Ciudad de residencia: {city}
        """
        send_mail(
            'Nuevo registro de formulario',
            message,
            'byron.toaquiza2645@utc.edu.ec',
            ['byron.toaquiza2645@utc.edu.ec'],
            fail_silently=False,)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)
#VistaPrevia publico
def index(request):
    return render(request, 'index.html')
def separte(request):
    return render(request, 'separte.html')
def registroseparte(request):
    return render(request, 'registroseparte.html')
def funyaj(request):
    return render(request,'funyaj.html')
def perfilToaquiza(request):
    return render(request,'perfilToaquiza.html')
def perfilTania(request):
    return render(request,'perfilTania.html')
def perfilMartha(request):
    return render(request,'perfilMartha.html')
def perfilFranklin(request):
    return render(request,'perfilFranklin.html')
def perfilJenny(request):
    return render(request,'perfilJenny.html')
def perfilFanny(request):
    return render(request,'perfilFanny.html')
def perfilWilmer(request):
    return render(request,'perfilWilmer.html')
def perfilSonia(request):
    return render(request,'perfilSonia.html')
def perfilJonathan(request):
    return render(request,'perfilJonathan.html')
def perfilLiliana(request):
    return render(request,'perfilLiliana.html')
def perfilRosa(request):
    return render(request,'perfilRosa.html')
def perfilAlexI(request):
    return render(request,'perfilAlexI.html')
def perfilJhonny(request):
    return render(request,'perfilJhonny.html')
def perfilKimberly(request):
    return render(request,'perfilKimberly.html')
def perfilWillian(request):
    return render(request,'perfilWillian.html')
def perfilIsmael(request):
    return render(request,'perfilIsmael.html')
def perfilOscar(request):
    return render(request,'perfilOscar.html')
def perfilAna(request):
    return render(request,'perfilAna.html')
def deporte(request):
    return render(request,'deporte.html')
def musica(request):
    return render(request,'musica.html')
def salud(request):
    return render(request,'salud.html')
def turismo(request):
    return render(request,'turismo.html')
def ayuda(request):
    return render(request,'ayuda.html')
def donacion(request):
    return render(request,'donacion.html')
def contactos(request):
    return render(request,'contactos.html')
def becarios(request):
    return render(request,'becarios.html')

#Login
def login(request):
    return render(request,'registration/login.html')



@login_required
def dashboard(request):
    estudiantes = Estudiante.objects.all()
    estudiantes_activos = estudiantes.filter(estado='Estudiante Activo')
    estudiantes_desertores = estudiantes.filter(estado='Desertor')
    estudiantes_graduados = estudiantes.filter(estado='Graduado')
    estudiantes_por_universidad = Estudiante.objects.values('universidad__nombre') \
        .annotate(total=Count('id')) \
        .order_by('universidad__nombre')
    total_universidades = Universidad.objects.count()
    total_estudiantes = estudiantes.count()
    pagos_por_mes = Pago.objects.annotate(month=TruncMonth('fecha_de_pago')) \
        .values('month') \
        .annotate(total_pago=Sum('monto')) \
        .order_by('month')
    context = {
        'estudiantes': estudiantes,
        'estudiantes_activos': estudiantes_activos,
        'estudiantes_desertores': estudiantes_desertores,
        'estudiantes_graduados': estudiantes_graduados,
        'estudiantes_por_universidad': estudiantes_por_universidad,
        'total_universidades': total_universidades,
        'total_estudiantes': total_estudiantes,
        'pagos_por_mes': pagos_por_mes,
    }
    return render(request, 'dashboard.html', context)
#Admin
@login_required
def administrador(request):
    return render(request,'administrador.html')
#Postulantes
def registrobeca(request):
    registrobecasBdd=PostulacionBeca.objects.all()
    return render(request,'registrobeca.html',{'registrobecas':registrobecasBdd})
def guardarpostulacion(request):
    nombres = request.POST["nombres"]
    apellidos = request.POST["apellidos"]
    provincia = request.POST["provincia"]
    canton = request.POST["canton"]
    parroquia = request.POST["parroquia"]
    comunidad = request.POST["comunidad"]
    cedula = request.POST["cedula"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]
    carrera = request.POST["carrera"]
    aceptacion_de_cupo =request.FILES.get("aceptacion_de_cupo")
    # Insertando datos mediante ORM de Django
    nuevorepostulacion = PostulacionBeca.objects.create(
        nombres=nombres,
        apellidos=apellidos,
        provincia=provincia,
        canton=canton,
        parroquia=parroquia,
        comunidad=comunidad,
        cedula=cedula,
        telefono=telefono,
        email=email,
        carrera=carrera,
        aceptacion_de_cupo=aceptacion_de_cupo,)

    messages.success(request, 'Datos enviado correctamente')
    return redirect('/registrobeca/')
def eliminarPostulantes(request,id):
    eliminarPostulantes = PostulacionBeca.objects.get(id=id)
    eliminarPostulantes.delete()
    messages.success(request, 'El dato se ha eliminado con éxito.')
    return redirect('/listpostulantes/')

#Postulantes
def listpostulantes(request):
    postulanteBdd=PostulacionBeca.objects.all()
    return render(request,'listpostulantes.html',{'postulante':postulanteBdd})

#Universidad
def listuniversidad(request):
    universidadBdd = Universidad.objects.all()
    estudiantes_por_universidad = Estudiante.objects.values('universidad').annotate(total=Count('id'))
    universidad_estudiantes = {est['universidad']: est['total'] for est in estudiantes_por_universidad}
    return render(request, 'listuniversidad.html', {
        'universidad': universidadBdd,
        'universidad_estudiantes': universidad_estudiantes,
    })
def agregaruniversidad(request):
    nombre = request.POST["nombre"]
    direccion = request.POST["direccion"]
    nuevouniversidad = Universidad.objects.create(
        nombre=nombre,
        direccion=direccion,)
    messages.success(request, 'El dato se guardó correctamente')
    return redirect('/listuniversidad/')

def eliminarUniversidad(request, id):
    try:
        universidad = Universidad.objects.get(id=id)
        universidad.delete()
        messages.success(request, 'El dato se ha eliminado con éxito.')
    except IntegrityError as e:
        pass
    except Universidad.DoesNotExist:
        pass
    return redirect('/listuniversidad/')
def editar_universidad(request, id):
    universidad = get_object_or_404 (Universidad, id=id)
    if request.method == 'POST':
        form = UniversidadForm(request.POST, instance=universidad)
        if form.is_valid():
            form.save()
            messages.success(request, 'El dato ha sido actualizado exitosamente.')
            return redirect('/listuniversidad/')

#Estudiantes
def listestudientes(request):
    universidadBdd=Universidad.objects.all()
    estudiantesBdd=Estudiante.objects.all()
    return render(request,'listestudientes.html',{'estudiantes':estudiantesBdd, 'universidad':universidadBdd})
def agregarestudiante(request):
    nombres = request.POST["nombres"]
    apellidos = request.POST["apellidos"]
    cedula = request.POST["cedula"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]
    id_universidad = request.POST["id_universidad"]
    universidadSeleccionado = Universidad.objects.get(id=id_universidad)
    carrera = request.POST["carrera"]
    año_de_ingreso = request.POST["año_de_ingreso"]
    estado = request.POST["estado"]
    nuevoestudiante = Estudiante.objects.create(
        nombres=nombres,
        apellidos=apellidos,
        cedula=cedula,
        direccion=direccion,
        telefono=telefono,
        email=email,
        universidad=universidadSeleccionado,
        carrera=carrera,
        año_de_ingreso=año_de_ingreso,
        estado=estado,)
    messages.success(request, 'El dato se guardó correctamente.')
    return redirect('/listestudientes/')
def eliminar_estudiante(request, id):
    try:
        estudiante = Estudiante.objects.get(id=id)
        estudiante.delete()
        messages.success(request, 'El estudiante se ha eliminado con éxito.')
    except IntegrityError as e:
        pass
    except Estudiante.DoesNotExist:
        pass
    return redirect('/listestudientes/')
def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)

    if request.method == 'POST':
        estudiante.nombres = request.POST.get('nombres')
        estudiante.apellidos = request.POST.get('apellidos')
        estudiante.cedula = request.POST.get('cedula')
        estudiante.telefono = request.POST.get('telefono')
        estudiante.email = request.POST.get('email')
        estudiante.carrera = request.POST.get('carrera')
        estudiante.año_de_ingreso = request.POST.get('año_de_ingreso')
        estudiante.estado = request.POST.get('estado')
        universidad_id = request.POST.get('id_universidad')
        if universidad_id:
            universidad = get_object_or_404(Universidad, id=universidad_id)
            estudiante.universidad = universidad
        estudiante.save()
        messages.success(request, 'El dato ha sido actualizado exitosamente.')
        return redirect('/listestudientes/')

#HistorialAcademico
def historialacademico(request):
    universidadBdd=Universidad.objects.all()
    academicoBdd=HistorialAcademico.objects.all()
    estudiantesBdd=Estudiante.objects.all()
    return render(request,'historialacademico.html',{'academico':academicoBdd, 'estudiantes':estudiantesBdd, 'universidad':universidadBdd})
def agregarhistorial(request):
    id_estudiante = request.POST["id_estudiante"]
    estudianteSeleccionado = Estudiante.objects.get(id=id_estudiante)
    id_universidad = request.POST["id_universidad"]
    universidadSeleccionado = Universidad.objects.get(id=id_universidad)
    semestre = request.POST["semestre"]
    campus = request.POST["campus"]
    residencia= request.POST["residencia"]
    nuevohistorial = HistorialAcademico.objects.create(
        estudiante=estudianteSeleccionado,
        universidad=universidadSeleccionado,
        semestre=semestre,
        campus=campus,
        residencia=residencia,)
    messages.success(request, 'El dato se guardó correctamente.')
    return redirect('/historialacademico/')
def eliminarHistorial(request, id):
    historial = get_object_or_404(HistorialAcademico, id=id)
    historial.delete()
    messages.success(request, 'El dato se ha eliminado con éxito.')
    return redirect('/historialacademico/')
def editar_historial(request, id):
    historial = get_object_or_404(HistorialAcademico, id=id)
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante')
        universidad_id = request.POST.get('universidad')
        semestre = request.POST.get('semestre')
        campus = request.POST.get('campus')
        residencia = request.POST.get('residencia')
        historial.estudiante_id = estudiante_id
        historial.universidad_id = universidad_id
        historial.semestre = semestre
        historial.campus = campus
        historial.residencia = residencia
        historial.save()
        messages.success(request, 'El dato ha sido actualizado exitosamente.')
        return redirect('historialacademico')

#PAGOS
def pagos(request):
    pagoBdd=Pago.objects.all()
    estudiantesBdd=Estudiante.objects.all()
    becasBdd=Beca.objects.all()
    return render(request,'pagos.html',{'pago':pagoBdd, 'estudiantes':estudiantesBdd, 'becas':becasBdd})
def agregarpagos(request):
    id_estudiante = request.POST["id_estudiante"]
    estudianteSeleccionado = Estudiante.objects.get(id=id_estudiante)
    id_beca = request.POST["id_beca"]
    becaSeleccionado = Beca.objects.get(id=id_beca)
    fecha_de_pago = request.POST["fecha_de_pago"]
    monto = request.POST["monto"]
    nuevopagos = Pago.objects.create(
        estudiante=estudianteSeleccionado,
        beca=becaSeleccionado,
        fecha_de_pago=fecha_de_pago,
        monto=monto,)
    messages.success(request, 'El dato se guardó correctamente.')
    return redirect('/pagos/')
def eliminarPagos(request, id):
    pagos = get_object_or_404(Pago, id=id)
    pagos.delete()
    messages.success(request, 'El dato se ha eliminado con éxito.')
    return redirect('/pagos/')
def editar_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    if request.method == 'POST':
        estudiante_id = request.POST.get('id_estudiante')
        beca_id = request.POST.get('id_beca')
        fecha_de_pago = request.POST.get('fecha_de_pago')
        monto = request.POST.get('monto')
        pago.estudiante_id = estudiante_id
        pago.beca_id = beca_id
        pago.fecha_de_pago = fecha_de_pago
        pago.monto = monto
        pago.save()
        messages.success(request, 'El dato ha sido actualizado exitosamente.')
        return redirect('/pagos/')

    #COOPERANTES
def listcooperante(request):
        cooperanteBdd=Cooperante.objects.all()
        return render(request,'listcooperante.html',{'cooperantes':cooperanteBdd})
def agregarcooperante(request):
        nombre = request.POST["nombre"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        nuevocooperante = Cooperante.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,)
        messages.success(request, 'El dato se guardó correctamente.')
        return redirect('/listcooperante/')
def eliminarCooperante(request,id):
        eliminarCooperante = Cooperante.objects.get(id=id)
        eliminarCooperante.delete()
        messages.success(request, 'El dato se ha eliminado con éxito.')
        return redirect('/listcooperante/')
def editar_cooperante(request, id):
    cooperante = get_object_or_404(Cooperante, id=id)
    if request.method == 'POST':
        cooperante.nombre = request.POST.get('nombre')
        cooperante.direccion = request.POST.get('direccion')
        cooperante.telefono = request.POST.get('telefono')
        cooperante.email = request.POST.get('email')
        cooperante.save()
        messages.success(request, 'El dato ha sido actualizado exitosamente.')
        return redirect('/listcooperante/')

#SOCIO
def listsocio(request):
    socioBdd=Socio.objects.all()
    return render(request,'listsocio.html',{'socios':socioBdd})
def agregarsocio(request):
    nombre = request.POST["nombre"]
    apellidos = request.POST["apellidos"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]
    nuevosocio = Socio.objects.create(
        nombre=nombre,
        apellidos=apellidos,
        direccion=direccion,
        telefono=telefono,
        email=email,)
    messages.success(request, 'El dato se guardó correctamente.')
    return redirect('/listsocio/')
def eliminarSocio(request,id):
    eliminarSocio = Socio.objects.get(id=id)
    eliminarSocio.delete()
    messages.success(request, 'El dato se ha eliminado con éxito.')
    return redirect('/listsocio/')
def editar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    if request.method == 'POST':
        socio.nombre = request.POST.get('nombre')
        socio.apellidos = request.POST.get('apellidos')
        socio.direccion = request.POST.get('direccion')
        socio.telefono = request.POST.get('telefono')
        socio.email = request.POST.get('email')
        socio.save()
        messages.success(request, 'El dato ha sido actualizado exitosamente.')
        return redirect('listsocio')
#VOLUNTARIOS
def voluntariado(request):
    voluntarioBdd=ActividadDeVoluntariado.objects.all()
    estudiantesBdd=Estudiante.objects.all()
    return render(request,'voluntariado.html',{'voluntario':voluntarioBdd, 'estudiantes':estudiantesBdd})
def agregarvoluntariado(request):
    id_estudiante = request.POST["id_estudiante"]
    estudianteSeleccionado = Estudiante.objects.get(id=id_estudiante)
    actividad = request.POST["actividad"]
    fecha = request.POST["fecha"]
    horas = request.POST["horas"]
    nuevovoluntario = ActividadDeVoluntariado.objects.create(
        estudiante=estudianteSeleccionado,
        actividad=actividad,
        fecha=fecha,
        horas=horas,)
    messages.success(request, 'El dato se guardó correctamente.')
    return redirect('/voluntariado/')
def eliminarVoluntario(request,id):
    eliminarVoluntario = ActividadDeVoluntariado.objects.get(id=id)
    eliminarVoluntario.delete()
    messages.success(request, 'El dato se ha eliminado con éxito')
    return redirect('/voluntariado/')

def editar_voluntariado(request, id):
    voluntariado = get_object_or_404(ActividadDeVoluntariado, id=id)

    if request.method == 'POST':
        estudiante_id = request.POST.get('id_estudiante')
        actividad = request.POST.get('actividad')
        fecha = request.POST.get('fecha')
        horas = request.POST.get('horas')

        if not estudiante_id or not actividad or not fecha or not horas:
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('editar_voluntariado', id=id)

        voluntariado.estudiante_id = estudiante_id
        voluntariado.actividad = actividad
        voluntariado.fecha = fecha
        voluntariado.horas = horas
        voluntariado.save()

        messages.success(request, 'El dato ha sido actualizado exitosamente.')
        return redirect('/voluntariado/')

    return render(request, 'editar_voluntariado.html', {'voluntariado': voluntariado})
#ADMINISTRADOR
def listadmin(request):
    adminBdd=Administrador.objects.all()
    return render(request,'listadmin.html',{'admin':adminBdd})

def salir(request):
    logout(request)
    return redirect('/')
