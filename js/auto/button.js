import { MDCRipple } from '@material/ripple';

document.addEventListener(
        'DOMContentLoaded',
        function()
        {
            for (let el of document.querySelectorAll('.mdc-button',
                    '.mdc-icon-button'))
            {
                new MDCRipple(el);
            }
        });
