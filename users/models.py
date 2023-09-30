from django.db import models
from django.contrib.auth.models import User



class Nchi(models.Model):
    jina = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.jina

    class Meta:
        verbose_name_plural = 'Nchi'


class Mkoa(models.Model):
    jina = models.CharField(max_length=200, null=True, blank=True)
    nchi = models.ForeignKey('Nchi', on_delete=models.CASCADE, default='Tanzania', related_name="mkoa_ya_nchi")

    def __str__(self):
        return self.jina


    class Meta:
        verbose_name_plural = 'Mikoa'


class Wilaya(models.Model):
    jina = models.CharField(max_length=200, null=True, blank=True)
    mkoa = models.ForeignKey('Mkoa', on_delete=models.CASCADE, related_name="wilaya_mikoa")

    def __str__(self):
        return self.jina

    class Meta:
        verbose_name_plural = 'Wilaya'



class Kata(models.Model):
    jina = models.CharField(max_length=200, null=True, blank=True)
    wilaya = models.ForeignKey('Wilaya', on_delete=models.CASCADE, null=True, blank=True, related_name="kata_wilaya")

    def __str__(self):
        return self.jina

    class Meta:
        verbose_name_plural = 'Kata'


class Mtaa(models.Model):
    jina = models.CharField(max_length=200, null=True, blank=True)
    kata = models.ForeignKey('Kata', on_delete=models.CASCADE, related_name="mitaa_kata")

    def __str__(self):
        return self.jina

    class Meta:
        verbose_name_plural = 'Mitaa'


class NyumbaKumi(models.Model):
    jina = models.CharField(max_length=200, null=True, blank=True)
    mtaa = models.ForeignKey('Mtaa', on_delete=models.CASCADE, null=True, related_name="barozi_mitaa")

    def __str__(self):
        return self.jina

    class Meta:
        verbose_name_plural = 'NyumbaKumi'


class Mtendaji(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    jina = models.CharField(max_length=200, null=True, blank=True)
    nambari_ya_simu = models.CharField(max_length=200, null=True, blank=True)
    barua_pepe = models.CharField(max_length=200, null=True, blank=True)
    mtaa = models.ForeignKey('Mtaa', on_delete=models.CASCADE, null=True, blank=True, related_name="mtendaji_mtaa")
    kata = models.ForeignKey('Kata', on_delete=models.CASCADE, null=True, blank=True, related_name="mtendaji_kata")
    wilaya = models.ForeignKey('Wilaya', on_delete=models.CASCADE, null=True, blank=True, related_name="mtendaji_wilaya")
    mkoa = models.ForeignKey('Mkoa', on_delete=models.CASCADE, null=True, blank=True, related_name="mtendaji_mkoa")
    nchi = models.ForeignKey('Nchi', on_delete=models.CASCADE, null=True, blank=True, related_name="mtendaji_nchi")

    class Meta:
        verbose_name_plural = 'Watendaji'

    def __str__(self):
        return self.jina


class Mwenyekiti(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    mtendaji = models.ForeignKey('Mtendaji', on_delete=models.CASCADE, null=True, blank=True, related_name="mwenyekiti_mtendaji")
    jina = models.CharField(max_length=200, null=True, blank=True)
    nambari_ya_simu = models.CharField(max_length=200, null=True, blank=True)
    barua_pepe = models.CharField(max_length=200, null=True, blank=True)
    nchi = models.ForeignKey('Nchi', on_delete=models.CASCADE, null=True, blank=True, related_name="mwenyekiti_nchi")
    mkoa = models.ForeignKey('Mkoa', on_delete=models.CASCADE, null=True, blank=True, related_name="mwenyekiti_mkoa")
    wilaya = models.ForeignKey('Wilaya', on_delete=models.CASCADE, null=True, blank=True, related_name="mwenyekiti_wilaya")
    kata = models.ForeignKey('Kata', on_delete=models.CASCADE, null=True, blank=True, related_name="mwenyekiti_kata")
    mtaa = models.ForeignKey('Mtaa', on_delete=models.CASCADE, null=True, blank=True, related_name="mwenyekiti_mtaa")
    nyumba_kumi = models.ForeignKey('NyumbaKumi', on_delete=models.CASCADE, null=True, blank=True, related_name="mwenyekiti_nyumba_kumi")

    class Meta:
        verbose_name_plural = 'Wenyeviti'

    def __str__(self):
        return self.jina


class Mjumbe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    mtendaji = models.ForeignKey('Mtendaji', on_delete=models.CASCADE, null=True, blank=True, related_name="mjumbe_mtendaji")
    mwenyekiti = models.ForeignKey('Mwenyekiti', on_delete=models.CASCADE, null=True, blank=True, related_name="mjumbe_mwenyekiti")
    jina = models.CharField(max_length=200, null=True, blank=True)
    nambari_ya_simu = models.CharField(max_length=200, null=True, blank=True)
    barua_pepe = models.CharField(max_length=200, null=True, blank=True)
    nchi = models.ForeignKey('Nchi', on_delete=models.CASCADE, null=True, blank=True, related_name="mjumbe_nchi")
    mkoa = models.ForeignKey('Mkoa', on_delete=models.CASCADE, null=True, blank=True, related_name="mjumbe_mkoa")
    wilaya = models.ForeignKey('Wilaya', on_delete=models.CASCADE, null=True, blank=True, related_name="mjumbe_wilaya")
    kata = models.ForeignKey('Kata', on_delete=models.CASCADE, null=True, blank=True, related_name="mjumbe_kata")
    mtaa = models.ForeignKey('Mtaa', on_delete=models.CASCADE, null=True, blank=True, related_name="mjumbe_mtaa")
    barozi = models.ForeignKey('NyumbaKumi', on_delete=models.CASCADE, null=True, blank=True, related_name="mjumbe_barozi")
    class Meta:
        verbose_name_plural = 'Wajumbe'

    def __str__(self):
        return self.jina



class Mwananchi(models.Model):
    jina = models.CharField(max_length=200, null=True, blank=True)
    mtendaji = models.ForeignKey('Mtendaji', on_delete=models.CASCADE, null=True, blank=True, related_name="mwananchi_mtendaji")
    mjumbe = models.ForeignKey('Mjumbe', on_delete=models.CASCADE, null=True, blank=True, related_name="mwananchi_mjumbe")
    nambari_ya_simu = models.CharField(max_length=200, null=True, blank=True)
    barua_pepe = models.CharField(max_length=200, null=True, blank=True)
    nchi = models.ForeignKey('Nchi', on_delete=models.CASCADE, null=True, blank=True, related_name="mwananchi_nchi")
    mkoa = models.ForeignKey('Mkoa', on_delete=models.CASCADE, null=True, blank=True, related_name="mwananchi_mkoa")
    wilaya = models.ForeignKey('Wilaya', on_delete=models.CASCADE, null=True, blank=True, related_name="mwananchi_wilaya")
    kata = models.ForeignKey('Kata', on_delete=models.CASCADE, null=True, blank=True, related_name="mwananchi_kata")
    mtaa = models.ForeignKey('Mtaa', on_delete=models.CASCADE, null=True, blank=True, related_name="mwananchi_mtaa")
    barozi = models.ForeignKey('NyumbaKumi', on_delete=models.CASCADE, null=True, blank=True, related_name="mwananchi_barozi")

    class Meta:
        verbose_name_plural = 'Wananchi'


    def __str__(self):
        return self.jina