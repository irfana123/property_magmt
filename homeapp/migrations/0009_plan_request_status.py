# Generated by Django 4.1.2 on 2022-11-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homeapp", "0008_plan_request_company_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="plan_request",
            name="status",
            field=models.IntegerField(default=0),
        ),
    ]