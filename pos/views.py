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
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'pos/new.html', context)

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    Review.objects.create(title=title, content=content)
    return redirect('pos:index')

def detail(request, pk_):
    detail = Review.objects.get(pk=pk_)
    detail.save()
    context = {
        'detail' : detail
    }
    return render(request, 'pos/detail.html', context)

def edit(request, pk_):
    detail = Review.objects.get(pk=pk_)
    context = {
        'detail' : detail
    }
    return render(request, 'pos/edit.html', context)

def update(request, pk_):
    detail = Review.objects.get(pk=pk_)
    title = request.GET.get('title')
    content = request.GET.get('content')
    detail.title = title
    detail.content = content
    detail.save()
    return redirect('pos:index')

def delete(request, pk_):
    delete = Review.objects.get(pk=pk_)
    delete.delete()
    return redirect('pos:index')