from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json
import requests
from users.models import (
    Nchi, Wilaya, Mkoa, Mtendaji,
    Kata, Mtaa, Mjumbe, Mwananchi, NyumbaKumi, Mwenyekiti
)
from ujumbe import models as ujumbe_models
from accounts.decorators import allowed_user, mjumbe_tu
from ujumbe.fomu import FomuYaKutumaUjumbe


@login_required
@mjumbe_tu
def dashboard(request):
    return render(request, 'dashboard/mjumbe.html', {})

@login_required
@mjumbe_tu
def tuma_kwa_mtaa(request):
    mjumbe = request.user.mjumbe
    mtaa = mjumbe.mtaa
    context = {
        'mtaa': mtaa,
    }
    return render(request, 'mjumbe/tuma_kwa_mtaa.html', context)
@login_required
@mjumbe_tu
def tuma_kwa_kata(request):
    mjumbe = request.user.mjumbe
    kata_id = mjumbe.kata.id
    kata = Kata.objects.get(id=kata_id)
    context = {
        'kata': kata,
    }
    return render(request, 'mjumbe/tuma_kwa_kata.html', context)
@login_required
@mjumbe_tu
def tuma_kwa_barozi(request):
    barozi = NyumbaKumi.objects.all()
    context = {
        'barozi': barozi,
    }
    return render(request, 'mjumbe/tuma_kwa_barozi.html', context)


@login_required
@mjumbe_tu
def orodha_ya_jumbe(request):
    mjumbe = request.user.mjumbe
    kata = mjumbe.kata
    jumbe = ujumbe_models.Ujumbe.objects.filter(kata=kata)
    context = {
        'jumbe': jumbe,
    }
    return render(request, 'mjumbe/orodha.html', context)

@login_required
@mjumbe_tu
def orodha_ya_jumbe_zilizotumwa(request):
    mjumbe = request.user.mjumbe
    kata = mjumbe.kata
    jumbe = ujumbe_models.UjumbeUliotumwa.objects.filter(kata=kata)
    context = {
        'jumbe': jumbe,
    }
    return render(request, 'mjumbe/jumbe_zilizotumwa.html', context)
@login_required
@mjumbe_tu
def tuma_ujumbe_kwa_mtaa(request):
    if request.method == "POST":
        mtaa = request.POST.get('mtaa')
        mtaa = Mtaa.objects.filter(jina=mtaa)
        for obj in mtaa:
            mtaa = obj.id
        form = FomuYaKutumaUjumbe()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(mtaa=mtaa)]))))
    return render(request, 'mjumbe/tuma_ujumbe.html', {'form': form})


@login_required
@mjumbe_tu
def tuma_ujumbe_kwa_kata(request):
    if request.method == "POST":
        kata = request.POST.get('kata')
        kata = Kata.objects.filter(jina=kata)
        for obj in kata:
            kata = obj.id
        form = FomuYaKutumaUjumbe()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(kata=kata)]))))
    return render(request, 'mjumbe/tuma_ujumbe.html', {'form': form})


@login_required
@mjumbe_tu
def tuma_ujumbe_kwa_barozi(request):
    if request.method == "POST":
        barozi = request.POST.get('barozi')
        barozi = NyumbaKumi.objects.filter(jina=barozi)
        for obj in barozi:
            barozi = obj.id
        form = FomuYaKutumaUjumbe()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(barozi=barozi)]))))
    return render(request, 'mjumbe/tuma_ujumbe.html', {'form': form})



@login_required
@mjumbe_tu
def tuma_ujumbe(request):
    response = {}
    if request.method == "POST":
        form = FomuYaKutumaUjumbe(request.POST)
        wapokeaji = request.POST.get('wapokeaji')
        ujumbe = request.POST.get('ujumbe')
        mjumbe = request.user.mjumbe
        kata = mjumbe.kata
       
        data = json.dumps({
            "recipient": wapokeaji,
            "sender_id": "BONGASMS",
            "type": "plain",
            "message": ujumbe,
        })
        headers = {
            "Authorization": "Bearer 66|nESGtIih5PoRtO07CPVnbSEfM51WDW0FyisXGUjL",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.post('https://app.bonga.co.tz/api/v3/sms/send', data=data, headers=headers)
        if response.status_code == 200:
            r = response.json()
            data = r['data']
            text_message = ujumbe_models.Ujumbe.objects.create(kata=kata, user=request.user, wapokeaji=wapokeaji, ujumbe=ujumbe)
            messages.success(request, f'message success')
            return JsonResponse({'data': data})
        else:
            messages.error(request, 'something went wring') 
            return render(request, 'mjumbe/tuma_ujumbe.html')
    return render(request, 'mjumbe/tuma_ujumbe.html')




@login_required
@mjumbe_tu
def hifadhi_jumbe_zilizotumwa_ajax(request):
    if request.method == "POST":
        ujumbe = request.POST.get('ujumbe')
        uid = request.POST.get('utu')
        nambari_ya_simu = request.POST.get('nambari_ya_simu')
        status = request.POST.get('status')
        mjumbe = request.user.mjumbe
        kata = mjumbe.kata
        is_delivered = False 
        if status == "Delivered":
            is_delivered = True
        ujumbe_data = ujumbe_models.UjumbeUliotumwa.objects.create(kata=kata, user=request.user, ujumbe=ujumbe, nambari_ya_simu=nambari_ya_simu, is_delivered=is_delivered, utambulisho_wa_ujumbe=uid)
        return JsonResponse({})