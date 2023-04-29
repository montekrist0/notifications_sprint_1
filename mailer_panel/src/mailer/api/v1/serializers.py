from rest_framework import serializers

from mailer.models import (GroupUser,
                           EmailTemplate)


class GroupUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupUser
        fields = '__all__'


class EmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = '__all__'
