# Generated by Django 5.0.6 on 2024-05-31 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="date",
            field=models.DateTimeField(auto_created=True),
        ),
    ]