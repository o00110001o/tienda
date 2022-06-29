#CORRESPONDE A LAS URLS QUE SE UTILIZARAN   
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)

urlpatterns = [
    path('api/', include(router.urls)), # estamos levantando el admin
]

#USAR XAMPP PARA LEVANTAR APACHE Y MYSQL, asi crear la bd y linkearla#
