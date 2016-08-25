from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from colorfield.fields import ColorField
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


position_types = (
        ('', _('disable')),
        ('left', _('left')),
        ('right', _('right')),
    )


class FullPage(models.Model):
    name = models.CharField(_('fullpage name'), max_length=100)
    autoScrolling = models.BooleanField(_('auto scrolling'), default=True)
    easingCss3 = models.BooleanField(_('css3 easing'), default=True)
    fitToSection = models.BooleanField(_('fit to section'), default=True)
    navigation = models.BooleanField(_('navigation'), default=True)
    navigationPosition = models.CharField(_('navigation position'), choices=position_types, default='left', max_length=5)
    continuousVertical = models.BooleanField(_('continuous vertical'), default=True)
    extraStyleSheet = models.TextField(_('extra styles'), default='')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('full page')
        verbose_name = _('full pages')

class Section(models.Model):
    name = models.CharField(_('section name'), max_length=100)
    fullPage  = models.ForeignKey(FullPage, verbose_name=_('full page'))
    color = ColorField(_('section color'), default='', blank=True)
    backgroundImage = models.ImageField(_('background image'), upload_to='fullpage/section_wallpagers', default='', blank=True)
    is_thumbnail = models.BooleanField(_('is thimbnail?'), default=True, help_text=_('if your background image is tiny this setting must be enable.'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')

class slides(models.Model):
    name = models.CharField(_('slide name'), max_length=100)
    section  = models.ForeignKey(Section, verbose_name=_('section'))
    content = RichTextUploadingField(_('content'), config_name='awesome_ckeditor', default='')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('slide')
        verbose_name_plural = ('slides')