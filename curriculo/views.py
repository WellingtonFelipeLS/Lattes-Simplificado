from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'home.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Cadastro realizado com sucesso." )
			return redirect("home")
		messages.error(request, "Cadastro não realizado. Informações inválidas.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Você agora está conectado como {username}.")
				return redirect("home")
			else:
				messages.error(request,"Nome de usuário ou senha inválido.")
		else:
			messages.error(request,"Nome de usuário ou senha inválido.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})