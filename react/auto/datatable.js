import { MDCDataTable } from '@material/data-table';

document.addEventListener(
        'DOMContentLoaded',
        function()
        {
            for (let el of document.querySelectorAll('.mdc-data-table'))
            {
                new MDCDataTable(el);
            }
        });
