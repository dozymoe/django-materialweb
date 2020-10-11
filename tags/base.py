from uuid import uuid4
#-
from django import template
from django.utils.functional import cached_property


class Node(template.Node):

    WANT_CHILDREN = False
    WANT_FORM_FIELD = False

    NODE_PROPS = ('mode', 'class', 'label')

    def __init__(self, *args, **kwargs):
        self.args = args
        self.context = None
        self.kwargs = kwargs


    @property
    def props(self):
        return ['%s="%s"' % item for item in self.kwargs.items()\
                if item[0] not in self.NODE_PROPS]


    @property
    def child(self):
        if self.WANT_CHILDREN:
            return self.args[0].render(self.context)
        return ''


    @cached_property
    def bound_field(self):
        if not self.WANT_FORM_FIELD:
            return None

        if self.WANT_CHILDREN:
            var = self.args[1]
        else:
            var = self.args[0]
        return var.resolve(self.context)


    @cached_property
    def id(self):
        if not self.WANT_FORM_FIELD:
            return uuid4().hex
        return self.bound_field.id_for_label


    @property
    def label(self):
        if 'label' in self.kwargs:
            return self.kwargs['label']
        if self.WANT_FORM_FIELD:
            return self.bound_field.label
        return ''


    @property
    def element(self):
        if not self.WANT_FORM_FIELD:
            return ''

        field = self.bound_field
        widget_attrs = field.field.widget.attrs

        attrs = {
            'class': widget_attrs.get('class', '').split(),
        }
        if field.help_text:
            attrs['aria-controls'] = self.id + '-hint'
            attrs['aria-describedby'] = self.id + '-hint'

        self.prepare_attributes(attrs, widget_attrs)
        attrs['class'] = ' '.join(attrs['class'])

        return field.as_widget(attrs=attrs)


    @property
    def element_attributes(self):
        if not self.WANT_FORM_FIELD:
            return {}
        return self.bound_field.field.widget.attrs


    @property
    def element_hint(self):
        return f'''
<div class="mdc-text-field-helper-line">
  <div id="{self.id}-hint" aria-hidden="true"
      class="mdc-text-field-helper-text">
    {self.bound_field.help_text}
  </div>
</div>
'''


    @cached_property
    def mode(self):
        return self.kwargs.get('mode', None)


    def render(self, context):
        self.context = context

        values = {
            'id': self.id,
            'label': self.label,
            'element': self.element,
            'child': self.child,
            'props': self.props,
            'class': self.kwargs.get('class', '').split(),
        }
        self.prepare_values(values)
        values['class'] = ' '.join(values['class'])
        values['props'] = ' '.join(values['props'])

        html = self.template.format(**values)

        if self.WANT_FORM_FIELD and self.bound_field.help_text:
            return html + '\n' + self.element_hint
        return html


    def prepare_attributes(self, attrs, default):
        pass


    def prepare_values(self, values):
        pass
