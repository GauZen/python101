.. _sec_numpy_array:

*****
Array
*****

The NumPy :class:`array <numpy.ndarray>` is the underlying mechanism that makes
NumPy so convenient and efficient.

Creating arrays
===============

A NumPy :class:`array <numpy.ndarray>` is easily initialized via

    >>> np.array([0, 1, 2])  # 1D array of integers
    array([0, 1, 2])
    >>> np.array([0.0, 1.0, 2.0])  # 1D array of floats
    array([ 0.,  1.,  2.])
    >>> np.array([[0, 1], [2, 3]])  # 2D array of integers
    array([[0, 1],
           [2, 3]])

So by nesting lists of numbers you are able to construct multi-dimensional
arrays. But there are also other methods to initialize
:class:`arrays <numpy.ndarray>`:

- :func:`numpy.zeros`:

      >>> np.zeros(3)
      array([ 0.,  0.,  0.])
      >>> np.zeros([2, 3])
      array([[ 0.,  0.,  0.],
             [ 0.,  0.,  0.]])

- :func:`numpy.zeros`:

      >>> np.ones(3)
      array([ 1.,  1.,  1.])
      >>> 3 * np.ones(3)
      array([ 3.,  3.,  3.])
      >>> np.ones([2, 3])
      array([[ 1.,  1.,  1.],
             [ 1.,  1.,  1.]])

- :func:`numpy.eye`:

      >>> np.eye(2)
      array([[ 1.,  0.],
             [ 0.,  1.]])
      >>> -2 * np.eye(2)
      array([[-2., -0.],
             [-0., -2.]])

- :func:`numpy.arange`: This one should feel rather familiar to the
  :class:`range` of regular Python. But where the latter is only able to deal
  with integers, the implementation of NumPy can also work with floats.

      >>> np.arange(5)
      array([0, 1, 2, 3, 4])
      >>> np.arange(3, 7)
      array([3, 4, 5, 6])
      >>> np.arange(2, 4, 0.5)
      array([ 2. ,  2.5,  3. ,  3.5])

- :func:`numpy.linspace`: If you need evenly spaced samples this way of
  initializing them is preferred to :func:`numpy.arange` due to the latter
  introducing slight roundoff errors which is caused by the implementation.

      >>> np.linspace(0, 4, 5)
      array([ 0.,  1.,  2.,  3.,  4.])
      >>> np.linspace(0.3, 0.7, 5)
      array([ 0.3,  0.4,  0.5,  0.6,  0.7])
      >>> np.linspace(0.3, 0.7, 4, endpoint=False)
      array([ 0.3,  0.4,  0.5,  0.6])


Array attributes
================

The :class:`arrays <numpy.ndarray>` also provide some information about
themselves which can be accessed by its attributes.


Number of dimensions
--------------------

The :attr:`ndim <numpy.ndarray.ndim>` attribute of an array is the amount of
dimensions of the array.

    >>> x = np.array([0.0, 1.0, 2.0])
    >>> x.ndim
    1
    >>> x = np.array([[0, 1, 2], [3, 4, 5]])
    >>> x.ndim
    2


Shape
-----

The :attr:`shape <numpy.ndarray.shape>` attribute of an array is a tuple
representing the number of elements along each dimension.

    >>> x = np.array([0.0, 1.0, 2.0])
    >>> x.shape
    (3,)
    >>> x = np.array([[0, 1, 2], [3, 4, 5]])
    >>> x.shape
    (2, 3)
    >>> x.shape[0]
    2
    >>> x.shape[1]
    3


Size
----

The :attr:`size <numpy.ndarray.size>` attribute of an array is the amount of
elements of the array.

    >>> x = np.array([0.0, 1.0, 2.0])
    >>> x.size
    3
    >>> x = np.array([[0, 1, 2], [3, 4, 5]])
    >>> x.size
    6

So essentially it is the product sum of the
:attr:`shape <numpy.ndarray.shape>`.


Accessing data
==============

Similarly to :class:`lists <list>` and :class:`tuples <tuple>` data is accessed
via referring to the indices:

    >>> x = np.array([[0, 1, 2],
    ...               [3, 4, 5]])
    >>> x[0, 0]
    0
    >>> x[0, 1]
    1
    >>> x[1, 0]
    3
    >>> x[1, 2]
    5


Slicing
=======

Slicing refers to extracting partial data from arrays. This is very efficient
as nothing is copied in memory.

    >>> x = np.array([[0, 1, 2, 3, 4],
    ...               [5, 6, 7, 8, 9],
    ...               [10, 11, 12, 13, 14],
    ...               [15, 16, 17, 18, 19],
    ...               [20, 21, 22, 23, 24]])
    >>> x[0, :]
    array([0, 1, 2, 3, 4])
    >>> x[1, :]
    array([5, 6, 7, 8, 9])
    >>> x[:, 1]
    array([ 1,  6, 11, 16, 21])
    >>> x[:3, :3]
    array([[ 0,  1,  2],
           [ 5,  6,  7],
           [10, 11, 12]])
    >>> x[2:, 2:]
    array([[12, 13, 14],
           [17, 18, 19],
           [22, 23, 24]])

.. note::

    Slices of an array share the memory of the original array. Hence all the
    changes you do to a slice are also represented in the original array:

        >>> x = np.array([[0, 1, 2, 3, 4],
        ...               [5, 6, 7, 8, 9],
        ...               [10, 11, 12, 13, 14],
        ...               [15, 16, 17, 18, 19],
        ...               [20, 21, 22, 23, 24]])
        >>> print(x)
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]
         [20 21 22 23 24]]
        >>> x_slice = x[1:-1, 1:-1]
        >>> print(x_slice)
        [[ 6  7  8]
         [11 12 13]
         [16 17 18]]
        >>> x_slice[1, 1] = 888
        >>> print(x_slice)
        [[  6   7   8]
         [ 11 888  13]
         [ 16  17  18]]
        >>> print(x)
        [[  0   1   2   3   4]
         [  5   6   7   8   9]
         [ 10  11 888  13  14]
         [ 15  16  17  18  19]
         [ 20  21  22  23  24]]
