# Generated by Django 5.0.1 on 2024-03-09 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0008_user_phone_number"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": [
                    ("view_all_users", "can view all users"),
                    ("view_user_email", "can view user's email field"),
                    ("view_user_phone_number", "can view user's phone number field"),
                    ("view_user_is_superuser", "can view user's is_superuser field"),
                    ("view_user_is_staff", "can view user's is_staff field"),
                    ("view_user_is_email_verified", "can view user's is_email_verified field"),
                    (
                        "view_user_password_changed_date",
                        "can view user's password_changed_date field",
                    ),
                    ("view_user_new_email", "can view user's new_email field"),
                    (
                        "view_user_is_new_email_confirmed",
                        "can view user's is_new_email_confirmed field",
                    ),
                ],
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
        ),
    ]
