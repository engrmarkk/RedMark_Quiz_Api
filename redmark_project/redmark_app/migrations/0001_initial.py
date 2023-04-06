# Generated by Django 4.1.7 on 2023-04-06 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import redmark_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email address"
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("scores", models.IntegerField(default=0)),
                ("taken", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "answer",
                    models.CharField(
                        choices=[
                            (redmark_app.models.Answer_enum["A"], "a"),
                            (redmark_app.models.Answer_enum["B"], "b"),
                            (redmark_app.models.Answer_enum["C"], "c"),
                            (redmark_app.models.Answer_enum["D"], "d"),
                            (redmark_app.models.Answer_enum["E"], "e"),
                        ],
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("question_text", models.TextField()),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question_answer",
                        to="redmark_app.answer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Options",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("a", models.TextField()),
                ("b", models.TextField()),
                ("c", models.TextField()),
                ("d", models.TextField()),
                ("e", models.TextField()),
                (
                    "question",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quest_options",
                        to="redmark_app.question",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Is_answered",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="redmark_app.question",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="redmark_app.question",
            ),
        ),
    ]