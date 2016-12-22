from django.shortcuts import render
from models import Dish

# Create your views here.
def home(request):
	dishes = Dish.objects.all()
	return render(request, 'menu/home.html', {'dishes': dishes})

def about(request):
	return render(request, 'menu/about.html')

def career(request):
	return render(request, 'menu/career.html')

def contact(request):
	return render(request, 'menu/contact.html')

def menu(request):
	return render(request, 'menu/menu.html')
