# Generated by Django 3.0.6 on 2021-04-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='nombre',
            field=models.CharField(default='', max_length=50),
        ),
    ]
