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
    return render(request, 'dashboard/mtendaji.html', {})





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

        if not jina:
            messages.success(request, f'Tafadhali jaza jina')
            return render(request, 'wananchi/sajiri_mwananchi.html', {'mataifa': mataifa})

        if not nambari_ya_simu:
            messages.success(request, f'Tafadhali jaza nambari ya simu')
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

        mwananchi_data = Mwananchi.objects.create(jina=jina, nambari_ya_simu=nambari_ya_simu, nchi=nchi, mkoa=mkoa, wilaya=wilaya, kata=kata, mtaa=mtaa, barozi=ubarozi)
        messages.success(request, f'{mwananchi_data} amesajiriwa kikamilifu')
        return redirect('sajiri-mwananchi')




    