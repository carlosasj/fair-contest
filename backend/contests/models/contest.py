from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _


def avoid_reserved_words(value):
    reserved_words = (
        'admin',
        '',
    )
    if value in reserved_words:
        raise ValidationError(
            _('%(value)s cannot be any of those words: %(reserved_words)s'),
            params={'value': value, 'reserved_words': reserved_words},
        )


class Contest(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=254,
        help_text=_('Contest\'s title'),
    )

    instructions = models.TextField(
        _('Instructions'),
        help_text=_('Instructions are shown above the "Contest\'s Password" field (accepts markdown)'),
        null=True,
        blank=True,
    )

    start_time = models.BigIntegerField(
        _('Start Time (optional)'),
        null=True,
        blank=True,
    )

    end_time = models.BigIntegerField(
        _('End Time (optional)'),
        null=True,
        blank=True,
    )

    password = models.CharField(
        _('Password'),
        max_length=254,
        help_text=_('Contest will be unlocked only after user types this password; '
                    'It will be used to encrypt the questions. (optional)'),
        null=True,
        blank=True,
    )

    url_tag_name = models.CharField(
        _('URL tag name'),
        validators=[avoid_reserved_words],
        max_length=254,
        help_text=_('So users can access the contest using domain.com/myUrlTagName'),
    )
