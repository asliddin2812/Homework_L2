# Generated by Django 5.2.1 on 2025-05-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_nato', '0004_alter_natomember_joined_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natomember',
            name='joined_year',
            field=models.DateTimeField(),
        ),
    ]
