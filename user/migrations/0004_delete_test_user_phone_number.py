# Generated by Django 4.1.2 on 2022-10-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
