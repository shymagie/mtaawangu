from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
import json
import requests
from users.models import (
    Nchi, Wilaya, Mkoa, Mtendaji,
    Kata, Mtaa, Mjumbe, Mwananchi, NyumbaKumi, Mwenyekiti
)
from ujumbe import models as ujumbe_models
from accounts.decorators import allowed_user, mtendaji_tu
from ujumbe.fomu import FomuYaKutumaUjumbe


# sajiri nchi
def sajiriNchi(request):
    if request.method == 'POST':
        jina = request.POST.get('jina')
        nchi = request.POST.get('nchi')
        nchi = Nchi.objects.get(id=nchi)
        if not jina:
            messages.error(request, 'jina ni lazima kujazwa')
            return redirect('sajiri-nchi')
        if not nchi:
            messages.error(request, 'chagua nchi gani')
            return redirect('sajiri-nchi')
        mkoa = Mkoa.objects.create(jina=jina, wilaya=wilaya)
        messages.success(request, f'{mkoa} imesajiriwa kikamilifu')
        return redirect('sajiri-nchi')
    nchi = Nchi.objects.all()
    context = {'nchi': nchi}
    return render(request, 'meta/sajiri_nchi.html', context)


def sajiriMkoa(request):
    if request.method == "POST":
        jina = request.POST.get('jina')
        nchi = request.POST.get('nchi')
        nchi = Nchi.objects.get(id=nchi)
        if not jina:
            messages.error(request, 'jina ni lazima kujazwa')
            return redirect('sajiri-mkoa')
        if not nchi:
            messages.error(request, 'chagua nchi gani')
            return redirect('sajiri-mkoa')
        mkoa = Mkoa.objects.create(jina=jina, nchi=nchi)
        messages.success(request, f'{mkoa} imesajiriwa kikamilifu')
        return redirect('sajiri-mkoa')
    nchi = Nchi.objects.all()
    context = {'nchi': nchi}
    return render(request, 'meta/sajiri_nchi.html', context)


def sajiriWilaya(request):
    pass


def sajiriKata(request):
    if request.method == 'POST':
        jina = request.POST.get('jina')
        wilaya = request.POST.get('wilaya')
        wilaya = Wilaya.objects.get(id=wilaya)
        if not jina:
            messages.error(request, 'jina ni lazima kujazwa')
            return redirect('sajiri-kata')
        if not wilaya:
            messages.error(request, 'chagua wilaya gani')
            return redirect('sajiri-kata')
        kata = Kata.objects.create(jina=jina, wilaya=wilaya)
        messages.success(request, f'{kata} imesajiriwa kikamilifu')
        return redirect('sajiri-kata')
    wilaya = Wilaya.objects.all()
    context = {'wilaya': wilaya}
    return render(request, 'meta/sajiri_kata.html', context)


def sajiriMtaa(request):
    pass


def orodha_ya_nchi(request):
    return render(request, '', {})




def dashboard(request):
    return render(request, 'dashboard/index.html', {})




    