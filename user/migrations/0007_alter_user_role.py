# Generated by Django 4.1.2 on 2022-11-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_is_staff_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, default='Риелтор', max_length=150, null=True),
        ),
    ]
