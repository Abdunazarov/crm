# Generated by Django 4.1.2 on 2022-11-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_buy', '0002_alter_requestbuy_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestbuy',
            name='status',
            field=models.CharField(choices=[('Активный', 'Активный'), ('Горящий', 'Горящий'), ('Звершенный', 'Звершенный')], default='Активный', max_length=30),
        ),
    ]
