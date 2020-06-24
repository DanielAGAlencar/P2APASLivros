from django.shortcuts import render, redirect
from livros.forms import LivroForm
from livros.models import Livro


def list_livro(request):
    livro = Livro.objects.all()
    return render(request, 'livro.html', {'livros': livro})


def create_livro(request):
    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_livro')
    return render(request, 'livro-form.html', {'form': form})


def update_livro(request, id):
    livro = Livro.objects.get(id=id)
    form = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect('list_livro')
    return render(request, 'livro-form.html', {'form': form, 'livro': livro})


def delete_livro(request, id):
    livro = Livro.objects.get(id=id)

    if request.method == 'POST':
        livro.delete()
        return redirect('list_livro')
    return render(request, 'livro-delete-confirm.html', {'livro': livro})
