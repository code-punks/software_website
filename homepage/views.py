from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Profile
from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .models import *

from django.shortcuts import *
from django.http import HttpResponse
from .forms import *

User = get_user_model()
# Create your views here.

from django.contrib.auth.decorators import login_required, user_passes_test
user_login_required = user_passes_test(lambda user: user.is_superuser, login_url='/admin/')
def admin_required(view_func):
    decorated_view_func = login_required(user_login_required(view_func))
    return decorated_view_func





def home(request):
    return render(request, 'homepage/landing_page.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'homepage/register2.html', {'form' : form})

@login_required(login_url='/login/')
def dashboard(request):
    user = request.user
    print(user)
    bill_objects = Bill.objects.all().filter(rfid__username__exact = user)
    amount_ = 0
    bill_amount = 0
    if len(bill_objects) != 0:
        for obj in bill_objects:
            bill_amount += obj.monthly_amount

        try:
            user_Balance = Balance.objects.get(rfid_id = request.user.id,month = datetime.now().month - 1)
            balance_fron_prev = user_Balance.payment_balance
        except Balance.DoesNotExist:
            balance_fron_prev = 0
        if(balance_fron_prev == None):
            balance_fron_prev = 0
        amount_ = bill_amount + balance_fron_prev
        print(amount_)
        if(amount_ == None):
            amount_ = 0
    print(amount_)
    return render(request, 'homepage/dashboard.html',{'amount':amount_})


@login_required(login_url='/login/')
def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)
    ProfileInlineFormset = inlineformset_factory(User, Profile, form = EditProfileForm2)
    formset = ProfileInlineFormset(instance=user)
 
    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
 
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
 
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/dashboard/')
 
        return render(request, "homepage/profile.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied


@login_required(login_url='/admin/')
@admin_required
def assign_rfid(request):
    unass_users = User.objects.all().filter( profile__rfid__isnull = True).exclude(username = 'admin')
    form = AssignRFIDForm(extra=unass_users)
    if request.method == "POST":
        form = AssignRFIDForm(request.POST, request.FILES, extra=unass_users)
        if form.is_valid():
            form.save() 

    return render(request, "homepage/assign_rfid.html",{
        "form" : form
        })
    
@login_required
def make_payment(request):
    get_the_bill = Bill.objects.all().filter(rfid__username__exact = request.user.username)
    form = PaymentForm(request.user.id) 
    print("Pass ",request.user.id)
    if request.method == "POST":
        form = PaymentForm(request.user.id,request.POST)
        print("pahuch gye")
        if form.is_valid():
            form.save()
        else:
            print("nhi valid ")
    return render(request,"homepage/make_payment.html",{"form":form})