"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from crm.views import inserisci_cliente_view, ClienteListViewCB, inserisci_p_view, PListViewCB
from crm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('inserisci_cliente/', inserisci_cliente_view, name='inserisci_cliente'),
    path('lista_clienti/', ClienteListViewCB.as_view(), name='lista_clienti'),
]

urlpatterns += [
    path('inserisci_professionista/', inserisci_p_view, name='inserisci_professionista'),
    path('lista_professionisti/', PListViewCB.as_view(), name='lista_professionisti'),
]