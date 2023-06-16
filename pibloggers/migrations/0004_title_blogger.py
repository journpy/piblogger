# Generated by Django 4.2.1 on 2023-05-18 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pibloggers', '0003_alter_blogpost_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='blogger',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
