import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


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
    title = models.TextField(verbose_name=_("E-mail subject"), blank=False, null=False)
    text = models.TextField(verbose_name=_("HTML"), blank=False, null=False)

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


class EmailTemplateContext(UUIDMixin, TimeStampedMixin, AdminTitleMixin):
    custom_title = models.CharField(verbose_name=_('Title'), max_length=100, blank=False, null=False)
    custom_subtitle = models.CharField(verbose_name=_('Subtitile'), max_length=300, blank=False, null=False)
    custom_movieurl = models.URLField(verbose_name=_('Movie page URL'), blank=False, null=False)
    custom_moviename = models.CharField(verbose_name=_('Movie name'), max_length=300, blank=False, null=False)
    custom_text = models.TextField(verbose_name=_('Text'), blank=False, null=False)
    custom_cta = models.CharField(verbose_name=_('Call to action on button'), max_length=30, blank=False, null=False)
    template = models.ForeignKey(EmailTemplateContent, verbose_name=_('E-mail template'), blank=False, null=False,
                                 on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'content"."email_template_context'
        verbose_name = _("Email template context")
        verbose_name_plural = _("Email templates contexts")

    def __str__(self):
        return self.admin_title

    def data_fields(self) -> dict:
        return {"custom_title": self.custom_title,
                "custom_subtitle": self.custom_subtitle,
                "custom_movieurl": self.custom_movieurl,
                "custom_moviename": self.custom_moviename,
                "custom_text": self.custom_text,
                "custom_cta": self.custom_cta}


class EmailAssembled(UUIDMixin, TimeStampedMixin, AdminTitleMixin):
    template = models.ForeignKey(EmailTemplateContent, verbose_name=_('E-mail template'), blank=False, null=False,
                                 on_delete=models.DO_NOTHING, related_name='EmailAssembled')
    context = models.ForeignKey(EmailTemplateContext, verbose_name=_('E-mail context'), blank=False, null=False,
                                on_delete=models.DO_NOTHING)

    title = models.TextField(verbose_name=_("E-mail subject"), blank=False, null=False)
    text = models.TextField(verbose_name=_("HTML"), blank=False, null=False)

    class Meta:
        db_table = 'content"."email_assembled'
        verbose_name = _("Assembled e-mail")
        verbose_name_plural = _("Assembled e-mails")

    def __str__(self):
        return self.admin_title
