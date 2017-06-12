.. _sec_strings:

*******
Strings
*******

You have worked with them for a while now: :class:`strings <str>`. In principle
strings are containers of characters in a certain order. As such they are
somewhat similar to :class:`lists` <list>`, and also support, e.g., indexing.

>>> my_first_string = 'Hello, World!'
>>> my_first_string[7:]
'World!'
>>> my_first_string[::-1]
'!dlroW ,olleH'

They offer a large amount of ways to work with text, of which a few selected
ones are outlined in the following.


``lower``
=========

Returns the lowercase version of the string.

>>> 'Hello, World!'.lower()
'hello, world!'


``upper``
=========

Returns the uppercase version of the string.

>>> 'Hello, World!'.upper()
'HELLO, WORLD!'


``split``
=========

Working with a whole string at once is needlessly complicated in many cases.
Hence the Python standard library offers a way to take a :class:`string <str>`
apart: :meth:`str.split`

>>> some_string = 'My first string'
>>> some_string.split()
['My', 'first', 'string']

By default it splits to an arbitrary amount of whitespace

>>> some_string = 'My     second     string'
>>> some_string.split()
['My', 'second', 'string']

.. note::

    In Python whitespace is everything you can not directly see like spaces,
    tabs (``\t`` in strings), and newlines (``\n`` in strings).

but you can also specify another string which is used to split the other string
apart:

>>> some_string = '0.1, 0.2, 0.3, 0.4, 0.5'
>>> some_string.split(',')
['0.1', ' 0.2', ' 0.3', ' 0.4', ' 0.5']

The string that is used to split with is consumed in the process. So to get rid
of the additional whitespace you might get the idea to add it to the string
used for the splitting

>>> some_string = '0.1, 0.2, 0.3, 0.4, 0.5'
>>> some_string.split(', ')
['0.1', '0.2', '0.3', '0.4', '0.5']

Eventually this might lead to problems if the string format is not strictly kept:

>>> some_string = '0.1,   0.2,0.3, 0.4,  0.5'
>>> some_string.split(', ')
['0.1', '  0.2,0.3', '0.4', ' 0.5']

But Python's got you covered...


``strip``
=========

To get rid of unwanted whitespace around a string you can use the
:meth:`str.strip` method:

>>> some_string = '\n\n    So much surrounding whitespace\n\n'
>>> print(some_string)
<BLANKLINE>
<BLANKLINE>
    So much surrounding whitespace
<BLANKLINE>
<BLANKLINE>
>>> some_string.strip()
'So much surrounding whitespace'

You can also get rid of something else than whitespace by specifying the
characters as an argument:

>>> more_string = '...Python...'
>>> more_string.strip('.')
'Python'

.. note::

    The characters you specify as an argument are not seen as a string but as
    a collection of characters you want to strip of the string:

    >>> incantation = 'abracadabra'
    >>> incantation.strip('bra')
    'cad'


Summary
=======

- Use :meth:`str.split` to split a :class:`string <str>` at a substring.
- Use :meth:`str.strip` to get rid of excess characters at the edges,
  especially whitespace.


Exercises
=========

.. toctree::

    exercises/split_and_strip
    exercises/is_palindrome_string
