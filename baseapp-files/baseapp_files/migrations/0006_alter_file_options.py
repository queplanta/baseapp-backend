# Generated by Django 4.2.3 on 2024-04-09 18:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("baseapp_files", "0005_alter_file_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="file",
            options={
                "ordering": ["id"],
                "verbose_name": "File",
                "verbose_name_plural": "Files",
            },
        ),
    ]
