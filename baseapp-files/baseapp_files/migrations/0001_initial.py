# Generated by Django 4.2.3 on 2023-12-11 01:52

import base.utils.upload
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
        ("pghistory", "0005_events_middlewareevents"),
    ]

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("parent_object_id", models.PositiveIntegerField(null=True)),
                (
                    "content_type",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("file_name", models.CharField(blank=True, max_length=512, null=True)),
                (
                    "file_size",
                    models.PositiveIntegerField(
                        help_text="File size in bytes", null=True
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        max_length=512,
                        upload_to=base.utils.upload.set_upload_to_random_filename(
                            "files"
                        ),
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=512, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="files_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "parent_content_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FileEvent",
            fields=[
                ("pgh_id", models.AutoField(primary_key=True, serialize=False)),
                ("pgh_created_at", models.DateTimeField(auto_now_add=True)),
                ("pgh_label", models.TextField(help_text="The event label.")),
                ("id", models.IntegerField()),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("parent_object_id", models.PositiveIntegerField(null=True)),
                (
                    "content_type",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("file_name", models.CharField(blank=True, max_length=512, null=True)),
                (
                    "file_size",
                    models.PositiveIntegerField(
                        help_text="File size in bytes", null=True
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        max_length=512,
                        upload_to=base.utils.upload.set_upload_to_random_filename(
                            "files"
                        ),
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=512, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        related_query_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "parent_content_type",
                    models.ForeignKey(
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        related_query_name="+",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "pgh_context",
                    models.ForeignKey(
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="pghistory.context",
                    ),
                ),
                (
                    "pgh_obj",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="event",
                        to="baseapp_files.file",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="file",
            trigger=pgtrigger.compiler.Trigger(
                name="snapshot_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "baseapp_files_fileevent" ("content_type", "created", "created_by_id", "description", "file", "file_name", "file_size", "id", "modified", "name", "parent_content_type_id", "parent_object_id", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "updated") VALUES (NEW."content_type", NEW."created", NEW."created_by_id", NEW."description", NEW."file", NEW."file_name", NEW."file_size", NEW."id", NEW."modified", NEW."name", NEW."parent_content_type_id", NEW."parent_object_id", _pgh_attach_context(), NOW(), \'snapshot\', NEW."id", NEW."updated"); RETURN NULL;',
                    hash="fdaabf389378057e7d8d7b2eeb304517c32c87f6",
                    operation="INSERT",
                    pgid="pgtrigger_snapshot_insert_03cf9",
                    table="baseapp_files_file",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="file",
            trigger=pgtrigger.compiler.Trigger(
                name="snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition="WHEN (OLD.* IS DISTINCT FROM NEW.*)",
                    func='INSERT INTO "baseapp_files_fileevent" ("content_type", "created", "created_by_id", "description", "file", "file_name", "file_size", "id", "modified", "name", "parent_content_type_id", "parent_object_id", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "updated") VALUES (NEW."content_type", NEW."created", NEW."created_by_id", NEW."description", NEW."file", NEW."file_name", NEW."file_size", NEW."id", NEW."modified", NEW."name", NEW."parent_content_type_id", NEW."parent_object_id", _pgh_attach_context(), NOW(), \'snapshot\', NEW."id", NEW."updated"); RETURN NULL;',
                    hash="3985b330fe91b2800d985c283c58abf491adc075",
                    operation="UPDATE",
                    pgid="pgtrigger_snapshot_update_11b9c",
                    table="baseapp_files_file",
                    when="AFTER",
                ),
            ),
        ),
    ]