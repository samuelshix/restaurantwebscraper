from django.shortcuts import render
from django.views import generic
from index.models import Restaurant

class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'restaurants' 

    def get_queryset(self):
        return Restaurant.objects.all()