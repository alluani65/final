# Generated by Django 5.0 on 2024-04-03 08:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0003_genere_image'),
        ('userapp', '0002_favouritemovie_genere'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favouritemovie',
            unique_together={('user', 'movie', 'genere')},
        ),
    ]
