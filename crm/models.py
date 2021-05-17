from django.db import models
import datetime
import os

# Create your models here.
class Cliente(models.Model):
    """ modello generico di autore """
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    intervento = models.CharField(max_length=20)
    pdf = models.FileField(upload_to='media/', null=True, blank=True)
    data_ins = models.DateField()

    def __str__(self):
        return self.nome + " " + self.cognome
    
    @property
    def filename(self):
        return os.path.basename(self.pdf.name)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clienti"


class Document(models.Model):
    docfile = models.FileField()


def _upload_path(instance, filename):
    return instance.get_upload_path(filename)


class Professionista(models.Model):
    """ modello generico di autore """
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    tel = models.IntegerField()
    Iscrizione_albo = models.BooleanField()
    Numero_iscrizione = models.CharField(max_length=20)
    pdf = models.FileField(upload_to='media/', null=True, blank=True)
    data_di_nascita = models.DateField()

    def __str__(self):
        return self.nome + " " + self.cognome

    @property
    def filename(self):
        return os.path.basename(self.pdf.name)

    class Meta:
        verbose_name = "Professionista"
        verbose_name_plural = "Professionisti"
