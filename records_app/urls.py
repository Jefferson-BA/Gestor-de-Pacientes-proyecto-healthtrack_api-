from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, DoctorViewSet, PacienteSearchAPIView

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet) 
router.register(r'doctores', DoctorViewSet)  

urlpatterns = [
   
    path('', include(router.urls)),
    
    path('pacientes/search/', PacienteSearchAPIView.as_view(), name='paciente-search'),
]