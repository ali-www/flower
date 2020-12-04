from django.shortcuts import render
from django.views.generic import TemplateView ,ListView ,DeleteView
from .models import PostFlower

# Create your views here.



class HomeView(ListView):
    template_name = 'home.html'
    model = PostFlower
    context_object_name = 'PostFlower'
    paginate_by = 2



class FlowerDetailView(DeleteView):
    template_name = 'detail.html'
    model = PostFlower
    context_object_name = 'flower'
   
