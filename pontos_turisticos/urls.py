from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracoesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
