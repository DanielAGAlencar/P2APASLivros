from django.contrib import admin
from .models import Livro, Escritor, Editora
# Register your models here.
admin.site.register(Livro)
admin.site.register(Escritor)
admin.site.register(Editora)
