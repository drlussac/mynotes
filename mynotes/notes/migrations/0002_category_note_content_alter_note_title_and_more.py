# Generated by Django 4.2.2 on 2023-06-20 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="note",
            name="content",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="note",
            name="title",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="note",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="notes.category"
            ),
        ),
    ]
