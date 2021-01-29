"""
Button
======

See: https://material.io/components/buttons

Buttons allow users to take actions, and make choices, with a single tap.

"""
from .base import Node


class Button(Node):
    """
    Provides template tag: :code:`Button`.

    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('outlined', 'raised')
    "Available variants."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."

    def prepare(self):
        if 'button_class' in self.context:
            self.values['class'].extend(self.context['button_class'])

        if self.mode == 'outlined':
            self.values['class'].append('mdc-button--outlined')
        elif self.mode == 'raised':
            self.values['class'].append('mdc-button--raised')


    @property
    def template(self):
        return '''
<div class="mdc-touch-target-wrapper">
  <{tag} class="mdc-button mdc-button--touch {class}" {props}>
    <div class="mdc-button__ripple"></div>
    {child}
    <div class="mdc-button__touch"></div>
  </{tag}>
</div>
'''


class Label(Node):

    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'span'
    "Rendered HTML tag."

    def template_default(self):
        return '''
<{tag} class="mdc-button__label {class}" {props}>
  {child}
</{tag}>
'''


class Icon(Node):

    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'span'
    "Rendered HTML tag."

    def prepare(self):
        if 'button_icon_class' in self.context:
            self.values['class'].extend(self.context['button_icon_class'])


    def template_default(self):
        return '''
<{tag} aria-hidden="true" class="mdc-button__icon {class}" {props}>
  {child}
</{tag}>
'''


class IconButton(Node):

    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."

    def prepare(self):
        if 'button_icon_class' in self.context:
            self.values['class'].extend(self.context['button_icon_class'])
        elif 'button_class' in self.context:
            self.values['class'].extend(self.context['button_class'])


    def template_default(self):
        return '''
<{tag} aria-label="{label}" title="{label}" {props}
    class="mdc-icon-button {class}">
  {child}
</{tag}>
'''


class ToggleButton(Node):

    NODE_PROPS = ('type', 'state', 'icon_when_on', 'icon_when_off')
    "Extended Template Tag arguments."

    def prepare(self):
        self.values['state'] = self.eval(self.kwargs.get('state'))
        self.values['icon_when_on'] = self.kwargs['icon_when_on']
        self.values['icon_when_off'] = self.kwargs['icon_when_off']

        if 'button_class' in self.context:
            self.values['class'].extend(self.context['button_class'])

        if self.values['state']:
            self.values['class'].append('mdc-icon-button--on')
            self.values['props'].append(('aria-pressed', 'true'))


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


components = {
    'Button': Button,
    'Button_Icon': Icon,
    'Button_Label': Label,
    'IconButton': IconButton,
    'ToggleButton': ToggleButton,
}
