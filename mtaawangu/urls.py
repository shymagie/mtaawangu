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

urlpatterns = [
    path('admin/', admin.site.urls),
    # dashibodi za users
    path('mwenyekiti/', ujumbe_views.dashboard, name="mwenyekiti-dashibodi"),
    path('mjumbe/', ujumbe_views.dashboard, name="mjumbe-dashibodi"),
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


    # UTUMAJI UJUMBE AJAX CALL ZA MTENDAJI
    path('mtendaji-hifadhi-jumbe-zilizotumwa-ajax/', views.hifadhi_jumbe_zilizotumwa_ajax, name="mtendaji-hifadhi-jumbe-zilizotumwa-ajax"),

    # SEHEMU YA ORODHA YA WANANCHI, NA USAJIRI WA WANANCHI
    path('wananchi/', views.orodha_ya_wananchi, name="orodha-ya-wananchi"),
    path('sajiri-mwananchi/', views.kusajiri_mwananchi, name="sajiri-mwananchi"),
    path('hifadhi-mwananchi/', views.hifadhi_mwananchi, name="hifadhi-mwananchi"),

    # NCHI, MIKOA, WILAYA, KATA, NA MITAA AJAX CALL 
    path('mikoa-na-ajax/', views.mikoa_na_ajax, name="mikoa-na-ajax"),
    path('wilaya-na-ajax/', views.wilaya_na_ajax, name="wilaya-na-ajax"),
    path('kata-na-ajax/', views.kata_na_ajax, name="kata-na-ajax"),
    path('mtaa-na-ajax/', views.mtaa_na_ajax, name="mtaa-na-ajax"),
    path('ubarozi-na-ajax/', views.ubarozi_na_ajax, name="ubarozi-na-ajax"),

    # USAJIRI WA UBAROZI, KATA, WILAYA, MIKOA, NA NCHI
    path('sajiri-kata/', ujumbe_views.sajiriKata, name="sajiri-kata"),
    path('sajiri-mkoa/', ujumbe_views.sajiriMkoa, name="sajiri-mkoa"),


    path('accounts/', include('accounts.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
