from django.conf.urls import url
from . import views

urlpatterns = [	
	url(r'^$', views.home, name='home'),
	url(r'^about/', views.about, name='about'),
	url(r'^career/', views.career, name='career'),
	url(r'^menu/', views.menu, name='menu'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^full-menu', views.full_menu, name='full-menu'),
]
