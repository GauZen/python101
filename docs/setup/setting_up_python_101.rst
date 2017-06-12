.. _sec_setting_up_python_101:

*********************
Setting up Python 101
*********************

First we will set up a *virtual environment* using the :mod:`venv` module of
Python.

.. code-block:: console

    $ python3 -m venv ~/.virtualenvs/python101

The virtual environment can be activated via

.. code-block:: console

    $ source ~/.virtualenvs/python101/bin/activate

If everything went fine you should see that your shell prompt now starts with
``(python101)``. This means that everything you do with regards to Python now
uses this *virtual environment*.

To make sure that the Python packages that are required for installing other
Python packages are up to date execute the following command:

.. code-block:: console

    $ pip install --upgrade pip setuptools

Now we will clone the *Python 101* repository using git_.

.. code-block:: console

    $ git clone https://github.com/ZeeD26/python101.git

We enter the newly created directory

.. code-block:: console

    $ cd python101

and :ref:`install <installing-index>` Python 101 along with its dependencies

.. code-block:: console

    $ python -m pip install -e .

.. attention::

    The ``.`` after ``python -m pip install -e`` is important!
    ``python -m pip install -e`` is not sufficient.


.. _git: https://git-scm.com/
