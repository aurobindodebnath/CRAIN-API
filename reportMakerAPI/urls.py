from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'appsec', views.appsecViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mnbvcxz/', admin.site.urls),
    path('va/', views.sendVAPTObs),
]
