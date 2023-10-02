from django.http import HttpResponse
from django.shortcuts import redirect


def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('mtendaji-dashibodi')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func



def allowed_user(allowed_role=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_vendor:
                wrapper_func(request, *args, **kwargs)
            elif request.user.is_office:
                wrapper_func(request, *args, **kwargs)
            elif request.user.is_reception:
                wrapper_func(request, *args, **kwargs)
            else:
                return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator



def mtendaji_tu(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'mjumbe' and request.user.is_active:
            return redirect('mjumbe-dashibodi')
        elif group == 'mwenyekiti' and request.user.is_active:
            return redirect('mwenyekiti-dashibodi')
        
        elif group == 'mtendaji' and request.user.is_active:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('ingia')
    return wrapper_func



def mwenyekiti_tu(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'mtendaji' and request.user.is_active:
            return redirect('mtendaji-dashibodi')
        elif group == 'mjumbe' and request.user.is_active:
            return redirect('mjumbe-dashibodi')
        elif group == 'mwenyekiti' and request.user.is_active:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('ingia')
    return wrapper_func



def mjumbe_tu(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'mtendaji' and request.user.is_active:
            return redirect('mtendaji-dashibodi')
        elif group == 'mwenyekiti' and request.user.is_active:
            return redirect('mwenyekiti-dashibodi')
        elif group == 'mjumbe' and request.user.is_active:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('ingia')
    return wrapper_func