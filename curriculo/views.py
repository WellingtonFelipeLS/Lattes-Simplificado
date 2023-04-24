from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *


def curriculo(request, id):
    pesquisador = Pesquisador.objects.get(user=id)
    context = {
        'curriculo': Curriculo.objects.get(user=id),
        'premio': Premio.objects.filter(curriculo_id=id),
        'linha_pesquisa': LinhaPesquisa.objects.filter(curriculo_id=id),
        'producao_bibliografica': ProducaoBibliografica.objects.filter(curriculo_id=id),
        'proeficiencia_idioma': ProeficienciaIdioma.objects.filter(curriculo_id=id),
        'producao_tecnic': ProducaoTecnica.objects.filter(curriculo_id=id),
        'orientacao_academica': OrientacaoAcademica.objects.filter(curriculo_id=id),
        'atuacao_profissional': AtuacaoProfissional.objects.filter(curriculo_id=id),
        'pesquisador': pesquisador,
        'endereco': pesquisador.endereco,
        'grad': Graduacao.objects.filter(curriculo_id=id),
        'posgrad': PosGraduacao.objects.filter(curriculo_id=id),
        'projeto_pesquisa': ProjetoPesquisa.objects.filter(curriculo_id=id)
    }
    return render(request, 'curriculo.html', context)


@receiver(signals.post_save, sender = User)
def create_curriculo_e_pesquisador(sender, instance, created, *args, **kwargs):
    if created:
        endereco = EnderecoProfissional.objects.create()
        Pesquisador.objects.create(user=instance, endereco=endereco)  
        Curriculo.objects.create(user=instance)

@login_required
def manage_curriculo(request, id):
    pesquisador = Pesquisador.objects.get(user=id)
    context = {
        'curriculo_form': CurriculoForm(request.POST or None, instance=Curriculo.objects.get(user=id)),
        'premio_form': modelformset_factory(Premio, form=PremioForm, extra=0)(request.POST or None, queryset=Premio.objects.filter(curriculo_id=id)),
        'linha_pesquisa_form': modelformset_factory(LinhaPesquisa, form=LinhaPesquisaForm, extra=0)(request.POST or None, queryset=LinhaPesquisa.objects.filter(curriculo_id=id)),
        'producao_bibliografica_form': modelformset_factory(ProducaoBibliografica, form=ProducaoBibliograficaForm, extra=0)(request.POST or None, queryset=ProducaoBibliografica.objects.filter(curriculo_id=id)),
        'proeficiencia_idioma_form': modelformset_factory(ProeficienciaIdioma, form=ProeficienciaIdiomaForm, extra=0)(request.POST or None, queryset=ProeficienciaIdioma.objects.filter(curriculo_id=id)),
        'producao_tecnica_form': modelformset_factory(ProducaoTecnica, form=ProducaoTecnicaForm, extra=0)(request.POST or None, queryset=ProducaoTecnica.objects.filter(curriculo_id=id)),
        'orientacao_academica_form': modelformset_factory(OrientacaoAcademica, form=OrientacaoAcademicaForm, extra=0)(request.POST or None, queryset=OrientacaoAcademica.objects.filter(curriculo_id=id)),
        'atuacao_profissional_form': modelformset_factory(AtuacaoProfissional, form=AtuacaoProfissionalForm, extra=0)(request.POST or None, queryset=AtuacaoProfissional.objects.filter(curriculo_id=id)),
        'pesquisador_form': PesquisadorForm(request.POST or None, request.FILES or None, instance=pesquisador),
        'endereco_form': EnderecoProfissionalForm(request.POST or None, instance=pesquisador.endereco),
        'grad_form': modelformset_factory(Graduacao, form=GraduacaoForm, extra=0)(request.POST or None, queryset=Graduacao.objects.filter(curriculo_id=id), prefix="grad"),
        'posgrad_form': modelformset_factory(PosGraduacao, form=PosGraduacaoForm, extra=0)(request.POST or None, queryset=PosGraduacao.objects.filter(curriculo_id=id), prefix="posgrad"),
        'projeto_pesquisa_form': modelformset_factory(ProjetoPesquisa, form=ProjetoPesquisaForm, extra=0)(request.POST or None, queryset=ProjetoPesquisa.objects.filter(curriculo_id=id)),
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
            context['grad_form'].save()
            context['posgrad_form'].save()
            return redirect(f'/manage/{id}#form_academ')
        if 'add_atuacao_prof' in request.POST:
            AtuacaoProfissional.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#atuacao_profissional')
        if 'save_atuacao_prof' in request.POST and context['atuacao_profissional_form'].is_valid():
            context['atuacao_profissional_form'].save()
            return redirect(f'/manage/{id}#atuacao_profissional')
        if 'add_linha_pesq' in request.POST:
            LinhaPesquisa.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#linha-de-pesquisa')
        if 'save_linha_pesq' in request.POST and context['linha_pesquisa_form'].is_valid():
            context['linha_pesquisa_form'].save()
            return redirect(f'/manage/{id}#linha-de-pesquisa')
        if 'add_proj_pesq' in request.POST:
            ProjetoPesquisa.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#projeto_pesquisa')
        if 'save_proj_pesq' in request.POST and context['projeto_pesquisa_form'].is_valid():
            context['projeto_pesquisa_form'].save()
            return redirect(f'/manage/{id}#projeto_pesquisa')
        if 'add_idioma' in request.POST:
            ProeficienciaIdioma.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#proeficiencia_idioma')
        if 'save_idioma' in request.POST and context['proeficiencia_idioma_form'].is_valid():
            context['proeficiencia_idioma_form'].save()
            return redirect(f'/manage/{id}#proeficiencia_idioma')
        if 'add_premio' in request.POST:
            Premio.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#premios')
        if 'save_premio' in request.POST and context['premio_form'].is_valid():
            context['premio_form'].save()
            return redirect(f'/manage/{id}#premios')
        if 'add_orient_acad' in request.POST:
            OrientacaoAcademica.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#orient_acad')
        if 'save_orient_acad' in request.POST and context['orientacao_academica_form'].is_valid():
            context['orientacao_academica_form'].save()
            return redirect(f'/manage/{id}#orient_acad')
        if 'add_prod_bib' in request.POST:
            ProducaoBibliografica.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#prod_bib')
        if 'save_prod_bib' in request.POST and context['producao_bibliografica_form'].is_valid():
            context['producao_bibliografica_form'].save()
            return redirect(f'/manage/{id}#prod_bib')
        if 'add_prod_tec' in request.POST:
            ProducaoTecnica.objects.create(curriculo_id=id)
            return redirect(f'/manage/{id}#prod_tec')
        if 'save_prod_tec' in request.POST and context['producao_tecnica_form'].is_valid():
            context['producao_tecnica_form'].save()
            return redirect(f'/manage/{id}#prod_tec')
        if 'btn-gerar' in request.POST:
            return curriculo(request, id)
        else:
            return HttpResponse('Inválido')

    return render(request, "manage-profile.html", context)

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

@login_required
def logout_request(request):
    logout(request)
    return redirect('/login')