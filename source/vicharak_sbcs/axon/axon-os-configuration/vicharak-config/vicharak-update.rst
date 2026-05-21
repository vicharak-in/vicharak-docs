Vicharak Update System
======================

Overview
--------

The **Vicharak Update System** provides a mechanism to remotely update system hosted on the Vicharak
update server.

The update framework performs the following tasks:

* Checks whether an update is available
* Maintains update history

Steps to follow for Update Vicharak Board 
------------------------------------------

1. Open a terminal window (``Ctrl+Alt+T``).

2. Run command ``sudo vicharak-config`` in it.

3. Select ``System Maintenance`` option in it by pressing ``Enter`` key.

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ Please select an option below:                                                           │
    │                                                                                          │
    │                                   System Maintenance                                     │
    │                                       Hardware                                           │
    │                                       Overlays                                           │
    │                                     Connectivity                                         │
    │                                   Advanced Options                                       │
    │                                     User Settings                                        │
    │                                     Localization                                         │
    │                                         About                                            │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    │                                                                                          │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

4. Select ``Vicharak Update`` option.

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ System Maintenance                                                                       │
    │                                                                                          │
    │                                    Vicharak Update                                       │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

5. Select ``Check & Apply Update`` option.

.. code-block:: console

    ┌───────────────────────────────────┤ VICHARAK_CONFIG ├────────────────────────────────────┐
    │ Vicharak Update Menu                                                                     │
    │                                                                                          │
    │                                   Check & Apply Updates                                  │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                                                                                          │
    │                      <Ok>                               <Cancel>                         │
    └──────────────────────────────────────────────────────────────────────────────────────────┘

6. The update system shows a terminal progress bar during upgradation process.

Example:

::

   Progress : [###############-------------] 45% (4/9)



System Log 
-----------

Logs are written to:

::

   /opt/vicharak-update/logs/update.log


The menu performs:

* Update availability check
* Progress display
* Success notification

Update Vicharak Kernel Using Command
-------------------------------------

To get ``KERNEL_VERSION``, Run below command in vicharak board.

.. code-block::

   uname -r

Run commands below to upgrade kernel.

.. code-block::

   sudo apt update
   sudo apt install linux-image-<KERNEL_VERSION>

Currently, **5.10.XXX** and **6.1.75** kernel supported in Axon Device.
