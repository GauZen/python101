r"""
The `Heaviside step function`_ can be defined as

.. math::
    :nowrap:

    \begin{equation}
        H(x) = \begin{cases} 0, &x < 0, \\ 1, &x \ge 0. \end{cases}
    \end{equation}
    
Write a function that implements the Heaviside step function following the
given definition:

.. autofunction:: heaviside_step_function

Start by downloading the
:exercise:`exercise template </exercises/heaviside_step_function.py>` and editing
this file. You can run tests via

.. code-block:: console

    $ python heaviside_step_function.py test

to check whether you got a correct solution. You can also take a look at
:solution:`one possible solution </exercises/heaviside_step_function.py>`.

.. _Heaviside step function: https://en.wikipedia.org/wiki/Heaviside_step_function

"""


def heaviside_step_function(n):
    """Return the value of the Heaviside step function of `n`.

    Parameters
    ----------
    n : float
        The number of which the Heaviside step function should be computed.

    Returns
    -------
    int
        The value of the Heaviside step function of `n`.

    """
    # begin solution
    if n < 0:
        res = 0
    else:
        res = 1
    return res
    # end solution

# -----------------------------------------------------------------------------
# In the following the tests for this exercise are given---do not modify them.
import sys
import pytest


@pytest.mark.parametrize(
    ('n', 'expected'),
    [
        (-2, 0),
        (-1, 0),
        (-0.1, 0),
        (0, 1),
        (0.1, 1),
        (1, 1),
        (2, 1)
    ])
def test_correct_result(n, expected):
    assert heaviside_step_function(n) == expected


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[-1] == 'test':
        pytest.main([__file__])
