# Generated by Django 4.2.11 on 2024-04-16 11:58

import baseapp_comments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp_pages", "0003_remove_page_snapshot_insert_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="comments_count",
            field=models.JSONField(
                default=baseapp_comments.models.default_comments_count,
                editable=False,
                verbose_name="comments count",
            ),
        ),
        migrations.AlterField(
            model_name="pageevent",
            name="comments_count",
            field=models.JSONField(
                default=baseapp_comments.models.default_comments_count,
                editable=False,
                verbose_name="comments count",
            ),
        ),
    ]
