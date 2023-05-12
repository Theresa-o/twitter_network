# Generated by Django 4.1.7 on 2023-04-17 10:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_remove_user_authors_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followers',
            old_name='follower',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='followers',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
