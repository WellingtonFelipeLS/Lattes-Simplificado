from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import Curriculo, EnderecoProfissional, Pesquisador


def curriculo(request):
    pesquisador = Pesquisador.objects.get(id=2)
    endereco = pesquisador.endereco
    context = {"nome": pesquisador.nome,
                "email": pesquisador.email,
                "logradouro": endereco.logradouro,
                "bairro": endereco.bairro,
                "cidade": endereco.cidade,
                "estado": endereco.estado}
    return render(request, 'teste.html', context)


@receiver(signals.post_save, sender = User)
def create_curriculo_e_pesquisador(sender, instance, created, *args, **kwargs):
    if created:
        endereco = EnderecoProfissional.objects.create()
        Pesquisador.objects.create(user=instance, endereco=endereco)  
        Curriculo.objects.create(user=instance)


'''@login_required
def manage_curriculo(request, id):
    pesquisador = Pesquisador.objects.get(id=id)
    form = PesquisadorForm(request.POST or None, instance=pesquisador)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('manage', id)
        else:
            return HttpResponse('INVÁLIDO')

    return render(request, "manage-profile.html", context={"form": form})'''

@login_required
def manage_curriculo(request, id):
    context = {
        'curriculo_form': CurriculoForm(request.POST or None, instance=Curriculo.objects.get(user=id)),
		'premio_form':PremioForm(request.POST or None),
		'linha_pesquisa_form': LinhaPesquisaForm(request.POST or None),
		'producao_bibliografica_form': ProducaoBibliograficaForm(request.POST or None),
		'proeficiencia_idioma_form': ProeficienciaIdiomaForm(request.POST or None),
		'producao_tecnica_form': ProducaoTecnicaForm(request.POST or None),
		'orientacao_academica_form': OrientacaoAcademicaForm(request.POST or None),
		'atuacao_profissional_form': AtuacaoProfissionalForm(request.POST or None),
		'pesquisador_form': PesquisadorForm(request.POST or None, instance=Pesquisador.objects.get(user=id)),
		'graduacao_form': GraduacaoForm(request.POST or None),
		'area_pesquisa_form': AreaPesquisaForm(request.POST or None),
		'posgraduacao_form': PosGraduacaoForm(request.POST or None),
		'projeto_pesquisa_form': ProjetoPesquisaForm(request.POST or None)
	}
    
    #endereco_profissional_form = EnderecoProfissionalForm(request.POST or None)
    if request.method == "POST":
        if all(form.is_valid() for form in context.values()):
            for form in context:
                form.save()
            return redirect('manage', id)
        else:
            return HttpResponse('INVÁLIDO')

    return render(request, "manage-profile.html", context)

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
                return redirect("manage", user.pk)
            else:
                messages.error(request,"Nome de usuário ou senha inválido.")
        else:
            messages.error(request,"Nome de usuário ou senha inválido.")
    
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})