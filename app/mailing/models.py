import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class AdminTitleMixin(models.Model):
    admin_title = models.CharField(
        verbose_name=_("Admin name"), blank=False, null=False, max_length=255
    )

    class Meta:
        abstract = True


class EmailTemplateContent(UUIDMixin, TimeStampedMixin, AdminTitleMixin):
    title = models.TextField(verbose_name=_("title"), blank=False, null=False)
    text = HTMLField()

    class Meta:
        db_table = 'content"."email_template'
        verbose_name = _("Email template")
        verbose_name_plural = _("Email templates")

    def __str__(self):
        return self.admin_title


class EmailTemplateImage(UUIDMixin, TimeStampedMixin, AdminTitleMixin):
    template = models.ForeignKey(
        EmailTemplateContent,
        verbose_name=_("Email template"),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        blank=False,
        null=False,
        upload_to="templates/email/%Y/%m/%d/",
    )

    class Meta:
        db_table = 'content"."email_template_picture'
        verbose_name = _("Email template picture")
        verbose_name_plural = _("Email templates pictures")

    def __str__(self):
        return self.admin_title
