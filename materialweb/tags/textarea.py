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
    DEFAULT_TAG = 'label'

    def prepare_attributes(self, attrs, default):
        """Prepare html input element's attributes.
        """
        attrs['aria-label'] = self.values['label']
        attrs['class'].append('mdc-text-field__input')


    def prepare(self):
        if self.values.get('label'):
            method = getattr(self, 'template_label_%s' % self.mode)
            self.values['html_label'] = method().format(**self.values)
        else:
            self.values['class'].append('mdc-text-field--no-label')
            self.values['html_label'] = ''


    def template_filled(self):
        """Get formatted literal string for filled TextArea.

        See: https://material.io/develop/web/components/text-fields#filled
        """
        return '''
<{tag}
    class="mdc-text-field mdc-text-field--filled mdc-text-field--textarea {class}"
    {props}>
  <span class="mdc-text-field__ripple"></span>
  <span class="mdc-text-field__resizer">
    {element}
  </span>
  {html_label}
  <span class="mdc-line-ripple"></span>
</{tag}>
'''


    def template_outlined(self):
        """Get formatted literal string for outlined TextArea.

        See: https://material.io/develop/web/components/text-fields#outlined
        """
        return '''
<{tag}
    class="mdc-text-field mdc-text-field--outlined mdc-text-field--textarea {class}"
    {props}>
  <span class="mdc-text-field__resizer">
    {element}
  </span>
  <span class="mdc-notched-outline">
    <span class="mdc-notched-outline__leading"></span>
    {html_label}
    <span class="mdc-notched-outline__trailing"></span>
  </span>
</{tag}>
'''


    def template_label_filled(self):
        return '''
<span id="{id}-label" class="mdc-floating-label">
  {label}
</span>
'''


    def template_label_outlined(self):
        return '''
<span class="mdc-notched-outline__notch">
  <span id="{id}-label" class="mdc-floating-label">
    {label}
  </span>
</span>
'''


components = {
    'TextArea': TextArea,
}
