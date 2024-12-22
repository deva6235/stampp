from django.shortcuts import render, redirect
from .models import Company  # Ensure you're using the correct model

# Create your views here.

def index(request):
    return render(request, 'index.html')


def data(request):
    if request.method == 'POST':
        # Get data from the form submission
        name = request.POST.get('name')
        address = request.POST.get('address')
        c_name = request.POST.get('c_name')
        gender = request.POST.get('gender')
        director = request.POST.get('director')
        date = request.POST.get('date')
        company = Company(name=name, address=address, c_name=c_name, gender=gender, director=director)
        company.save()
        return redirect('db')

        
    return render(request, 'submit.html')

def view(request):
    companies = Company.objects.all()  # Fetch all company details from the database
    return render(request, 'db.html', {'companies': companies})


def form(request):
    save = Company.objects.all()  # Fetch all company details from the database
    return render(request, 'form.html', {'save': save})
    

def delete(request):
    # if request.method == "GET":
    #     Company.objects.all().delete()  # Delete all records from the Company table
    #     return redirect('db')  # Redirect to the view that shows the database contents
    # return render(request, 'delete.html') 
    a=Company.objects.all()
    a.delete()
    return render(request,'delete.html')