from django.db import models

class Doctor(models.Model):
    ESPECIALIDADES = [
        ('Cardiología', 'Cardiología'),
        ('Pediatría', 'Pediatría'),
        ('Neurología', 'Neurología'),
        ('General', 'Medicina General'),
        ('Dermatología', 'Dermatología'),
    ]
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50, choices=ESPECIALIDADES)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"Dr. {self.nombre} ({self.especialidad})"

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    diagnostico = models.CharField(max_length=255)

    doctor_asignado = models.ForeignKey(
        Doctor,
        related_name='pacientes', 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre}, {self.edad} años. Dx: {self.diagnostico}"