# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class School(models.Model):

    #__School_FIELDS__
    school_code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    externalid = models.CharField(max_length=255, null=True, blank=True)

    #__School_FIELDS__END

    class Meta:
        verbose_name        = _("School")
        verbose_name_plural = _("School")


class Classroom(models.Model):

    #__Classroom_FIELDS__
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    cicle_id = models.ForeignKey(Cicle, on_delete=models.CASCADE)
    classroom_code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Classroom_FIELDS__END

    class Meta:
        verbose_name        = _("Classroom")
        verbose_name_plural = _("Classroom")


class Cicle(models.Model):

    #__Cicle_FIELDS__
    year = models.IntegerField(null=True, blank=True)
    start = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Cicle_FIELDS__END

    class Meta:
        verbose_name        = _("Cicle")
        verbose_name_plural = _("Cicle")



#__MODELS__END
