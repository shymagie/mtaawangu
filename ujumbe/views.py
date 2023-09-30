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




def tuma_kwa_mtaa(request):
    mitaa = Mtaa.objects.all()
    context = {
        'mitaa': mitaa,
    }
    return render(request, 'ujumbe/tuma_kwa_mtaa.html', context)

def tuma_kwa_kata(request):
    kata = Kata.objects.all()
    context = {
        'kata': kata,
    }
    return render(request, 'ujumbe/tuma_kwa_kata.html', context)

def tuma_kwa_barozi(request):
    barozi = NyumbaKumi.objects.all()
    context = {
        'barozi': barozi,
    }
    return render(request, 'ujumbe/tuma_kwa_barozi.html', context)



def orodha_ya_jumbe(request):
    jumbe = ujumbe_models.Ujumbe.objects.all()
    context = {
        'jumbe': jumbe,
    }
    return render(request, 'ujumbe/orodha.html', context)


def orodha_ya_jumbe_zilizotumwa(request):
    jumbe = ujumbe_models.UjumbeUliotumwa.objects.all()
    context = {
        'jumbe': jumbe,
    }
    return render(request, 'ujumbe/jumbe_zilizotumwa.html', context)

def tuma_ujumbe_kwa_mtaa(request):
    if request.method == "POST":
        mtaa = request.POST.get('mtaa')
        mtaa = Mtaa.objects.filter(jina=mtaa)
        for obj in mtaa:
            mtaa = obj.id
        form = FomuYaKutumaUjumbe()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(mtaa=mtaa)]))))
    return render(request, 'ujumbe/tuma_ujumbe.html', {'form': form})



def tuma_ujumbe_kwa_kata(request):
    if request.method == "POST":
        kata = request.POST.get('kata')
        kata = Kata.objects.filter(jina=kata)
        for obj in kata:
            kata = obj.id
        form = FomuYaKutumaUjumbe()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(kata=kata)]))))
    return render(request, 'ujumbe/tuma_ujumbe.html', {'form': form})


@allowed_user(allowed_role=['mtendaji'])
def tuma_ujumbe_kwa_barozi(request):
    if request.method == "POST":
        barozi = request.POST.get('barozi')
        barozi = NyumbaKumi.objects.filter(jina=barozi)
        for obj in barozi:
            barozi = obj.id
        form = FomuYaKutumaUjumbe()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(barozi=barozi)]))))
    return render(request, 'ujumbe/tuma_ujumbe.html', {'form': form})



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
            print(data)
            text_message = ujumbe_models.Ujumbe.objects.create(wapokeaji=wapokeaji, ujumbe=ujumbe)
            messages.success(request, f'message success')
            return JsonResponse({'data': data})
        else:
            messages.error(request, 'something went wring') 
            return render(request, 'ujumbe/tuma_ujumbe.html')
    return render(request, 'ujumbe/tuma_ujumbe.html')



def kusajiri_mwananchi(request):
    mataifa = Nchi.objects.all()
    return render(request, 'wananchi/sajiri_mwananchi.html', {'mataifa': mataifa})

def orodha_ya_wananchi(request):
    wananchi = Mwananchi.objects.all()
    return render(request, 'wananchi/orodha_ya_wananchi.html', {'wananchi': wananchi})



def mikoa_na_ajax(request):
    if request.method == "POST":
        nchi_id = request.POST.get('nchi_id')
        nchi = Nchi.objects.get(id=nchi_id)
        mikoa = nchi.mkoa_ya_nchi.all()

        data = []
        for obj in mikoa:
            item = {
                'id': obj.id,
                'jina': obj.jina
            }
            data.append(item)
        
        return JsonResponse({'mikoa': data})


def wilaya_na_ajax(request):
    if request.method == "POST":
        mkoa_id = request.POST.get('mkoa_id')
        mkoa = Mkoa.objects.get(id=mkoa_id)
        wilaya = mkoa.wilaya_mikoa.all()
        print(wilaya)
        data = []
        for obj in wilaya:
            item = {
                'id': obj.id,
                'jina': obj.jina
            }
            data.append(item)
        
        return JsonResponse({'wilaya': data})



def kata_na_ajax(request):
    if request.method == "POST":
        wilaya_id = request.POST.get('wilaya_id')
        wilaya = Wilaya.objects.get(id=wilaya_id)
        kata = wilaya.kata_wilaya.all()
        print(wilaya)
        data = []
        for obj in kata:
            item = {
                'id': obj.id,
                'jina': obj.jina
            }
            data.append(item)
        
        return JsonResponse({'kata': data})



def mtaa_na_ajax(request):
    if request.method == "POST":
        kata_id = request.POST.get('kata_id')
        kata = Kata.objects.get(id=kata_id)
        mitaa = kata.mitaa_kata.all()
        print(mitaa)
        data = []
        for obj in mitaa:
            item = {
                'id': obj.id,
                'jina': obj.jina
            }
            data.append(item)
        
        return JsonResponse({'mitaa': data})



def ubarozi_na_ajax(request):
    if request.method == "POST":
        mtaa_id = request.POST.get('mtaa_id')
        mtaa = Mtaa.objects.get(id=mtaa_id)
        barozi = mtaa.barozi_mitaa.all()
        print(barozi)
        data = []
        for obj in barozi:
            item = {
                'id': obj.id,
                'jina': obj.jina
            }
            data.append(item)
        
        return JsonResponse({'barozi': data})




def hifadhi_mwananchi(request):
    if request.method == "POST":
        jina = request.POST.get('jina')
        nambari_ya_simu = request.POST.get('nambari_ya_simu')
        nchi_id = request.POST.get('nchi')
        mkoa_id = request.POST.get('mkoa')
        wilaya_id = request.POST.get('wilaya')
        kata_id = request.POST.get('kata')
        mtaa_id = request.POST.get('mtaa')
        ubarozi_id = request.POST.get('ubarozi')

        nchi = Nchi.objects.get(id=nchi_id)
        mkoa = Mkoa.objects.get(id=mkoa_id)
        wilaya = Wilaya.objects.get(id=wilaya_id)
        kata = Kata.objects.get(id=kata_id)
        mtaa = Mtaa.objects.get(id=mtaa_id)
        ubarozi = NyumbaKumi.objects.get(id=ubarozi_id)

        mwananchi_data = Mwananchi.objects.create(jina=jina, nambari_ya_simu=nambari_ya_simu, nchi=nchi, mkoa=mkoa, wilaya=wilaya, kata=kata, mtaa=mtaa, barozi=ubarozi)
        messages.success(request, f'{mwananchi_data} amesajiriwa kikamilifu')
        return redirect('sajiri-mwananchi')



def hifadhi_jumbe_zilizotumwa_ajax(request):
    if request.method == "POST":
        ujumbe = request.POST.get('ujumbe')
        nambari_ya_simu = request.POST.get('nambari_ya_simu')
        status = request.POST.get('status')
        print(nambari_ya_simu)
        is_delivered = False 
        if status == "Delivered":
            is_delivered = True
        ujumbe_data = ujumbe_models.UjumbeUliotumwa.objects.create(ujumbe=ujumbe, nambari_ya_simu=nambari_ya_simu, is_delivered=is_delivered)
        return JsonResponse({})
    