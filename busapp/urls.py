from django.contrib import admin
from django.urls import path
from busapp import views

urlpatterns = [
    path("",views.home,name='home'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name='contact'),
    path("feedback/",views.feedback,name='feedback'),
    path("search/",views.search,name="search"),

]
