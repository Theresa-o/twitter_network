# Generated by Django 4.1.7 on 2023-04-12 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_user_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='authors',
        ),
    ]
