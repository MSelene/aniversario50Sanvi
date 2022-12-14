"""aniversario50Sanvi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import settiltangle
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from core import views as core_views
from noticias import views as noticias_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('contacto/', core_views.contacto, name="contacto"),
    path('noticias/', noticias_views.noticias, name="noticias"),
    path('acerca_de/', core_views.acerca_de, name="acerca_de"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
