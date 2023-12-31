# Generated by Django 4.2.6 on 2023-11-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
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
                ("seed_conditions", models.CharField(blank=True, max_length=100)),
                ("seed_varieties", models.CharField(blank=True, max_length=100)),
                ("N", models.PositiveIntegerField(null=True)),
                ("P", models.PositiveIntegerField(null=True)),
                ("K", models.PositiveIntegerField(null=True)),
                ("temp", models.PositiveIntegerField(null=True)),
                ("humid", models.PositiveIntegerField(null=True)),
                ("ph", models.PositiveIntegerField(null=True)),
                ("rain", models.PositiveIntegerField(null=True)),
                ("predictions", models.CharField(blank=True, max_length=100)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
