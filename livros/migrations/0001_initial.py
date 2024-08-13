# Generated by Django 5.1 on 2024-08-13 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('escritores', '0001_initial'),
        ('generos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('paginas', models.IntegerField()),
                ('data_criado', models.DateTimeField(auto_now_add=True)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('escritor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escritores.escritor')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generos.genero')),
            ],
        ),
    ]
