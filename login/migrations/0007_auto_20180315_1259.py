# Generated by Django 2.0.2 on 2018-03-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_stories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='url',
            field=models.URLField(max_length=500, unique=True),
        ),
    ]
