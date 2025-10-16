from rest_framework import serializers
from .models import Paciente, Doctor

class DoctorMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['nombre', 'especialidad']

class DoctorSerializer(serializers.ModelSerializer):
    pacientes_asignados = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'nombre', 'especialidad', 'pacientes_asignados']

    def get_pacientes_asignados(self, obj):
        return obj.pacientes.count()

class PacienteSerializer(serializers.ModelSerializer):
   
    doctor_info = DoctorMinSerializer(source='doctor_asignado', read_only=True)
    

    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'edad', 'diagnostico', 'doctor_asignado', 'doctor_info']
        extra_kwargs = {
            'doctor_asignado': {'write_only': True} 
        }