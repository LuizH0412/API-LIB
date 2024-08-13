# Generated by Django 5.1 on 2024-08-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escritor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField()),
                ('data_falecimento', models.DateField(blank=True, null=True)),
                ('idade', models.IntegerField()),
                ('nacionalidade', models.CharField(max_length=20)),
                ('data_criado', models.DateTimeField(auto_now_add=True)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'escritores',
            },
        ),
    ]
