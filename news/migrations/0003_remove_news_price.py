# Generated by Django 4.1.2 on 2022-11-07 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_id_alter_news_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='price',
        ),
    ]
