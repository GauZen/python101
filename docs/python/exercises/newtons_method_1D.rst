.. _sec_newtons_method_1d:

====================
Newton's method (1D)
====================

Newton's method is a rather popular iterative root finding algorithm. Starting
at an initial guess :math:`x_0` it tries to find better and better
approximations of the root of a function :math:`f(x)`. For this it uses the
first derivative :math:`f'(x)` of the function. The process

.. math::

    x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}

is repeated until a value :math:`f(x_n)` is reached that is within a predefined
tolerance to zero. For further information see the `Wikipedia`_ page.

The way it is supposed to work is as follows:

>>> def f(x):
...     return x**2 - 2
...
>>> def df_dx(x):
...     return 2*x
...
>>> newtons_method_1d(f, df_dx, x0=4, tol=1e-8)  # doctest:+SKIP
1.4142135623730951



.. _Wikipedia: https://en.wikipedia.org/wiki/Newton's_method
