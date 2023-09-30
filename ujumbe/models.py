from django.db import models
from users.models import (
   Nchi, Wilaya, Mkoa, Mtendaji,
    Kata, Mtaa, Mjumbe, Mwananchi
    ) 




class Ujumbe(models.Model):
    mtendaji = models.ForeignKey(Mtendaji, on_delete=models.CASCADE, null=True, related_name="ujumbe_mtendaji")
    mjumbe = models.ForeignKey(Mjumbe, on_delete=models.CASCADE, null=True, related_name="ujumbe_mjumbe")
    ujumbe = models.TextField()
    wapokeaji = models.CharField(max_length=80, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Jumbe'




class UjumbeUliotumwa(models.Model):
    mtendaji = models.ForeignKey(Mtendaji, on_delete=models.CASCADE, null=True, related_name="zilizotumwa_mtendaji")
    mjumbe = models.ForeignKey(Mjumbe, on_delete=models.CASCADE, null=True, related_name="zilizotumwa_mjumbe")
    ujumbe = models.TextField(null=True)
    nambari_ya_simu = models.CharField(max_length=80, null=True, blank=True)
    is_deliverd = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'jumbeZilizotumwa'


    def __str__(self):
        return self.nambari_ya_simu