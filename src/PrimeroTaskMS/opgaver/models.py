from django.db import models

# Create your models here.
class Opgaver(models.Model):
    kunde_navn =               models.CharField(max_length=20) #Når man bruger char skal man have en max længde
    ansvarlig =                models.IntegerField(choices=((1, ("Alle")),
                                             (2, ("Magnus")),
                                             (3, ("Martin")),
                                             (4, ("Alex")),
                                             (5, ("Sebastian"))), default=1)
    opgave_beskrivelse =       models.TextField(blank=True, null=True)
    noter =                    models.TextField(blank=True, null=True)
    tid_brugt =                models.FloatField()
    status =                   models.IntegerField(choices=((1, ("Mangler")),
                                          (2, ("Startet")),
                                          (3, ("Halvvejs")),
                                          (4, ("Sidste Detaljer")),
                                          (5, ("Færdig"))), default=1)
    prioritet =                models.IntegerField(choices=((1, ("Høj")),
                                          (2, ("Mellem")),
                                          (3, ("Lav"))), default=3)
    deadline =                 models.DateField()





