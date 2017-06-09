.. _sec_basics:

======
Basics
======

.. epigraph::

    "The  canonical, 'Python is a great first language', elicited, 'Python is a
    great last language!'"

    ---Noah Spurrier

Now we are going to introduce the basics of the Python programming language. We
start with the infamous *Hello, World!* program and the basic syntax of a
Python script.

.. attention::

    Make sure you have your virtual environment activated! If you do not have
    ``(python101)`` in front of your command line prompt you need to activate
    it using

    .. code-block:: shell

        $ source ~/.virtualenvs/python101/bin/activate

Execute the following command to start the interactive Python interpreter:

.. code-block:: shell

    $ python

You should see a couple of lines printed in the terminal, with the first line
stating, among the current date and time, the version of Python you use. The
very last line should start with ``>>>`` which indicates the Python prompt. You
can write Python commands there and execute them.

.. attention::

    In the previous chapter :ref:`sec_shell` the basic commands for the Unix
    shell were introduced. Notice how every command was preceeded by a ``$``
    character. In this tutorial code blocks that start with a ``$`` sign are
    meant to be executed in the Unix shell. If the code block is preceeded by
    ``>>>`` it means that it should either be executed in the Python
    interpreter or be used in a Python script.


Python as an interactive calculator
===================================

To get your feet wet with Python you can use the Python interpreter as a
calculator. You have the usual mathematical operators at your disposal, like

:``+``: addition,
:``-``: subtraction,
:``*``: multiplication,
:``/``: division,
:``**``: exponent,
:``//``: integer division, and
:``%``: modulus.

If you are not familiar with one of them just give it a try in the Python
interpreter---do not only use integers, but also floating point numbers. You
can also use brackets as you would use them in mathematical expressions. Try
whether Python uses the proper mathematical rules with regards to the order of
execution of the operators.

.. note::

    At one point you will enter an "invalid" expression like ``1 + * 2``.
    Python will then raise a ``SyntaxError`` to tell you that whatever you
    typed is not valid Python syntax. In many cases Python will also give you
    additional information about the error. There are many more errors you can
    encounter, and it is perfectly normal to have errors. The only difference
    between a seasoned programmer and a beginner is the time it takes to fix
    those errors. The more errors and mistakes you made the better you know how
    to solve them.

To leave the Python interpreter you either execute

>>> quit()  # doctest:+SKIP

or you press ``Ctrl + D``. Besides the interactive Python interpreter you can
also write scripts with Python. Scripts are files that can be executed from the
command line interface. They contain Python expressions that get executed once
you call the scripts. A script can be simple and merely rename files or it can
be complex and run a complete simulation of a car crash. You decide how simple
they are.


Your first Python script
========================

We will start with the infamous `Hello, World! Program`_. Open a new terminal,
activate your virtual environment, and create a new file named
``hello_world.py`` via

.. code-block:: shell

    $ touch hello_world.py

Open it with your favorite text editor, e.g., *Atom* or *SublimeText*. In the
former case you would open the file via

.. code-block:: shell

    $ atom hello_world.py

Now type (not copy!) the following into the file

.. code-block:: python
    :caption: hello_world.py

    print('Hello, World!')

Save the file, switch to your command line interface, and execute

.. code-block:: shell

    $ python hello_world.py

If you did everything correctly you should see the phrase ``Hello, World!``
popping up in your command line interface. If you see something like

.. code-block:: py3tb

      File "hello_world.py", line 1
        print('Hello, World!)
                            ^
    SyntaxError: EOL while scanning string literal

or

.. code-block:: py3tb

      File "hello_world.py", line 2

                             ^
    SyntaxError: unexpected EOF while parsing

it means that you have either forgotten the closing ``'`` or ``)``,
respectively. As you can see Python tries its best to describe the error to you
so that it can be fixed quickly.

If everything went fine: **Congratulations!** You wrote your first Python
script!

.. _Hello, World! Program:
   https://en.wikipedia.org/wiki/%22Hello,_World!%22_program


The ``print`` function
======================

The function you used in your first Python script, the :func:`print` function,
has a rather simple goal: Take whatever you have in there and display it in the
command line interface. In the Python interpreter (the command line starting
with ``>>>``) the result of an expression was displayed automatically. Try
creating a new file ``math_expressions.py`` and enter several mathematical
expressions like you did earlier. Save the file, switch to your terminal and
execute the file via

.. code-block:: shell

    python math_expressions.py

You should not see a single thing happening. That is because you never told
Python what to actually do with those expressions. So what it does is evaluate
them and nothing more. Now wrap the mathematical expressions in the
:func:`print` function, for example like this:

.. code-block:: python3

    print((3 + 4)*6)

If you execute the script again you should see the expected output.


Integers, floats and strings
============================

In the previous examples you worked with integers, floating-point numbers, and
with strings. ``-4``, ``0``, and ``2`` are all integers. ``1.2``, ``1.0`` and
``-2e2`` (which is the scientific notation for ``-200.0``) are floating-point
numbers. Finally, ``'Hello, World!'`` is a string. These categories are called
data types. Every value in Python is of a certain data type.

The meaning of operators may depend on the data types of the values surrounding
it. Take, e.g., the addition operator ``+``:

>>> 1 + 2
3
>>> 1.2 + 3.4
4.6
>>> 'My first sentence.' + 'My second sentence.'
'My first sentence.My second sentence.'
>>> 'My ' + 3 + 'rd sentence.'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly

In the last case the addition operator has no idea how to combine the integer
``1`` with the strings. What you can do to solve this is to convert the integer
to a string using :func:`str`:

>>> 'My ' + str(3) + 'rd sentence.'
'My 3rd sentence.'

If you want to convert something to a string you use :func:`str`, to convert to
an integer you use :func:`int`, for floating-point numbers you use
:func:`float`.

>>> '1.2' + '3.4'
'1.23.4'
>>> float('1.2') + float('3.4')
4.6
>>> int('1.4')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '1.4'
>>> str(1e2)
'100.0'

Play around with those three functions to see what can be converted and what
can not. Try the different operators, e.g., try to multiply a string with an
integer, etc.


Variables
=========

Like in mathematics you can also use variables to store values. A variable has
a name by which it is called and a value. There are three rules that a variable
name must comply:

#. It must be exactly one word.
#. It must comprise only letters, numbers, and the underscore character.
#. It must not begin with a number.

Other than that anything goes.

.. warning::

    Although anything else is a viable variable name, you should take special
    care not to use names of built-in objects like, e.g., ``int``. If you name
    a variable after some function or class it is not usable anymore in the
    subsequent code.

To assign a value to a variable you use the
equal sign ``=`` with the variable name on the left and the value on the right:

>>> my_first_variable = 21
>>> 2*my_first_variable
42
>>> my_second_variable = 3
>>> my_first_variable/my_second_variable
7.0
>>> my_third_variable = my_first_variable
>>> print(my_third_variable)
21

Here is a slightly more complex example:

.. testcode::

    students = 35
    tutors = 2
    classrooms = 1
    pizza_orders = 20

    students_per_tutor = students / tutors
    persons = students + tutors
    persons_per_classroom = persons / classrooms
    hungry_persons = persons - pizza_orders

    print('There are', students, 'students and', tutors, 'tutors.')
    print('That makes', persons, 'persons in', classrooms, 'class room(s).')
    print(hungry_persons, 'have to stay hungry...')

The advantages of using variables are two-fold:

- If the amount of students, tutors, classrooms or pizza_orders changes you
  only have to update one line instead of many. This is less error-prone and
  faster.

- You give the values some meaning which should be represented in the variable
  name. You could in principle read "the students per tutor is the amount of
  students divided by the amount of tutors." This makes your code easily
  comprehensible and you need fewer comments. But you still should write them
  when they make sense!

And here is what the output should look like:

.. testoutput::

    There are 35 students and 2 tutors.
    That makes 37 persons in 1 class room(s).
    17 have to stay hungry...

Notice how we used ``,`` to separate strings and variable names in
:func:`print`, but everything was composed in a nice way? The reason for this
is that :func:`print` can take an arbitrary amount of arguments. Just chain
them using ``,`` and you are good to go. How this works is part of the section
:ref:`sec_functions`.


User input
==========

In some cases you may want to ask the user of your script to provide some
additional information, like the path to a file or parameters for a simulation.
For this the :func:`input` can be used.

.. code-block:: python

    print('What is your name?')
    name = input()
    print('Nice to meet you,', name)

.. note::

    The value returned by :func:`input` is always a string. So when you are
    asking for numbers you have to convert them.

    .. code-block:: python

        print('What is your age in years?')
        age = int(input())
        print('In 5 years you will be', age+5, 'years old.')


Imports
=======

Sometimes the features that Python offers by default are not enough. What if
you want to use the :math:`\sin(x)` function? For more specialized topics
Python offers modules or packages, either ones that already ship with every
Python installation or packages from external parties. The packages that Python
ships with are called the `standard library`_. External packages may be, e.g.,
NumPy_ and SciPy_ for scientific computing with Python, or Matplotlib_ for
plotting.

You activate this additional functionality by *importing* these packages:

>>> import math

Now we have access to all functions available in the :mod:`math` module.

>>> math.pi
3.141592653589793
>>> math.sin(0.5*math.pi)
1.0

Take your time and browse the documentation of the :mod:`math` module, try some
of the provided functions like :func:`math.ceil`, :func:`math.exp`, etc.

.. _standard library: https://docs.python.org/3/library/
.. _NumPy: http://www.numpy.org/
.. _SciPy: http://www.scipy.org/
.. _Matplotlib: http://matplotlib.org/


Summary
=======

.. highlights::

    * You can use the interactive Python interpreter to execute small commands.

    * You can execute scripts that hold several commands using Python.

    * You can display results of computations or strings using the
      :func:`print` function

    * You can use :func:`str`, :func:`int`, :func:`float` to convert from one
      data type to another---if it is somehow possible.

    * You can store values in variables to access them at a later point in your
      script.

    * You can import modules or packages to extend Pythons builtin
      functionality using the :ref:`import <import>` statement.


Exercises
=========

#. Write a script that asks the user for the radius of a circle and
   subsequently shows the circumference and the area of the circle in the
   terminal.
