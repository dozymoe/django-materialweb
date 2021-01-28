from .base import Node


class Button(Node):

    WANT_CHILDREN = True
    MODES = ('outlined', 'raised')
    DEFAULT_TAG = 'button'

    def prepare(self):
        if 'button_class' in self.context:
            self.values['class'].extend(self.context['button_class'])

        if self.mode == 'outlined':
            self.values['class'].append('mdc-button--outlined')
        elif self.mode == 'raised':
            self.values['class'].append('mdc-button--raised')


    @property
    def template(self):
        """Get formatted literal string for different types of Button.

        Overridden because the templates are the same.
        """
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
    DEFAULT_TAG = 'span'

    def template_default(self):
        return '''
<{tag} class="mdc-button__label {class}" {props}>
  {child}
</{tag}>
'''


class Icon(Node):

    WANT_CHILDREN = True
    DEFAULT_TAG = 'span'

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
    DEFAULT_TAG = 'button'

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
