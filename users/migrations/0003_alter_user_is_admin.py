# Generated by Django 4.2 on 2023-05-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
