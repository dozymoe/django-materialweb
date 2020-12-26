"""Implements Material Design Web Component: TextField

Text fields let users enter and edit text.

The text field class consists of the following types:
* Filled text
* Outlined text

See: https://material-components.github.io/material-components-web-catalog/#/component/text-field
""" # pylint:disable=line-too-long

from .base import Node


class TextArea(Node):
    """Textarea component.

    See: https://material.io/develop/web/components/text-fields#textarea
    """
    WANT_FORM_FIELD = True
    MODES = ('filled', 'outlined')

    def prepare_attributes(self, attrs, default):
        """Prepare html input element's attributes.
        """
        attrs['aria-label'] = self.label
        attrs['class'].append('mdc-text-field__input')


    def template_outlined(self):
        """Get formatted literal string for outlined TextArea.

        See: https://material.io/develop/web/components/text-fields#outlined
        """
        return '''
<label class="mdc-text-field mdc-text-field--outlined mdc-text-field--textarea mdc-text-field--no-label {class}">
  <span class="mdc-text-field__resizer">
    {element}
  </span>
  <span class="mdc-notched-outline">
    <span class="mdc-notched-outline__leading"></span>
    <span class="mdc-notched-outline__trailing"></span>
  </span>
</label>
'''


    def template_filled(self):
        """Get formatted literal string for filled TextArea.

        See: https://material.io/develop/web/components/text-fields#filled
        """
        return '''
<label class="mdc-text-field mdc-text-field--filled mdc-text-field--textarea mdc-text-field--no-label {class}">
  <span class="mdc-text-field__ripple"></span>
  <span class="mdc-text-field__resizer">
    {element}
  </span>
  <span class="mdc-line-ripple"></span>
</label>
'''


components = {
    'TextArea': TextArea,
}
