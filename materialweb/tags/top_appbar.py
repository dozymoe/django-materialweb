"""Implements Material Design Web Component: TopAppBar

The top app bar provides content and actions related to the current screen. It's
used for branding, screen titles, navigation, and actions.

There are two types of top app bar:
1. Regular top app bar
2. Contextual action bar

See: https://material-components.github.io/material-components-web-catalog/#/component/top-app-bar
""" # pylint:disable=line-too-long
from .base import Node

class TopAppBar(Node):
    """TopAppBar component.
    """

    WANT_CHILDREN = True
    MODES = ('short', 'short_closed', 'fixed', 'prominent', 'dense')

    def prepare_values(self, values):
        if self.mode == 'short':
            values['class'].append('mdc-top-app-bar--short')
        elif self.mode == 'short_closed':
            values['class'].append('mdc-top-app-bar--short')
            values['class'].append('mdc-top-app-bar--short-collapsed')
        elif self.mode == 'fixed':
            values['class'].append('mdc-top-app-bar--fixed')
        elif self.mode == 'prominent':
            values['class'].append('mdc-top-app-bar--prominent')
        elif self.mode == 'dense':
            values['class'].append('mdc-top-app-bar--dense')


    @property
    def template(self):
        """Get formatted literal string for different types of TopAppBar.

        Overridden because the templates are the same.
        """
        return '''
<header class="mdc-top-app-bar {class}" {props}>
  <div class="mdc-top-app-bar__row">
    {child}
  </div>
</header>
'''


class LeftSection(Node):
    """TopAppBar left section
    """
    WANT_CHILDREN = True

    def template_default(self):
        return '''
<section {props}
    class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start {class}">
  {child}
</section>
'''


class BrandButton(Node):
    """TopAppBar brand button
    """
    WANT_CHILDREN = True

    def template_default(self):
        return '''
<button type="button" aria-label="{label}" title="{label}" {props}
    class="mdc-top-app-bar__navigation-icon mdc-icon-button {class}">
  {child}
</button>
'''


class BrandLink(Node):
    """TopAppBar brand button
    """
    WANT_CHILDREN = True

    NODE_PROPS = ('mode', 'class', 'label', 'href')

    def prepare_values(self, values):
        values['href'] = self.kwargs.get('href', '#')


    def template_default(self):
        return '''
<a href="{href}" aria-label="{label}" title="{label}" {props}
    class="mdc-top-app-bar__navigation-icon mdc-icon-button {class}">
  {child}
</a>
'''


class Title(Node):
    """TopAppBar title
    """
    WANT_CHILDREN = True

    NODE_PROPS = ('mode', 'class', 'tag')

    def prepare_values(self, values):
        values['tag'] = self.kwargs.get('tag', 'span')


    def template_default(self):
        return '<{tag} class="mdc-top-app-bar__title {class}">{child}</{tag}>'


class RightSection(Node):
    """TopAppBar left section
    """
    WANT_CHILDREN = True

    def template_default(self):
        return '''
<section role="toolbar" {props}
    class="mdc-top-app-bar__section mdc-top-app-bar__section--align-end {class}">
  {child}
</section>
'''


class IconButton(Node):
    """TopAppBar button icon
    """
    WANT_CHILDREN = True

    def template_default(self):
        return '''
<button type="button" aria-label="{label}" title="{label}" {props}
    class="mdc-top-app-bar__action-item mdc-icon-button {class}">
  {child}
</button>
'''


class Link(Node):
    """TopAppBar link item
    """
    WANT_CHILDREN = True

    NODE_PROPS = ('mode', 'class', 'label', 'href')

    def prepare_values(self, values):
        values['href'] = self.kwargs.get('href', '#')


    def template_default(self):
        return '''
<a href="{href}" aria-label="{label}" title="{label}" {props}
    class="mdc-top-app-bar__action-item mdc-icon-button {class}">
  {child}
</a>
'''
