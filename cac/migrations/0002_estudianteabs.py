# Generated by Django 3.2.14 on 2022-11-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstudianteAbs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=150, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, null=True)),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('matricula', models.CharField(max_length=10, verbose_name='Matricula')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
