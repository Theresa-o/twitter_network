# Generated by Django 4.1.7 on 2023-04-17 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0021_remove_followers_follows_remove_followers_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='followers',
            name='follows_before',
            field=models.ManyToManyField(blank=True, related_name='fans_before', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followers',
            name='user_before',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors_before', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='fans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
