from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django.db.models import Q
from .models import Paciente, Doctor
from .serializers import PacienteSerializer, DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
 
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre', 'especialidad']

class PacienteViewSet(viewsets.ModelViewSet):
 
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteSearchAPIView(ListAPIView):

    serializer_class = PacienteSerializer
    
    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query is not None:
            return Paciente.objects.filter(
                Q(nombre__icontains=query) | Q(diagnostico__icontains=query)
            )
        return Paciente.objects.all()