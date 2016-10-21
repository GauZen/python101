.. _sec_setting_up_python_101:

=====================
Setting Up Python 101
=====================

First we will set up a *virtual environment* using the :mod:`venv` module of
Python.

.. code-block:: shell

    $ python3 -m venv ~/.virtualenvs/python101

The virtual environment can be activated via

.. code-block:: shell

    $ source ~/.virtualenvs/python101/bin/activate

If everything went fine you should see that your shell prompt now starts with
``(python101)``. This means that everything you do with regards to Python now
uses this *virtual environment*.

Now we will clone the *Python 101* repository using git_.

.. code-block:: shell

    $ git clone https://github.com/ZeeD26/python101.git

We enter the newly created directory

.. code-block:: shell

    $ cd python101

and :ref:`install <installing-index>` Python 101 along with its dependencies

.. code-block:: shell

    $ python -m pip install -e .

.. attention::

    The ``.`` after ``pip install -e`` is important! ``pip install -e`` is not
    sufficient.


.. _git: https://git-scm.com/
