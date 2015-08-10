from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    main_character = models.OneToOneField(
            'profile.Character',
            related_name='main_user',
            null=True, blank=True)

    def __unicode__(self):
        if self.main_character is not None:
            return self.main_character.fullname
        return self.username


class Character(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    owner = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name='characters',
            null=True, blank=True)

    @property
    def fullname(self):
        if self.lastname is not None:
            return self.firstname + ' ' + self.lastname
        return self.firstname

    def __unicode__(self):
        return self.fullname

    class Meta:
        unique_together = (('firstname', 'lastname'),)
