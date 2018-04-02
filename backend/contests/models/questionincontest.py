from django.db import models
from django.utils.translation import gettext as _


class QuestionInContest(models.Model):
    question = models.ForeignKey(
        'questions.Question',
        on_delete=models.CASCADE,
        verbose_name=_('Question')
    )

    contest = models.ForeignKey(
        'contests.Contest',
        on_delete=models.CASCADE,
        verbose_name=_('Contest')
    )

    value = models.PositiveSmallIntegerField(
        _('Question\'s value in this contest')
    )

    tries = models.PositiveSmallIntegerField(
        _('How many times the user can try to submit an answer to this question')
    )

    class Meta:
        order_with_respect_to = 'contest'
        unique_together = ('question', 'contest')
