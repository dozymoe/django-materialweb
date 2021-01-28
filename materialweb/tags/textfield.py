"""Implements Material Design Web Component: TextField

Text fields let users enter and edit text.

The text field class consists of the following types:
* Filled text
* Outlined text

See: https://material-components.github.io/material-components-web-catalog/#/component/text-field
""" # pylint:disable=line-too-long

from .base import Node


class TextField(Node):
    """Text field component.

    See: https://material.io/develop/web/components/text-fields
    """
    WANT_FORM_FIELD = True
    MODES = ('filled', 'outlined', 'fullwidth')
    DEFAULT_TAG = 'label'

    def prepare_attributes(self, attrs, default):
        """Prepare html input element's attributes.
        """
        if self.mode == 'fullwidth':
            attrs['aria-label'] = self.values['label']
        else:
            attrs['aria-labelledby'] = self.values['id'] + '-label'
        if not 'placeholder' in attrs:
            attrs['placeholder'] = self.values['label']
        attrs['class'].append('mdc-text-field__input')


    def template_filled(self):
        """Formatted literal string for filled TextField.

        See: https://material.io/develop/web/components/text-fields#filled-text
        """
        return '''
<{tag} class="mdc-text-field mdc-text-field--filled {class}" {props}>
  <span class="mdc-text-field__ripple"></span>
  {element}
  <span id="{id}-label" class="mdc-floating-label">
    {label}
  </span>
  <span className="mdc-line-ripple"></span>
</{tag}>
'''


    def template_outlined(self):
        """Formatted literal string for outlined TextField.

        See: https://material.io/develop/web/components/text-fields#outlined-text
        """ # pylint:disable=line-too-long
        return '''
<{tag} class="mdc-text-field mdc-text-field--outlined {class}" {props}>
  {element}
  <span class="mdc-notched-outline">
    <span class="mdc-notched-outline__leading"></span>
    <span class="mdc-notched-outline__notch">
      <span id="{id}-label" class="mdc-floating-label">
        {label}
      </span>
    </span>
    <span class="mdc-notched-outline__trailing"></span>
  </span>
</{tag}>
'''


    def template_fullwidth(self):
        """Formatted literal string for fullwidth TextField.
        """
        return '''
<{tag}
    className="mdc-text-field mdc-text-field--filled mdc-text-field--fullwidth {class}"
    {props}>
  <span class="mdc-text-field__ripple"></span>
  {element}
  <span class="mdc-line-ripple"></span>
</{tag}>
'''


components = {
    'TextField': TextField,
}
