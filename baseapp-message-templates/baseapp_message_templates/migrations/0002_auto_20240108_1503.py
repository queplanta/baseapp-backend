# Generated by Django 3.2.23 on 2024-01-08 15:03

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("baseapp_message_templates", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SmsTemplate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Unique name used to identify this message",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "message",
                    models.TextField(blank=True, help_text="Message to be sent", null=True),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.AlterModelOptions(
            name="emailtemplate",
            options={"ordering": ["-id"]},
        ),
    ]
