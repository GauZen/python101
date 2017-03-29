.. _sec_file_io:

=======
File IO
=======

.. testsetup:: csv_file

    import sys
    from io import StringIO
    import builtins
    from contextlib import contextmanager

    _files = {
        'csv_file.txt': StringIO(
            '1, 2, 3\n'
            '4, 5, 6\n'
            '7, 8, 9\n')
    }

    class open:
        def __init__(
                self, file, mode='r', buffering=-1, encoding=None, errors=None,
                newline=None, closefd=True, opener=None):
            try:
                self.stringio = _files[file]
            except KeyError:
                self.stringio = StringIO()

        def read(self, size=None):
            return self.stringio.read(size)

        def write(self, s):
            return self.stringio.write(s)

        def close(self):
            self.stringio.seek(0)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.close()

        def __iter__(self):
            for line in self.stringio:
                yield line

Usually the result of your program is important not only now but in the future
as well. For this it is a good practice to store the results in file so that
you can work with them later on if necessary. This is called file input and
output, or in short: file IO.


Reading from a file
===================

The best way to open a file in Python is by using
:ref:`the with statement <with>`. This automatically opens the file, keeps a
lock on it so that no one is able to modify it while you are working with it,
and closes it afterwards. Interacting with the file is then done by working
with the variable that you specify after ``as``. This is called a
:term:`file object`. To get the complete content of a file use its ``read()``
method like this:

.. doctest:: csv_file

    >>> with open('csv_file.txt', 'r') as f:
    ...     file_content = f.read()
    ...
    >>> print(file_content)
    1, 2, 3
    4, 5, 6
    7, 8, 9
    <BLANKLINE>

where the first parameter is the path to the file and the second parameter is
the so-called file mode. ``r`` is for read-only.

.. note::

    In some tutorials and also production code you may find something along the
    lines of this to interact with a file:

    .. doctest:: csv_file

        >>> f = open('csv_file.txt', 'r')
        >>> file_content = f.read()
        >>> f.close()
        >>> print(file_content)
        1, 2, 3
        4, 5, 6
        7, 8, 9
        <BLANKLINE>

    This is kind of the old style of working with files when
    :ref:`the with statement <with>` did not exist yet. It has the huge
    downside that you have to take care about closing the file. And if an error
    is raised between ``open`` and ``close`` it is not closed at all.
    :ref:`The with statement <with>` takes care of this for you even in the
    case of an exception and is subsequently the preferred way.

You can also iterate over ``f`` as if it is some form of container:

.. doctest:: csv_file

    >>> with open('csv_file.txt', 'r') as f:
    ...     for i, line in enumerate(f):
    ...         print('Line', i, '--', line)
    ...
    Line 0 -- 1, 2, 3
    <BLANKLINE>
    Line 1 -- 4, 5, 6
    <BLANKLINE>
    Line 2 -- 7, 8, 9
    <BLANKLINE>

As you can see you get some additional white lines. The reason for this is that
each line still contains its newline character ``\n`` in the end. To this one
:func:`print` adds an additional one by default so you end up with an empty
line. To circumvent this use the :meth:`~str.strip` method of the line string:

.. doctest:: csv_file

    >>> with open('csv_file.txt', 'r') as f:
    ...     for i, line in enumerate(f):
    ...         stripped_line = line.strip()
    ...         print('Line', i, '--', stripped_line)
    ...
    Line 0 -- 1, 2, 3
    Line 1 -- 4, 5, 6
    Line 2 -- 7, 8, 9


Writing to a file
=================

To write to a file you have to open it first, this time with ``w`` as file
opening mode, to indicate that you want to write to the file. Then you can
use the ``write()`` method of the file object to write to the file:

.. doctest:: csv_file

    >>> with open('my_first_file.txt', 'w') as f:
    ...     f.write('This is smart.')
    ...     f.write('This is even smarter.')
    ...
    14
    21

Now the content of your file would be

.. code-block:: text

    This is smart.This is even smarter.

Which is not nicely formatted. So you have to take care that you add the
newline character ``\n`` and spaces accordingly:

.. doctest:: csv_file

    >>> with open('my_first_file.txt', 'w') as f:
    ...     f.write('This is smart.\n')
    ...     f.write('This is even smarter.\n')
    ...
    15
    22

Subsequently the content of your file would be

.. code-block:: text

    This is smart.
    This is even smarter.


Summary
=======

.. highlights::

    * You can open a file using the ``open()`` function in a ``with``
      statement.
    * To merely read from a file open it with the filemode ``r`` and use the
      ``read()`` method of the file object.
    * To write from a file open it with the filemode ``w`` and use the
      ``write`` method of the file object.
