# Generated by Django 4.1.7 on 2023-03-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mailing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="emailtemplatecontent",
            name="admin_title",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Picture name"
            ),
        ),
        migrations.AddField(
            model_name="emailtemplateimage",
            name="admin_title",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Picture name"
            ),
        ),
        migrations.AlterField(
            model_name="emailtemplateimage",
            name="image",
            field=models.ImageField(
                upload_to="templates/email/%Y/%m/%d/", verbose_name="Image"
            ),
        ),
    ]
