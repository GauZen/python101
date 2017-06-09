.. _sec_functions:

*********
Functions
*********

Introduction
============

Some tasks in your code may be performed a lot of times. Say you want to say
"Hello" not only to the world but to a lot of people. You would have to write

.. code-block:: python

    print('Hello, {name}!')

an awful lot of times. It would be way shorter if we were able to write

.. code-block:: python

    greet('{name}')

and it would just print ``Hello, {name}!``. OK, it is not that shorter... But
imagine you want to find the roots of some functions. There is way more code
involved and having a nice little shortcut to execute all that code without
writing it over and over again would be nice, wouldn't it? This is in the
spirit of the DRY_ principle! As a nice side effect you only have to change the
routine in one place of your code instead of all of them if you find a bug or
want to use some more sophisticated routine.

But even if you do only use a code snippet once in your program it may be more
declarative to give it a short name and hide the implementation somewhere else.
This also helps you to `divide and conquer`_ larger problems!

The nice thing is that you already know a function: :func:`print`!
You used it like this:

.. code-block:: python

    print('Hello, World!')

Let's take a closer look at the parts that make up a function.

.. _DRY: https://en.wikipedia.org/wiki/Don't_repeat_yourself
.. _divide and conquer:
    https://en.wikipedia.org/wiki/Divide_and_conquer_algorithms


Components of a function
========================

Name
----

Most functions have names [#lambdas]_. The name of :func:`print` is -- never
would have guessed -- *print*. Printing the function without calling it reveals
that it is a built-in function:

>>> print(print)
<built-in function print>

There are a lot more :ref:`python:built-in-funcs`, among them, for example,
:class:`float() <float>`.


Positional arguments
--------------------

:class:`float() <float>` is a function that lets you convert a number or a
string that represents a number to a floating point number. Its interface is
defined as

.. function:: float(x)
    :noindex:

where ``x`` is its argument.
To be more precise it is its *positional argument*.
By calling :class:`float() <float>` and passing an integer as argument the
result is the corresponding float:

>>> float(1)
1.0
>>> float(-2)
-2.0

You can also pass strings that represent numbers to :class:`float() <float>`:

>>> float('1')
1.0
>>> float('-2')
-2.0
>>> float('1.500')
1.5
>>> float('1e-2')
0.01
>>> float('+1E6')
1000000.0

A similar function also exists for integer. It is the function
:class:`int() <int>`.


Keyword arguments
-----------------

:class:`int() <int>` is a function that lets you convert a number or a string
that represents a number to an integer. Its interface is defined as

.. function:: int(x, base=10)
    :noindex:

where ``x`` is its *positional argument* and ``base`` is its *keyword
argument*. While positional arguments must be passed to a function keyword
arguments are optional and provide default values. The default value of
``base`` is ``10``.

When passing floats to :class:`int() <int>` everything after the decimal point
is dropped:

>>> int(1.0)
1
>>> int(-2.0)
-2
>>> int(1.3)
1
>>> int(1.8)
1
>>> int(-1.3)
-1
>>> int(-1.8)
-1

When passing strings to :class:`int() <int>` the ``base`` keyword argument is
used to indicate how the number should be interpreted in terms of which base it
is given in.

>>> int('1')
1
>>> int('-2')
-2
>>> int('101010')
101010
>>> int('101010', base=2)
42

You do not have to write out the keyword arguments, they will be interpreted in
the same order as they are in the interface:

>>> int('101010', 2)
42

But you can not convert strings that represent floating point numbers to
integers like this:

>>> int('1.0')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '1.0'

For this you would have to chain :class:`int() <int>` and
:class:`float() <float>`:

>>> int(float('1.0'))
1


Defining a function
===================

A function is defined by starting with the ``def`` keyword. Subsequently you
provide the name of the function and its arguments in paranthesis. You can then
use it like the functions you already used.

>>> def greet(name):
...     print('Hello', name)
...
>>> greet('World')
Hello World
>>> greet('you')
Hello you

>>> def add_reciprocal(a, b):
...     return 1/a + 1/b
>>> add_reciprocal(4, 8)
0.375

To provide keyword arguments you let the argument have a default value by
assigning a value to it:

>>> def name_and_favorite_food(name, favorite_food='pizza'):
...     return name + "'s favorite food is " + favorite_food + '.'
...
>>> name_and_favorite_food('Dominik')
"Dominik's favorite food is pizza."
>>> name_and_favorite_food('Stefan', 'kimchi')
"Stefan's favorite food is kimchi."

If you execute them in the interactive Python interpreter the value returned by
a function is automatically displayed if you do not assign it to a variable. It
is important to know that the ``return`` keyword is used to make the value
accessible to the outer scope, that is outside of the function. See the
following example, where we first do not have a return statement:

>>> def is_positive_without_return(x):
...     if x >= 0:
...         print(True)
...     else:
...         print(False)
...
>>> is_positive_without_return(1)
True
>>> is_positive_without_return(-1)
False
>>> a = is_positive_without_return(1)
True
>>> print(a)
None

As you can see the variable ``a`` has no value at all. If you want ``a`` to
receive the result of the function you have to return it, not print it:

>>> def is_positive_without_return(x):
...     if x >= 0:
...         return True
...     else:
...         return False
...
>>> is_positive_without_return(1)
True
>>> is_positive_without_return(-1)
False
>>> a = is_positive_without_return(1)
>>> print(a)
True


Functions as function arguments
===============================

You are able to pass almost anything to a function---even functions itself!
This is especially useful if you want to do data fitting or root finding of
mathematical functions.

.. testcode::

    def format_heading(text):
        return '\n' + text + '\n' + '='*len(text) + '\n'

    def prettify(sections, header_formatter):
        # Assume that `sections` is a list of dictionaries with the keys
        # ``heading`` for the heading text and ``content`` for the content
        # of the section.
        # Assume that the `header_formatter` is a function that takes a string
        # as argument and formats it in a way that is befitting for a heading.
        text = ''
        for section in sections:
            heading = section['heading']
            content = section['content']
            text += format_heading(heading) + content + '\n'
        # Before returning it we make shure that all surrounding whitespace is
        # gone.
        return text.strip()

    secs = [
        {
            'heading': 'Introduction',
            'content': 'In this section we introduce some smart method to teach Python.'
        },
        {
            'heading': 'Results',
            'content': 'More than 42 % of participants in this study learned Python.'
        }
    ]

    pretty_text = prettify(secs, header_formatter=format_heading)
    print(pretty_text)

So as you can see the argument ``header_formatter`` is just treated as if it
was a function. If you run this script the output will be:

.. testoutput::

    Introduction
    ============
    In this section we introduce some smart method to teach Python.

    Results
    =======
    More than 42 % of participants in this study learned Python.


Summary
=======

.. highlights::

    * Functions can make your life easier by streamlining repeated tasks or giving
      a name to complex programming logic.
    * Functions may have two different kinds of arguments, *positional arguments*
      that must be given to the function and *keyword arguments* which provide
      default values.
    * Functions are defined using the ``def`` keyword.
    * Functions may return values by using the ``return`` keyword.


Exercises
=========

.. toctree::
    :maxdepth: 1

    exercises/heaviside_step_function
    exercises/newtons_method_1D
    exercises/sum_of_multiples_of_3_and_5
    exercises/even_fibonacci_numbers

.. rubric:: Footnotes

.. [#lambdas] :ref:`python:lambdas` are the exception to the rule as they
              define anonymous functions.
