# Generated by Django 5.1 on 2024-08-13 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='status',
            field=models.CharField(choices=[('P', 'Pendente'), ('D', 'Devolvido')], default='Pendente', max_length=10),
        ),
    ]
