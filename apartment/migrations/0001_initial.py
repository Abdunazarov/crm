# Generated by Django 4.1.2 on 2022-11-03 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('rooms', models.IntegerField(blank=True, null=True)),
                ('levels', models.IntegerField(blank=True, null=True)),
                ('condition', models.CharField(choices=[('Без ремонта', 'Без ремонта'), ('Средний ремонт', 'Средний ремонт'), ('Евро ремонт', 'Евро ремонт')], default='Средний ремонт', max_length=20)),
                ('comments', models.TextField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='')),
                ('image8', models.ImageField(blank=True, null=True, upload_to='')),
                ('image9', models.ImageField(blank=True, null=True, upload_to='')),
                ('image10', models.ImageField(blank=True, null=True, upload_to='')),
                ('image11', models.ImageField(blank=True, null=True, upload_to='')),
                ('image12', models.ImageField(blank=True, null=True, upload_to='')),
                ('image13', models.ImageField(blank=True, null=True, upload_to='')),
                ('image14', models.ImageField(blank=True, null=True, upload_to='')),
                ('rieltor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
    ]
