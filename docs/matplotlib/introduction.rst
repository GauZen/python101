.. _sec_matplotlib:

##########
Matplotlib
##########

.. epigraph::

    "The purpose of visualization is insight, not pictures."

    ---Ben Shneiderman

Visualization is one of the most important means for the interpretation of
the results of scientific computations. The package that is mostly used for
this task is Matplotlib_.

The ``matplotlib`` package is typically imported via

.. code-block:: python

    import matplotlib.pyplot as plt

And subsequently all plotting commands are called using the prefix ``plt``.


The anatomy of a figure
=======================

The ``matplotlib`` documentation offers a nice introduction to lay out the
`parts of a figure`_. At the top you have the
:class:`~matplotlib.figure.Figure` itself. To create a
:class:`~matplotlib.figure.Figure` use

.. literalinclude:: ../pyplots/empty_figure.py

which will create an empty figure:

.. plot:: pyplots/empty_figure.py
    :align: center

Typically a figure contains one to several
:class:`~matplotlib.axes.Axes` objects, that are what you typically think of as
"a plot."

The easiest way to create a figure with one :class:`~matplotlib.axes.Axes`
object is via

.. literalinclude:: ../pyplots/figure_with_one_axes.py

which results in:

.. plot:: pyplots/figure_with_one_axes.py
    :align: center

An :class:`~matplotlib.axes.Axes` object itself has two [#three-axis-in-3D]_
:class:`~matplotlib.axis.Axis` objects, one for the x-axis and one for the
y-axis.

.. todo::

    Describe how to manipulate the axis objects.


.. _parts of a figure: https://matplotlib.org/faq/usage_faq.html#parts-of-a-figure



A tale of two interfaces
========================

Originally ``matplotlib`` tried to emulate the MATLAB® graphics commands,
without depending on it. Part of this emulation also involved mimicking the
way of interfacing. In the case of MATLAB® it is a state-based interface.
:func:`plt.subplots`




Rather than exercises that want you to get some results you are shown simple
examples for the most common types of plots.

.. note::

    Producing scientific plots that manage to support your chain of arguments
    in a presentation or publication can not be overestimated. To a certain
    degree it could be considered an art, but there are some best practices,
    e.g., for :ref:`picking colormaps <colormaps>`.

.. rubric:: Footnotes

.. [#three-axis-in-3D]
    In the case of 3-dimensional plots, an :class:`~matplotlib.axes.Axes`
    contains three :class:`~matplotlib.axis.Axis` objects, .

.. _Matplotlib: http://matplotlib.org/
