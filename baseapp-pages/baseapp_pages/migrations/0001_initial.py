# Generated by Django 5.0.1 on 2024-02-05 01:01

import baseapp_core.models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import pgtrigger.compiler
import pgtrigger.migrations
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("pghistory", "0005_events_middlewareevents"),
    ]

    operations = [
        migrations.CreateModel(
            name="Metadata",
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
                ("target_object_id", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "language",
                    models.CharField(
                        blank=True,
                        choices=settings.LANGUAGES,
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "meta_title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="meta title"
                    ),
                ),
                (
                    "meta_description",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="meta description"
                    ),
                ),
                ("meta_robots", models.CharField(blank=True, max_length=100, null=True)),
                ("meta_og_type", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "meta_og_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=baseapp_core.models.random_name_in("pages/metadata/og_image"),
                    ),
                ),
                (
                    "target_content_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "unique_together": {("target_content_type", "target_object_id", "language")},
            },
        ),
        migrations.CreateModel(
            name="MetadataEvent",
            fields=[
                ("pgh_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "pgh_operation",
                    models.IntegerField(
                        choices=[
                            (1, "Insert"),
                            (2, "Update"),
                            (3, "Delete"),
                            (4, "Insertorupdate"),
                        ],
                        null=True,
                    ),
                ),
                ("pgh_created_at", models.DateTimeField(auto_now_add=True)),
                ("pgh_label", models.TextField(help_text="The event label.")),
                ("id", models.IntegerField()),
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
                ("target_object_id", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "language",
                    models.CharField(
                        blank=True,
                        choices=settings.LANGUAGES,
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "meta_title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="meta title"
                    ),
                ),
                (
                    "meta_description",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="meta description"
                    ),
                ),
                ("meta_robots", models.CharField(blank=True, max_length=100, null=True)),
                ("meta_og_type", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "meta_og_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=baseapp_core.models.random_name_in("pages/metadata/og_image"),
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
                        to="baseapp_pages.metadata",
                    ),
                ),
                (
                    "target_content_type",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        related_query_name="+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="URLPath",
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
                ("path", models.CharField(max_length=500, unique=True)),
                (
                    "language",
                    models.CharField(
                        blank=True,
                        choices=settings.LANGUAGES,
                        max_length=10,
                        null=True,
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
                (
                    "target_object_id",
                    models.PositiveIntegerField(blank=True, db_index=True, null=True),
                ),
                (
                    "target_content_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "URL Path",
                "verbose_name_plural": "URL Paths",
            },
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="metadata",
            trigger=pgtrigger.compiler.Trigger(
                name="snapshot_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "baseapp_pages_metadataevent" ("created", "id", "language", "meta_description", "meta_og_image", "meta_og_type", "meta_robots", "meta_title", "modified", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "pgh_operation", "target_content_type_id", "target_object_id") VALUES (NEW."created", NEW."id", NEW."language", NEW."meta_description", NEW."meta_og_image", NEW."meta_og_type", NEW."meta_robots", NEW."meta_title", NEW."modified", _pgh_attach_context(), NOW(), \'snapshot\', NEW."id", 1, NEW."target_content_type_id", NEW."target_object_id"); RETURN NULL;',
                    hash="053a0e377975654cd1748b1b9e3d309845a2e842",
                    operation="INSERT",
                    pgid="pgtrigger_snapshot_insert_61603",
                    table="baseapp_pages_metadata",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="metadata",
            trigger=pgtrigger.compiler.Trigger(
                name="snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition="WHEN (OLD.* IS DISTINCT FROM NEW.*)",
                    func='INSERT INTO "baseapp_pages_metadataevent" ("created", "id", "language", "meta_description", "meta_og_image", "meta_og_type", "meta_robots", "meta_title", "modified", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "pgh_operation", "target_content_type_id", "target_object_id") VALUES (NEW."created", NEW."id", NEW."language", NEW."meta_description", NEW."meta_og_image", NEW."meta_og_type", NEW."meta_robots", NEW."meta_title", NEW."modified", _pgh_attach_context(), NOW(), \'snapshot\', NEW."id", 2, NEW."target_content_type_id", NEW."target_object_id"); RETURN NULL;',
                    hash="bdeab265107d187a9cba9f2ed2cc6aae84b4a184",
                    operation="UPDATE",
                    pgid="pgtrigger_snapshot_update_0e8cb",
                    table="baseapp_pages_metadata",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="metadata",
            trigger=pgtrigger.compiler.Trigger(
                name="snapshot_delete",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "baseapp_pages_metadataevent" ("created", "id", "language", "meta_description", "meta_og_image", "meta_og_type", "meta_robots", "meta_title", "modified", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "pgh_operation", "target_content_type_id", "target_object_id") VALUES (OLD."created", OLD."id", OLD."language", OLD."meta_description", OLD."meta_og_image", OLD."meta_og_type", OLD."meta_robots", OLD."meta_title", OLD."modified", _pgh_attach_context(), NOW(), \'snapshot\', OLD."id", 3, OLD."target_content_type_id", OLD."target_object_id"); RETURN NULL;',
                    hash="854a6ecb5833cbbb1b8af832cad1f6c12d3652a4",
                    operation="DELETE",
                    pgid="pgtrigger_snapshot_delete_86b8d",
                    table="baseapp_pages_metadata",
                    when="AFTER",
                ),
            ),
        ),
        migrations.AddIndex(
            model_name="urlpath",
            index=models.Index(
                fields=["target_content_type", "target_object_id"],
                name="baseapp_pag_target__0566b8_idx",
            ),
        ),
        migrations.AddConstraint(
            model_name="urlpath",
            constraint=models.UniqueConstraint(
                condition=models.Q(("is_active", True)),
                fields=("path", "language"),
                name="unique_active_path",
            ),
        ),
    ]
