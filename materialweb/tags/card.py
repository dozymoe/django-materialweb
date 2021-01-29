"""
Card
====

See: https://material.io/components/cards

Cards contain content and actions about a single subject.

"""
from .base import Node

class Card(Node):
    """
    Provides template tag: :code:`Card`.

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('elevated', 'outlined')
    "Available variants."

    def prepare(self):
        if self.mode == 'elevated':
            self.values['class'].append('mdc-card--elevated')
        elif self.mode == 'outlined':
            self.values['class'].append('mdc-card--outlined')


    @property
    def template(self):
        return '''
<{tag} class="mdc-card {class}" {props}>
  {child}
</{tag}>
'''


class PrimaryAction(Node):
    """
    If a majority of the card (or even the entire card) should be actionable.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-card__primary-action {class}" tabindex="0" {props}>
  {child}
</{tag}>
'''


class RichMedia(Node):
    """
    This area is used for showing rich media in cards, and optionally as a
    container.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'square')
    "Available variants."

    def prepare(self):
        if self.mode == 'square':
            self.values['class'].append('mdc-card__media--square')


    @property
    def template(self):
        return '''
<{tag} class="mdc-card__media {class}" {props}>
  <div class="mdc-card__media-content">
    {child}
  </div>
</{tag}>
'''


class Actions(Node):
    """
    This area is used to show different actions the user can take, typically at
    the bottom of a card. It's often used with buttons.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'full_bleed')
    "Available variants."

    def prepare(self):
        if self.mode == 'full_bleed':
            self.values['class'].append('mdc-card__actions--full-bleed')

        self.context['button_class'] = ['mdc-card__action',
                'mdc-card__action--button']
        self.context['button_icon_class'] = ['mdc-card__action',
                'mdc-card__action--icon']


    @property
    def template(self):
        return '''
<{tag} class="mdc-card__actions {class}" {props}>
  {child}
</{tag}>
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
    "Template Tag needs closing end tag."

    def template_default(self):
        return '''
<{tag} class="mdc-card__content {class}" {props}>
  {child}
</{tag}>
'''


components = {
    'Card': Card,
    'Card_PrimaryAction': PrimaryAction,
    'Card_Media': RichMedia,
    'Card_Actions': Actions,
    'Card_Content': Content,
}
