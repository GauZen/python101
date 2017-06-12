r"""
A palindrome_ is a word, phrase, number or sequence of characters which reads
the same backward as forward. Examples for words are *radar*, *level*, and
*racecar*. Write a function that checks whether a :class:`strings <str>` is a
palindrome or not.

.. autofunction:: is_palindrome_string

Start by downloading the
:exercise:`exercise template </exercises/is_palindrome_string.py>` and editing
this file. You can run tests via

.. code-block:: console

    $ python is_palindrome_string.py test

to check whether you got a correct solution. You can also take a look at
:solution:`one possible solution </exercises/is_palindrome_string.py>`.

.. _palindrome: https://en.wikipedia.org/wiki/Palindrome

"""


def is_palindrome_string(string):
    """Return whether `string` is a palindrome, ignoring the case.

    Parameters
    ----------
    string : str
        The string to check.

    Returns
    -------
    bool
        A boolean representing whether `string` is a palindrome or not.

    """
    # begin solution
    return string.lower() == string[::-1].lower()
    # end solution

# -----------------------------------------------------------------------------
# In the following the tests for this exercise are given---do not modify them.
import sys
import pytest


@pytest.mark.parametrize(
    ('string', 'expected'),
    [
        ('racecar', True),
        ('Racecar', True),
        ('racecar racecar', True),
        ('abracadabra', False)
    ])
def test_correct_result(string, expected):
    assert is_palindrome_string(string) == expected


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[-1] == 'test':
        pytest.main([__file__])
