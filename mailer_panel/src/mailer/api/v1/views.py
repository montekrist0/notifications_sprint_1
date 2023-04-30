from rest_framework import viewsets, filters

from mailer.models import GroupUser, EmailTemplate
from mailer.api.v1.serializers import GroupUserSerializer, EmailTemplateSerializer


class GroupUserViewSet(viewsets.ModelViewSet):
    queryset = GroupUser.objects.all()
    serializer_class = GroupUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'group_id',
    ]


class EmailTemplateReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'id',
    ]
