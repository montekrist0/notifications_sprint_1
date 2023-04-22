from django.db.models import ForeignKey, OneToOneField, ManyToManyField
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender='mailing.EmailTemplateContext')
def email_assembly(sender, instance, created, **kwargs):
    raw_html = instance.template.text
    context = instance.data_fields()

    for tag, value in context.items():
        tag = '{{' + tag + '}}'
        raw_html = raw_html.replace(tag, value)

    print(f'\n\n\n\n\n\n\n {raw_html} \n\n\n\n\n\n\n')


