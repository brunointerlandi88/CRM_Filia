from django import forms
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field, Button
from crispy_forms.helper import FormHelper
from django.urls import reverse

from .models import Cliente, Professionista

class DateInput(forms.DateInput):
    input_type = 'date'

class ClienteForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'nome'}))
    cognome = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Cognome'}))
    intervento = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Intervento'}), required=False)
    pdf = forms.FileField(label='Select a file', required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='form-group col-md-6 mb-0'),
                Column('cognome', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('intervento', css_class='form-group col-md-6 mb-0'),
                Column('pdf', css_class='form-group col-md-4 mb-0'),
                Column('data_ins', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Conferma'),
            Button('delete', 'Annulla', onclick='window.location.href="{}"'.format(reverse('lista_clienti')), css_class="btn btn-warning")
        )
        super(ClienteForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Cliente
        fields = ["nome", "cognome",
                           "intervento", "pdf", 'data_ins']
        widgets = {
            'data_ins': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select Date', 'type': 'date'}),
        }


class PForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'nome'}))
    cognome = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'cognome'}))
    tel = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'numero di telefono'}))
    Iscrizione_albo = forms.BooleanField(widget=forms.TextInput(
        attrs={'placeholder': 'iscritto'}))
    Numero_iscrizione = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Numero di iscrizione'}))
    pdf = forms.FileField(label='Select a file', required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='form-group col-md-6 mb-0'),
                Column('cognome', css_class='form-group col-md-6 mb-0'),
                Column('tel', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Iscrizione_albo', css_class='form-group col-md-6 mb-0'),
                Column('Numero_iscrizione', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('pdf', css_class='form-group col-md-6 mb-0'),
                Column('data_di_nascita', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Conferma'),
            Button('delete', 'Annulla', onclick='window.location.href="{}"'.format(
                reverse('lista_professionisti')), css_class="btn btn-warning")
        )
        super(PForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Professionista
        fields = ["nome", "cognome",
                  "tel", "Iscrizione_albo", 'Numero_iscrizione', 'pdf', 'data_di_nascita']
        widgets = {
            'data_di_nascita': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select Date', 'type': 'date'}),
        }
