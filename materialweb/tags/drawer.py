"""Implements Material Design Web Component: Drawer

A navigation drawer provides access to destinations and app functionality, such
as switching accounts. It can either be permanently on-screen or controlled by
a navigation menu icon.

A navigation drawer is recommended for:

 - Apps with five or more top-level destinations
 - Apps with two or more levels of navigation hierarchy
 - Quick navigation between unrelated destinations

See: https://material.io/components/navigation-drawer
""" # pylint:disable=line-too-long

from .base import Node

class Drawer(Node):
    """Drawer component.
    """
    WANT_CHILDREN = True
    MODES = ('standard', 'modal', 'dismissible')

    def template_standard(self):
        """Get formatted literal string for standard Drawer.
        """
        return '''
<aside class="mdc-drawer {class}" {props}>
  {child}
</aside>
'''


    def template_modal(self):
        """Get formatted literal string for modal Drawer.
        """
        return '''
<aside class="mdc-drawer mdc-drawer--modal {class}" {props}>
  {child}
</aside>
<div class="mdc-drawer-scrim"></div>
'''


    def template_dismissible(self):
        """Get formatted literal string for dismissible Drawer.
        """
        return '''
<aside class="mdc-drawer mdc-drawer--dismissible {class}" {props}>
  {child}
</aside>
'''


class Header(Node):
    """Drawer's header.
    """
    WANT_CHILDREN = True

    def template_default(self):
        """Get formatted literal string for Drawer header.
        """
        return '''
<div class="mdc-drawer__header {class}" {props}>
  {child}
</div>
'''


class Title(Node):
    """Drawer's header title.
    """
    WANT_CHILDREN = True
    NODE_PROPS = ('tag',)

    def prepare_values(self, values):
        values['tag'] = self.kwargs.get('tag', 'h3')


    def template_default(self):
        """Get formatted literal string for Drawer header title.
        """
        return '''
<{tag} class="mdc-drawer__title {class}" {props}>
  {child}
</{tag}>
'''


class SubTitle(Node):
    """Drawer's header subtitle.
    """
    WANT_CHILDREN = True
    NODE_PROPS = ('tag',)

    def prepare_values(self, values):
        values['tag'] = self.kwargs.get('tag', 'h6')


    def template_default(self):
        """Get formatted literal string for Drawer header subtitle.
        """
        return '''
<{tag} class="mdc-drawer__subtitle {class}" {props}>
  {child}
</{tag}>
'''


class Content(Node):
    """Drawer's content.
    """
    WANT_CHILDREN = True

    def template_default(self):
        """Get formatted literal string for Drawer content.
        """
        return '''
<div class="mdc-drawer__content {class}" {props}>
  <nav class="mdc-list">
    {child}
  </nav>
</div>
'''


class AppContent(Node):
    """Wrapper for main content when using Dismissible Drawer.

    Main content includes TopAppBar.
    """
    WANT_CHILDREN = True

    def template_default(self):
        """Get formatted literal string for main content wrapper.
        """
        return '''
<div class="mdc-drawer-app-content {class}" {props}>
  {child}
</div>
'''
