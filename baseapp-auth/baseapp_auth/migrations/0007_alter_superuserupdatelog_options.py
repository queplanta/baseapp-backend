# Generated by Django 4.2.3 on 2024-04-09 18:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("baseapp_auth", "0006_alter_superuserupdatelog_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="superuserupdatelog",
            options={"ordering": ["-created"]},
        ),
    ]
