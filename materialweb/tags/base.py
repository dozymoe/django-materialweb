import logging
from uuid import uuid4
#-
from django import template

_logger = logging.getLogger(__name__)


class Node(template.Node):

    WANT_CHILDREN = False
    WANT_FORM_FIELD = False
    MODES = ()
    MUST_HAVE_NODE_PROPS = ('mode', 'class', 'label')
    NODE_PROPS = ()

    def __init__(self, *args, **kwargs):
        self.args = template.NodeList(*args)
        self.context = None
        self.kwargs = kwargs
        self.bound_field = None
        self.id = None
        self.mode = None
        self.values = None


    @property
    def props(self):
        return ['%s="%s"' % (key, self.eval(val))\
                for (key, val) in self.kwargs.items()\
                if key not in self.MUST_HAVE_NODE_PROPS\
                and key not in self.NODE_PROPS]


    @property
    def child(self):
        if self.WANT_CHILDREN:
            return self.args.render(self.context)
        return ''


    @property
    def label(self):
        if 'label' in self.kwargs:
            return self.eval(self.kwargs['label'])
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


    def eval(self, value):
        if isinstance(value, template.Variable):
            return value.resolve(self.context)
        return value


    def render(self, context):
        self.context = context
        self.mode = self.kwargs.get('mode', None)

        if self.MODES:
            if not self.mode:
                self.mode = self.MODES[0]
            elif self.mode not in self.MODES:
                raise NotImplementedError("Method %s is not allowed." %\
                        self.mode)
        else:
            self.mode = 'default'

        if self.WANT_FORM_FIELD:
            if self.WANT_CHILDREN:
                self.bound_field = self.args[1].resolve(context)
            else:
                self.bound_field = self.args[0].resolve(context)
            self.id = self.bound_field.id_for_label
        else:
            self.id = uuid4().hex

        self.values = values = {
            'id': self.id,
            'label': self.label,
            'element': self.element,
            'props': self.props,
            'class': self.eval(self.kwargs.get('class', '')).split(),
        }
        self.prepare_values(values)
        values['child'] = self.child
        values['class'] = ' '.join(values['class'])

        # Cleanup props
        added_props = set()
        clean_props = []
        for prop in reversed(values['props']):
            prop_name = prop.split('=')[0]
            if prop_name in added_props:
                continue
            added_props.add(prop_name)
            clean_props.append(prop)
        values['props'] = ' '.join(clean_props)

        html = self.template.format(**values)

        if self.WANT_FORM_FIELD and self.bound_field.help_text:
            return html + '\n' + self.element_hint
        return html


    def prepare_attributes(self, attrs, default):
        pass


    def prepare_values(self, values):
        pass


    @property
    def template(self):
        """Get formatted literal string for different types of TextField.
        """
        method = getattr(self, 'template_%s' % self.mode, None)
        if not method:
            raise NotImplementedError("Method is missing: template_%s" %\
                    self.mode)

        return method()
