==========
Python 101
==========

Welcome to the Python 101 course of the Institute of Materials Simulation.
The tutorial comes in the form of Python package and thus has to be installed
as such. It is a good practice to use something call *virtual environments* for
this. You can create a new virtual environment via::

    python3 -m venv ~/.virtualenvs/python101

After creating the virtual environment you can activate it using the command::

    source ~/.virtualenvs/python101/bin/activate

If your command line prompt now has ``(python101)`` as prefix you have
successfully activated your newly created virtual environment. Every Python
package you install while having your virtual environment activated will only
be installed in this virtual environment. Now you can install the Python 101
package via::

    pip install -e .

Now that you have installed the Python 101 package you can build the
documentation which contains the tutorial. To do this change to the ``docs``
directory via::

    cd docs

and build the documentation via::

    make html

Subsequently you can view the documentation in your browser by opening the file
``python101/docs/build/html/index.html``. This page is the starting point for
your tutorial.
