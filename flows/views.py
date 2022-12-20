from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import AtualizarEtapaForm, CriarEtapaForm, CriarFluxoForm
from .models import Etapa, Fluxo


def pagina_inicial_view(request):
    fluxos = Fluxo.objects.all()
    return render(request, 'flows/fluxo/home.html', {'fluxos': fluxos})


def adicionar_fluxo_view(request):
    form = CriarFluxoForm()
    if request.method == 'POST':
        form = CriarFluxoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flows:inicio')
    return render(request, 'flows/fluxo/adicionar.html', {'form': form})


def detalhes_fluxo_view(request, pk):
    fluxo = get_object_or_404(Fluxo, id=pk)
    return render(request, 'flows/fluxo/detalhes.html', {'fluxo': fluxo})

def editar_fluxo_view(request, pk):
    flow = Fluxo.objects.get(id=pk)
    form = CriarFluxoForm(instance=flow)

    if (request.method == 'POST'):
        form = CriarFluxoForm(request.POST, instance=flow)

        if(form.is_valid()):
            form.save()
            return redirect('/fluxos')
        else:
            return render(request, 'flows/editar.html', {'form': form, 'flow': flow})
            
    else:
        return render(request, 'flows/editar.html', {'form': form, 'flow': flow})


def adicionar_etapa_view(request, fluxo_pk):
    fluxo = get_object_or_404(Fluxo, id=fluxo_pk)
    form = CriarEtapaForm()
    if request.method == 'POST':
        form = CriarEtapaForm(request.POST)
        if form.is_valid():
            etapa = form.save(commit=False)
            etapa.fluxo = fluxo
            etapa.save()
            return redirect('flows:detalhes_fluxo', pk=fluxo_pk)
    return render(request, 'flows/etapa/adicionar.html', {'form': form, 'fluxo': fluxo})


def editar_etapa_view(request, fluxo_pk, pk):
    etapa = get_object_or_404(Etapa, id=pk)
    fluxo = get_object_or_404(Fluxo, id=fluxo_pk)
    form = AtualizarEtapaForm(instance=etapa)
    if request.method == 'POST':
        form = AtualizarEtapaForm(request.POST)
        if form.is_valid():
            nova_etapa = form.save(commit=False)
            nova_etapa.fluxo = fluxo
            nova_etapa.id = pk
            nova_etapa.save()
            return redirect('flows:detalhes_fluxo', pk=fluxo_pk)
    return render(request, 'flows/etapa/editar.html', {'form': form, 'etapa': etapa})


def excluir_etapa_view(request, fluxo_pk, pk):
    get_object_or_404(Fluxo, id=fluxo_pk)
    etapa = get_object_or_404(Etapa, id=pk)
    if request.method == 'POST':
        if etapa.data_inicio <= timezone.now().date():
            messages.error(
                request, 'Não é possível excluir uma etapa que já iniciou')
            return redirect('flows:detalhes_fluxo', pk=fluxo_pk)
        etapa.delete()
        return redirect('flows:detalhes_fluxo', pk=fluxo_pk)
    return render(request, 'flows/etapa/excluir.html', {'etapa': etapa})
