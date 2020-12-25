import logging
#-
from django import template
#-
from ..tags import banner, button, card, checkbox, data_table, drawer, imagelist
from ..tags import select, textarea, textfield, top_appbar

_logger = logging.getLogger(__name__)
register = template.Library()


MATERIAL_TAGS = {
    'Banner': banner.Banner,
    'Banner_Content': banner.Content,
    'Banner_Icon': banner.Icon,
    'Banner_Text': banner.Text,
    'Banner_Actions': banner.Actions,
    'Button': button.Button,
    'Button_Icon': button.Icon,
    'Button_Label': button.Label,
    'Card': card.Card,
    'Card_PrimaryAction': card.PrimaryAction,
    'Card_Media': card.RichMedia,
    'Card_Actions': card.Actions,
    'Card_Content': card.Content,
    'CheckBox': checkbox.CheckBox,
    'CheckBox_Input': checkbox.CheckBoxInput,
    'Drawer': drawer.Drawer,
    'Drawer_Header': drawer.Header,
    'Drawer_Title': drawer.Title,
    'Drawer_SubTitle': drawer.SubTitle,
    'Drawer_Content': drawer.Content,
    'Drawer_AppContent': drawer.AppContent,
    'DataTable': data_table.DataTable,
    'DataTable_Head': data_table.Head,
    'DataTable_Head_Row': data_table.HeadRow,
    'DataTable_Head_Col': data_table.HeadColumn,
    'DataTable_Body': data_table.Body,
    'DataTable_Row': data_table.BodyRow,
    'DataTable_Col': data_table.BodyColumn,
    'DataTable_ColHeader': data_table.BodyColumnHeader,
    'IconButton': button.IconButton,
    'ImageList': imagelist.ImageList,
    'ImageList_Item': imagelist.ListItem,
    'Link': button.Link,
    'Select': select.Select,
    'Select_Item': select.Item,
    'TextArea': textarea.TextArea,
    'TextField': textfield.TextField,
    'ToggleButton': button.ToggleButton,
    'TopAppBar': top_appbar.TopAppBar,
    'TopAppBar_Left': top_appbar.LeftSection,
    'TopAppBar_Right': top_appbar.RightSection,
    'TopAppBar_BrandButton': top_appbar.BrandButton,
    'TopAppBar_BrandLink': top_appbar.BrandLink,
    'TopAppBar_Title': top_appbar.Title,
    'TopAppBar_Button': top_appbar.IconButton,
    'TopAppBar_Link': top_appbar.Link,
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
