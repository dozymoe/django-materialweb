import { MDCSelect } from '@material/select';
import { omit, uniqueId } from 'lodash';
import { observable } from 'mobx';
import { observer } from 'mobx-react';
import React, { Component } from 'react';
//-
import { ensurePrimitive, ensurePrimitiveProps, extract
       } from '../misc/mobx.js';


@observer
export class Select extends Component
{
    @observable label = ''

    constructor(props)
    {
        super(props);
        this.el = new React.createRef();
        this.id = uniqueId('MDCSelect');
    }

    updateLabel(value)
    {
        let el = this.el.current.querySelector('.mdc-list-item [data-value="'
                + value + '"] .mdc-list-item__text');
        this.label = el ? el.textContent : '';
    }

    componentDidMount()
    {
        this.updateLabel(this.props.value || '');
        this.mdc = new MDCSelect(this.el.current);
        this.mdc.listen('MDCSelect:change', () =>
                {
                    this.updateLabel(this.mdc.value);
                    if (this.props.onChange)
                    {
                        this.props.onChange(this.mdc.value, el);
                    }
                });
    }

    componentWillUnmount()
    {
        this.mdc.destroy();
    }

    renderDropdownIcon()
    {
        return (

            <span className="mdc-select__dropdown-icon">
              <svg viewBox="7 10 10 5"
                  className="mdc-select__dropdown-icon-graphic">
                <polygon points="7 10 12 15 17 10" stroke="none"
                    fillRule="evenodd"
                    className="mdc-select__dropdown-icon-inactive" />
                <polygon points="7 15 12 10 17 15" stroke="none"
                      fillRule="evenodd"
                      className="mdc-select__dropdown-icon-active" />
              </svg>
            </span>

        );
    }

    renderFilled(props, values)
    {
        return (

<div ref={this.el} {...ensurePrimitiveProps(props)}
    className={'mdc-select mdc-select--filled' + values.className}>
  <div role="button" aria-haspopup="listbox"
      aria-labelledby={props.id + '_label ' + props.id + '-selected-text'}
      aria-required={values.required}
      aria-disabled={values.disabled}
      className="mdc-select__anchor">
    <span className="mdc-select__ripple" />
    <span id={props.id + '-selected-text'}
        className="mdc-select__selected-text">
      {this.label}
    </span>
    {this.renderDropdownIcon()}
    {values.label ?
      <span id={props.id + '-label'}
          className="mdc-floating-label mdc-floating-label--float-above">
        {values.label}
      </span> :null}
    <span className="mdc-line-ripple" />
  </div>

  <div role="listbox"
      className={'mdc-select__menu mdc-menu mdc-menu-surface' +
        ' mdc-menu-surface--fullwidth'}>
    <ul className="mdc-list">
      {React.Children.map(this.props.children, (child, idx) =>
          {
            if (React.isValidElement(child))
            {
              let value = child.props.value;
              return React.cloneElement(
                  child,
                  {
                    ...child.props,
                    selected: value === values.value,
                  });
            }
            return child;
          })}
    </ul>
  </div>
</div>

        );
    }

    renderOutlined(props, values)
    {
        return (

<div ref={this.el} {...ensurePrimitiveProps(props)}
    className={'mdc-select mdc-select--outlined' + values.className}>
  <div role="button" aria-haspopup="listbox"
      aria-labelledby={props.id + '-label ' + props.id + '-selected-text'}
      aria-required={values.required}
      aria-disabled={values.disabled}
      className="mdc-select__anchor">
    <span id={props.id + '-selected-text'}
        className="mdc-select__selected-text">
      {this.label}
    </span>
    {this.renderDropdownIcon()}
    <span className="mdc-notched-outline">
      <span className="mdc-notched-outline__leading" />
      {values.label ?
        <span className="mdc-notched-outline__notch">
          <span id={props.id + '-label'}
              className="mdc-floating-label mdc-floating-label--float-above">
            {values.label}
          </span>
        </span> :null}
      <span className="mdc-notched-outline__trailing" />
    </span>
  </div>

  <div role="listbox"
      className={'mdc-select__menu mdc-menu mdc-menu-surface' +
        ' mdc-menu-surface--fullwidth'}>
    <ul className="mdc-list">
      {React.Children.map(this.props.children, (child, idx) =>
          {
            if (React.isValidElement(child))
            {
              let value = child.props.value;
              return React.cloneElement(
                  child,
                  {
                    ...child.props,
                    selected: value === values.value,
                  });
            }
            return child;
          })}
    </ul>
  </div>
</div>

        );
    }

    render()
    {
        let options, props, values;
        [options, props] = extract(this.props, 'outlined', 'filled');
        [values, props] = extract(props, 'className', 'label', 'value',
                'disabled', 'required', 'hint');

        values.className = values.className ? ' ' + values.className : '';
        values.label = ensurePrimitive(values.label);
        values.value = ensurePrimitive(values.value);
        values.disabled = ensurePrimitive(values.disabled);
        values.required = ensurePrimitive(values.required);
        props.id = props.id ? ensurePrimitive(props.id) : this.id;
        if (values.disabled)
        {
            values.className += ' mdc-select--disabled';
        }
        if (values.required)
        {
            values.className += ' mdc-select--required';
        }
        if (!values.label)
        {
            values.className += ' mdc-select--no-label';
        }

        let html;
        if (options.outlined)
        {
            html = this.renderOutlined(props, values);
        }
        else
        {
            html = this.renderFilled(props, values);
        }

        return <>

            {html}
            {values.hint ?
              <div className="mdc-text-field-helper-line">
                <div id={props.id + '-hint'} aria-hidden="true"
                    className="mdc-text-field-helper-text">
                  {values.hint}
                </div>
              </div> :null}
        </>;
    }
}

Select.Item = class extends Component
{
    render()
    {
        let className = this.props.className || '';
        let props = omit(this.props, ['className', 'disabled', 'selected',
                'value']);
        if (this.props.disabled)
        {
            className += ' mdc-list-item--disabled';
        }
        if (this.props.selected)
        {
            className += ' mdc-list-item--selected';
        }

        return (

            <li {...props} role="option" data-value={this.props.value || ''}
                aria-selected={this.props.selected}
                aria-disabled={this.props.disabled}
                className={'mdc-list-item ' + className}>
              <span className="mdc-list-item__ripple" />
              <span className="mdc-list-item__text">
                {this.props.children}
              </span>
            </li>
        );
    }
}
