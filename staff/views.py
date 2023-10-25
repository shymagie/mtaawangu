from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
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
from staff.fomu import FomuYaKutumaTangazo


@login_required
@staff_tu
def dashboard(request):
    return render(request, 'dashboard/staff.html', {})

@login_required
@staff_tu
def tuma_kwa_mtaa(request):
    nchi = Nchi.objects.all()
    context = {
        'mataifa': nchi,
    }
    return render(request, 'staff/tuma_kwa_mtaa.html', context)

@login_required
@staff_tu
def tuma_kwa_kata(request):
    nchi = Nchi.objects.all()
    context = {
        'mataifa': nchi,
    }
    return render(request, 'staff/tuma_kwa_kata.html', context)


@login_required
@staff_tu
def tuma_kwa_barozi(request):
    nchi = Nchi.objects.all()
    context = {
        'mataifa': nchi,
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
        if mtaa == '------chagua mtaa------':
            return redirect('staff-tuma-kwa-mtaa')
        mtaa = Mtaa.objects.get(id=mtaa)
        form = FomuYaKutumaTangazo()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(mtaa=mtaa)]))))
    return render(request, 'staff/tuma_ujumbe.html', {'form': form})



@login_required
@staff_tu
def tuma_ujumbe_kwa_kata(request):
    if request.method == "POST":
        kata = request.POST.get('kata')
        if kata == '------chagua kata------':
            return redirect('staff-tuma-kwa-kata')
        kata = Kata.objects.get(id=kata)
        form = FomuYaKutumaTangazo()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(kata=kata)]))))
    return render(request, 'staff/tuma_ujumbe.html', {'form': form})


@login_required
@staff_tu
def tuma_ujumbe_kwa_barozi(request):
    if request.method == "POST":
        barozi_id = request.POST.get('ubarozi')
        if barozi_id == '------chagua ubarozi------':
            return redirect('staff-tuma-kwa-barozi')
        barozi = NyumbaKumi.objects.get(id=barozi_id)
        form = FomuYaKutumaTangazo()
        form.fields['wapokeaji'].initial = ','.join(list(set(map(str, [active.nambari_ya_simu for active in Mwananchi.objects.filter(barozi=barozi)]))))
    return render(request, 'staff/tuma_ujumbe.html', {'form': form})




@login_required
@staff_tu
def tuma_ujumbe(request):
    response = {}
    if request.method == "POST":
        form = FomuYaKutumaTangazo(request.POST)
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


@login_required
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
        # if User.objects.get(username=username).exists():
        #     messages.success(request, 'Jina limeshatumika, tafadhali chagua jina jingine')
        #     return render(request, 'staff/usajiri/mtendaji-sign-up.html')
        group = Group.objects.get(name='mtendaji')
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
            user.groups.add(group)
            return redirect('sajiri-mtendaji', user.id)
    return render(request, 'staff/usajiri/mtendaji-sign-up.html')


@login_required
def mwenyekiti_registration(request):
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
        if User.objects.get(username=username).exists():
            messages.success(request, 'Jina limeshatumika, tafadhali chagua jina jingine')
            return render(request, 'staff/usajiri/mtendaji-sign-up.html')
        group = Group.objects.get(name='mwenyekiti')
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
            user.groups.add(group)
            return redirect('sajiri-mwenyekiti', user.id)
    return render(request, 'staff/usajiri/mwenyekiti-sign-up.html')


@login_required
def mjumbe_registration(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if not username:
            messages.success(request, 'tafadhali jaza jina la mtumiaji')
            return render(request, 'staff/usajiri/mtendaji-sign-up.html')
        if not email:
            messages.success(request, 'tafadhali jaza barua pepe')
            return render(request, 'staff/usajiri/mtendaji-sign-up.html')
        if not password1:
            messages.success(request, 'tafadhali jaza nywila')
            return render(request, 'staff/usajiri/mtendaji-sign-up.html') 
        if not password2:
            messages.success(request, 'tafadhali rudia nywila')
            return render(request, 'staff/usajiri/mtendaji-sign-up.html')
        if not first_name:
            messages.success(request, 'tafadhali jaza jina la kwanzo')
            return render(request, 'staff/usajiri/mtendaji-sign-up.html') 
        if not last_name:
            messages.success(request, 'tafadhali jaza jina la mwisho')
            return render(request, 'staff/usajiri/mtendaji-sign-up.html')
        if User.objects.get(username=username).exists():
            messages.success(request, 'Jina la mtumiaji limeshatumika, tafadhali chagua jina jingine')
            return render(request, 'staff/usajiri/mtendaji-sign-up.html')
        group = Group.objects.get(name='mjumbe')
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
            user.groups.add(group)
            return redirect('sajiri-mjumbe', user.id)
    return render(request, 'staff/usajiri/mjumbe-sign-up.html')

@login_required
def kusajiri_mtendaji(request, pk):
    user = User.objects.get(id=pk)
    jina = f'{user.first_name} {user.last_name}'
    user_id = user.id 
    mataifa = Nchi.objects.all()
    return render(request, 'staff/usajiri/sajiri_mtendaji.html', {'mataifa': mataifa, 'jina': jina, 'user_id': user_id})



@login_required
def kusajiri_mjumbe(request, pk):
    user = User.objects.get(id=pk)
    jina = f'{user.first_name} {user.last_name}'
    watendaji = Mtendaji.objects.all()
    wenyeviti = Mwenyekiti.objects.all()
    user_id = user.id 
    mataifa = Nchi.objects.all()
    return render(request, 'staff/usajiri/sajiri_mjumbe.html', {
        'mataifa': mataifa, 
        'jina': jina,
        'user_id': user_id,
        'wenyeviti': wenyeviti,
        'watendaji': watendaji,
        })


@login_required
def kusajiri_mwenyekiti(request, pk):
    user = User.objects.get(id=pk)
    jina = f'{user.first_name} {user.last_name}'
    watendaji = Mtendaji.objects.all()
    user_id = user.id 
    mataifa = Nchi.objects.all()
    return render(request, 'staff/usajiri/sajiri_mwenyekiti.html', {'mataifa': mataifa, 'jina': jina, 'user_id': user_id, 'watendaji':watendaji})

@login_required
def hifadhi_mtendaji(request):
    mataifa = Nchi.objects.all()
    if request.method == "POST":
        jina = request.POST.get('jina')
        user_id = request.POST.get('user_id')
        nambari_ya_simu = request.POST.get('nambari_ya_simu')
        nchi_id = request.POST.get('nchi')
        mkoa_id = request.POST.get('mkoa')
        wilaya_id = request.POST.get('wilaya')
        kata_id = request.POST.get('kata')
        mtaa_id = request.POST.get('mtaa')
        ubarozi_id = request.POST.get('ubarozi')
        jinsia = request.POST.get('jinsia')

        user = User.objects.get(id=user_id)

        if not jina:
            messages.success(request, f'Tafadhali jaza jina')
            return render(request, 'staff/usajiri/sajiri_mtendaji.html', {'mataifa': mataifa})
        

        if not nambari_ya_simu:
            messages.success(request, f'Tafadhali jaza nambari ya simu')
            return render(request, 'staff/usajiri/sajiri_mtendaji.html', {'mataifa': mataifa})

        if jinsia == '--------Chagua jinsia---------':
            messages.success(request, f'Tafadhali chagua jinsia')
            return render(request, 'staff/usajiri/sajiri_mtendaji.html', {'mataifa': mataifa})


        if wilaya_id == '--------Chagua wilaya---------':
            messages.success(request, f'Tafadhali chagua wilaya')
            return render(request, 'staff/usajiri/sajiri_mtendaji.html', {'mataifa': mataifa})

        if kata_id == '--------Chagua kata---------':
            messages.success(request, f'Tafadhali chagua kata')
            return render(request, 'staff/usajiri/sajiri_mtendaji.html', {'mataifa': mataifa})

        if mtaa_id == '--------Chagua mtaa---------':
            messages.success(request, f'Tafadhali chagua mtaa')
            return render(request, 'staff/usajiri/sajiri_mtendaji.html', {'mataifa': mataifa})

        nchi = Nchi.objects.get(id=nchi_id)
        mkoa = Mkoa.objects.get(id=mkoa_id)
        wilaya = Wilaya.objects.get(id=wilaya_id)
        kata = Kata.objects.get(id=kata_id)
        mtaa = Mtaa.objects.get(id=mtaa_id)
        ubarozi = NyumbaKumi.objects.get(id=ubarozi_id)
        mtendaji_data = Mtendaji.objects.create(jina=jina, user=user, barozi=ubarozi, nambari_ya_simu=nambari_ya_simu, nchi=nchi, mkoa=mkoa, wilaya=wilaya, kata=kata, jinsia=jinsia, mtaa=mtaa)
        messages.success(request, f'{mtendaji_data} amesajiriwa kikamilifu')
        return redirect('staff-dashibodi')





@login_required
def hifadhi_mwenyekiti(request):
    mataifa = Nchi.objects.all()
    if request.method == "POST":
        jina = request.POST.get('jina')
        user_id = request.POST.get('user_id')
        nambari_ya_simu = request.POST.get('nambari_ya_simu')
        nchi_id = request.POST.get('nchi')
        mkoa_id = request.POST.get('mkoa')
        wilaya_id = request.POST.get('wilaya')
        mtendaji_id = request.POST.get('mtendaji')
        kata_id = request.POST.get('kata')
        mtaa_id = request.POST.get('mtaa')
        ubarozi_id = request.POST.get('ubarozi')
        jinsia = request.POST.get('jinsia')

        user = User.objects.get(id=user_id)

        if not jina:
            messages.success(request, f'Tafadhali jaza jina')
            return render(request, 'staff/usajiri/sajiri_mwenyekiti.html', {'mataifa': mataifa})
        

        if not nambari_ya_simu:
            messages.success(request, f'Tafadhali jaza nambari ya simu')
            return render(request, 'staff/usajiri/sajiri_mwenyekiti.html', {'mataifa': mataifa})

        if jinsia == '--------Chagua jinsia---------':
            messages.success(request, f'Tafadhali chagua jinsia')
            return render(request, 'staff/usajiri/sajiri_mwenyekiti.html', {'mataifa': mataifa})


        if wilaya_id == '--------Chagua wilaya---------':
            messages.success(request, f'Tafadhali chagua wilaya')
            return render(request, 'staff/usajiri/sajiri_mwenyekiti.html', {'mataifa': mataifa})

        if kata_id == '--------Chagua kata---------':
            messages.success(request, f'Tafadhali chagua kata')
            return render(request, 'staff/usajiri/sajiri_mwenyekiti.html', {'mataifa': mataifa})

        if mtaa_id == '--------Chagua mtaa---------':
            messages.success(request, f'Tafadhali chagua mtaa')
            return render(request, 'staff/usajiri/sajiri_mwenyekiti.html', {'mataifa': mataifa})

        nchi = Nchi.objects.get(id=nchi_id)
        mkoa = Mkoa.objects.get(id=mkoa_id)
        wilaya = Wilaya.objects.get(id=wilaya_id)
        kata = Kata.objects.get(id=kata_id)
        mtaa = Mtaa.objects.get(id=mtaa_id)
        mtendaji = Mtendaji.objects.get(id=mtendaji_id)
        ubarozi = NyumbaKumi.objects.get(id=ubarozi_id)
        mwenyekiti_data = Mwenyekiti.objects.create(jina=jina, mtendaji=mtendaji, user=user, nambari_ya_simu=nambari_ya_simu, nchi=nchi, mkoa=mkoa, wilaya=wilaya, kata=kata, jinsia=jinsia, mtaa=mtaa, barozi=ubarozi)
        messages.success(request, f'{mwenyekiti_data} amesajiriwa kikamilifu')
        return redirect('staff-dashibodi')






@login_required
def hifadhi_mjumbe(request):
    mataifa = Nchi.objects.all()
    if request.method == "POST":
        jina = request.POST.get('jina')
        user_id = request.POST.get('user_id')
        nambari_ya_simu = request.POST.get('nambari_ya_simu')
        nchi_id = request.POST.get('nchi')
        mkoa_id = request.POST.get('mkoa')
        mtendaji_id = request.POST.get('mtendaji')
        mwenyekiti_id = request.POST.get('mwenyekiti')
        wilaya_id = request.POST.get('wilaya')
        kata_id = request.POST.get('kata')
        mtaa_id = request.POST.get('mtaa')
        ubarozi_id = request.POST.get('ubarozi')
        jinsia = request.POST.get('jinsia')

        user = User.objects.get(id=user_id)

        if not jina:
            messages.success(request, f'Tafadhali jaza jina')
            return render(request, 'staff/usajiri/sajiri_mjumbe.html', {'mataifa': mataifa})
        

        if not nambari_ya_simu:
            messages.success(request, f'Tafadhali jaza nambari ya simu')
            return render(request, 'staff/usajiri/sajiri_mjumbe.html', {'mataifa': mataifa})

        if jinsia == '--------Chagua jinsia---------':
            messages.success(request, f'Tafadhali chagua jinsia')
            return render(request, 'staff/usajiri/sajiri_mjumbe.html', {'mataifa': mataifa})


        if wilaya_id == '--------Chagua wilaya---------':
            messages.success(request, f'Tafadhali chagua wilaya')
            return render(request, 'staff/usajiri/sajiri_mjumbe.html', {'mataifa': mataifa})

        if kata_id == '--------Chagua kata---------':
            messages.success(request, f'Tafadhali chagua kata')
            return render(request, 'staff/usajiri/sajiri_mjumbe.html', {'mataifa': mataifa})

        if mtaa_id == '--------Chagua mtaa---------':
            messages.success(request, f'Tafadhali chagua mtaa')
            return render(request, 'staff/usajiri/sajiri_mjumbe.html', {'mataifa': mataifa})

        nchi = Nchi.objects.get(id=nchi_id)
        mkoa = Mkoa.objects.get(id=mkoa_id)
        wilaya = Wilaya.objects.get(id=wilaya_id)
        kata = Kata.objects.get(id=kata_id)
        mtaa = Mtaa.objects.get(id=mtaa_id)
        mtendaji = Mtendaji.objects.get(id=mtendaji_id)
        mwenyekiti = Mwenyekiti.objects.get(id=mwenyekiti_id)
        ubarozi = NyumbaKumi.objects.get(id=ubarozi_id)
        mjumbe_data = Mjumbe.objects.create(jina=jina, mwenyekiti=mwenyekiti, mtendaji=mtendaji, user=user, nambari_ya_simu=nambari_ya_simu, nchi=nchi, mkoa=mkoa, wilaya=wilaya, kata=kata, jinsia=jinsia, mtaa=mtaa, barozi=ubarozi)
        messages.success(request, f'{mjumbe_data} amesajiriwa kikamilifu')
        return redirect('staff-dashibodi')






def sponsor_register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not first_name:
            pass 

        if not last_name:
            pass 
        if not email:
            pass
        if not password1:
            pass

        if password1 == password2:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password1)
