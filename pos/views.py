from django.shortcuts import redirect, render
from .models import Review
# Create your views here.

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'pos/index.html', context)

def new(request):
    
    return redirect('pos:new')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    Review.objects.create(title=title, content=content)
    return redirect('pos:new')

def detail(request):
    return redirect('pos:index')