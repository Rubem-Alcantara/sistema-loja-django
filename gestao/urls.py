from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('novo/', views.produto_novo, name='produto_novo'),
    path('editar/<int:produto_id>/', views.produto_edit, name='produto_edit'),
    path('excluir/<int:produto_id>/', views.produto_delete, name='produto_delete'),
    path('accounts/register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]