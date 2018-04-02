from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _


def validate_range_0_100(value):
    if not (0 <= value <= 100):
        raise ValidationError(
            _('%(value)s must be in the interval [0, 100]'),
            params={'value': value},
        )


class Question(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=254,
        help_text=_('Question\'s short title'),
    )

    body = models.TextField(
        _('Body'),
        help_text=_('Question\'s body (accepts markdown)'),
    )

    level = models.PositiveSmallIntegerField(
        _('Level'),
        validators=[validate_range_0_100],
        help_text=_('Your own classification of level'),
        default=0
    )
