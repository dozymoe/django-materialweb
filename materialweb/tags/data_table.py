import logging
#-
from .base import Node
from .button import IconButton, Icon, Link

_logger = logging.getLogger(__name__)


class DataTable(Node):

    WANT_CHILDREN = True
    NODE_PROPS = ('pager', 'row_selectable', 'row_movable')

    def prepare_values(self, values):
        self.context['selectable'] = self.eval(
                self.kwargs.get('row_selectable'))
        self.context['movable'] = self.eval(
                self.kwargs.get('row_movable'))

        pager = self.eval(self.kwargs.get('pager'))
        if pager:
            self.values['pagination'] = self.render_pagination(pager)
        else:
            self.values['pagination'] = ''


    def render_pagination(self, pager):
        if pager.has_previous():
            cls = Link
            extra_kwargs = {}
        else:
            cls = IconButton
            extra_kwargs = {'disabled': 'disabled'}

        first_button = cls(
                Icon('first_page'),
                **{
                    'label': "First Page",
                    'data-first-page': 'true',
                    'class': 'material-icons mdc-data-table__pagination-button',
                },
                **extra_kwargs)
        prev_button = cls(
                Icon('chevron_left'),
                **{
                    'label': "Previous Page",
                    'data-prev-page': 'true',
                    'class': 'material-icons i'
                        'mdc-data-table__pagination-button',
                },
                **extra_kwargs)

        if pager.has_next():
            cls = Link
            extra_kwargs = {}
        else:
            cls = IconButton
            extra_kwargs = {'disabled': 'disabled'}

        next_button = cls(
                Icon('chevron_right'),
                **{
                    'label': "Next Page",
                    'data-next-page': 'true',
                    'class': 'material-icons mdc-data-table__pagination-button',
                },
                **extra_kwargs)
        last_button = cls(
                Icon('last_page'),
                **{
                    'label': "Next Page",
                    'data-last-page': 'true',
                    'class': 'material-icons mdc-data-table__pagination-button',
                },
                **extra_kwargs)

        values = {
            'page_size': pager.paginator.per_page,
            'total_pages': pager.paginator.num_pages,
            'total_items': pager.paginator.count,
            'start': pager.start_index(),
            'end': pager.end_index(),
            'first_button': first_button.render(self.context),
            'prev_button': prev_button.render(self.context),
            'next_button': next_button.render(self.context),
            'last_button': last_button.render(self.context),
        }
        template = '''
<div class="mdc-data-table__pagination">
  <div class="mdc-data-table__pagination-trailing">
    <div class="mdc-data-table__pagination-rows-per-page">
      <div class="mdc-data-table__pagination-rows-per-page-label">
        Rows per page
      </div>

      <div class="mdc-select mdc-select--outlined mdc-select--no-label mdc-data-table__pagination-rows-per-page-select">
        <div role="button" aria-haspopup="listbox"
            aria-labelledby="demo-pagination-select" tabindex="0"
            class="mdc-select__anchor">
          <span id="demo-pagination-select" class="mdc-select__selected-text">
            {page_size}
          </span>
          <span class="mdc-select__dropdown-icon">
            <svg
                class="mdc-select__dropdown-icon-graphic"
                viewBox="7 10 10 5">
              <polygon
                  class="mdc-select__dropdown-icon-inactive"
                  stroke="none"
                  fill-rule="evenodd"
                  points="7 10 12 15 17 10">
              </polygon>
              <polygon
                  class="mdc-select__dropdown-icon-active"
                  stroke="none"
                  fill-rule="evenodd"
                  points="7 15 12 10 17 15">
              </polygon>
            </svg>
          </span>
          <span class="mdc-notched-outline mdc-notched-outline--notched">
            <span class="mdc-notched-outline__leading"></span>
            <span class="mdc-notched-outline__trailing"></span>
          </span>
        </div>

        <div role="listbox"
            class="mdc-select__menu mdc-menu mdc-menu-surface mdc-menu-surface--fullwidth">
          <ul class="mdc-list">
            <li aria-selected="true" role="option" data-value="10"
                class="mdc-list-item mdc-list-item--selected">
              <span class="mdc-list-item__text">10</span>
            </li>
            <li class="mdc-list-item" role="option" data-value="25">
              <span class="mdc-list-item__text">25</span>
            </li>
            <li class="mdc-list-item" role="option" data-value="100">
              <span class="mdc-list-item__text">100</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="mdc-data-table__pagination-navigation">
      <div class="mdc-data-table__pagination-total">
        {start}‑{end} of {total_items}
      </div>
      {first_button}
      {prev_button}
      {next_button}
      {last_button}
    </div>
  </div>
</div>
'''
        return template.format(**values)


    def template_default(self):
        return '''
<div class="mdc-data-table">
  <div class="mdc-data-table__table-container">
    <table aria-label="{label}" {props} class="mdc-data-table__table {class}">
      {child}
    </table>
  </div>
  {pagination}
</div>
'''


class Head(Node):

    WANT_CHILDREN = True

    def template_default(self):
        return '<thead {props} class="{class}">{child}</thead>'


class HeadRow(Node):

    WANT_CHILDREN = True

    def prepare_values(self, values):
        if self.context['selectable']:
            values['select_checkbox'] = self.render_select()
        else:
            values['select_checkbox'] = ''


    def render_select(self):
        return '''
<th role="columnheader" scope="col"
    class="mdc-data-table__header-cell mdc-data-table__header-cell--checkbox">
  <div class="mdc-checkbox mdc-data-table__header-row-checkbox mdc-checkbox--selected">
    <input type="checkbox" aria-label="Toggle all rows"
        class="mdc-checkbox__native-control" />
    <div class="mdc-checkbox__background">
      <svg viewBox="0 0 24 24" class="mdc-checkbox__checkmark">
        <path fill="none" d="M1.73,12.91 8.1,19.28 22.79,4.59"
            class="mdc-checkbox__checkmark-path" />
      </svg>
      <div class="mdc-checkbox__mixedmark"></div>
    </div>
    <div class="mdc-checkbox__ripple"></div>
  </div>
</th>
'''


    def template_default(self):
        return '''
<tr {props} class="mdc-data-table__header-row {class}">
  {select_checkbox}
  {child}
</tr>
'''


class HeadColumn(Node):

    WANT_CHILDREN = True
    NODE_PROPS = ('type',)

    def prepare_values(self, values):
        type_ = self.kwargs.get('type')
        if type_ == 'num':
            values['class'].append('mdc-data-table__header-cell--numeric')


    def template_default(self):
        return '''
<th role="columnheader" scope="col" {props} class="mdc-data-table__header-cell {class}">
  {child}
</th>
'''


class Body(Node):

    WANT_CHILDREN = True

    def template_default(self):
        return '''
<tbody {props} class="mdc-data-table__content {class}">
  {child}
</tbody>
'''


class BodyRow(Node):

    WANT_CHILDREN = True

    def prepare_values(self, values):
        if self.context['selectable']:
            values['select_checkbox'] = self.render_select()
        else:
            values['select_checkbox'] = ''


    def render_select(self):
        return '''
<td class="mdc-data-table__cell mdc-data-table__cell--checkbox">
  <div class="mdc-checkbox mdc-data-table__row-checkbox">
    <input type="checkbox" aria-labelledby="u0"
        class="mdc-checkbox__native-control" />
    <div class="mdc-checkbox__background">
      <svg viewBox="0 0 24 24" class="mdc-checkbox__checkmark">
        <path fill="none" d="M1.73,12.91 8.1,19.28 22.79,4.59"
            class="mdc-checkbox__checkmark-path" />
      </svg>
      <div class="mdc-checkbox__mixedmark"></div>
    </div>
    <div class="mdc-checkbox__ripple"></div>
  </div>
</td>
'''


    def template_default(self):
        return '''
<tr {props} class="mdc-data-table__row {class}">
  {select_checkbox}
  {child}
</tr>
'''


class BodyColumn(Node):

    WANT_CHILDREN = True
    NODE_PROPS = ('type',)

    def prepare_values(self, values):
        type_ = self.kwargs.get('type')
        if type_ == 'num':
            values['class'].append('mdc-data-table__header-cell--numeric')


    def template_default(self):
        return '<td {props} class="mdc-data-table__cell {class}">{child}</td>'


class BodyColumnHeader(Node):

    WANT_CHILDREN = True
    NODE_PROPS = ('type',)

    def prepare_values(self, values):
        type_ = self.kwargs.get('type')
        if type_ == 'num':
            values['class'].append('mdc-data-table__header-cell--numeric')


    def template_default(self):
        return '''
<th scope="row" {props} class="mdc-data-table__cell {class}">
  {child}
</th>
'''
