from .base import Node


class TextField(Node):

    WANT_FORM_FIELD = True

    def prepare_attributes(self, attrs, default):
        if self.mode == 'fullwidth':
            attrs['aria-label'] = self.label
        else:
            attrs['aria-labelledby'] = self.id + '-label'
        if not 'placeholder' in default:
            attrs['placeholder'] = self.label
        attrs['class'].append('mdc-text-field__input')


    @property
    def template(self):
        if self.mode == 'outlined':
            return self.template_outlined()
        if self.mode == 'fullwidth':
            return self.template_fullwidth()
        return self.template_filled()


    def template_outlined(self):
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
        return '''
<label className="mdc-text-field mdc-text-field--filled mdc-text-field--fullwidth {class}">
  <span class="mdc-text-field__ripple"></span>
  {element}
  <span class="mdc-line-ripple"></span>
</label>
'''
