from django.shortcuts import render, redirect
from .forms import NewUserForm, PesquisadorForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Pesquisador

def render_curriculo(request, id):
	pesquisador = Pesquisador.objects.get(id=id)
	endereco = pesquisador.endereco
	context = {"nome": pesquisador.nome,
				"email": pesquisador.email,
				"logradouro": endereco.logradouro,
				"bairro": endereco.bairro,
				"cidade": endereco.cidade,
				"estado": endereco.estado}
	return render(request, 'teste.html', context)

def manage_curriculo(request, id):
	if request.method == "POST":
		data = {}
		pesquisador = Pesquisador.objects.get(id=id)
		form = PesquisadorForm(request.POST or None, instance=pesquisador)
		data['form'] = form

		if form.is_valid():
			form.save()
			return render(request, "home.html")

	return render(request, "manage-profile.html", data)

def home(request):
    return render(request, 'home.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Cadastro realizado com sucesso." )
			return redirect("login")
		messages.error(request, "Cadastro não realizado. Informações inválidas.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

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
				return manage_curriculo(request, user.pk)
			else:
				messages.error(request,"Nome de usuário ou senha inválido.")
		else:
			messages.error(request,"Nome de usuário ou senha inválido.")
	
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})