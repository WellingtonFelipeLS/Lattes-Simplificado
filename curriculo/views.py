from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import signals, Q
from django.dispatch import receiver
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django import template

from .forms import *


register = template.Library()

def curriculo(request, id):
    pesquisador = Pesquisador.objects.get(user_id=id)
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

@register.filter(name='zip')
def zip_lists(a, b):
  return zip(a, b)

@login_required
def manage_curriculo(request, id):
    pesquisador = Pesquisador.objects.get(user=id)
    context = {
        'curriculo_form': CurriculoForm(request.POST or None, instance=Curriculo.objects.get(user=id)),
        'premio_form':PremioForm(request.POST or None),
        'linha_pesquisa_form': modelformset_factory(LinhaPesquisa, form=LinhaPesquisaForm, extra=0)(request.POST or None, queryset=LinhaPesquisa.objects.filter(curriculo_id=id)),
        'producao_bibliografica_form': ProducaoBibliograficaForm(request.POST or None),
        'proeficiencia_idioma_form': modelformset_factory(ProeficienciaIdioma, form=ProeficienciaIdiomaForm, extra=0)(request.POST or None, queryset=ProeficienciaIdioma.objects.filter(curriculo_id=id)),
        'producao_tecnica_form': ProducaoTecnicaForm(request.POST or None),
        'orientacao_academica_form': OrientacaoAcademicaForm(request.POST or None),
        'atuacao_profissional_form': AtuacaoProfissionalForm(request.POST or None),
        'pesquisador_form': PesquisadorForm(request.POST or None, instance=pesquisador),
        'endereco_form': EnderecoProfissionalForm(request.POST or None, instance=pesquisador.endereco),
        'grad_form': modelformset_factory(Graduacao, form=GraduacaoForm, extra=0)(request.POST or None, queryset=Graduacao.objects.filter(curriculo_id=id), prefix="grad"),
        'posgrad_form': modelformset_factory(PosGraduacao, form=PosGraduacaoForm, extra=0)(request.POST or None, queryset=PosGraduacao.objects.filter(curriculo_id=id), prefix="posgrad"),
        'projeto_pesquisa_form': ProjetoPesquisaForm(request.POST or None)
    }

    if request.method == "POST":
        if 'salvar_dados_pessoais' in request.POST and context['pesquisador_form'].is_valid() and context['endereco_form'].is_valid() and context['curriculo_form'].is_valid():
            context['pesquisador_form'].save()
            context['endereco_form'].save()
            context['curriculo_form'].save()
            return redirect(f'/manage/{id}#dados-pessoais')
        if 'add_grad' in request.POST:
            Graduacao.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#form_academ')
        if 'add_posgrad' in request.POST:
            PosGraduacao.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#form_academ')
        if 'save_form_acad' in request.POST and context['grad_form'].is_valid() and context['posgrad_form'].is_valid():
            print(request.POST)
            context['grad_form'].save()
            context['posgrad_form'].save()
            return redirect(f'/manage/{id}#form_academ')
        if 'add_linha_pesq' in request.POST:
            LinhaPesquisa.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#linha-de-pesquisa')
        if 'save_linha_pesq' in request.POST and context['linha_pesquisa_form'].is_valid():
            context['linha_pesquisa_form'].save()
            return redirect(f'/manage/{id}#linha-de-pesquisa')
        if 'add_idioma' in request.POST:
            ProeficienciaIdioma.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#proeficiencia_idioma')
        if 'save_idioma' in request.POST and context['proeficiencia_idioma_form'].is_valid():
            print(request.POST)
            context['proeficiencia_idioma_form'].save()
            return redirect(f'/manage/{id}#proeficiencia_idioma')
        if 'btn-gerar' in request.POST:
            return curriculo(request, id)
        else:
            return HttpResponse('Inválido')

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