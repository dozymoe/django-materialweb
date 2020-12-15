from .base import Node


class Button(Node):

    WANT_CHILDREN = True
    MODES = ('outlined', 'raised')
    NODE_PROPS = ('type',)

    def prepare_values(self, values):
        values['type'] = self.kwargs.get('type', 'button')
        if self.mode == 'outlined':
            values['class'].append('mdc-button--outlined')
        elif self.mode == 'raised':
            values['class'].append('mdc-button--raised')


    @property
    def template(self):
        """Get formatted literal string for different types of Button.

        Overridden because the templates are the same.
        """
        return '''
<div class="mdc-touch-target-wrapper">
  <button type="{type}" class="mdc-button mdc-button--touch {class}" {props}>
    <div class="mdc-button__ripple"></div>
    {child}
    <div class="mdc-button__touch"></div>
  </button>
</div>
'''


class Label(Node):

    WANT_CHILDREN = True

    def template_default(self):
        return '<span class="mdc-button__label">{child}</span>'


class Icon(Node):

    WANT_CHILDREN = True

    def template_default(self):
        return '''
<span aria-hidden="true" class="mdc-button__icon {class}">
  {child}
</span>
'''


class IconButton(Node):

    WANT_CHILDREN = True
    NODE_PROPS = ('type',)

    def prepare_values(self, values):
        values['type'] = self.kwargs.get('type', 'button')


    def template_default(self):
        return '''
<button type="{type}" aria-label="{label}" title="{label}" {props}
    class="mdc-icon-button {class}">
  {child}
</button>
'''


class ToggleButton(Node):

    NODE_PROPS = ('type', 'state', 'icon_when_on', 'icon_when_off')

    def prepare_values(self, values):
        values['state'] = self.eval(self.kwargs.get('state'))
        values['icon_when_on'] = self.kwargs['icon_when_on']
        values['icon_when_off'] = self.kwargs['icon_when_off']

        if values['state']:
            values['class'].append('mdc-icon-button--on')
            values['props'].append(('aria-pressed', 'true'))


    def template_default(self):
        return '''
<button type="button" aria-label="{label}" title="{label}" {props}
    class="mdc-icon-button toggle {class}">
  <i class="material-icons mdc-icon-button__icon mdc-icon-button__icon--on">
    {icon_when_on}
  </i>
  <i class="material-icons mdc-icon-button__icon">
    {icon_when_off}
  </i>
</button>
'''


class Link(Node):
    """Button as link
    """
    WANT_CHILDREN = True
    NODE_PROPS = ('href',)

    def prepare_values(self, values):
        values['href'] = self.eval(self.kwargs.get('href')) or '#'


    def template_default(self):
        return '''
<a href="{href}" aria-label="{label}" title="{label}" {props}
    class="mdc-icon-button {class}">
  {child}
</a>
'''
