from django.shortcuts import render, redirect

from store.models import Customer
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method =="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(
                user = user,
                name = user.username,
                email = user.email
            )
        return redirect("/login")
    else:
        form = RegisterForm()
    
    return render(response, "register/register.html", {"form":form})
