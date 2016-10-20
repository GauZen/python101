.. _sec_fitting_a_frequency_measurement:

===============================
Fitting a Frequency Measurement
===============================

Use the data provided :download:`here <frequency_measurement.csv>` and compute
the amplitude :math:`A`, the frequency :math:`f`, and the phase offset
:math:`\varphi` of the measurement.

.. rubric:: Recommended Steps

#. Read the data from the file.
#. Plot the data to get a feeling for it.
#. Think of a function that may be well suited for your data, and define
   it. In this case

   .. math::

        f(t) = A \sin (2 \pi f \cdot t - \varphi) + b

#. Try to fit it to the data. Are there any problems? How could you solve
   them?
#. Find a good initial guess by taking the data into account. It may be useful
   to smoothen the data first to reduce the noise. The :mod:`scipy.signal`
   module provides a variety of filters to do this. Use the smoothed data to
   get estimates for

   - the amplitude :math:`A`
   - the frequency :math:`f`
   - the phase offset :math:`\varphi`
   - the amplitude offset :math:`b`

#. Use the initial guess to fit the function to the raw data again.
#. Store the results in a file.
