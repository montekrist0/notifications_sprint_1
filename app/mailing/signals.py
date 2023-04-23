from django.db.models import ForeignKey, OneToOneField, ManyToManyField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from .models import EmailAssembled, EmailTemplateContent


@receiver(post_save, sender='mailing.EmailTemplateContext')
def email_assembly(sender, instance, created, **kwargs):
    raw_html = instance.template.text
    context = instance.data_fields()

    for tag, value in context.items():
        tag = '{{' + tag + '}}'
        raw_html = raw_html.replace(tag, value)

    email_template = get_object_or_404(EmailTemplateContent, pk=instance.template.id)

    EmailAssembled.objects.create(
        admin_title=f'templ_{instance.template.admin_title}+context_{instance.admin_title}',
        title=instance.template.title,
        template=email_template,
        context=instance,
        text=raw_html
    )
