# Generated by Django 4.1.2 on 2022-11-04 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request_buy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestbuy',
            options={'verbose_name': 'Заявка на покупку', 'verbose_name_plural': 'Заявки на покупку'},
        ),
    ]
