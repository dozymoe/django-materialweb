import { MDCTextField } from '@material/textfield';

document.addEventListener(
        'DOMContentLoaded',
        function()
        {
            for (let el of document.querySelectorAll('.mdc-text-field'))
            {
                new MDCTextField(el);
            }
        });
