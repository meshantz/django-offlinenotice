offlinenotice
=============

Provide a template tag that will display a message if a notice is turned on.
Originally intended for use to display a message that the site will be down for
maintenance in the near future.

To install::

    pip install https://github.com/meshantz/django-offlinenotice.git

Then add ``offlinenotice`` to your installed apps. ::

    INSTALLED_APPS = (
        ...
        'offlinenotice',
        ...
    )

Usage
-----

Once you've installed django-offlinenotice, a new model ``Notice`` is available
in the admin. When you create objects of this type, they become available for
use in the custom template tag ``{% notice <notice-slug> %}``.

You can use reStructuredText_ in your notification messages.

To use a Notice object in your templates, first load the custom templates
provided with django-offlinenotice, and then use the tag::

    {% load notice %}
    ...
    {% notice 'my-notice' %}

Where ``my-notice`` is the slug for a Notice object that you have created. The
tag usage is displayed in the listing of Notices.

You can also enable and disable notices from the admin pages.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
