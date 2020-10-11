import { MDCDialog } from '@material/dialog';
import { omit, uniqueId } from 'lodash';
import { observer } from 'mobx-react';
import React, { Component } from 'react';
//-
import { Button } from './button.jsx';


@observer
export class Dialog extends Component
{
    constructor(props)
    {
        super(props);
        this.el = new React.createRef();
        this.id = uniqueId('MDCDialog');
    }

    componentDidMount()
    {
        this.mdc = new MDCDialog(this.el.current);

        if (this.props.onOpen)
        {
            this.mdc.listen('MDCDialog:opened', this.props.onOpen);
        }
        if (this.props.onClose)
        {
            this.mdc.listen('MDCDialog:closing', this.props.onClose);
        }
        if (this.props.outsideElement)
        {
            this.mdc.listen('MDCDialog:opened', () =>
                    {
                        this.props.outsideElement.setAttribute('aria-hidden',
                                'true');
                    });
            this.mdc.listen('MDCDialog:closing', () =>
                    {
                        this.props.outsideElement.removeAttribute(
                                'aria-hidden');
                    });
        }
    }

    componentWillUnmount()
    {
        this.mdc.destroy();
    }

    componentDidUpdate(old)
    {
        if (this.props.visible !== old.visible)
        {
            if (this.props.visible)
            {
                this.mdc.open();
            }
            else
            {
                this.mdc.close();
            }
        }
    }

    render()
    {
        return (

<div ref={this.el} id={this.id} className="mdc-dialog">
  <div className="mdc-dialog__container">
    <div role="alertdialog" aria-modal="true"
        aria-labelledby={this.id + '-title'}
        aria-describedby={this.id + '-content'}
        className="mdc-dialog__surface">
      {React.Children.map(this.props.children, child =>
          {
            if (React.isValidElement(child))
            {
              return React.cloneElement(child, {dialogId: this.id});
            }
            return child;
          })}
    </div>
  </div>
  <div className="mdc-dialog__scrim" />
</div>

        );
    }
}

Dialog.Title = @observer class extends Component
{
    render()
    {
        return (

            <h2 id={this.props.dialogId + '-title'}
                className="mdc-dialog__title">
              {this.props.children}
            </h2>

        );
    }
}

Dialog.Content = @observer class extends Component
{
    render()
    {
        return (

            <div id={this.props.dialogId + '-content'}
                className="mdc-dialog__content">
              {this.props.children}
            </div>
        );
    }
}

Dialog.Actions = @observer class extends Component
{
    render()
    {
        return (

            <div className="mdc-dialog__actions">
              {this.props.children}
            </div>

        );
    }

    static CANCEL = 'cancel'
    static SUBMIT = 'submit'
}

Dialog.Button = @observer class extends Component
{
    render()
    {
        let className = this.props.className || '';
        let props = omit(this.props, ['className', 'action']);
        className += ' mdc-dialog__button';
        if (this.props.action)
        {
            props['data-mdc-dialog-action'] = this.props.action;
        }

        return (

            <Button className={className} {...props}>
              {this.props.children}
            </Button>

        );
    }
}
