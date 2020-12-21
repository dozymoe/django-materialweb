"""Implements Material Design Web Component: Card

Cards contain content and actions about a single subject.

See: https://material.io/components/cards
"""
from .base import Node

class Card(Node):
    """Card component.
    """
    WANT_CHILDREN = True
    MODES = ('elavated', 'outlined')

    def prepare_values(self, values):
        if self.mode == 'elevated':
            values['class'].append('mdc-card--elevated')
        elif self.mode == 'outlined':
            values['class'].append('mdc-card--outlined')


    @property
    def template(self):
        """Get formatted literal string for different types of Card.

        Overridden because the templates are the same.
        """
        return '''
<div class="mdc-card {class}" {props}>
  {child}
</div>
'''


class PrimaryAction(Node):
    """If a majority of the card (or even the entire card) should be actionable.
    """
    WANT_CHILDREN = True

    def template_default(self):
        """Get formatted literal string for actionable Card.
        """
        return '''
<div class="mdc-card__primary-action {class}" tabindex="0" {props}>
  {child}
</div>
'''


class RichMedia(Node):
    """
    This area is used for showing rich media in cards, and optionally as a
    container.
    """
    WANT_CHILDREN = True
    MODES = ('default', 'square')

    def prepare_values(self, values):
        if self.mode == 'square':
            values['class'].append('mdc-card__media--square')


    @property
    def template(self):
        """Get formatted literal string for Card's media.
        """
        return '''
<div class="mdc-card__media {class}" {props}>
  <div class="mdc-card__media-content">
    {child}
  </div>
</div>
'''


class Actions(Node):
    """
    This area is used to show different actions the user can take, typically at
    the bottom of a card. It's often used with buttons.
    """
    WANT_CHILDREN = True
    MODES = ('full_bleed',)

    def prepare_values(self, values):
        if self.mode == 'full_bleed':
            values['class'].append('mdc-card__actions--full-bleed')

        self.context['button_class'] = ['mdc-card__action',
                'mdc-card__action--button']
        self.context['button_icon_class'] = ['mdc-card__action',
                'mdc-card__action--icon']


    @property
    def tempate(self):
        """Get formatted literal string for Card's actions.
        """
        return '''
<div class="mdc-card__actions {class}" {props}>
  {child}
</div>
'''


class Content(Node):
    """
    It can occasionally be useful to add non-semantic elements to a card. For
    instance, some implementations might do this to add an overlay layer.

    In this case, it's important to delineate between semantic (real) content
    and non-semantic content added by the implementation. To achieve this,
    simply wrap the semantic content in an mdc-card__content element. The
    non-semantic content can remain at the card's top level.
    """
    WANT_CHILDREN = True

    def template_default(self):
        """Get formatted literal string for Non-semantic content.
        """
        return '<div class="mdc-card__content {class}" {props}>{child}</div>'
