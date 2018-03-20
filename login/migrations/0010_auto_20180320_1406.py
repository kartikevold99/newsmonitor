# Generated by Django 2.0.2 on 2018-03-20 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20180320_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcing',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_sourcing_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sourcing',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='updated_sourcing_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
