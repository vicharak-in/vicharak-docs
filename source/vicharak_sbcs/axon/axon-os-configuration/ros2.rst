==========================================
ROS2 (Robot Operating System)
==========================================

The Robot Operating System (ROS) is a set of powerful open-source software libraries and tools that help developers build robotic applications. It provides device drivers, state-of-the-art algorithms, distributed communication, and developer tools that simplify robotics software development.

.. image:: /_static/images/rk3588-axon/software-ros-logo.webp
   :width: 100%

Why ROS2 on Vicharak SBCs?
==========================

ROS2 applications often require reliable compute performance, stable Linux environments, and predictable dependency handling all of which are core strengths of Vicharak boards.

Vicharak SBCs are designed to be:

- Powerful enough for robotics workloads suitable for real-time ROS2 nodes
- Optimized for Linux development
- Hardware-friendly ideal for robotics integrations
- Efficient and portable

Installation Guide
===================

1. Set Locale
--------------

Check for UTF-8 support:

.. code-block:: bash

    locale

Install locale packages:

.. code-block:: bash

    sudo apt update && sudo apt install locales

Generate and configure locale:

.. code-block:: bash

    sudo locale-gen en_US en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    export LANG=en_US.UTF-8

Verify the settings:

.. code-block:: bash

    locale

2. Setup Sources
----------------

You will need to add the ROS 2 apt repository to your system.

.. code-block:: bash

    sudo apt install software-properties-common
    sudo add-apt-repository universe

The ros-apt-source packages provide keys and apt source configuration for the various ROS repositories.

Installing the ros2-apt-source package will configure ROS 2 repositories for your system. Updates to repository configuration will occur automatically when new versions of this package are released to the ROS repositories.

Install curl:

.. code-block:: bash

    sudo apt update && sudo apt install curl -y

Download and install ROS 2 apt source:

.. code-block:: bash

    export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')

.. code-block:: bash

    curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"

.. code-block:: bash

    sudo dpkg -i /tmp/ros2-apt-source.deb

3. Install ROS 2 Packages
--------------------------

Update your apt repository caches after setting up the repositories.

.. code-block:: bash

    sudo apt update

ROS 2 packages are built on frequently updated Ubuntu systems. It is always recommended that you ensure your system is up to date before installing new packages.

.. code-block:: bash

    sudo apt upgrade

.. warning::

    Due to early updates in Ubuntu 22.04 it is important that systemd and udev-related packages are updated before installing ROS 2. The installation of ROS 2's dependencies on a freshly installed system without upgrading can trigger the removal of critical system packages.

    Please refer to `ros2/ros2#1272 <https://github.com/ros2/ros2/issues/1272>`_ and `Launchpad #1974196 <https://bugs.launchpad.net/ubuntu/+bug/1974196>`_ for more information.

Installation Variants
~~~~~~~~~~~~~~~~~~~~~~

Choose your installation variant based on your needs:

.. tip::

    Check your Ubuntu version by running the command : cat /etc/os-release , to make your choice

.. note::

    You have to install only one package given below, ROS-Core already comes with ROS-Base + other packages

.. list-table:: ROS 2 Installation Variants
   :header-rows: 1
   :widths: 15 15 25 45

   * - Ubuntu Version
     - ROS 2 Version
     - Installation Type
     - Installation Command & Description

   * - Ubuntu 22.04 (Jammy)
     - Humble
     - **ROS-Base Install** (Recommended)
     - Communication libraries, message packages, command line tools.
     
       .. code-block:: bash
       
           sudo apt install ros-humble-ros-base

   * - Ubuntu 24.04 (Noble)
     - Jazzy
     - **ROS-Base Install** (Recommended)
     - Communication libraries, message packages, command line tools.
     
       .. code-block:: bash
       
           sudo apt install ros-jazzy-ros-base

   * - Ubuntu 22.04 (Jammy)
     - Humble
     - **ROS-Core**
     - Minimal core packages only.
     
       .. code-block:: bash
       
           sudo apt install ros-humble-ros-core

   * - Ubuntu 24.04 (Noble)
     - Jazzy
     - **ROS-Core**
     - Minimal core packages only.
     
       .. code-block:: bash
       
           sudo apt install ros-jazzy-ros-core

   * - Ubuntu 22.04 (Jammy)
     - Humble
     - **Development Tools**
     - Compilers and other tools to build ROS packages.
     
       .. code-block:: bash
       
           sudo apt install ros-dev-tools

   * - Ubuntu 24.04 (Noble)
     - Jazzy
     - **Development Tools**
     - Compilers and other tools to build ROS packages.
     
       .. code-block:: bash
       
           sudo apt install ros-dev-tools

4. Environment Setup
---------------------

Sourcing the Setup Script
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    You have to replace <distro-name> in below commands with your ROS distro version, for example for humble : source /opt/ros/humble/setup.bash , for Jazzy : source /opt/ros/jazzy/setup.bash

Set up your environment by sourcing the following file.

.. code-block:: bash

    source /opt/ros/<distro-name>/setup.bash

.. note::

    Replace .bash with your shell if you’re not using bash. Possible values are: setup.bash, setup.sh, setup.zsh.

Getting Started
==================

Talker-Listener
---------------

If you installed ros-humble-desktop above you can try some examples.

.. note::

    Replace the <distro-name> with your actual distro name. For example, for humble : sudo apt install ros-humble-demo-nodes-cpp

Install the demo-nodes packages

.. code-block:: bash 

   sudo apt install ros-<distro-name>-demo-nodes-cpp

.. code-block:: bash

   sudo apt install ros-<distro-name>-demo-nodes-py

In one terminal, source the setup file and then run a C++ talker:

.. code-block:: bash

    source /opt/ros/<distro-name>/setup.bash
    ros2 run demo_nodes_cpp talker

In another terminal source the setup file and then run a Python listener:

.. code-block:: bash

    source /opt/ros/<distro-name>/setup.bash
    ros2 run demo_nodes_py listener

You should see the talker saying that it's Publishing messages and the listener saying I heard those messages. This verifies both the C++ and Python APIs are working properly. Hooray you ran your first ros program! Now you can experiment and build your own projects.

Uninstall
=========

If you need to uninstall ROS 2 or switch to a source-based install once you have already installed from binaries, run the following command:

.. code-block:: bash

    sudo apt remove '~nros-<distro-name>-*' && sudo apt autoremove

You may also want to remove the repository:

.. code-block:: bash

    sudo apt remove ros2-apt-source

Update package lists:

.. code-block:: bash

    sudo apt update

Remove unused packages:

.. code-block:: bash

    sudo apt autoremove

Upgrade remaining packages (consider upgrading for packages previously shadowed):

.. code-block:: bash

    sudo apt upgrade
