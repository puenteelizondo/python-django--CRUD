from django.urls import path
from .views import RegistroView

# Vistas JWT ya listas (no las reinventes)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Endpoint para registrar usuario
    path('registro/', RegistroView.as_view(), name='registro'),

    # Login: devuelve access y refresh token
    path('login/', TokenObtainPairView.as_view(), name='login'),

    # Endpoint para renovar access token
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]