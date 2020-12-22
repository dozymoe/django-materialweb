"""Implements Material Design Web Component: Banner

A banner displays an important, succinct message, and provides actions for
users to address (or dismiss the banner). It requires a user action to be
dismissed.

Banners should be displayed at the top of the screen, below a top app bar.
They’re persistent and nonmodal, allowing the user to either ignore them or
interact with them at any time. Only one banner should be shown at a time.

See: https://material.io/components/banners
"""
from .base import Node

class Banner(Node):
    """Banner component.
    """
    WANT_CHILDREN = True
    MODES = ('default', 'stacked')

    def prepare_values(self, values):
        if self.mode == 'stacked':
            values['class'].append('mdc-banner--mobile-stacked')


    @property
    def template(self):
        """Get formatted literal string for Banner.

        Overridden because the templates are the same.
        """
        return '''
<div class="mdc-banner {class}" role="banner" {props}>
  <div class="mdc-banner__content" role="status" aria-live="assertive">
    {child}
  </div>
</div>
'''


class Content(Node):
    """Banner content wrapper.
    """
    WANT_CHILDREN = True

    def template_default(self):
        """Get formatted literal string for Banner content wrapper.
        """
        return '''
<div class="mdc-banner__graphic-text-wrapper {class}" {props}>
  {child}
</div>
'''


class Icon(Node):
    """Banner icon content.
    """
    WANT_CHILDREN = True

    def template_default(self):
        """Get formatted literal string for Banner icon content.
        """
        return '''
<div class="mdc-banner__graphic" role="img" alt="{label}">
  <span class="mdc-banner__icon {class}" {props}>
    {child}
  </span>
</div>
'''


class Text(Node):
    """Banner text content.
    """
    WANT_CHILDREN = True

    def template_default(self):
        """Get formatted literal string for Banner text content.
        """
        return '''
<div class="mdc-banner__text {class}" {props}>
  {child}
</div>
'''


class Actions(Node):
    """Banner actions.
    """
    WANT_CHILDREN = True

    def template_default(self):
        """Get formatted literal string for Banner actions.
        """
        return '''
<div class="mdc-banner__actions {class}" {props}>
  {child}
</div>
'''
