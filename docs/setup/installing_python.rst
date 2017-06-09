.. _sec_installing_python:

*****************
Installing Python
*****************

How to install Python depends a lot on your operating system.


macOS
=====

For macOS two popular choices for package managers exist: Homebrew_ and
MacPorts_. Both are solid so the choice is up to you, I currently prefer
Homebrew.


.. _Homebrew: https://brew.sh
.. _MacPorts: https://www.macports.org/install.php


Homebrew
--------

#. Install the command line tools via

   .. code-block:: shell

       $ xcode-select --install

#. Agree to the Xcode license by running

   .. code-block:: shell

       $ sudo xcodebuild -license

#. Install Homebrew_.

#. Install the required formulas by running

   .. code-block:: shell

       $ brew install git python3 hdf5 freetype libpng


MacPorts
--------

#. Install the current version of Xcode_ on your Mac via the `Mac App Store`_.

#. Open your terminal and install the Xcode Command Line Utilities and run

   .. code-block:: shell

       $ xcode-select --install

#. Agree to the Xcode license by running

   .. code-block:: shell

       $ sudo xcodebuild -license

#. Install MacPorts_ for your version of macOS.

#. Install the required ports via

   .. code-block:: shell

       $ sudo port install freetype libpng git hdf5 python35


.. _Xcode: https://developer.apple.com/xcode/
.. _Mac App Store: https://itunes.apple.com/de/app/xcode/id497799835?mt=12


Fedora 25
=========

Install the required packages via

.. code-block:: shell

    $ sudo dnf install python3-tkinter hdfview


Ubuntu 16.04 LTS
================

Install the required packages via

.. code-block:: shell

    $ sudo apt-get install cmake gfortran git libfreetype6-dev libatlas-dev liblapack-dev libhdf5-dev python3-dev python3-venv python3-pip python3-tk


Ubuntu 16.10
============

Install the required packages via

.. code-block:: shell

    sudo apt-get install python3-venv python3-tk hdfview
