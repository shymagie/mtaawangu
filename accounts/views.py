
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from accounts.decorators import authenticated_user, mtendaji_tu
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages



def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return render_to_response('inventory/errors/403.html', ctx)

    
@authenticated_user
def UserLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('mtendaji-dashibodi')
        else: 
            messages.info(request, 'Username or password is incorrect!')
            return redirect('ingia')
    context ={}
    return render(request, 'auth/app_login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('ingia')



# class PasswordsChangeView(PasswordChangeView):
#     form_class = PasswordChangingForm

#     success_url = reverse_lazy('success_password')

# @login_required
# def success_page(request):
#     return render(request, 'partials/success_page.html', {})

# @login_required
# def password_changed_success(request):
#     return render(request, 'partials/password_success_change.html', {})



