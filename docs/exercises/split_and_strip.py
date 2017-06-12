r"""
From time to time you may want to split a string by a delimiting character like
``,``, but the whitespace is all over the place.

>>> some_string = '0.1,   0.2,0.3, 0.4,  0.5'
>>> some_string.split(',')
['0.1', '   0.2', '0.3', ' 0.4', '  0.5']
>>> some_string.split(', ')
['0.1', '  0.2,0.3', '0.4', ' 0.5']

So a pure splitting operation does not really do the trick. Write a function
that improves this behavior for this case, so that you can use it as follows:

>>> strip_and_split(some_string, ',')  # doctest:+SKIP
['0.1', '0.2', '0.3', '0.4', '0.5']

.. autofunction:: split_and_strip

Start by downloading the
:exercise:`exercise template </exercises/split_and_strip.py>` and editing
this file. You can run tests via

.. code-block:: console

    $ python split_and_strip.py test

to check whether you got a correct solution. You can also take a look at
:solution:`one possible solution </exercises/split_and_strip.py>`.

"""


def split_and_strip(string, delimiter):
    """
    Return a list of stripped strings after splitting `string` by `delimiter`.

    Parameters
    ----------
    string : str
        The string to split and strip.
    delimiter : str
        The string to split by.

    Returns
    -------
    list[str]
        The list of strings that are stripped after splitting by `delimiter`.

    """
    # begin solution
    return [s.strip() for s in string.split(delimiter)]
    # end solution

# -----------------------------------------------------------------------------
# In the following the tests for this exercise are given---do not modify them.
import sys
import pytest


@pytest.mark.parametrize(
    ('string', 'delimiter', 'expected'),
    [
        ('1,2,3', ',', ['1', '2', '3']),
        ('1,2, 3', ',', ['1', '2', '3']),
        ('1,2,3', ':', ['1,2,3'])
    ])
def test_correct_result(string, delimiter, expected):
    assert split_and_strip(string, delimiter) == expected


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[-1] == 'test':
        pytest.main([__file__])
