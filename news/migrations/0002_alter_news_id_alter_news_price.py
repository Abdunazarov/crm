# Generated by Django 4.1.2 on 2022-11-07 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]