from django.shortcuts import render, redirect
from .forms import ArtefatoCreateForm
from artifacts.models import Artefato

def create_artifact_view(request):
    form = ArtefatoCreateForm()
    if request.method == 'POST':
        form = ArtefatoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artifacts:listar')
    return render(request, 'artifacts/novo-artefato.html', {'form': form})

def artifact_list(request):
    artifacts = Artefato.objects.all()
    return render(request, 'artifacts/list_all_artifacts.html', {'artifacts': artifacts})

def home_artifact(request):

    name = request.GET.get('nome', None)

    if name:
        artifacts = Artefato.objects.filter(nome__contains=name)
        return render(request, 'artifacts/home_artifacts.html', {'artifacts': artifacts})
    else:
        return render(request, 'artifacts/home_artifacts.html')
def update_artifact(request, pk):
    artifact = Artefato.objects.get(id=pk)
    form = ArtefatoCreateForm(instance=artifact)

    if (request.method == 'POST'):
        form = ArtefatoCreateForm(request.POST, instance=artifact)

        if(form.is_valid()):
            form.save()
            return redirect('/artefatos/listar')
        else:
            return render(request, 'artifacts/update_artefato.html', {'form': form, 'artifact': artifact})
            
    else:
        return render(request, 'artifacts/update_artefato.html', {'form': form, 'artifact': artifact})

def delete_artifact(request, pk):
    artifact = Artefato.objects.get(id=pk)
    artifact.delete()

    return redirect('/artefatos/listar')
