from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import CharField, FileField, EmailField, TextField


class Compliant(models.Model):
    name = CharField(_("Full name"), max_length=255, null=False, blank=False)
    email = EmailField(
        _("Email address"), max_length=255, null=False, blank=False, unique=True
    )
    phone = CharField(
        _("Phone number"), max_length=20, blank=False, null=False, unique=True
    )
    compliant = TextField()
    file = FileField(upload_to="media/", null=True, blank=True)

    def __str__(self):
        return self.name
