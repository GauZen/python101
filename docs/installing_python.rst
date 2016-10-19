.. _sec_installing_python:

=================
Installing Python
=================

How to install Python depends a lot on your operating system.


macOS
=====

#. Install the current version of Xcode_ on your Mac.

#. Open your terminal and install the Xcode Command Line Utilities and run

   .. code-block:: shell

       xcode-select --install

#. Agree to the Xcode license by running

   .. code-block:: shell

       sudo xcodebuild -license

#. Install MacPorts_ for your version of macOS.

#. Install the required ports via

   .. code-block:: shell

       sudo port install freetype libpng git hdf5 python35


.. _Xcode: https://developer.apple.com/xcode/
.. _MacPorts: https://www.macports.org/install.php


Ubuntu 16.04 LTS
================

Install the required packages via

.. code-block:: shell

    sudo apt-get install cmake gfortran git libfreetype6-dev libatlas-dev liblapack-dev libhdf5-dev python3-dev python3-venv python3-pip python3-tk
