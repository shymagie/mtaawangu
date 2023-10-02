from django.db import models
from django.contrib.auth.models import User
from users.models import (
   Nchi, Wilaya, Mkoa, Mtendaji,
    Kata, Mtaa, Mjumbe, Mwananchi
    ) 




class Ujumbe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="ujumbe_user")
    ujumbe = models.TextField()
    wapokeaji = models.CharField(max_length=80, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Jumbe'


    def __str__(self):
        return f'{self.date_created}'

class UjumbeUliotumwa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="zilizotumwa_user")
    ujumbe = models.TextField(null=True)
    utambulisho_wa_ujumbe = models.CharField(max_length=255, null=True)
    nambari_ya_simu = models.CharField(max_length=80, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'jumbeZilizotumwa'


    def __str__(self):
        return f'{self.date_created}'