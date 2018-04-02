from django.db import models
from django.utils.translation import gettext as _


class QuestionCase(models.Model):
    input = models.TextField(
        _('Question Case\'s Input'),
    )

    output = models.TextField(
        _('Question Case\'s Output'),
    )

    question = models.ForeignKey(
        'questions.Question',
        on_delete=models.CASCADE,
        verbose_name=_('Question')
    )

    class Meta:
        order_with_respect_to = 'question'
