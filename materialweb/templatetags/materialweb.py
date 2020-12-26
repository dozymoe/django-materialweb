import logging
#-
from django import template
#-
from ..tags import banner, button, card, checkbox, data_table, drawer, imagelist
from ..tags import lists, select, textarea, textfield, top_appbar

_logger = logging.getLogger(__name__)
register = template.Library()


MATERIAL_TAGS = {
    **banner.components,
    **button.components,
    **card.components,
    **checkbox.components,
    **data_table.components,
    **drawer.components,
    **imagelist.components,
    **lists.components,
    **select.components,
    **textarea.components,
    **textfield.components,
    **top_appbar.components,
}


class TagParser:

    def __init__(self, tags):
        self.tags = tags

    def __call__(self, parser, token):
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
                val = template.Variable(val)

            if key:
                kwargs[key] = val
            else:
                args.append(val)

        cls = self.tags[tagname]

        if getattr(cls, 'WANT_CHILDREN', False):
            nodelist = parser.parse(('end' + tagname,))
            parser.delete_first_token()
            args.insert(0, nodelist)

        return cls(*args, **kwargs)


_parser = TagParser(MATERIAL_TAGS)
for name in MATERIAL_TAGS:
    register.tag(name, _parser)
