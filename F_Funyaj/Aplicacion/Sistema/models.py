from django.db import models

class Socio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.nombre

class Cooperante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.nombre

class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

class Universidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    cedula = models.CharField(max_length=15)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=250)
    universidad = models.ForeignKey('Universidad', on_delete=models.PROTECT)
    carrera = models.CharField(max_length=250)
    año_de_ingreso = models.IntegerField()
    estado = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    def nombre_completo(self):
        return f'{self.nombres} {self.apellidos}'

class Beca(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=250)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_de_inicio = models.DateField()
    fecha_de_fin = models.DateField()

    def __str__(self):
        return self.tipo



class HistorialAcademico(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    universidad = models.ForeignKey(Universidad, on_delete=models.PROTECT, blank=True, null=True)
    semestre = models.CharField(max_length=250)
    campus = models.CharField(max_length=250)
    residencia = models.CharField(max_length=250)
    def __str__(self):
        return f'{self.estudiante.nombre_completo()} - {self.semestre}'

class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    beca = models.ForeignKey(Beca, on_delete=models.PROTECT)
    fecha_de_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.estudiante.nombre_completo()} - {self.fecha_de_pago}'

class ActividadDeVoluntariado(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    actividad = models.CharField(max_length=250)
    fecha = models.DateField()
    horas = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.estudiante.nombre_completo()} - {self.actividad}'

class PostulacionBeca(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    provincia = models.CharField(max_length=250)
    canton = models.CharField(max_length=250)
    parroquia = models.CharField(max_length=250)
    comunidad = models.CharField(max_length=250)
    cedula = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=250)
    carrera = models.CharField(max_length=250)
    aceptacion_de_cupo =  models.FileField(upload_to='PDF', null=True, blank=True)

    def __str__(self):
        return f'{self.nombres} {self.apellidos} - {self.carrera}'
