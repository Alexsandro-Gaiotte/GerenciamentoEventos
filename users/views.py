from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("evento:evento_list")
    else:
        form = UserCreationForm()
    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control m-3'})
        
    return render(request, 'users/register.html', {"form":form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("evento:evento_list")
    else:
        form = AuthenticationForm()
        
    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control m-3'})
    
    return render(request, 'users/login.html', {"form":form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("evento:evento_list")