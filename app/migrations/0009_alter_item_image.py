# Generated by Django 4.1.3 on 2023-06-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_item_my_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.ImageField(upload_to="media", verbose_name="画像"),
        ),
    ]