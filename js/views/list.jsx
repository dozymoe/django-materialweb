import { MDCList } from '@material/list';
import { MDCRipple } from '@material/ripple';
import { omit } from 'lodash';
import { observer } from 'mobx-react';
import React, { Component } from 'react';


@observer
export class List extends Component
{
    constructor(props)
    {
        super(props);
        this.el = new React.createRef();
    }

    componentDidMount()
    {
        this.mdc = new MDCList(this.el.current);
        if (this.props.selection)
        {
            this.mdc.singleSelection = true;
        }
    }

    componentWillUnmount()
    {
        this.mdc.destroy();
    }

    render()
    {
        let className = this.props.className || '';
        let selection = this.props.selection;
        let selected = this.props.value;
        let props = omit(this.props, ['className', 'twoLines', 'selection',
                'value']);
        if (this.props.twoLines)
        {
            className += ' mdc-list--two-line';
        }

        return (

            <ul ref={this.el} className={'mdc-list ' + className}
                role={selection ? 'listbox' : null}>
              {React.Children.map(this.props.children, (child, idx) =>
                  {
                    if (React.isValidElement(child))
                    {
                      let value = child.props.value
                                || child.props['data-value'];
                      let className = child.props.className || '';
                      let props = omit(child.props, ['className']);
                      if (selection && value === selected)
                      {
                        className += ' mdc-list-item--selected';
                      }
                      return React.cloneElement(
                          child,
                          {
                            ...props,
                            className: className,
                            role: selection ? 'option' : null,
                            tabIndex: idx,
                            'aria-selected': selection ? value === selected
                                : null,
                          });
                    }
                    return child;
                  })}
            </ul>

        );
    }
}

List.Item = @observer class extends Component
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
        let props = omit(this.props, ['onClick', 'className']);

        return (

            <li ref={this.el} {...props} onClick={this.props.onClick}
                className={'mdc-list-item ' + className}>
              <span className="mdc-list-item__ripple"></span>
              <span className="mdc-list-item__text">
                {this.props.children}
              </span>
            </li>

        );
    }
}

List.Item.Primary = @observer class extends Component
{
    render()
    {
        return (

            <span className="mdc-list-item__primary-text">
              {this.props.children}
            </span>

        );
    }
}

List.Item.Secondary = @observer class extends Component
{
    render()
    {
        return (

            <span className="mdc-list-item__secondary-text">
              {this.props.children}
            </span>

        );
    }
}

List.Divider = class extends Component
{
    shouldComponentUpdate = () => false

    render()
    {
        return <li role="separator" className="mdc-list-divider" />;
    }
}


@observer
export class ListGroup extends Component
{
    render()
    {
        let className = this.props.className || '';
        let props = omit(this.props, ['className']);

        return (

            <div {...props} className={'mdc-list-group ' + className}>
              {this.props.children}
            </div>

        );
    }
}

ListGroup.Heading = @observer class extends Component
{
    render()
    {
        let className = this.props.className || '';
        let props = omit(this.props, ['className']);

        return (

            <h3 className={'mdc-list-group__subheader ' + className}>
              {this.props.children}
            </h3>

        );
    }
}
