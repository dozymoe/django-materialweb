from .base import Node


class TextArea(Node):

    WANT_FORM_FIELD = True

    def prepare_attributes(self, attrs, default):
        attrs['aria-label'] = self.label
        attrs['class'].append('mdc-text-field__input')


    @property
    def template(self):
        if self.mode == 'outlined':
            return self.template_outlined()
        return self.template_filled()


    def template_outlined(self):
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
        return '''
<label class="mdc-text-field mdc-text-field--filled mdc-text-field--textarea mdc-text-field--no-label {class}">
  <span class="mdc-text-field__ripple"></span>
  <span class="mdc-text-field__resizer">
    {element}
  </span>
  <span class="mdc-line-ripple"></span>
</label>
'''
