# Generated by Django 4.1.2 on 2022-11-08 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_buy', '0005_requestbuy_finished_alter_requestbuy_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestbuy',
            name='no_attention',
            field=models.BooleanField(default=False),
        ),
    ]
