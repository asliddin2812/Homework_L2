# Generated by Django 5.2.1 on 2025-05-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_nato', '0003_alter_natomember_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natomember',
            name='joined_year',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
