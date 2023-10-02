"""
URL configuration for streatinfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mtendaji import views
from ujumbe import views as ujumbe_views
from mwenyekiti import views as mwenyekiti_views
from mjumbe import views as mjumbe_views
from staff import views as staff_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # dashibodi za users
    path('mwenyekiti/', mwenyekiti_views.dashboard, name="mwenyekiti-dashibodi"),
    path('mjumbe/', mjumbe_views.dashboard, name="mjumbe-dashibodi"),
    path('staff/', staff_views.dashboard, name="staff-dashibodi"),
    path('', views.dashboard, name="mtendaji-dashibodi"),

    # UTUMAJI WA UJUMBE PAMOJA NA ORODHA MBALI MBALI ZA JUMBE KWA UMMA ZA MTENDAJI
    path('mtendaji-tuma-kwa-mtaa/', views.tuma_kwa_mtaa, name="mtendaji-tuma-kwa-mtaa"),
    path('mtendaji-tuma-kwa-kata/', views.tuma_kwa_kata, name="mtendaji-tuma-kwa-kata"),
    path('mtendaji-tuma-kwa-barozi/', views.tuma_kwa_barozi, name="mtendaji-tuma-kwa-barozi"),
    path('mtendaji-tuma-ujumbe-kwa-mtaa/', views.tuma_ujumbe_kwa_mtaa, name="mtendaji-tuma-ujumbe-kwa-mtaa"),
    path('mtendaji-tuma-ujumbe-kwa-kata/', views.tuma_ujumbe_kwa_kata, name="mtendaji-tuma-ujumbe-kwa-kata"),
    path('mtendaji-tuma-ujumbe-kwa-barozi/', views.tuma_ujumbe_kwa_barozi, name="mtendaji-tuma-ujumbe-kwa-barozi"),
    path('mtendaji-jumbe/tuma-ujumbe/', views.tuma_ujumbe, name="mtendaji-tuma-ujumbe"),
    path('mtendaji-jumbe/orodha-ya-jumbe/', views.orodha_ya_jumbe, name="mtendaji-orodha-ya-jumbe"),
    path('mtendaji-jumbe-zilizotumwa/', views.orodha_ya_jumbe_zilizotumwa, name="mtendaji-jumbe-zilizotumwa"),


    # UTUMAJI WA UJUMBE PAMOJA NA ORODHA MBALI MBALI ZA JUMBE KWA UMMA ZA MWENYEKITI
    path('mwenyekiti-tuma-kwa-mtaa/', mwenyekiti_views.tuma_kwa_mtaa, name="mwenyekiti-tuma-kwa-mtaa"),
    path('mwenyekiti-tuma-kwa-kata/', mwenyekiti_views.tuma_kwa_kata, name="mwenyekiti-tuma-kwa-kata"),
    path('mwenyekiti-tuma-kwa-barozi/', mwenyekiti_views.tuma_kwa_barozi, name="mwenyekiti-tuma-kwa-barozi"),
    path('mwenyekiti-tuma-ujumbe-kwa-mtaa/', mwenyekiti_views.tuma_ujumbe_kwa_mtaa, name="mwenyekiti-tuma-ujumbe-kwa-mtaa"),
    path('mwenyekiti-tuma-ujumbe-kwa-kata/', mwenyekiti_views.tuma_ujumbe_kwa_kata, name="mwenyekiti-tuma-ujumbe-kwa-kata"),
    path('mwenyekiti-tuma-ujumbe-kwa-barozi/', mwenyekiti_views.tuma_ujumbe_kwa_barozi, name="mwenyekiti-tuma-ujumbe-kwa-barozi"),
    path('mwenyekiti-jumbe/tuma-ujumbe/', mwenyekiti_views.tuma_ujumbe, name="mwenyekiti-tuma-ujumbe"),
    path('mwenyekiti-jumbe/orodha-ya-jumbe/', mwenyekiti_views.orodha_ya_jumbe, name="mwenyekiti-orodha-ya-jumbe"),
    path('mwenyekiti-jumbe-zilizotumwa/', mwenyekiti_views.orodha_ya_jumbe_zilizotumwa, name="mwenyekiti-jumbe-zilizotumwa"),


    # UTUMAJI WA UJUMBE PAMOJA NA ORODHA MBALI MBALI ZA JUMBE KWA UMMA ZA MJUMBE
    path('mjumbe-tuma-kwa-mtaa/', mjumbe_views.tuma_kwa_mtaa, name="mjumbe-tuma-kwa-mtaa"),
    path('mjumbe-tuma-kwa-kata/', mjumbe_views.tuma_kwa_kata, name="mjumbe-tuma-kwa-kata"),
    path('mjumbe-tuma-kwa-barozi/', mjumbe_views.tuma_kwa_barozi, name="mjumbe-tuma-kwa-barozi"),
    path('mjumbe-tuma-ujumbe-kwa-mtaa/', mjumbe_views.tuma_ujumbe_kwa_mtaa, name="mjumbe-tuma-ujumbe-kwa-mtaa"),
    path('mjumbe-tuma-ujumbe-kwa-kata/', mjumbe_views.tuma_ujumbe_kwa_kata, name="mjumbe-tuma-ujumbe-kwa-kata"),
    path('mjumbe-tuma-ujumbe-kwa-barozi/', mjumbe_views.tuma_ujumbe_kwa_barozi, name="mjumbe-tuma-ujumbe-kwa-barozi"),
    path('mjumbe-jumbe/tuma-ujumbe/', mjumbe_views.tuma_ujumbe, name="mjumbe-tuma-ujumbe"),
    path('mjumbe-jumbe/orodha-ya-jumbe/', mjumbe_views.orodha_ya_jumbe, name="mjumbe-orodha-ya-jumbe"),
    path('mjumbe-jumbe-zilizotumwa/', mjumbe_views.orodha_ya_jumbe_zilizotumwa, name="mjumbe-jumbe-zilizotumwa"),



    # UTUMAJI WA UJUMBE PAMOJA NA ORODHA MBALI MBALI ZA JUMBE KWA UMMA ZA STAFF
    path('staff-tuma-kwa-mtaa/', staff_views.tuma_kwa_mtaa, name="staff-tuma-kwa-mtaa"),
    path('staff-tuma-kwa-kata/', staff_views.tuma_kwa_kata, name="staff-tuma-kwa-kata"),
    path('staff-tuma-kwa-barozi/', staff_views.tuma_kwa_barozi, name="staff-tuma-kwa-barozi"),
    path('staff-tuma-ujumbe-kwa-mtaa/', staff_views.tuma_ujumbe_kwa_mtaa, name="staff-tuma-ujumbe-kwa-mtaa"),
    path('staff-tuma-ujumbe-kwa-kata/', staff_views.tuma_ujumbe_kwa_kata, name="staff-tuma-ujumbe-kwa-kata"),
    path('staff-tuma-ujumbe-kwa-barozi/', staff_views.tuma_ujumbe_kwa_barozi, name="staff-tuma-ujumbe-kwa-barozi"),
    path('staff-jumbe/tuma-ujumbe/', staff_views.tuma_ujumbe, name="staff-tuma-ujumbe"),
    path('staff-jumbe/orodha-ya-jumbe/', staff_views.orodha_ya_jumbe, name="staff-orodha-ya-jumbe"),
    path('staff-jumbe-zilizotumwa/', staff_views.orodha_ya_jumbe_zilizotumwa, name="staff-jumbe-zilizotumwa"),




    # UTUMAJI UJUMBE AJAX CALL ZA MTENDAJI
    path('mtendaji-hifadhi-jumbe-zilizotumwa-ajax/', views.hifadhi_jumbe_zilizotumwa_ajax, name="mtendaji-hifadhi-jumbe-zilizotumwa-ajax"),
    path('mwenyekiti-hifadhi-jumbe-zilizotumwa-ajax/', mwenyekiti_views.hifadhi_jumbe_zilizotumwa_ajax, name="mwenyekiti-hifadhi-jumbe-zilizotumwa-ajax"),
    path('mjumbe-hifadhi-jumbe-zilizotumwa-ajax/', mjumbe_views.hifadhi_jumbe_zilizotumwa_ajax, name="mjumbe-hifadhi-jumbe-zilizotumwa-ajax"),
    path('staff-hifadhi-jumbe-zilizotumwa-ajax/', staff_views.hifadhi_jumbe_zilizotumwa_ajax, name="staff-hifadhi-jumbe-zilizotumwa-ajax"),

    # SEHEMU YA ORODHA YA WANANCHI, NA USAJIRI WA WANANCHI
    path('wananchi/', ujumbe_views.orodha_ya_wananchi, name="orodha-ya-wananchi"),
    path('sajiri-mwananchi/', ujumbe_views.kusajiri_mwananchi, name="sajiri-mwananchi"),
    path('hifadhi-mwananchi/', ujumbe_views.hifadhi_mwananchi, name="hifadhi-mwananchi"),

    # NCHI, MIKOA, WILAYA, KATA, NA MITAA AJAX CALL 
    path('mikoa-na-ajax/', ujumbe_views.mikoa_na_ajax, name="mikoa-na-ajax"),
    path('wilaya-na-ajax/', ujumbe_views.wilaya_na_ajax, name="wilaya-na-ajax"),
    path('kata-na-ajax/', ujumbe_views.kata_na_ajax, name="kata-na-ajax"),
    path('mtaa-na-ajax/', ujumbe_views.mtaa_na_ajax, name="mtaa-na-ajax"),
    path('ubarozi-na-ajax/', ujumbe_views.ubarozi_na_ajax, name="ubarozi-na-ajax"),

    # USAJIRI WA UBAROZI, KATA, WILAYA, MIKOA, NA NCHI
    path('sajiri-kata/', ujumbe_views.sajiriKata, name="sajiri-kata"),
    path('sajiri-mkoa/', ujumbe_views.sajiriMkoa, name="sajiri-mkoa"),


    path('accounts/', include('accounts.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
