# Generated by Django 4.1.7 on 2023-04-17 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_alter_followers_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='authors',
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_from_set', to=settings.AUTH_USER_MODEL)),
                ('follow_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_to_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
