from django.db import models
from django.utils.translation import gettext as _


class Example(models.Model):
    pre_text = models.TextField(
        _('Text before input'),
        help_text=_('Accepts markdown'),
        null=True,
        blank=True,
    )

    input = models.TextField(
        _('Example\'s Input'),
    )

    in_text = models.TextField(
        _('Text between input and output'),
        help_text=_('Accepts markdown'),
        null=True,
        blank=True,
    )

    output = models.TextField(
        _('Example\'s Output'),
    )

    post_text = models.TextField(
        _('Text after output'),
        help_text=_('Accepts markdown'),
        null=True,
        blank=True,
    )

    question = models.ForeignKey(
        'questions.Question',
        on_delete=models.CASCADE,
        verbose_name=_('Question')
    )

    class Meta:
        order_with_respect_to = 'question'
