from django.shortcuts import render, get_object_or_404, redirect
from .models import Application
from django.utils import timezone
from .forms import CreateForm

# Create your views here.
def home(request):
    humans = Application.objects
    return render(request,"home.html", {'humans':humans})

def detail(request,human_id):
    human_detail = get_object_or_404(Application, pk=human_id)
    return render(request, 'detail.html', {'human_detail':human_detail})

def create(request,human_id):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            human = form.save(commit=False)
            human.gender = request.POST['gender']
            human.save()
        return redirect('/detail/'+str(human.id))
    else:
        form = CreateForm()
    return render(request, 'create.html', {'form': form})

def update(request,human_id):
    human = Application.objects.get(id=human_id)
    if request.method =="POST":
        form = CreateForm(request.POST, instance=human)
        if form.is_valid():
            human = form.save()
        return redirect('/detail/'+str(human.id))
    else:
        form = CreateForm(instance=human)
        return render(request, 'create.html', {'form':form})

def delete(request,human_id):
    human = Application.objects.get(id=human_id)
    human.delete()
    return redirect('home')


