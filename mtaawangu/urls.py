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
from django.urls import path
from ujumbe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name="dashboard"),

    # UTUMAJI WA UJUMBE PAMOJA NA ORODHA MBALI MBALI ZA JUMBE KWA UMMA
    path('tuma-kwa-mtaa/', views.tuma_kwa_mtaa, name="tuma-kwa-mtaa"),
    path('tuma-kwa-kata/', views.tuma_kwa_kata, name="tuma-kwa-kata"),
    path('tuma-kwa-barozi/', views.tuma_kwa_barozi, name="tuma-kwa-barozi"),
    path('tuma-ujumbe-kwa-mtaa/', views.tuma_ujumbe_kwa_mtaa, name="tuma-ujumbe-kwa-mtaa"),
    path('tuma-ujumbe-kwa-kata/', views.tuma_ujumbe_kwa_kata, name="tuma-ujumbe-kwa-kata"),
    path('tuma-ujumbe-kwa-barozi/', views.tuma_ujumbe_kwa_barozi, name="tuma-ujumbe-kwa-barozi"),
    path('jumbe/tuma-ujumbe/', views.tuma_ujumbe, name="tuma-ujumbe"),
    path('jumbe/orodha-ya-jumbe/', views.orodha_ya_jumbe, name="orodha-ya-jumbe"),
    path('jumbe-zilizotumwa/', views.orodha_ya_jumbe_zilizotumwa, name="jumbe-zilizotumwa"),

    # UTUMAJI UJUMBE AJAX CALL
    path('hifadhi-jumbe-zilizotumwa-ajax/', views.hifadhi_jumbe_zilizotumwa_ajax, name="hifadhi-jumbe-zilizotumwa-ajax"),

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
    path('sajiri-kata/', views.sajiriKata, name="sajiri-kata"),
    path('sajiri-mkoa/', views.sajiriMkoa, name="sajiri-mkoa"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
