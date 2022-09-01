from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from .models import Project,Tag,Review
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    
    return render(request, 'projects/project.html', context)

def project(request, pk):
    obj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': obj})

def createProject(request):
    form = ProjectForm()
    context = {'form':form}
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, "projects/project_form.html", context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    context = {'form':form}
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {'object':project}
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, "projects/delete_template.html", context)