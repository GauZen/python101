.. _sec_flow_control:

************
Flow control
************

.. epigraph::

    | "Would you tell me, please, which way I ought to go from here?"
    | "That depends a good deal on where you want to get to," said the Cat.
    | "I don’t much care where---" said Alice.
    | "Then it doesn’t matter which way you go," said the Cat.
    | "---so long as I get *somewhere*," Alice added as an explanation.
    | "Oh, you're sure to do that," said the Cat, "if you only walk long
      enough."

    ---:title:`Alice's Adventures in Wonderland`

Up until now the code war rather... underwhelming. You only executed a sequence
of commands each and every time. But with the introduction of the control flow
of a program a whole new world of programs reveals itself. It is up to your
experience and creativity to use the control flow tools to structure your code
in a way that complex tasks can be handled.


Boolean expressions
===================
Knowing boolean expressions is essential for the control flow of a program.
Python handles this rather intuitively. The most important boolean operations
are

:``==``: equal to
:``!=``: unequal to
:``<``: less than
:``<=``: less than or equal to
:``>``: greater than
:``>=``: greater than or equal to

>>> 1 == 1
True
>>> 1 + 1 != 2
False
>>> 5*2 >= 11
False

.. warning::

    Beware of :class:`float` comparisons, as the way computers represent
    floating-point numbers internally might lead to some seemingly weird
    behavior.

    >>> 0.1 + 0.2 == 0.3
    False

    This is certainly unexpected behavior. To deal with this shortcoming
    version 3.5 of Python introduced the ``isclose`` function in its
    :mod:`math` module.

    >>> import math
    >>> math.isclose(0.1 + 0.2, 0.3)  # doctest: +SKIP
    True

    If you are working with an older version there are still convenience
    solutions. The ``numpy`` package that is introduced later on in this
    tutorial also provides the means for :class:`float` comparisons.

In many cases a simple boolean expression is not sufficient to correctly
specify the control flow of a program. Sometimes a code block should only be
executed when a condition is not met, when several conditions are met all at
once or when at least one of several conditions is met. For this Python hast
the keywords ``not``, ``and``, and ``or``, respectively. Their behavior is
outlined in the following tables.

.. table:: Truth table for ``not``

    =====  =====
    A      not A
    =====  =====
    True   False
    False  True
    =====  =====

.. table:: Truth table for ``and``

    =====  =====  =======
    A      B      A and B
    =====  =====  =======
    True   True   True
    True   False  False
    False  True   False
    False  False  False
    =====  =====  =======

.. table:: Truth table for ``or``

    =====  =====  ======
    A      B      A or B
    =====  =====  ======
    True   True   True
    True   False  True
    False  True   True
    False  False  False
    =====  =====  ======

Combining boolean expressions using these keywords is an essential skill for
programming.

>>> i = 3
>>> i < 4 and i >= 0
True
>>> i < 4 and i > 3
False
>>> i < 4 and not i > 3
True
>>> i >= 0 or i > 3
True

You can furthermore use brackets to specify the order of the evaluation of the
subexpressions like you would in equations.

.. note::

    In Python :data:`False` is not the only thing that is "false" in Python.
    :data:`False`, :data:`None`, numeric zero of all types, and empty strings
    and containers are all interpreted as false.

The most important construct using boolean expressions is introduced in the
following.


The ``if`` statement
====================

A construct every programming language provides is the
:ref:`if statement <if>`. The basic structure is as follows:

.. code-block:: python3

    if <expression>:
        <code block>

The result is that the *code block* is only executed when *expression* is
:data:`True`.

.. note::

    Test


>>> x = 0
>>> y = 1
>>> if x > 0:
...     print('Larger than 0')
...
>>> if y > 0:
...     print('Larger than 0')
...
Larger than 0

The *expression* can also include a negation using :ref:`not`:

>>> x = 0
>>> y = 1
>>> if not x > 0:
...     print('Not larger than 0')
...
Not larger than 0
>>> if not y > 0:
...     print('Not larger than 0')
...

If you want to cover both cases you can also use the :ref:`else <else>`
keyword:

>>> x = 1
>>> if x < 0:
...     print('Negative')
... else:
...     print('Positive')
...
Positive

But as you can see this does not cover all the cases. What if ``x`` is 0? For
this we have to use :ref:`elif <elif>`:

>>> x = 0
>>> if x < 0:
...     print('Negative')
... elif x == 0:
...     print('Zero')
... else:
...     print('Positive')
...
Zero

And you can add as many :ref:`elifs <elif>` as you want.


The ``while`` loop
==================

Sometimes it is necessary to perform a routine until a certain condition is
met. This is achieved using a :ref:`while loop <while>`.

>>> x = 0
>>> while x < 5:
...     print(x)
...     x += 1
...
0
1
2
3
4

Assume you want to exit the :ref:`while loop <while>` when a certain condition
is met. This is possible with :ref:`the break statement<break>`.

>>> x = 0
>>> while x < 5:
...     if x == 3:
...         break
...     print(x)
...     x += 1
...
0
1
2

.. attention::

    Although :ref:`while loops <while>` are a common building stone in every
    programming language I advise you to avoid using them whenever possible. It
    happens quite easily that the criterion for exiting the loop is never
    reached and your program gets stuck performing the same task more often
    than you intended. In many cases a :ref:`while loop <while>` can be
    substituted with a :ref:`for loop <for>`.


The ``for`` loop
================

In a lot of cases you just want to work on all the elements of a container one
at a time. This is easily achieved with :ref:`for loops <for>`.

>>> x = [1, 2, 3]
>>> for i in x:
...     print(i)
...
1
2
3

Here ``i`` takes on the value of the elements of ``x`` one after the other.
This allows you to work with ``i`` inside of this :ref:`for loop <for>`. After
all elements have been visited you automatically exit the loop. A more
sophisticated example might be to store the squared values of another list in
a new list.

>>> x = [1, 2, 3]
>>> x_squared = []
>>> for value in x:
...     x_squared.append(value**2)
...
>>> print(x_squared)
[1, 4, 9]


``range``
---------

A shortcut to loop over integers is given as the :func:`range` function.

>>> for i in range(3):
...     print(i)
...
0
1
2
>>> for i in range(3, 6):
...     print(i)
...
3
4
5
>>> for i in range(3, 12, 3):
...     print(i)
...
3
6
9


``enumerate``
-------------

Sometimes you also want to track where you currently are in your iteration. For
example you want to know what the current state of your program is, but
printing the value you are operating on each single time is kind of too much.
Then you could use :func:`enumerate` like this:

>>> results = []
>>> for i, value in enumerate(range(100,900)):
...     if i % 200 == 0:
...         print('Current step:', i, '-- Value:', value)
...     results.append(i**2 % 19)
...
Current step: 0 -- Value: 100
Current step: 200 -- Value: 300
Current step: 400 -- Value: 500
Current step: 600 -- Value: 700

As you can see we now have comma-separated variables ``i`` and ``value``. ``i``
get the current index we are in whereas ``value`` holds the actual object of
the container.


``zip``
-------

Another common task is that you have to loop over several lists at the same
time. Use the :func:``zip`` function for this:

>>> fruits = ['banana', 'orange', 'cherry']
>>> colors = ['yellow', 'orange', 'red']
>>> for fruit, color in zip(fruits, colors):
...     print('The color of', fruit, 'is', color)
...
The color of banana is yellow
The color of orange is orange
The color of cherry is red

.. note::

    :func:`zip` stops the :ref:`for <for>` loop as soon as one :class:`list` is
    empty:

    >>> fruits = ['banana', 'orange', 'cherry', 'apple', 'lemon']
    >>> colors = ['yellow', 'orange', 'red']
    >>> for fruit, color in zip(fruits, colors):
    ...     print('The color of', fruit, 'is', color)
    ...
    The color of banana is yellow
    The color of orange is orange
    The color of cherry is red


Errors
======

As Python is a dynamic language it can never be garantueed that the input of
your functions is what you want it to be. Take as an example a function whose
purpose is the computation of the sum of the digits in a number. What if by
accident someone passes a string as argument to this function? In some cases it
is hence a good idea to check the input of a function for its sanity. If the
input does not hold this test you may :ref:`raise <raise>` and error like this:

>>> raise ValueError('The input was wrong')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: The input was wrong


Summary
=======

.. highlights::

    - :ref:`if statements <if>` are a way to add a branch into your code.
    - :ref:`while loops <while>` should be avoided whenever possible.
    - :ref:`for loops <for>` are used to work on items of a container.
    - :class:`range() <range>` is used to ad-hoc generate containers holding
      integers.
    - :func:`enumerate` is used to keep track of the current index in a
      :ref:`for loop <for>`.
    - :func:`zip` is used to loop over several containers at once.
    - :ref:`raise <raise>` is used to raise an error when something is fishy.
