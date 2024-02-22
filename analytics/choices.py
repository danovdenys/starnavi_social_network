from django.db import models
from django.utils.translation import gettext_lazy as _

class UserActivityChoice(models.TextChoices):
    LOGIN = 'login', _('Login')
    REQUEST = 'request', _('Request')
