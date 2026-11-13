from django.db import migrations

REPORT_TYPES = (
    ("spam", "Spam", ("comment",), None),
    ("inappropriate", "Inappropriate", ("comment",), None),
    ("fake", "Fake", ("comment",), None),
    ("other", "Other", ("comment", "page", "profile"), None),
    ("scam", "Scam or fraud", ("page", "profile"), None),
    ("adult_content", "Adult Content", ("page", "profile"), None),
    ("violence", "Violence, hate or exploitation", ("page", "profile"), None),
    ("bulling", "Bulling or unwanted contact", ("page", "profile"), None),
    ("pornography", "Pornography", ("page", "profile"), "adult_content"),
    ("childAbuse", "Child abuse", ("page", "profile"), "adult_content"),
    ("prostituition", "Prostituition", ("page", "profile"), "adult_content"),
)


def seed_report_types(apps, schema_editor):
    alias = schema_editor.connection.alias
    ReportType = apps.get_model("baseapp_reports", "ReportType")
    ContentType = apps.get_model("contenttypes", "ContentType")
    targets = {
        "comment": apps.get_model("comments", "Comment"),
        "page": apps.get_model("baseapp_pages", "Page"),
        "profile": apps.get_model("profiles", "Profile"),
    }
    content_types = {}
    for name, model in targets.items():
        content_types[name], _ = ContentType.objects.using(alias).get_or_create(
            app_label=model._meta.app_label, model=model._meta.model_name
        )

    saved = {}
    for key, label, target_names, parent_key in REPORT_TYPES:
        report_type, _ = ReportType.objects.using(alias).update_or_create(
            key=key,
            defaults={"label": label, "parent_type": saved.get(parent_key)},
        )
        report_type.content_types.set([content_types[name] for name in target_names])
        saved[key] = report_type


def remove_report_types(apps, schema_editor):
    keys = [key for key, _, _, _ in REPORT_TYPES]
    apps.get_model("baseapp_reports", "ReportType").objects.using(
        schema_editor.connection.alias
    ).filter(key__in=keys).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("testapp", "0001_initial"),
        ("baseapp_reports", "0001_initial"),
        ("comments", "0003_initial"),
        ("profiles", "0002_initial"),
        ("baseapp_pages", "0002_page_body_es_page_body_pt_page_title_es_and_more"),
    ]

    operations = [migrations.RunPython(seed_report_types, remove_report_types)]
