import logging
from uuid import uuid4
#-
from django import template
from django.template.base import TextNode # pylint:disable=unused-import

_logger = logging.getLogger(__name__)


class Node(template.Node):

    WANT_CHILDREN = False
    "Template Tag needs closing end tag."
    WANT_FORM_FIELD = False
    "Template Tag needs form field as first argument."
    HIDE_FORM_FIELD = False
    "Render form field as hidden input."
    MODES = ()
    "Available variants."
    MUST_HAVE_NODE_PROPS = ('mode', 'tag', 'class', 'label')
    "Base Template Tag arguments."
    NODE_PROPS = ()
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'div'
    "Rendered HTML tag."

    def __init__(self, *args, **kwargs):
        if self.WANT_CHILDREN:
            self.nodelist = args[0]
            self.args = args[1:]
        else:
            self.args = args

        self.context = None
        self.kwargs = kwargs
        self.bound_field = None
        self.id = None
        self.mode = None
        self.values = None


    @property
    def props(self):
        props = [(key, self.eval(val))\
                for (key, val) in self.kwargs.items()\
                if key not in self.MUST_HAVE_NODE_PROPS\
                and key not in self.NODE_PROPS]
        # Ignore properties with falsy value except empty string.
        return [x for x in props if bool(x[1]) or x[1] == '']


    @property
    def child(self):
        if self.WANT_CHILDREN:
            return self.nodelist.render(self.context)
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

        attrs = dict(self.values['props'])
        attrs['class'] = widget_attrs.get('class', '').split()
        if field.help_text:
            attrs['aria-controls'] = self.id + '-hint'
            attrs['aria-describedby'] = self.id + '-hint'

        self.prepare_attributes(attrs, widget_attrs)
        attrs['class'] = ' '.join(attrs['class'])

        if self.HIDE_FORM_FIELD:
            return self.bound_field.as_hidden(attrs=attrs)
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
                raise NotImplementedError("Mode %s is not allowed." %\
                        self.mode)
        else:
            self.mode = 'default'

        if self.WANT_FORM_FIELD:
            self.bound_field = self.args[0].resolve(context)
            self.id = self.bound_field.id_for_label
        else:
            self.id = uuid4().hex

        self.values = values = {
            'id': self.id,
            'tag': self.eval(self.kwargs.get('tag', self.DEFAULT_TAG)),
            'label': self.label,
            'props': self.props,
            'class': self.eval(self.kwargs.get('class', '')).split(),
        }
        self.prepare()

        # Cleanup props
        values['props'] = self.prune_attributes(values['props'])

        values['child'] = self.child
        values['element'] = self.element
        values['class'] = ' '.join(values['class'])
        values['props'] = self.join_attributes(values['props'])

        html = self.template.format(**values)

        if self.WANT_FORM_FIELD and self.bound_field.help_text:
            return html + '\n' + self.element_hint
        return html


    def prune_attributes(self, attrs):
        """Cleanup duplicate attributes.
        """
        added_props = set()

        def _clean_attributes():
            for prop in reversed(attrs):
                prop_name = prop[0]
                if prop_name in added_props:
                    continue
                added_props.add(prop_name)
                yield prop

        return list(_clean_attributes())


    def join_attributes(self, attrs):
        return ' '.join('%s="%s"' % x for x in attrs)


    def prepare_attributes(self, attrs, default):
        pass


    def prepare(self):
        pass


    @property
    def template(self):
        method = getattr(self, 'template_%s' % self.mode, None)
        if not method:
            raise NotImplementedError("Method is missing: template_%s" %\
                    self.mode)

        return method()
