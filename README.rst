offlinenotice
=============

Provide a template tag that will display a message if a notice is turned on.
Originally intended for use to display a message that the site will be down for
maintenance in the near future.

To install::

    pip install https://github.com/<username>/django-offlinenotice.git

Then add the ``offlinenotice`` to your installed apps. ::

    INSTALLED_APPS = (
        ...
        'offlinenotice',
        ...
    )

