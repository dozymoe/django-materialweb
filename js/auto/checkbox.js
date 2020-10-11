import { MDCCheckbox } from '@material/checkbox';

document.addEventListener(
        'DOMContentLoaded',
        function()
        {
            for (let el of document.querySelectorAll('.mdc-checkbox'))
            {
                new MDCCheckbox(el);
            }
        });
