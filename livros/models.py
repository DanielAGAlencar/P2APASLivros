from django.db import models


class Escritor(models.Model):
    escritor = models.CharField(max_length=100)
    ano_nascimento = models.CharField(max_length=20, null = True)
    nacionalidade = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.escritor


class Editora(models.Model):
    editora = models.CharField(max_length=100)
    ano_fundacao = models.CharField(max_length=20, null = True)
    pais_origem = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.editora


# Create your models here.
class Livro(models.Model):
    nome = models.CharField(max_length=100)
    ano_publicacao = models.CharField(max_length=20)
    ed = models.CharField(max_length=20)
    n_paginas = models.CharField(max_length=100)
    escritor = models.ForeignKey(Escritor, on_delete = models.SET_NULL, null = True)
    editora = models.ForeignKey(Editora, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.nome