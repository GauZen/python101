.. _sec_numpy_gaussian_elimination_eye:

**********************************
Gaussian Elimination (Eye Variant)
**********************************

Solving systems of linear equations is one of the basic tasks in numerical
mathematics---hence it is also one of the basic tasks in computational
materials science. A system of linear equations like

.. math::

     2x + y -  z  &=   8  & \quad L_1 \\
    -2x - y + 2z  &= -11  & \quad L_2 \\
    -2x + y + 2z  &=  -3  & \quad L_3

may also be described via

.. math::

    \vec{A} \vec{x} = \vec{b}

where

.. math::

    A = \begin{bmatrix}
            2 & 1 & -1 \\
            -3 & -1 & 2 \\
            -2 & 1 & 2
        \end{bmatrix}
    \quad
    x = \begin{bmatrix}
            x \\
            y \\
            z
        \end{bmatrix}
    \quad
    b = \begin{bmatrix}
            8 \\
            -11 \\
            -3
        \end{bmatrix}

The solution algorithm makes use of the augmented matrix form

.. math::

      \begin{bmatrix}
          2 & 1 & -1 & | & 8 \\
          -3 & -1 & 2 & | & -11 \\
          -2 & 1 & 2 & | & -3
      \end{bmatrix}

The procedure is then to first get this augmented matrix form into triangle
form and subsequently form the identity matrix on the left hand side. The
right hand side then is the solution. For further information see `Gaussian
elimination`_

Start with the following template, complete it, and test it:

.. code-block:: python

    def gaussian_elimination_eye(A, b):

.. _Gaussian elimination: https://en.wikipedia.org/wiki/Gaussian_elimination
