from django.db import models
from django.contrib.auth.models import User
from users.models import (
   Nchi, Wilaya, Mkoa, Mtendaji,
    Kata, Mtaa, Mjumbe, Mwananchi
    ) 



class Tangazo(models.Model):
    pass


class UjumbeWaTangazo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="tangazo_user")
    ujumbe = models.TextField()
    eneo = models.CharField(max_length=255, null=True)
    wapokeaji = models.CharField(max_length=80, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Jumbe'


    def __str__(self):
        return f'{self.date_created}'

class UjumbeWaTangazoUlioFika(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="limefika_user")
    ujumbe = models.TextField(null=True)
    eneo = models.CharField(max_length=255, null=True)
    utambulisho_wa_ujumbe = models.CharField(max_length=255, null=True)
    nambari_ya_simu = models.CharField(max_length=80, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'UumbeZaTangazoZilizoFika'


    def __str__(self):
        return f'{self.date_created}'