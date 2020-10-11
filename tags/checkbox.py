from .base import Node


class CheckBox(Node):

    WANT_FORM_FIELD = True

    def prepare_attributes(self, attrs, default):
        indeterminate = default.get('indeterminate', None)
        if not indeterminate is None:
            attrs['data-indeterminate'] = 'true'
        attrs['class'].append('mdc-checkbox__native-control')


    def prepare_values(self, values):
        disabled = self.element_attributes.get('disabled', None)
        if not disabled is None:
            values['class'].append('mdc-checkbox--disabled')


    @property
    def template(self):
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

    WANT_FORM_FIELD = True

    def prepare_attributes(self, attrs, default):
        indeterminate = default.get('indeterminate', None)
        if not indeterminate is None:
            attrs['data-indeterminate'] = 'true'
        attrs['class'].append('mdc-checkbox__native-control')


    def prepare_values(self, values):
        disabled = self.element_attributes.get('disabled', None)
        if not disabled is None:
            values['class'].append('mdc-checkbox--disabled')


    @property
    def template(self):
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
