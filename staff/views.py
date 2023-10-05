from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
import json
import requests
from users.models import (
    Nchi, Wilaya, Mkoa, Mtendaji,
    Kata, Mtaa, Mjumbe, Mwananchi, NyumbaKumi, Mwenyekiti
)
from staff import models as tangazo_models
from accounts.decorators import allowed_user, staff_tu
from ujumbe.fomu import FomuYaKutumaUjumbe


@login_required
@staff_tu
def dashboard(request):
    return render(request, 'dashboard/staff.html', {})

@login_required
@staff_tu
def tuma_kwa_mtaa(request):
    mitaa = Mtaa.objects.all()
    context = {
        'mitaa': mitaa,
    }
    return render(request, 'staff/tuma_kwa_mtaa.html', context)

@login_required
@staff_tu
def tuma_kwa_kata(request):
    kata = Kata.objects.all()
    context = {
        'kata': kata,
    }
    return render(request, 'staff/tuma_kwa_kata.html', context)


@login_required
@staff_tu
def tuma_kwa_barozi(request):
    barozi = NyumbaKumi.objects.all()
    context = {
        'barozi': barozi,
    }
    return render(request, 'staff/tuma_kwa_barozi.html', context)



@login_required
@staff_tu
def orodha_ya_jumbe(request):
    jumbe = tangazo_models.UjumbeWaTangazo.objects.all()
    context = {
        'jumbe': jumbe,
    }
    return render(request, 'staff/orodha.html', context)

@login_required
@staff_tu
def orodha_ya_jumbe_zilizotumwa(request):
    jumbe = tangazo_models.UjumbeWaTangazoUlioFika.objects.all()
    context = {
        'jumbe': jumbe,
    }
    return render(request, 'staff/jumbe_zilizotumwa.html', context)


@login_required
@staff_tu
def tuma_ujumbe_kwa_mtaa(request):
    if request.method == "POST":
        mtaa = request.POST.get('mtaa')
        mtaa = Mtaa.objects.filter(jina=mtaa)
        for obj in mtaa:
            mtaa = obj.id
        form = FomuYaKutumaUjumbe()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(mtaa=mtaa)]))))
    return render(request, 'staff/tuma_ujumbe.html', {'form': form})



@login_required
@staff_tu
def tuma_ujumbe_kwa_kata(request):
    if request.method == "POST":
        kata = request.POST.get('kata')
        kata = Kata.objects.filter(jina=kata)
        for obj in kata:
            kata = obj.id
        form = FomuYaKutumaUjumbe()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(kata=kata)]))))
    return render(request, 'staff/tuma_ujumbe.html', {'form': form})


@login_required
@staff_tu
def tuma_ujumbe_kwa_barozi(request):
    if request.method == "POST":
        barozi = request.POST.get('barozi')
        barozi = NyumbaKumi.objects.filter(jina=barozi)
        for obj in barozi:
            barozi = obj.id
        form = FomuYaKutumaUjumbe()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(barozi=barozi)]))))
    return render(request, 'staff/tuma_ujumbe.html', {'form': form})




@login_required
@staff_tu
def tuma_ujumbe(request):
    response = {}
    if request.method == "POST":
        form = FomuYaKutumaUjumbe(request.POST)
        wapokeaji = request.POST.get('wapokeaji')
        ujumbe = request.POST.get('ujumbe')
       
       
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
            text_message = tangazo_models.UjumbeWaTangazo.objects.create(wapokeaji=wapokeaji, ujumbe=ujumbe, user=request.user)
            messages.success(request, f'message success')
            return JsonResponse({'data': data})
        else:
            messages.error(request, 'something went wring') 
            return render(request, 'staff/tuma_ujumbe.html')
    return render(request, 'staff/tuma_ujumbe.html')






@login_required
@staff_tu
def hifadhi_jumbe_zilizotumwa_ajax(request):
    if request.method == "POST":
        ujumbe = request.POST.get('ujumbe')
        uid = request.POST.get('utu')
        nambari_ya_simu = request.POST.get('nambari_ya_simu')
        status = request.POST.get('status')
        is_delivered = False 
        if status == "Delivered":
            is_delivered = True
        ujumbe_data = tangazo_models.UjumbeWaTangazoUlioFika.objects.create(ujumbe=ujumbe, nambari_ya_simu=nambari_ya_simu, is_delivered=is_delivered, utambulisho_wa_ujumbe=uid, user=request.user)
        return JsonResponse({})






# USAJILI MTENDAJI, MWENYEKITI, MJUMBE N.K 


def mtendaji_registration(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if not username:
            pass
        if not email:
            pass 
        if not password1:
            pass 
        if not password2:
            pass
        if not first_name:
            pass 
        if not last_name:
            pass
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
            return redirect('sajiri-mtendaji', user.id)
    return render(request, '', context)

def kusajiri_mtendaji(request, pk):
    user = User.objects.get(id=pk)
    mataifa = Nchi.objects.all()
    return render(request, 'staff/usajiri/sajiri_mtendaji.html', {'mataifa': mataifa})


def kusajiri_mjumbe(request, pk):
    user = User.objects.get(id=pk)
    mataifa = Nchi.objects.all()
    return render(request, 'staff/usajiri/sajiri_mjumbe.html', {'mataifa': mataifa})


def kusajiri_mwenyekiti(request, pk):
    user = User.objects.get(id=pk)
    mataifa = Nchi.objects.all()
    return render(request, 'staff/usajiri/sajiri_mwenyekiti.html', {'mataifa': mataifa})

def hifadhi_mtendaji(request):
    mataifa = Nchi.objects.all()
    if request.method == "POST":
        jina = request.POST.get('jina')
        nambari_ya_simu = request.POST.get('nambari_ya_simu')
        nchi_id = request.POST.get('nchi')
        mkoa_id = request.POST.get('mkoa')
        wilaya_id = request.POST.get('wilaya')
        kata_id = request.POST.get('kata')
        mtaa_id = request.POST.get('mtaa')
        ubarozi_id = request.POST.get('ubarozi')
        jinsia = request.POST.get('jinsia')

        if not jina:
            messages.success(request, f'Tafadhali jaza jina')
            return render(request, 'wananchi/sajiri_mwananchi.html', {'mataifa': mataifa})
        

        if not nambari_ya_simu:
            messages.success(request, f'Tafadhali jaza nambari ya simu')
            return render(request, 'wananchi/sajiri_mwananchi.html', {'mataifa': mataifa})

        if ubarozi_id == '--------Chagua jinsia---------':
            messages.success(request, f'Tafadhali chagua jinsia')
            return render(request, 'wananchi/sajiri_mwananchi.html', {'mataifa': mataifa})

        if ubarozi_id == '--------Chagua ubarozi---------':
            messages.success(request, f'Tafadhali chagua ubarozi')
            return render(request, 'wananchi/sajiri_mwananchi.html', {'mataifa': mataifa})

        if wilaya_id == '--------Chagua wilaya---------':
            messages.success(request, f'Tafadhali chagua wilaya')
            return render(request, 'wananchi/sajiri_mwananchi.html', {'mataifa': mataifa})

        if kata_id == '--------Chagua kata---------':
            messages.success(request, f'Tafadhali chagua kata')
            return render(request, 'wananchi/sajiri_mwananchi.html', {'mataifa': mataifa})

        if mtaa_id == '--------Chagua mtaa---------':
            messages.success(request, f'Tafadhali chagua mtaa')
            return render(request, 'wananchi/sajiri_mwananchi.html', {'mataifa': mataifa})

        nchi = Nchi.objects.get(id=nchi_id)
        mkoa = Mkoa.objects.get(id=mkoa_id)
        wilaya = Wilaya.objects.get(id=wilaya_id)
        kata = Kata.objects.get(id=kata_id)
        mtaa = Mtaa.objects.get(id=mtaa_id)
        ubarozi = NyumbaKumi.objects.get(id=ubarozi_id)

        mtendaji_data = Mtendaji.objects.create(jina=jina, nambari_ya_simu=nambari_ya_simu, nchi=nchi, mkoa=mkoa, wilaya=wilaya, kata=kata, jinsia=jinsia, mtaa=mtaa, barozi=ubarozi)
        messages.success(request, f'{mwananchi_data} amesajiriwa kikamilifu')
        return redirect('sajiri-mwananchi')
