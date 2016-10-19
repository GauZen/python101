.. _sec_strip_and_split:

===============
Split and Strip
===============

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
['0.1', '0.2', '0.3', '0.4', ' 0.5']

You can take the following template:

.. code-block:: python

    def split_and_strip(string, delimiter):
