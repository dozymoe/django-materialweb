Getting Started
===============

Introduction
------------

Provides `Material Design Web`_ as Django_ template tags, aimed at advanced
frontend developers.

At the moment, this project does not provide CSS files and javascript files and
assumes that whoever uses this has learned about including those assets
themselves after getting familiar with `Material Design Web`_ documentation and
its components.

Beginner frontend developers will face some difficulties trying to implement
the css and javascript assets.

This project only offers the HTML markups as described in
`Material Design Web`_, it is also designed so you can easily extends the
project with your own components.

Some components work with forms and require that you pass the form field
to the template tags as its first argument.

As a general rule, this project is only going to be used in Django_ templates.

There is a sister project `react-materialweb`_ that gives overview on what
preparing css files and javascript files look like. I used it in my projects to
build assets.

`react-materialweb`_ implements this project as a react_ + mobx_ library, the
components and how to use them is almost exactly the same.


Installation
------------

.. code-block:: sh

    pip install django-materialweb


Requirements
------------

NPM packages @material/* version "^8.0.0".

You may use other versions, but do check if the html markups matched. You can
also extends this project and write your own template tags.


Advanced Usage
--------------

How to extends this project with your own components.

Checkout the tags_ and templatetags_ directories.

Write your own components in your module :code:`tags` directory, following the
examples in this project's tags_ directory.

Create a file in your module :code:`templatetags` directory, for example:
**website_material.py**.

Example content:

.. code-block:: python

    from django import template
    from materialweb.templatetags.materialweb import TagParser
    #-
    from ..tags import mycomponent

    register = template.Library()

    MATERIAL_TAGS = {
        **mycomponent.components,
    }

    _parser = TagParser(MATERIAL_TAGS)
    for name in MATERIAL_TAGS:
        register.tag(name, _parser)


Similar Projects
----------------

 *  `django-material`_, Django-Material offers the alternative approach to
    rendering forms in django. Strong Python/HTML code separation keeps you code
    DRY and free from underline HTML/CSS rendering details.

 *  `django-material-admin`_

Both uses MaterializeCSS_, A modern responsive front-end framework based on
Material Design.

The main difference with their approach is that this project aimed at
implementing the original `Material Design Web`_, it works only on the level of
templates, and provides more than form rendering.

The drawbacks of this project, I think is that MaterializeCSS_ aimed at being
easier to use compared to the original `Material Design Web`_, the class names
are shorter, and more resilient to changes in the framework itself.


.. _Django: https://docs.djangoproject.com/
.. _Material Design Web: https://material.io/design/introduction
.. _django-material: https://github.com/viewflow/django-material
.. _django-material-admin: https://pypi.org/project/django-material-admin/
.. _MaterializeCSS: https://materializecss.com/
.. _react-materialweb: https://github.com/dozymoe/react-materialweb
.. _react: https://reactjs.org
.. _mobx: https://mobx.js.org/README.html
.. _tags: https://github.com/dozymoe/django-materialweb/tree/main/materialweb/tags
.. _templatetags: https://github.com/dozymoe/django-materialweb/tree/main/materialweb/templatetags
