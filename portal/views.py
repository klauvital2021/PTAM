from django.shortcuts import render, redirect, get_object_or_404
from portal.forms import ImovelForm, PadraoForm, NomecondominioForm, EstadoconserForm, TipoForm
from portal.models import Imovel, Padrao, Nomecondominio, Estadoconser, Tipo


def home(request):
    return render(request, 'portal/home.html')

'''
def imovel_edit(request, imovel_pk):
    imovel = Imovel.objects.get(pk=imovel_pk)
    form = ImovelForm(request.POST or None, instance=imovel)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('imoveis')

    context = {
        'form': form,
    }
    return render(request, 'portal/imovel_edit.html', context)
'''


def imovel_edit(request, imovel_pk):
    imovel = get_object_or_404(Imovel, pk=imovel_pk)
    form = ImovelForm(instance=imovel)

    if (request.method == 'POST'):
        form = ImovelForm(request.POST, instance=imovel)

        if (form.is_valid()):
            imovel = form.save(commit=False)
            imovel.save()
            return redirect('imoveis')
        else:
            return render(request, 'portal/imovel_edit..html', {'form': form, 'post': imovel})

    elif (request.method == 'GET'):
        return render(request, 'portal/imovel_edit.html', {'form': form, 'post': imovel})


def imovel(request):
    imoveis = Imovel.objects.all()
    context = {
        'imoveis': imoveis
    }
    return render(request, 'portal/imoveis.html', context)


def imovel_add(request):
    form = ImovelForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('imoveis')

    context = {
        'form': form,
    }
    return render(request, 'portal/imovel_add.html', context)


def imovel_delete(request, imovel_pk):
    imovel = Imovel.objects.get(pk=imovel_pk)
    imovel.delete()
    return redirect('imoveis')


def padrao (request):
    padrao = Padrao.objects.all()
    context = {
        'padrao': padrao
    }
    return render(request, 'portal/padrao.html', context)

def padrao_add(request):
    form = PadraoForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('padrao')

    context = {
        'form': form,
    }
    return render(request, 'portal/padrao_add.html', context)

def condominio (request):
    condominio = Nomecondominio.objects.all()
    context = {
        'condominio': condominio
    }
    return render(request, 'portal/condominio.html', context)

def cond_add(request):
    form = NomecondominioForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('condominio')

    context = {
        'form': form,
    }
    return render(request, 'portal/cond_add.html', context)


def cond_edit(request, cond_pk):
    condominio = Imovel.objects.get(pk=cond_pk)

    form = ImovelForm(request.POST or None, instance=condominio)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('condominio')

    context = {
        'form': form,
    }
    return render(request, 'portal/cond_edit.html', context)

def cond_delete(request, cond_pk):
    condominio = Imovel.objects.get(pk=cond_pk)
    condominio.delete()

    return redirect('condominio')

def estadoConserv (request):
    estadoConservacao = Estadoconser.objects.all()
    context = {
        'estadoCons': estadoConservacao
    }
    return render(request, 'portal/estadoConservacao.html', context)

def estadoConserv_add(request):
    form = EstadoconserForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('estadoConservacao')

    context = {
        'form': form,
    }
    return render(request, 'portal/estadoConservacao_add.html', context)


def tipo(request):
    tipos = Tipo.objects.all()
    context = {
        'tipos': tipos
    }
    return render(request, 'portal/tipo.html', context)


def tipo_add(request):
    form = TipoForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('tipo')

    context = {
        'form': form,
    }

    return render(request, 'portal/tipo_add.html', context)