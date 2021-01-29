"""
CheckBox
========

See: https://material.io/components/checkboxes

Selection controls allow the user to select options.

Use checkboxes to:

 * Select one or more options from a list
 * Present a list containing sub-selections
 * Turn an item on or off in a desktop environment

"""
from .base import Node


class CheckBox(Node):
    """
    Provides template tag: :code:`CheckBox`.

    """
    WANT_FORM_FIELD = True
    "Template Tag needs form field as first argument."

    def prepare_attributes(self, attrs, default):
        indeterminate = default.get('indeterminate', None)
        if not indeterminate is None:
            attrs['data-indeterminate'] = 'true'
        attrs['class'].append('mdc-checkbox__native-control')


    def prepare(self):
        disabled = self.element_attributes.get('disabled', None)
        if not disabled is None:
            self.values['class'].append('mdc-checkbox--disabled')


    def template_default(self):
        return '''
<{tag} class="mdc-form-field {class}" {props}>
  <div class="mdc-checkbox">
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
</{tag}>
'''


class CheckBoxInput(Node):
    """
    Only the input field without the label.
    """
    WANT_FORM_FIELD = True
    "Template Tag needs form field as first argument."

    def prepare_attributes(self, attrs, default):
        indeterminate = default.get('indeterminate', None)
        if not indeterminate is None:
            attrs['data-indeterminate'] = 'true'
        attrs['class'].append('mdc-checkbox__native-control')


    def prepare(self):
        disabled = self.element_attributes.get('disabled', None)
        if not disabled is None:
            self.values['class'].append('mdc-checkbox--disabled')


    def template_default(self):
        return '''
<div class="mdc-touch-target-wrapper">
  <{tag} class="mdc-checkbox mdc-checkbox--touch {class}" {props}>
    {element}
    <div class="mdc-checkbox__background">
      <svg class="mdc-checkbox__checkmark" viewBox="0 0 24 24">
        <path class="mdc-checkbox__checkmark-path" fill="none"
              d="M1.73,12.91 8.1,19.28 22.79,4.59"/>
      </svg>
      <div class="mdc-checkbox__mixedmark"></div>
    </div>
    <div class="mdc-checkbox__ripple"></div>
  </{tag}>
</div>
'''


components = {
    'CheckBox': CheckBox,
    'CheckBox_Input': CheckBoxInput,
}
