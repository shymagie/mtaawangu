from django.urls import path
from accounts import views
urlpatterns = [
    path('login/', views.UserLogin, name="ingia"),
    path('logout/', views.logoutUser, name="toka"),
]