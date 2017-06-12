r"""

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

Hence, implement a function following the given definition:

.. autofunction:: newtons_method_1d

Start by downloading the
:exercise:`exercise template </exercises/newtons_method_1d.py>` and
editing this file. You can run tests via

.. code-block:: console

    $ python newtons_method_1d.py test

to check whether you got a correct solution. You can also take a look at
:solution:`one possible solution </exercises/newtons_method_1d.py>`.

.. _Wikipedia: https://en.wikipedia.org/wiki/Newton's_method

"""


def newtons_method_1d(f, df_dx, x0, tol):
    """Return the root of `f` within `tol` by using Newton's method.

    Parameters
    ----------
    f : callable[[float], float]
        The function of which the root should be found.
    df_dx : callable[[float], float]
        The derivative of `f`.
    x_0 : float
        The initial guess for the algorithm.
    tol : float
        The tolerance of the method.

    Returns
    -------
    float
        The root of `f` within a tolerance of `tol`.

    """
    # begin solution
    x = x0
    while abs(f(x)) > tol:
        x -= f(x) / df_dx(x)
    return x
    # end solution

# -----------------------------------------------------------------------------
# In the following the tests for this exercise are given---do not modify them.
import sys
import pytest
from numpy.testing import assert_allclose


@pytest.mark.parametrize(
    ('f', 'df_dx', 'x0', 'tol', 'expected'),
    [
        (lambda x: x**2 - 2, lambda x: 2*x, 4, 1e-8, 2**(1/2)),
        (lambda x: x**2 - 2, lambda x: 2*x, -4, 1e-8, -2**(1/2)),
        (lambda x: x**3 - 5, lambda x: 3*x**2, 4, 1e-8, 5**(1/3))
    ])
def test_correct_result(f, df_dx, x0, tol, expected):
    assert_allclose(
        newtons_method_1d(f, df_dx, x0, tol),
        expected,
        rtol=0,
        atol=tol)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[-1] == 'test':
        pytest.main([__file__])
