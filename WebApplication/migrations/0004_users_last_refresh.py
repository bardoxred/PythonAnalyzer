# Generated by Django 5.0 on 2024-01-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "WebApplication",
            "0003_users_is_active_users_is_staff_users_last_login_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="last_refresh",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]