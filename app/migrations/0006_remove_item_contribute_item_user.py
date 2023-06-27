# Generated by Django 4.1.3 on 2023-06-19 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0005_remove_item_user_item_contribute"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="contribute",
        ),
        migrations.AddField(
            model_name="item",
            name="user",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
