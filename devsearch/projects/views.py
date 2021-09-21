from django.shortcuts import render, redirect
from .models import Project
from .forms import ModelForm, ProjectForm


projectsList = [
    {
        'id': '1',
        'title':'ecommerce',
        'description':'functional ecommmerce website'
        },
    {
        'id': '2',
        'title':'portfolio',
        'description':'functional portfolio website'
        },
    {
        'id': '3',
        'title':'users',
        'description':'functional users website'
        },
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return	render(request, 'projects/projects.html', context)


def singleproject(request, pk):
    projectObj = Project.objects.get(id = pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/singleproject.html', {'project':projectObj, 'tags': tags})

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance = project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance = project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

def deleteProject(request, pk):
    project =Project.objects.get(id = pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request,'projects/delete_object.html', context)