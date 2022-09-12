from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages


# Create your views here.
def inside(request):
    return render(request, 'login/prueba.html', {})

def logout_user(request):
    auth_logout(request)
    messages.success(request, "Saliste exitosamente")
    return redirect('login:login_user')

def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page.
            #messages.success(request, 'Hubo un error on el Log In, intente de nuevo.')
            #return redirect('login:inside')
            return redirect('drag_drop:drag_drop_screen')
            #return redirect('reg_diario:pacients_list')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'Usuario o contraseña son incorrectos !!!')
            return redirect('login:login_user')
    else:
        return render(request, 'login/login.html', {})