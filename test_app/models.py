from django.contrib.auth.models import AbstractUser
from django.db import models

from ansible_base.lib.abstract_models import AbstractOrganization, AbstractTeam
from ansible_base.lib.abstract_models.common import NamedCommonModel


class EncryptionModel(NamedCommonModel):
    class Meta:
        app_label = "test_app"

    encrypted_fields = ['testing1', 'testing2']

    testing1 = models.CharField(max_length=1, null=True, default='a')
    testing2 = models.CharField(max_length=1, null=True, default='b')


class Organization(AbstractOrganization):
    pass


class User(AbstractUser):
    pass


class Team(AbstractTeam):
    pass