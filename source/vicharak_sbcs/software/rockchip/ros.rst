ROS2 (Robot Operating System)
=============================

The Robot Operating System (ROS) is a set of powerful open-source software libraries and tools that help developers build robotic applications. It provides device drivers, state-of-the-art algorithms, distributed communication, and developer tools that simplify robotics software development.

.. image::  /_static/images/software/software-ros2-logo.webp
    :width: 70%

ROS2 Support at Vicharak
------------------------

Vicharak provides **native and wrapped ROS2 support** across multiple environments through a unified tool called: **vicharak-ros2**

``vicharak-ros2`` is a universal installation and management layer tool designed to:

- Run ROS2 in **any environment**
- Simplify dependency handling
- Provide reproducible setups
- Support multiple ROS2 distributions
- Work across Linux distros and SBCs

The objective is simple:

``Run ROS2 anywhere, without setup friction.``

.. note::

   **Ubuntu & RHEL users:** ROS2 can be installed natively following official documentation on your systems. However, **vicharak-ros2** is recommended for other distros or if you don't want to manage dependency yourself, want simplified management, consistent and quick setup.

Why ROS2 on Vicharak SBCs?
--------------------------

ROS2 applications often require reliable compute performance, stable Linux environments, and predictable dependency handling — all of which are core strengths of Vicharak boards.

Vicharak SBCs are designed to be:

- Powerful enough for robotics workloads suitable for real-time ROS2 nodes
- Optimized for Linux development
- Hardware-friendly ideal for robotics integrations
- Efficient and portable


Vicharak-Ros2
--------------

Currently Available Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**vicharak-ros2** enables you to install any combination of these distributions and packages:

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Distribution
     - **ros-core**
     - **ros-base**
     - **Other**
   * - **Humble**
     - ✓ 
     - ✓ 
     - Manual Installation
   * - **Jazzy**
     - ✓ 
     - ✓ 
     - Manual Installation

.. tip::

   **ros-base** is recommended for most users as it includes essential tools and development support. You can install additional packages manually after setup.


Getting Started
----------------

Install using .deb Package
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download the package


2. Install the package

   .. code-block:: bash

      sudo apt install ./vicharak-ros2-all.deb

3. Run the installer

   .. code-block:: bash

      sudo vicharak-ros2-install

.. note::

   **Installation taking too long?** If the installation process seems stalled, you can safely interrupt it with **Ctrl+C** and rerun: **sudo vicharak-ros2-install**

4. Select your preferred ROS2 distribution and package profile:

   .. image::  /_static/images/software/software-ros2-menu01.webp
       :width: 70%

   .. image::  /_static/images/software/software-ros2-menu02.webp
       :width: 70%

5. Launch ROS2 Environment

   .. code-block:: bash

      sudo ros2-shell

   This opens the configured ROS2 environment.

Uninstall
~~~~~~~~~

1. Exit the ros2-shell

.. code-block:: bash

   exit

2. Remove Vicharak-Ros2

.. code-block:: bash

   sudo apt remove vicharak-ros2

Let's try some examples
-----------------------

Talker and Listener
~~~~~~~~~~~~~~~~~~~

If you installed **ros-base**, you can test ROS2 with built-in demo nodes.

**Terminal 1 - Run the talker (C++):**

.. code-block:: bash

   sudo apt install ros-humble-demo-nodes-cpp

.. code-block:: bash

   ros2 run demo_nodes_cpp talker

**Terminal 2 - Run the listener (Python):**

.. code-block:: bash

   sudo apt install ros-humble-demo-nodes-py

.. code-block:: bash

   ros2 run demo_nodes_py listener

**Expected Output:**

You should see the talker publishing messages and the listener receiving them. This verifies both C++ and Python ROS2 APIs are working correctly.

.. tip::

   This basic example confirms your ROS2 installation is set up correctly. You can now explore more complex examples like running the talker in one in one board and listener in other board.

