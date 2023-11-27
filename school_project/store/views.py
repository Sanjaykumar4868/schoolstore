from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Department,Course
from .forms import PersonCreationForm

def Home(request):
    return render(request,'home.html')

def Register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Login_page")
    return render(request, 'register.html', { 'form': form})    
    


def Login_page(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('person_add')
        else:
            return HttpResponse("Invalid user")
    return render(request,'login.html')
        
    
def Logout_view(request):
    logout(request)
    return redirect('/')


def NewForm(request):
    return render(request,'newform.html')



def allProdCat(request,c_slug=None):
    c_page = None
    if c_slug != None:
        c_page = get_object_or_404(Department,slug = c_slug)
    return render(request,'category.html',{'category':c_page})



def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Order confirmed successfully.')
            return redirect('success')
    return render(request, 'newform.html', {'form': form})
        

def Success(request):   
    return render(request,'success.html')



# AJAX
def load_cities(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'city_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)