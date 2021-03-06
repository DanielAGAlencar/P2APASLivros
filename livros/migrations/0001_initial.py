# Generated by Django 3.0.7 on 2020-06-23 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editora', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Escritor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escritor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano_publicacao', models.CharField(max_length=20)),
                ('ed', models.CharField(max_length=20)),
                ('n_paginas', models.CharField(max_length=100)),
                ('editora', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livros.Editora')),
                ('escritor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livros.Escritor')),
            ],
        ),
    ]
