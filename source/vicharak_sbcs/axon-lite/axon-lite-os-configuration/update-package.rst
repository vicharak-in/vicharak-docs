##################
Update Package
##################

This documentation provides, if there are any updated packages are available from Vicharak and Debian, user will get to
know.

.. warning::
    
    Make sure, Board is connected to internet properly.
   
Debian ( GUI ) 
---------------

1. Select ``Menu`` option and Click on ``Administation``, you will find ``Software Updater``.

.. image:: /_static/images/rk3576-axon-lite/software-update.webp
   :width: 60%

2. ``Software Updater`` will check, if there are any updated packages are available.

.. image:: /_static/images/rk3576-axon-lite/fetch-package.webp
    :width: 60%

3. It will show all updated available packages. You can select which packages you want to update.

.. image:: /_static/images/rk3576-axon-lite/update-package-full.webp 
   :width: 60%

4. Click on ``Install Now``, in order to update it.


Using Command line
-------------

.. code::

    sudo apt update
    sudo apt upgrade
