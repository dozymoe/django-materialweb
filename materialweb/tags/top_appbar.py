"""Implements Material Design Web Component: TopAppBar

The top app bar provides content and actions related to the current screen. It's
used for branding, screen titles, navigation, and actions.

There are two types of top app bar:
1. Regular top app bar
2. Contextual action bar

See: https://material-components.github.io/material-components-web-catalog/#/component/top-app-bar
""" # pylint:disable=line-too-long

from django.utils.translation import gettext as _
#-
from .base import Node

class TopAppBar(Node):
    """TopAppBar component.
    """
    WANT_CHILDREN = True
    MODES = ('default', 'short', 'short_closed', 'fixed', 'prominent', 'dense')
    DEFAULT_TAG = 'header'

    def prepare(self):
        if self.mode == 'short':
            self.values['class'].append('mdc-top-app-bar--short')
        elif self.mode == 'short_closed':
            self.values['class'].append('mdc-top-app-bar--short')
            self.values['class'].append('mdc-top-app-bar--short-collapsed')
        elif self.mode == 'fixed':
            self.values['class'].append('mdc-top-app-bar--fixed')
        elif self.mode == 'prominent':
            self.values['class'].append('mdc-top-app-bar--prominent')
        elif self.mode == 'dense':
            self.values['class'].append('mdc-top-app-bar--dense')


    @property
    def template(self):
        """Get formatted literal string for different types of TopAppBar.

        Overridden because the templates are the same.
        """
        return '''
<{tag} class="mdc-top-app-bar {class}" {props}>
  <div class="mdc-top-app-bar__row">
    {child}
  </div>
</{tag}>
'''


class LeftSection(Node):
    """TopAppBar left section
    """
    WANT_CHILDREN = True
    DEFAULT_TAG = 'section'

    def prepare(self):
        self.context['button_class'] = ['mdc-top-app-bar__action-item']


    def template_default(self):
        return '''
<{tag} {props}
    class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start {class}">
  {child}
</{tag}>
'''


class Menu(Node):
    """TopAppBar navigation button
    """
    WANT_CHILDREN = True

    def prepare(self):
        if not self.values['label']:
            self.values['label'] = _("Open navigation menu")


    def template_default(self):
        return '''
<button type="button" aria-label="{label}" title="{label}" {props}
    class="mdc-top-app-bar__navigation-icon mdc-icon-button {class}">
  {child}
</button>
'''


class Title(Node):
    """TopAppBar title
    """
    WANT_CHILDREN = True

    def template_default(self):
        return '<{tag} class="mdc-top-app-bar__title {class}">{child}</{tag}>'


class RightSection(Node):
    """TopAppBar left section
    """
    WANT_CHILDREN = True
    DEFAULT_TAG = 'section'

    def prepare(self):
        self.context['button_class'] = ['mdc-top-app-bar__action-item']


    def template_default(self):
        return '''
<{tag} role="toolbar" {props}
    class="mdc-top-app-bar__section mdc-top-app-bar__section--align-end {class}">
  {child}
</{tag}>
'''


components = {
    'TopAppBar': TopAppBar,
    'TopAppBar_Left': LeftSection,
    'TopAppBar_Right': RightSection,
    'TopAppBar_Menu': Menu,
    'TopAppBar_Title': Title,
}
