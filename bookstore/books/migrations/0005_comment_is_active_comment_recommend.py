# Generated by Django 4.2.6 on 2023-10-11 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0004_alter_comment_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="comment",
            name="recommend",
            field=models.BooleanField(default=True),
        ),
    ]
