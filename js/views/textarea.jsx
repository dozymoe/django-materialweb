import { MDCTextField } from '@material/textfield';
import { uniqueId } from 'lodash';
import { observer } from 'mobx-react';
import React, { Component } from 'react';
//-
import { ensurePrimitive, ensurePrimitiveProps, extract
       } from '../misc/mobx.js';


@observer
export class TextArea extends Component
{
    constructor(props)
    {
        super(props);
        this.el = new React.createRef();
        this.id = uniqueId('MDCTextField');
    }

    componentDidMount()
    {
        this.mdc = new MDCTextField(this.el.current);
    }

    componentWillUnmount()
    {
        this.mdc.destroy();
    }

    renderFilled(props, values)
    {
        return (

            <label ref={this.el}
                className={'mdc-text-field mdc-text-field--filled'
                    + ' mdc-text-field--textarea mdc-text-field--no-label'
                    + values.className}>
              <span className="mdc-text-field__ripple" />
              <span className="mdc-text-field__resizer">
                <textarea {...ensurePrimitiveProps(props)}
                    aria-label={values.label}
                    aria-controls={values.hint ? props.id + '-hint' : null}
                    aria-describedby={values.hint ? props.id + '-hint' : null}
                    className="mdc-text-field__input"></textarea>
              </span>
              <span className="mdc-line-ripple" />
            </label>

        );
    }

    renderOutlined(props, values)
    {
        return (

            <label ref={this.el}
                className={'mdc-text-field mdc-text-field--outlined'
                    + ' mdc-text-field-textarea mdc-text-field--no-label'
                    + values.className}>
              <span className="mdc-text-field__resizer">
                <textarea {...ensurePrimitiveProps(props)}
                    aria-label={values.label}
                    aria-controls={values.hint ? props.id + '-hint' : null}
                    aria-describedby={values.hint ? props.id + '-hint' : null}
                    className="mdc-text-field__input"></textarea>
              </span>
              <span className="mdc-notched-outline">
                <span className="mdc-notched-outline__leading" />
                <span className="mdc-notched-outline__trailing" />
              </span>
            </label>

        );
    }

    render()
    {
        let options, props, values;
        [options, props] = extract(this.props, 'outlined', 'fullwidth',
                'filled');
        [values, props] = extract(props, 'label', 'className', 'hint');

        values.className = values.className ? ' ' + values.className : '';
        if (ensurePrimitive(props.disabled))
        {
            values.className += ' mdc-text-field--disabled';
        }
        props.id = props.id ? ensurePrimitive(props.id) : this.id;

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
