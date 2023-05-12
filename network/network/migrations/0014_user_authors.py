# Generated by Django 4.1.7 on 2023-04-12 12:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_remove_user_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='fans', to=settings.AUTH_USER_MODEL),
        ),
    ]
