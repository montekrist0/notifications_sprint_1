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


class EmailTemplate(TimeStampedMixin):
    name = models.CharField(_('name'), blank=False, null=False, max_length=255)
    html_text = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'email_templates'
        verbose_name = _('Email Template')
        verbose_name_plural = _('Email Templates')


class GroupUser(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('name'), blank=False, null=False, max_length=255)
    group_id = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'groups_users'
        verbose_name = _('Group user')
        verbose_name_plural = _('Groups users')


class MassNotification(UUIDMixin, TimeStampedMixin):
    body = models.TextField(_('body'), blank=False, null=False)
    group = models.ForeignKey(GroupUser, on_delete=models.SET_NULL, verbose_name=_('group_users'), blank=True,
                              null=True)
    delay = models.IntegerField(_('delay'), blank=False, null=False)

    class Meta:
        db_table = 'mass_notifications'
        verbose_name = _('Mass Notification')
        verbose_name_plural = _('Mass Notifications')


class IndividualNotification(UUIDMixin, TimeStampedMixin):
    email = models.EmailField(_('email'), blank=False, null=False)
    username = models.CharField(_('username'), blank=False, null=False, max_length=255)
    body = models.TextField(_('body'), blank=False, null=False)
    delay = models.IntegerField(_('delay'), blank=False, null=False)

    class Meta:
        db_table = 'individual_notifications'
        verbose_name = _('Individual Notification')
        verbose_name_plural = _('Individual Notifications')
