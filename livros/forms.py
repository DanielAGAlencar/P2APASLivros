from django import forms
from livros.models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'ano_publicacao', 'ed',
                  'n_paginas', 'escritor', 'editora']
