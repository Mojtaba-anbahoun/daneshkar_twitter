# Generated by Django 4.2.1 on 2023-06-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_managers_user_age_user_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(help_text='Password to login', max_length=150, verbose_name='Password:'),
        ),
    ]
