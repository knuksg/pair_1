from django.urls import path
from . import views

app_name = "pos"

urlpatterns = [
    path('index/', views.index, name='index' ),
    path('new/', views.new, name='new' ),
    path('create/', views.create, name='create' ),
    path('detail/<int:pk_>', views.detail, name='detail' ),
]
