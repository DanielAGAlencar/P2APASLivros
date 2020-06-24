from django.urls import path
from .views import list_livro, create_livro, update_livro, delete_livro

urlpatterns = [
    path('', list_livro, name='list_livro'),
    path('new', create_livro, name='create_livro'),
    path('update/<int:id>/', update_livro, name='update_livro'),
    path('delete/<int:id>/', delete_livro, name='delete_livro'),
]