# Generated by Django 3.0.6 on 2021-04-02 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do_list', '0003_auto_20210401_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='usuario',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
