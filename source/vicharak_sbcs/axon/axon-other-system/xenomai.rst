=================
Xenomai Support 
=================

This comprehensive guide outlines the complete process for building, configuring, and installing the **Xenomai Real-Time Framework** on the **Vicharak Axon** single-board computer using the **Vicharak Linux Kernel 6.1-xenomai** branch. 

Follow these steps sequentially to set up your real-time development environment, apply hardware-specific patches, configure the kernel, and build the requisite Debian (``.deb``) installation packages.

.. tip::
     
     - Xenomai Version : **3.2.x**
     - Vichara Kernel  : **6.1.75-axon**
 	
------------------------------------------------------------
Prerequisites & Requirements
------------------------------------------------------------
.. tip::
        
	It is highly recommended to compile **Vicharak kernel** in **Axon** itself and having `TTY To USB Module (UART Module) will be helpful while developing kernel </vicharak_sbcs/axon/axon-getting-started/#using-serial-console>`_.

* **Operating System:** Ubuntu 22.04 LTS /24.04 LTS (recommended)
* **Toolchain:** ``aarch64-linux-gnu-`` cross-compiler installed and added to your system path.
* **Dependencies:** Standard build utilities (``build-essential``, ``libncurses-dev``, ``bison``, ``flex``, ``libssl-dev``, ``bc``, ``rsync``).


.. code-block::

	sudo apt-get update
	
	sudo apt-get install build-essential python3 python-is-python3 libssl-dev \
	git-core gcc-arm-linux-gnueabihf u-boot-tools device-tree-compiler \
	gcc-aarch64-linux-gnu mtools parted llvm clang pv bc bison flex gawk


------------------------------------------------------------
Step-by-Step Compilation & Installation Guide
------------------------------------------------------------

Step 1: Clone the Vicharak Linux Kernel
========================================

Clone the official Vicharak Linux Kernel repository, targeting the designated ``6.1-xenomai`` development branch. It is critical to initialize and update submodules to pull in hardware-specific definitions and dependencies.

.. code-block:: bash

    # Clone the repository with the specified branch
    git clone -b 6.1-xenomai https://github.com/vicharak-in/rockchip-linux-kernel.git
    cd rockchip-linux-kernel

    # Initialize and update all embedded git submodules
    git submodule update --init

Step 2: Clone the Xenomai Source Framework
==========================================

In a separate workspace directory, clone the stable Xenomai 3 repository and check out the verified ``stable/v3.2.x`` branch.

.. code-block:: bash

    # Navigate to your external workspace directory
    cd ..

    # Clone the Xenomai 3 repository
    git clone https://gitlab.com/Xenomai/xenomai3/xenomai.git
    cd xenomai

    # Checkout the stable 3.2.x release branch
    git checkout stable/v3.2.x

Step 3: Apply the Rockchip-Specific Patch
=========================================

Xenomai requires low-level architectural modifications to support the Rockchip platform architecture integrated into the Vicharak Axon. Apply the patch to the Xenomai source tree.

1. Download patch 
-------------------

User can download the patch file directly using standard command-line tools like ``curl`` or ``wget``.

**Using cURL**


To download the patch using ``curl``, open your terminal and execute:

.. code-block:: bash

   curl -O https://vicharak-files.vicharak.in/patch/xenomai/0001-xenomai-v3.2.x-on-rockchip.patch

**Using wget**

Alternatively, you can use ``wget``:

.. code-block:: bash

   wget https://vicharak-files.vicharak.in/patch/xenomai/0001-xenomai-v3.2.x-on-rockchip.patch

2. Apply Patch
---------------

.. code-block:: bash

    # Apply the required platform patch to the Xenomai codebase
    patch -p1 < /path/to/0001-xenomai-v3.2.x-on-rockchip.patch

.. note::
    Replace ``/path/to/0001-xenomai-v3.2.x-on-rockchip.patch`` with the actual absolute or relative path to where your patch file is stored.

Step 4: Configure the Kernel with Xenomai
=========================================

Navigate back to the kernel repository, initialize the default configuration for the **Axon** hardware profile, and enable Xenomai kernel options via the interactive menu configuration utility.

.. code-block:: bash

    # Return to the kernel root directory
    cd rockchip-linux-kernel

    # Launch the interactive configuration wizard
    ./vicharak/build.sh -l

Interactive Selection Steps
---------------------------

1. When prompted by the layout setup script, locate the **Axon** board profile option.
2. Press **3** to select and load the primary Axon hardware configuration definitions.

Once the initial board configuration is loaded, launch the kernel terminal configuration utility (``menuconfig``) targeted for the ARM64 architecture with the custom output build directory:

.. code-block:: bash

    # Open the interactive kernel menu configuration interface
    make ARCH=arm64 O=out menuconfig

Within the graphical ``menuconfig`` interface, verify and toggle the following parameters to ensure proper real-time dual-kernel operation:

Required Xenomai Configuration Matrix
======================================

Navigate to **General setup --->** and apply the following parameters:

*   **Preemption Model**
    
    *   Set to: ``Preemptible Kernel (Low-Latency Desktop)`` --> ``(X) Low-Latency Desktop``

*   **Local version - append to kernel release**
    
    *   Set to: ``-xenomai`` or ``-xeno-3.2.1``

*   **Timers subsystem**
    
    *   ``[*] High Resolution Timer Support`` (Enable)

**Processor Type and Features**

Navigate to **Processor type and features --->** and configure as follows:

*   **Processor family**
    
    *   Set to: ``(X) Core 2/newer Xeon``
    *   *Note: If "cat /proc/cpuinfo | grep family" returns 6, set as Generic; otherwise, on devices like Raspberry Pi, this may return nothing.*

*   **Multi-core scheduler support**
    
    *   ``[*] Multi-core scheduler support`` (Enable/Disable depending on your hardware strategy, typically enabled for x86 multi-core architectures)
    *   ``[ ] CPU core priorities scheduler support`` (Disable)

**Xenomai / Cobalt Settings**

Navigate to **Xenomai/cobalt --->** to tune the real-time sub-system metrics:

**Sizes and Static Limits**

Modify the limits to prevent allocation starvation under load:

===============================================  =============  =============
Setting                                          Old Value      New Value
===============================================  =============  =============
Number of registry slots                         512            **4096**
Size of system heap (Kb)                         4096           **4096**
Size of private heap (Kb)                        256            **256**
Size of shared heap (Kb)                         256            **256**
Maximum number of POSIX timers per process       256            **512**
===============================================  =============  =============

**Drivers & RTnet Configuration**

Navigate to **Drivers ---> RTnet --->**:

*   ``[*] RTnet, TCP/IP socket interface`` (Enable)
*   **Drivers --->**
    
    *   ``<M> New intel(R) PRO/1000 PCIe(Gigabit)`` (Set as Module)
    *   ``<M> Realtek 8169(Gigabit)`` (Set as Module)
    *   ``<M> Loopback`` (Set as Module)

*   **Add-Ons --->**
    
    *   ``<M> Real-Time Capturing Support`` (Set as Module)

**Power Management and ACPI Options**

Real-time performance is severely degraded by dynamic power state changes. Disable them entirely.

Navigate to **Power management and ACPI options --->**:

*   **CPU Frequency scaling --->**
    
    *   ``[ ] CPU Frequency scaling`` (Disable)

*   **ACPI (Advanced Conservation and Power Interface) Support --->**
    
    *   ``< > Processor`` (Disable)

*   **CPU Idle --->**
    
    *   ``[ ] CPU idle PM support`` (Disable)

**Memory Management Options**

Dynamic memory operations cause non-deterministic latencies. Navigate to **Memory Management options --->** and ensure the following are **disabled**:

*   ``[ ] Contiguous Memory Allocator (CMA)``
*   ``[ ] Transparent Hugepage Support``
*   ``[ ] Allow for memory compaction``
*   ``[ ] Page migration``

**Device Drivers & Virtualization Guardrails**

Disable guest/virtualization drivers that can cause unpredictable timing drops.

*   **Microsoft Hyper-V guest support --->**
    
    *   ``< > Microsoft Hyper-V client drivers`` (Disable)

*   **Device Drivers --->**
    
    *   ``[ ] Unisys visorbus driver`` (Disable)

.. note::
   After setting these options, save your configuration file in ``out/.config``.
 
.. warning::
    **Verification Step:** Save your layout selections and exit ``menuconfig``. Before compiling, it is mandatory to confirm that your options have written successfully by cross-checking the generated configuration file:

    .. code-block:: bash

        cat out/.config | grep -i "CONFIG_XENOMAI"

Step 5: Compile the Kernel and Generate Debian Packages
=======================================================

Vicharak provides native build hooks to compile both standard raw binaries and distribution-ready package architectures.

Option A: Compile Standard Binaries
-----------------------------------

To perform a standard compilation test or build raw images (``Image``, ``dtb``):

.. code-block:: bash

    ./vicharak/build.sh -k

Option B: Compile Debian Packages (Recommended)
-----------------------------------------------

To package the kernel, headers, and core developer tools into a native Debian architecture suitable for deployment on your target device, execute:

.. code-block:: bash

    ./vicharak/build.sh -K

------------------------------------------------------------
Deployment & Installation Guide
------------------------------------------------------------

After a successful compilation using the packages command (``./vicharak/build.sh -K``), navigate to the generated build **out** folder to copy the binaries to your device.

1. Extract Target Packages
==========================

Navigate into the compiler output directory:

.. code-block:: bash

    cd out/

Locate the following three auto-generated Debian packages (the exact string components ``<kernel-version>`` and ``<compiled_date>`` will vary depending on your compilation timeline):

* ``linux-headers-<kernel-version>-axon_<compiled_date>-axon_arm64.deb``
* ``linux-image-<kernel-version>-axon_<compiled_date>-axon_arm64.deb``
* ``linux-libc-dev_<compiled_date>-axon_arm64.deb``

2. Copy to Target Board
=======================

Transfer these files over to your Vicharak Axon hardware platform using Secure Copy (``scp``) or an external flash storage drive.

.. code-block:: bash

    # Example using network transfer
    scp linux-*.deb vicharak@<axon_board_ip_address>:/home/vicharak/

3. Installation Execution
=========================

Log directly into your **Vicharak Axon** command terminal, navigate to the directory holding the transferred packages, and execute the native package manager installation routine:

.. code-block:: bash

    # Execute local installation of all compiled kernel structures
    sudo apt install ./linux*.deb

4. Verification Post-Reboot
===========================

Reboot your system to apply the newly compiled real-time kernel:

.. code-block:: bash

    sudo reboot

Once back online, verify that the Xenomai dual-kernel architecture is running correctly by inspecting the system message logs and confirming kernel release naming conventions:

.. code-block:: bash

    uname -a
    dmesg | grep -i xenomai

.. code-block:: bash

    zcat /proc/config.gz | grep -i xenomai

------------------------------------------------------------

If you face any issue, generate query on `Vicharak Forum <https://discuss.vicharak.in>`_
