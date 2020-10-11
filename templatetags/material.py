from django import template
#-
from material.tags import button, checkbox, textarea, textfield

register = template.Library()


MATERIAL_TAGS = {
    'Button': button.Button,
    'ButtonIcon': button.Icon,
    'ButtonLabel': button.Label,
    'CheckBox': checkbox.CheckBox,
    'CheckBoxInput': checkbox.CheckBoxInput,
    'IconButton': button.IconButton,
    'TextArea': textarea.TextArea,
    'TextField': textfield.TextField,
    'ToggleButton': button.ToggleButton,
}


def do_parse_tag(parser, token):
    params = token.split_contents()
    tagname = params.pop(0)

    args = []
    kwargs = {}
    for param in params:
        if '=' in param:
            key, val = param.split('=', 1)
        else:
            key, val = (None, param)

        if val[0] in ('"', "'"):
            val = val.strip('"\'')
        else:
            val = template.Variable(param)

        if key:
            kwargs[key] = val
        else:
            args.append(val)

    cls = MATERIAL_TAGS[tagname]

    if getattr(cls, 'WANT_CHILDREN', False):
        nodelist = parser.parse(('end' + tagname,))
        parser.delete_first_token()
        args.insert(0, nodelist)

    return cls(*args, **kwargs)


for name in MATERIAL_TAGS:
    register.tag(name, do_parse_tag)
