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

    def prepare_attributes(self, attrs, default):
        """Prepare html input element's attributes.
        """
        if self.mode == 'fullwidth':
            attrs['aria-label'] = self.label
        else:
            attrs['aria-labelledby'] = self.id + '-label'
        if not 'placeholder' in default:
            attrs['placeholder'] = self.label
        attrs['class'].append('mdc-text-field__input')


    def template_outlined(self):
        """Formatted literal string for outlined TextField.

        See: https://material.io/develop/web/components/text-fields#outlined-text
        """ # pylint:disable=line-too-long
        return '''
<label class="mdc-text-field mdc-text-field--outlined {class}">
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
</label>
'''


    def template_filled(self):
        """Formatted literal string for filled TextField.

        See: https://material.io/develop/web/components/text-fields#filled-text
        """
        return '''
<label class="mdc-text-field mdc-text-field--filled {class}">
  <span class="mdc-text-field__ripple"></span>
  {element}
  <span id="{id}-label" class="mdc-floating-label">
    {label}
  </span>
  <span className="mdc-line-ripple"></span>
</label>
'''


    def template_fullwidth(self):
        """Formatted literal string for fullwidth TextField.
        """
        return '''
<label className="mdc-text-field mdc-text-field--filled mdc-text-field--fullwidth {class}">
  <span class="mdc-text-field__ripple"></span>
  {element}
  <span class="mdc-line-ripple"></span>
</label>
'''


components = {
    'TextField': TextField,
}
