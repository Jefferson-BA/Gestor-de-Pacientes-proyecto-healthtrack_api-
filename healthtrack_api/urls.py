from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='api/v1/pacientes/', permanent=False)), # <-- NEW
    
    path('api/v1/', include('records_app.urls')),
]