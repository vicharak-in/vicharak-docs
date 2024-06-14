.. _common-ssh:

Board supports **SSH (Secure Shell)**, which allows for secure remote access
to the system. By establishing an SSH connection, users can remotely connect to
the board from another device, such as a computer or smartphone, over a network.
This method provides a secure command-line interface to administer, configure,
and execute commands on the board.

Install OpenSSH server
``````````````````````

You can install both OpenSSH components on Windows devices using the
**Windows Settings**.

To install the OpenSSH components, follow these steps:

1. Open the Settings menu and click on Apps, then select **Optional Features**.
2. Look through the list to check if OpenSSH is already installed.
   If it's not, at the top of the page, click on **Add a feature** and then:

   - Find OpenSSH Client and click on Install.
   - Find OpenSSH Server and click on Install.
3. After the installation process is complete, go back to
   **Apps and Optional Features** to verify that **OpenSSH** is listed.
4. Open the Services desktop app. 

.. code-block:: text

    Click on Start, type services.msc in the search box and then click on the Service app or press ENTER.

5. In the details pane, double-click on **OpenSSH SSH Server**.
6. On the General tab, choose **Automatic** from the Startup type drop-down
   menu.
7. To start the service, click on **Start**.


Verify OpenSSH server
`````````````````````

Once installed, you can connect to **OpenSSH Server** from a Windows device
with the **OpenSSH client** installed.

From a PowerShell prompt, run the following command.

.. code-block:: powershell

    ssh username@ip_address

Example:

.. code-block:: powershell

    ssh vicharak@192.168.29.69

.. tip::

	To find your IP address on Windows, use the following command:
	``ipconfig``

	For Linux users, use the following command:
	``ip a``

Accessing Board through SSH
````````````````````````````

To access the board through SSH, you can use either of the following commands:

|

1. SSH using the IP address

.. code-block::

    ssh username@ip_address

.. tip::
    Replace **"username"** with the appropriate username for the board and
    **"ip_address"** with the actual IP address assigned to the board on the
    network.

2. SSH using the PC name (hostname)

.. code-block::

    ssh username@pc-name.local

.. tip::
    Replace **"username"** with the appropriate username for the board and
    **"pc-name"** with the actual PC name assigned to the board on the network.

    For Linux users, you can find your username using ``whoami`` command and,
    hostname using ``cat /etc/hostname``


