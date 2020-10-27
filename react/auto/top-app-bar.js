import { MDCTopAppBar } from '@material/top-app-bar';

document.addEventListener(
        'DOMContentLoaded',
        function()
        {
            window.appbar = new MDCTopAppBar(document.querySelector(
                    '.mdc-top-app-bar'));

            let el = document.getElementById('main');
            if (el)
            {
                window.appbar.setScrollTarget(el);
            }
        });
