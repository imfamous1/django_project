# Generated by Django 5.1.6 on 2025-03-04 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_alter_users_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
