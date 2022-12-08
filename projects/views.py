from django.views.generic import UpdateView
from projects.models import Projeto
from django.shortcuts import render, redirect
from .forms import ProjectForm

def home_project(request):

    name = request.GET.get('nome', None)

    if name:
        projects = Projeto.objects.filter(nome__contains=name)
        return render(request, 'projects/home.html', {'projects': projects})
    else:
        return render(request, 'projects/home.html')

def new_project(request):  
    if (request.method == 'POST'):
        form = ProjectForm(request.POST)

        if (form.is_valid()):
            form.save()
            return redirect('/projetos')
    else :
        form = ProjectForm()
        return render(request, 'projects/new_project.html', {'form': form})

def project_list(request):
    projects = Projeto.objects.all()
    return render(request, 'projects/list_all_projects.html', {'projects' : projects})

def update_project(request, pk):
    project = Projeto.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if (request.method == 'POST'):
        form = ProjectForm(request.POST, instance=project)

        if(form.is_valid()):
            form.save()
            return redirect('/projetos/listar')
        else:
            return render(request, 'projects/update_project.html', {'form': form, 'project': project})
            
    else:
        return render(request, 'projects/update_project.html', {'form': form, 'project': project})

def delete_project(request, pk):
    project = Projeto.objects.get(id=pk)
    project.delete()

    return redirect('/projetos/listar')

def search_by_name(request):
    name = request.GET.get('name', None)
    projects = Projeto.objects.filter(nome__contains=name)
    return render(request, 'projects/filter_project.html', {'projects': projects})

class ProjetoUpdateView(UpdateView):
    model = Projeto
    fields = '__all__'

    def get_success_url(self):
        return '/'


update_view = ProjetoUpdateView.as_view()