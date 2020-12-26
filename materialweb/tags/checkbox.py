"""Implements Material Design Web Component: CheckBox

Selection controls allow the user to select options.

Use checkboxes to:
* Select one or more options from a list
* Present a list containing sub-selections
* Turn an item on or off in a desktop environment

See: https://material-components.github.io/material-components-web-catalog/#/component/checkbox
""" # pylint:disable=line-too-long

from .base import Node


class CheckBox(Node):
    """Checkboxes component.

    See: https://material.io/develop/web/components/input-controls/checkboxes
    """
    WANT_FORM_FIELD = True

    def prepare_attributes(self, attrs, default):
        """Prepare html input element's attributes.
        """
        indeterminate = default.get('indeterminate', None)
        if not indeterminate is None:
            attrs['data-indeterminate'] = 'true'
        attrs['class'].append('mdc-checkbox__native-control')


    def prepare_values(self, values):
        """Prepare values for the formatted literal string.
        """
        disabled = self.element_attributes.get('disabled', None)
        if not disabled is None:
            values['class'].append('mdc-checkbox--disabled')


    def template_default(self):
        """Formatted literal string for CheckBox.
        """
        return '''
<div class="mdc-form-field">
  <div class="mdc-checkbox {class}">
    {element}
    <div class="mdc-checkbox__background">
      <svg class="mdc-checkbox__checkmark" viewBox="0 0 24 24">
        <path class="mdc-checkbox__checkmark-path" fill="none"
              d="M1.73,12.91 8.1,19.28 22.79,4.59"/>
      </svg>
      <div class="mdc-checkbox__mixedmark"></div>
    </div>
    <div class="mdc-checkbox__ripple"></div>
  </div>
  <label for="{id}">{label}</label>
</div>
'''


class CheckBoxInput(Node):
    """Checkboxes component.

    Only the input field without the label.

    See: https://material.io/develop/web/components/input-controls/checkboxes
    """
    WANT_FORM_FIELD = True

    def prepare_attributes(self, attrs, default):
        """Prepare html input element's attributes.
        """
        indeterminate = default.get('indeterminate', None)
        if not indeterminate is None:
            attrs['data-indeterminate'] = 'true'
        attrs['class'].append('mdc-checkbox__native-control')


    def prepare_values(self, values):
        """Prepare values for the formatted literal string.
        """
        disabled = self.element_attributes.get('disabled', None)
        if not disabled is None:
            values['class'].append('mdc-checkbox--disabled')


    def template_default(self):
        """Formatted literal string for CheckBox.
        """
        return '''
<div class="mdc-touch-target-wrapper">
  <div class="mdc-checkbox mdc-checkbox--touch {class}">
    {element}
    <div class="mdc-checkbox__background">
      <svg class="mdc-checkbox__checkmark" viewBox="0 0 24 24">
        <path class="mdc-checkbox__checkmark-path" fill="none"
              d="M1.73,12.91 8.1,19.28 22.79,4.59"/>
      </svg>
      <div class="mdc-checkbox__mixedmark"></div>
    </div>
    <div class="mdc-checkbox__ripple"></div>
  </div>
</div>
'''


components = {
    'CheckBox': CheckBox,
    'CheckBox_Input': CheckBoxInput,
}
