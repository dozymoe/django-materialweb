import { MDCFormField } from '@material/form-field';

document.addEventListener(
        'DOMContentLoaded',
        function()
        {
            for (let el of document.querySelectorAll('.mdc-form-field'))
            {
                new MDCFormField(el);
            }
        });
