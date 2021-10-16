from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogLIstView.as_view(), name='home'), 
    path('<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
]
