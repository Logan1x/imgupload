# Generated by Django 3.0.7 on 2020-06-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeapph', '0002_user_titletext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='titletext',
            field=models.CharField(max_length=60),
        ),
    ]
