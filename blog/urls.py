from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogLIstView.as_view(), name='home'), 
    path('<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('new/', views.BlogCreateView.as_view(), name='new_post',),
    path('<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),

]
