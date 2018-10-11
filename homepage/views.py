from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import *


def home(request):
    
    return render(request, 'homepage/home.html')


def login_view(request):
    print(request.user.is_authenticated())
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username  = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        print(request.user.is_authenticated())
        #redirect
        return redirect("/home")
    return render(request, "home/form.html", {"form":form,"title":title})

def logout_view(request):
    logout(request)
    return redirect("/home")

User = get_user_model()
def register_view(request):
    print(request.user.is_authenticated())
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/home")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "home/form.html", context)
