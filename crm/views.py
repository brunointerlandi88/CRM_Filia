from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import CreateView
from django.urls import reverse

from .forms import ClienteForm, PForm

from .models import Cliente, Professionista

def homepage(request):
    return render(request, "homepage.html")

# Create your views here.
class ClienteDetailViewCB(DetailView):
    model = Cliente
    template_name = "cliente.html"


class ClienteListViewCB(ListView):
    model = Cliente
    template_name = "lista_clienti.html"


class PDetailViewCB(DetailView):
    model = Professionista
    template_name = "professionista.html"


class PListViewCB(ListView):
    model = Professionista
    template_name = "lista_professionisti.html"


def inserisci_cliente_view(request):

    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            print("Il Form è Valido!")
            new_cliente = form.save()
            print("new_cliente: ", new_cliente)
            return HttpResponse("<h1>inserito con successo!</h1>")
    else:
        form = ClienteForm()
    context = {"form": form}
    return render(request, "inserisci_cliente.html", context)


def cliente_list(request):
    clients = Cliente.objects.all()
    return render(request, 'lista_clienti.html', {
        'clients': clients
    })

def updateCliente(request, pk):

	clients = Cliente.objects.get(id=pk)
	form = ClienteForm(instance=clients)

	if request.method == 'POST':
		form = ClienteForm(request.POST, request.FILES, instance=clients)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('lista_clienti'))

	context = {'form':form}
	return render(request, 'aggiorna_cliente.html', context)

def vediCliente(request, pk_test):
    clients = Cliente.objects.get(id=pk_test)
    context = {
        'cliente':clients
    }
    return render(request, 'cliente.html', context)

def deleteCliente(request, pk):
	cli = Cliente.objects.get(id=pk)
	if request.method == "POST":
		cli.delete()
		return HttpResponseRedirect(reverse('lista_clienti'))

	context = {'item':cli}
	return render(request, 'cancella_cliente.html', context)

def inserisci_p_view(request):
    
    if request.method == "POST":
        form = PForm(request.POST, request.FILES)
        if form.is_valid():
            print("Il Form è Valido!")
            new_prof = form.save()
            print("new_prof: ", new_prof)
            return HttpResponse("<h1>inserito con successo!</h1>")
    else:
        form = PForm()
    context = {"form": form}
    return render(request, "inserisci_professionista.html", context)


def p_list(request):
    profs = Professionista.objects.all()
    return render(request, 'lista_professionisti.html', {
        'profs': profs
    })

def updateP(request, pk):

	profs = Professionista.objects.get(id=pk)
	form = PForm(instance=profs)

	if request.method == 'POST':
		form = PForm(request.POST, request.FILES, instance=profs)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('lista_professionisti'))

	context = {'form':form}
	return render(request, 'aggiorna_professionista.html', context)

def vediP(request, pk_test):
    profs = Professionista.objects.get(id=pk_test)
    context = {
        'profs':profs
    }
    return render(request, 'professionista.html', context)

def deleteP(request, pk):
	p = Professionista.objects.get(id=pk)
	if request.method == "POST":
		p.delete()
		return HttpResponseRedirect(reverse('lista_professionisti'))

	context = {'item':p}
	return render(request, 'cancella_professionista.html', context)
