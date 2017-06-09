.. _sec_numpy_math:

****
Math
****

The goal of NumPy is to provide functions and classes that make numerical
computations easier. For an extensive overview see the section
:ref:`routines.linalg`. of the NumPy documentation. Some of them require the
part ``linalg`` after ``numpy``. In combination with

.. code-block:: python

    import numpy as np

the functions and classes may be used via

.. code-block:: python

    np.linalg.<function>

The functions that require this import are indicated by this usage.


Componentwise math operations
=============================

NumPy :class:`arrays <numpy.ndarray>` support the typical math operations
introduced in :ref:`sec_basics` and they are executed componentwise. Here are
a few examples:

    >>> x = np.array([1, 2, 3, 4, 5])
    >>> y = np.array([6, 5, 8, 9, 10])
    >>> z = 2.0
    >>> x + z
    array([ 3.,  4.,  5.,  6.,  7.])
    >>> x + y
    array([ 7,  7, 11, 13, 15])
    >>> y % z
    array([ 0.,  1.,  0.,  1.,  0.])
    >>> y / x
    array([ 6.        ,  2.5       ,  2.66666667,  2.25      ,  2.        ])


Dot
===

If you need a scalar product for 1D :class:`arrays <numpy.ndarray>` or matrix
multiplication for 2D :class:`arrays <numpy.ndarray>` the function
:func:`numpy.dot` is the function of choice:

    >>> x = np.array([1, 2, 3, 4, 5])
    >>> y = np.array([6, 5, 8, 9, 10])
    >>> np.dot(x, y)
    126
    >>> x.dot(y)  # alternative syntax
    126
    >>> x = np.array([[1, 2, 3],
    ...               [4, 5, 6],
    ...               [7, 8, 9]])
    >>> y = np.array([[10, 11, 12],
    ...               [13, 14, 15],
    ...               [16, 17, 18]])
    >>> z = np.array([[1/19, 1/20, 1/21],
    ...               [1/22, 1/23, 1/24],
    ...               [1/25, 1/26, 1/27]])
    >>> np.dot(x, np.dot(y, z))  # this is a bit convoluted
    array([[ 12.35196172,  11.80535117,  11.30555556],
           [ 29.63712919,  28.32591973,  27.12698413],
           [ 46.92229665,  44.84648829,  42.9484127 ]])
    >>> x.dot(y).dot(z)  # better
    array([[ 12.35196172,  11.80535117,  11.30555556],
           [ 29.63712919,  28.32591973,  27.12698413],
           [ 46.92229665,  44.84648829,  42.9484127 ]])


Eigenvalues
===========

The function :func:`numpy.linalg.eig` may be used to compute the `eigenvalues
and eigenvectors`_ of a square array:

    >>> x = np.array([[1, 2, 3],
    ...               [4, 5, 6],
    ...               [7, 8, 9]])
    >>> np.linalg.eig(x)
    (array([  1.61168440e+01,  -1.11684397e+00,  -1.30367773e-15]), array([[-0.23197069, -0.78583024,  0.40824829],
           [-0.52532209, -0.08675134, -0.81649658],
           [-0.8186735 ,  0.61232756,  0.40824829]]))

The output is a bit messy, but ss you can read in the documentation of
:func:`numpy.linalg.eig` the function actually returns two things: an array
holding the eigenvalues and an array holding the eigenvectors as columns:

    >>> eigenvalues, eigenvectors = np.linalg.eig(x)
    >>> for i in range(eigenvalues.size):
    ...     print(eigenvalues[i], eigenvectors[:, i])
    ...
    16.1168439698 [-0.23197069 -0.52532209 -0.8186735 ]
    -1.11684396981 [-0.78583024 -0.08675134  0.61232756]
    -1.30367772647e-15 [ 0.40824829 -0.81649658  0.40824829]

.. _eigenvalues and eigenvectors:
    https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors


Norm
====

Computing the norm of a vector is a fairly common task, so it seems obvious
that NumPy also provides a function for this: :func:`numpy.linalg.norm`.

    >>> x = np.array([3, 4])
    >>> np.linalg.norm(x)
    5.0

Besided the regularly used :math:`\ell^2`-norm this function also offers other
norms. For further information use the documentation of
:func:`numpy.linalg.norm`.


Determinant
===========

Knowing the determinant of an array may tell you whether it is singular or,
in the case of a :math:`3x3` array, tell you the volume of the rhomboid that is
spanned by the vectors composing the array.

    >>> x = np.array([[1, 2, 3],
    ...               [4, 5, 4],
    ...               [3, 2, 1]])
    >>> np.linalg.det(x)
    -7.9999999999999982

This should be :math:`-8` so it is an interesting way to see that the
determinant computed by NumPy is computed numerically and not analytically.


Exercises
=========

.. toctree::

    exercises/gaussian_elimination_eye
