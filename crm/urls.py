from django.urls import path
from django.conf.urls import include
from .forms import ClienteForm

from .views import ClienteListViewCB, ClienteDetailViewCB, inserisci_cliente_view, updateCliente, updateP, vediCliente, deleteCliente, homepage, inserisci_p_view, PListViewCB, updateP, deleteP, vediP
urlpatterns = [
    path('', homepage, name='home'),
    path('lista_clienti/', ClienteListViewCB.as_view(), name='lista_clienti'),
    path('lista_professionisti/', PListViewCB.as_view(), name='lista_professionisti'),
    path('inserisci_cliente/', inserisci_cliente_view, name='inserisci_cliente'),
    path('aggiorna_cliente/<str:pk>/', updateCliente, name='aggiorna_cliente'),
    path('cliente/<str:pk_test>/', vediCliente, name='cliente'),
    path('cancella_cliente/<str:pk>/', deleteCliente, name='cancella_cliente'),
    path('inserisci_professionista/', inserisci_p_view, name='inserisci_professionista'),
    path('aggiorna_professionista/<str:pk>/', updateP, name='aggiorna_professionista'),
    path('cancella_professionista/<str:pk>/', deleteP, name='cancella_professionista'),
    path('professionista/<str:pk_test>/', vediP, name='professionista'),
]
