from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    print(request.session.get('first_name', 'unkwnown'))
    context = {
        'title': 'Home page',
        'content': 'Welcome to the home page.'
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        'title': 'About page',
        'content': 'Welcome to the about page.'
    }

    return render(request, 'home_page.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact page',
        'content': 'Welcome to the contact page.',
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, 'contact/view.html', context)

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }
    print(request.user.is_authenticated)
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            return redirect("/login")
        print("Error")
    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "form": register_form
    }
    if register_form.is_valid():
        print(register_form.cleaned_data)
        username = register_form.cleaned_data.get("username")
        password = register_form.cleaned_data.get("password")
        email = register_form.cleaned_data.get("email")
        new_user = User.objects.create_user(username, email, password)
    return render(request, "auth/register.html", context)
