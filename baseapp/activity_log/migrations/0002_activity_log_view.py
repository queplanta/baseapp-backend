from django.db import migrations

CREATE_VIEW = """
CREATE VIEW v_activity_log AS
SELECT
    context.id,
    context.created_at,
    context.updated_at,
    NULLIF(context.metadata ->> 'user', '')::bigint AS user_id,
    NULLIF(context.metadata ->> 'profile', '')::bigint AS profile_id,
    context.metadata ->> 'url' AS url,
    context.metadata ->> 'verb' AS verb,
    NULLIF(context.metadata ->> 'visibility', '')::integer AS visibility,
    context.metadata ->> 'ip_address' AS ip_address,
    context.metadata
FROM pghistory_context AS context
"""


class Migration(migrations.Migration):
    dependencies = [
        ("baseapp_activity_log", "0001_initial"),
        ("pghistory", "0006_delete_aggregateevent"),
    ]

    operations = [
        migrations.RunSQL(CREATE_VIEW, reverse_sql="DROP VIEW v_activity_log"),
    ]
