# Generated by Django 4.1.2 on 2022-11-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_buy', '0004_requestbuy_rieltor'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestbuy',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='requestbuy',
            name='status',
            field=models.CharField(choices=[('Теплый', 'Теплый'), ('Горящий', 'Горящий'), ('Звершенный', 'Звершенный')], default='Теплый', max_length=30),
        ),
    ]
