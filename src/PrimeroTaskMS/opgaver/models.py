from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Opgaver(models.Model):
    kunde_navn = models.CharField(max_length=30)  # Når man bruger char skal man have en max længde
    ansvarlig = models.IntegerField(choices=((1, ("Alle")),
                                             (2, ("Magnus")),
                                             (3, ("Martin")),
                                             (4, ("Alex")),
                                             (5, ("Sebastian"))), default=1)
    opgave_beskrivelse = models.TextField(blank=True, null=True)
    noter = models.TextField(blank=True, null=True)
    tid_brugt = models.FloatField()
    status = models.IntegerField(choices=((1, ("Mangler")),
                                          (2, ("Startet")),
                                          (3, ("Halvvejs")),
                                          (4, ("Sidste Detaljer")),
                                          (5, ("Færdig"))), default=1)
    prioritet = models.IntegerField(choices=((1, ("Høj")),
                                             (2, ("Mellem")),
                                             (3, ("Lav"))), default=3)
    deadline = models.DateField(default=datetime.now)
    afsluttet = models.BooleanField(default=False)

    def __str__(self):
        return self.kunde_navn


Opgaver.objects.order_by('-id')


class Kunder(models.Model):
    kunde_id = models.CharField(max_length=4, unique=True)
    kunde_navn = models.CharField(max_length=30)
    kunde_installation = models.TextField(blank=True, null=True)
    kunde_adresse = models.TextField(blank=True, null=True, help_text="Gadenavn, nr., Postnummer og By")
    kontaktperson = models.CharField(max_length=30)
    kontakt_tlf = models.CharField(max_length=10)
    kontakt_mail = models.EmailField(max_length=254)

    def __str__(self):
        return self.kunde_navn


class Meta:
    ordering = ['prioritet']
