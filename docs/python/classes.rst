.. _sec_classes:

*******
Classes
*******

Especially for larger code bases the rather mathematical way of programming
may become slightly convoluted. A paradigm that tries to alleviate this is
`object-oriented programming`_. Let us just dive right in with the definition
of a rectangle class. Each rectangle has a length and a width, from which one
can compute its area and perimeter. Here is the definition:

.. _object-oriented programming:
    https://en.wikipedia.org/wiki/Object-oriented_programming

.. testcode:: geometric_classes

    class Rectangle:
        """A rectangle that is described by its length and width."""

        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            """Return the area of the rectangle."""
            return self.length*self.width

        def perimeter(self):
            """Return the perimeter of the rectangle."""
            return 2*(self.length + self.width)

Let us go over this step by step. The definition of a class starts with the
keyword ``class`` followed by the name of the class. Within the class you can
define *methods*. They are like functions that are attached to the class. What
is slightly peculiar is, that all take ``self`` as their first argument---
we will come to that in a second. The first method is ``__init__``.

.. code-block:: python

    def __init__(self, length, width):
        self.length = length
        self.width = width

As you use classes you *instantiate* *objects* of that class. During the
*instantiation* you can provide some initial arguments to the class to
customize the resulting object using the special ``__init__`` method. In this
example a rectangle object can be *initialized* with values for its length
:math:`l` and for its width :math:`w`. These values are then stored in the
*instance* as *attributes*. The reference to the instance is the ``self``
argument, that each method has as its first argument. So by attaching
information to ``self``, each distinct object has its own state.

Now we can exploit this in other methods. The area :math:`A` of a rectangle is
defined as

.. math::

    A = l \cdot b

In the code this is described by the following definition:

.. code-block:: python

    def area(self):
        """Return the area of the rectangle."""
        return self.length*self.width

Where a method is defined, that takes the length of the rectangle
``self.length``, multiplies it with ``self.width`` and then returns it. If we
did not use ``self.length`` but just ``length`` or used ``width`` instead of
``self.width`` we would not have accessed the values we stored in this
rectangle during its initialization, but some global values instead. So to make
sure that we only use the attributes of our specific rectangle we access them
from ``self``.

The method used to get the perimeter :math:`P`, which, for a rectangle, is
defined as

.. math::

    P = 2 (l + b)

follows the same theme:

.. code-block:: python

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2*(self.length + self.width)

In the following the usage of this class is shown.

.. testcode:: geometric_classes

    first_rectangle = Rectangle(length=2, width=3)
    print('Information about the first rectangle')
    print('Length:', first_rectangle.length)
    print('Width:', first_rectangle.width)
    print('Area:', first_rectangle.area())
    print('Perimeter:', first_rectangle.perimeter())

First an object of the class ``Rectangle`` is instantiated with the ``length``
argument set to ``2`` and the ``width`` argument set to ``3``. The name of our
first ``Rectangle`` object is ``first_rectangle``. Subsequently the attributes
``length`` and ``width`` of the object ``first_rectangle`` can be accessed via
``first_rectangle.length`` and ``first_rectangle.width``, respectively. One
could say that what ever has been ``self`` in the class definition now is
replaced by the name of the object. In the case of the methods the ``self``
argument is implicitly supplied by calling the method from the object. So it is
sufficient to use ``first_rectangle.area()``, and not
``first_rectangle.area(self)`` or ``first_rectangle.area(first_rectangle)``---
both of which would be wrong. The output of the above code is

.. testoutput:: geometric_classes

    Information about the first rectangle
    Length: 2
    Width: 3
    Area: 6
    Perimeter: 10

If another rectangle is instantiated with different values the information
changes accordingly. So in the case of a ``second_rectangle``

.. testcode:: geometric_classes

    second_rectangle = Rectangle(length=5, width=7)
    print('Information about the second rectangle')
    print('Length:', second_rectangle.length)
    print('Width:', second_rectangle.width)
    print('Area:', second_rectangle.area())
    print('Perimeter:', second_rectangle.perimeter())

the output would be

.. testoutput:: geometric_classes

    Information about the second rectangle
    Length: 5
    Width: 7
    Area: 35
    Perimeter: 24


Inheritance
===========

A square is a special case of a rectangle, i.e., a rectangle with equal sides.
As the computation of the geometrical properties remains the same, one option
of initializing a square could be

.. testcode:: geometric_classes

    square = Rectangle(length=2, width=2)

But maybe you want to be more explicit when initializing squares. This is where
inheritance kicks in. Let us take a look at the definition of a ``Square``
class that inherits from the previously defined ``Rectangle`` class:

.. testcode:: geometric_classes

    class Square(Rectangle):
        """A square that is described by its side length."""

        def __init__(self, side_length):
            super().__init__(length=side_length, width=side_length)

As opposed to the ``Rectangle`` class the name of the ``Square`` class is
followed by parenthesis containing ``Rectangle``. This tells Python that the
``Rectangle`` class is the *superclass* of ``Square``, i.e., ``Square``
inherits from ``Rectangle``. To inherit means that, if not otherwise defined,
``Square`` has the exact same method definitions as its superclass
``Rectangle``.

But as the ``__init__`` method of ``Rectangle`` takes the arguments ``length``
and ``width``, which is not required for the definition of a square, we can
simplify it. Now it takes only one argument ``side_length``. If we stored it as
we did in the ``Rectangle`` class, i.e., as

.. code-block:: python

    def __init__(self, side_length):
        self.side_length = side_length

The methods that ``Square`` inherits from ``Rectangle`` would fail to be
callable, as they access the attributes ``length`` and ``width``, which would
not be defined if we took this definition of the ``__init__`` method. Instead
we could do this:

.. code-block:: python

    def __init__(self, side_length):
        self.length = side_length
        self.width = side_length

So now the definition looks awfully similar to the one of the ``Rectangle``
class. A bit too similar maybe, and we do not want to repeat ourselves.
Another side-effect is that, should the ``__init__`` method of the
``Rectangle`` implement some more code, it would have to be copied to
``Square`` as well. As this is error-prone there is a way to leverage the
method of a superclass within the child class, and this is done using the
:func:`super` function. If used within a method definition followed by calling
a method it will resolve to the first parent class that implements a method
with this name and call it for the current object. So by implementing it via

.. code-block:: python

    def __init__(self, side_length):
        super().__init__(length=side_length, width=side_length)

we tell Python to call the ``__init__`` method of the superclass of ``Square``
and pass the side_length for the ``length`` and ``width``.

Using the class can now be done like this:

.. testcode:: geometric_classes

    first_square = Square(side_length=2)
    print('Information about the first square')
    print('Length:', first_square.length)
    print('Width:', first_square.width)
    print('Area:', first_square.area())
    print('Perimeter:', first_square.perimeter())

The respective output:

.. testoutput:: geometric_classes

    Information about the first square
    Length: 2
    Width: 2
    Area: 4
    Perimeter: 8


Type checking
=============

.. testcode:: geometric_classes

    def what_is_it(object):
        if isinstance(object, Rectangle):
            print('It is a rectangle.')
        if isinstance(object, Square):
            print('It is a square.')

.. testcode:: geometric_classes

    what_is_it(first_rectangle)

.. testoutput:: geometric_classes

    It is a rectangle.

.. testcode:: geometric_classes

    what_is_it(first_square)

.. testoutput:: geometric_classes

    It is a rectangle.
    It is a square.


Exercises
=========

- Copy the definition of the ``Rectangle`` class and extend it by adding a
  method ``aspect_ratio`` which returns the ratio of its length to its width.

- Define a ``Circle`` class with the radius :math:`r` as defining attribute.
  Implement the ``area`` and ``perimeter`` class accordingly.
