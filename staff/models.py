from django.db import models
from django.contrib.auth.models import User
from users.models import (
   Nchi, Wilaya, Mkoa, Mtendaji,
    Kata, Mtaa, Mjumbe, Mwananchi
    ) 



class MaeneoYaTangazo(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    orodha_ya_kutangazia = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'
        
class Tangazo(models.Model):
    CHAGUA_WALENGWA = (
        ('wote', 'wote'),
        ('wanaume', 'wanaume'),
        ('wanawake', 'wanawake'),
    )
    title = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="ujumbe_wa_tangazo_user")
    ujumbe = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now=True)
    kwa_ajili_ya = models.CharField(max_length=50, null=True, choices=CHAGUA_WALENGWA)
    ukanda_gani = models.CharField(max_length=420, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Matangazo'



class UjumbeWaTangazo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="tangazo_user")
    ujumbe = models.ForeignKey(Tangazo, on_delete=models.CASCADE, null=True)
    eneo = models.CharField(max_length=255, null=True)
    wapokeaji = models.CharField(max_length=80, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'JumbeZaMatangazo'


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
        verbose_name_plural = 'JumbeZaTangazoZilizoFika'


    def __str__(self):
        return f'{self.date_created}'