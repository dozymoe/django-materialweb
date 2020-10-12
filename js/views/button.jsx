import { MDCIconButtonToggle } from '@material/icon-button';
import { MDCRipple } from '@material/ripple';
import { omit } from 'lodash';
import React, { Component } from 'react';


export class Button extends Component
{
    constructor(props)
    {
        super(props);
        this.el = new React.createRef();
    }

    componentDidMount()
    {
        this.mdc = new MDCRipple(this.el.current);
    }

    componentWillUnmount()
    {
        this.mdc.destroy();
    }

    render()
    {
        let className = this.props.className || '';
        let props = omit(this.props, ['onClick', 'className', 'outlined',
                'raised']);
        if (this.props.outlined)
        {
            className += ' mdc-button--outlined';
        }
        else if (this.props.raised)
        {
            className += ' mdc-button--raised';
        }

        return (

            <div className="mdc-touch-target-wrapper">
              <button ref={this.el} {...props} type={props.type || 'button'}
                  onClick={this.props.onClick}
                  className={'mdc-button mdc-button--touch ' + className}>
                <div className="mdc-button__ripple" />
                {this.props.children}
                <div className="mdc-button__touch" />
              </button>
            </div>

        );
    }
}

Button.Label = class extends Component
{
    shouldComponentUpdate = () => false

    render()
    {
        return (

            <span className="mdc-button__label">
              {this.props.children}
            </span>

        );
    }
}

Button.Icon = class extends Component
{
    render()
    {
        let className = this.props.className || '';
        return (

            <i aria-hidden="true" className={'mdc-button__icon ' + className}>
              {this.props.children}
            </i>

        );
    }
}


export class IconButton extends Component
{
    constructor(props)
    {
        super(props);
        this.el = new React.createRef();
    }

    componentDidMount()
    {
        this.mdc = new MDCRipple(this.el.current);
        this.mdc.unbounded = true;
    }

    componentWillUnmount()
    {
        this.mdc.destroy();
    }

    render()
    {
        let className = this.props.className || '';
        let props = omit(this.props, ['onClick', 'label', 'className', 'icon']);

        return (

            <button ref={this.el} {...props} type={props.type || 'button'}
                onClick={this.props.onClick}
                aria-label={this.props.label} title={this.props.label}
                className={'mdc-icon-button ' + className}>
              {this.props.children}
            </button>

        );
    }
}


export class ToggleButton extends Component
{
    constructor(props)
    {
        super(props);
        this.el = new React.createRef();
    }

    componentDidMount()
    {
        this.mdc = new MDCIconButtonToggle(this.el.current);
    }

    componentWillUnmount()
    {
        this.mdc.destroy();
    }

    render()
    {
        let className = this.props.className || '';
        let props = omit(this.props, ['className', 'state']);
        if (this.props.state)
        {
            className += ' mdc-icon-button--on';
        }

        return (

<button ref={this.el} {...props} type="button" onClick={this.props.onClick}
    aria-label={this.props.label} title={this.props.label}
    aria-pressed={this.props.state}
    className={'mdc-icon-button toggle ' + className}>
  <i className="material-icons mdc-icon-button__icon mdc-icon-button__icon--on">
    {this.props.icon_when_on}
  </i>
  <i className="material-icons mdc-icon-button__icon">
    {this.props.icon_when_off}
  </i>
</button>

        );
    }
}
