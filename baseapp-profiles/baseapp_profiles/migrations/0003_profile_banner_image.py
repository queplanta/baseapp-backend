# Generated by Django 5.0.3 on 2024-08-14 21:19

import baseapp_core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp_profiles", "0002_profile_blockers_count_profile_blocking_count_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="banner_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=baseapp_core.models.random_name_in("profile_banner_images"),
                verbose_name="banner image",
            ),
        ),
    ]
