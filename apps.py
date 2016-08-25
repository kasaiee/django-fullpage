from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class FullpageConfig(AppConfig):
    name = 'fullpage'
    verbose_name = _('full page')
