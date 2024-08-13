# Generated by Django 5.1 on 2024-08-13 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0002_alter_emprestimo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='status',
            field=models.CharField(choices=[('Pen', 'Pendente'), ('Dev', 'Devolvido')], default='Pendente', max_length=10),
        ),
    ]
