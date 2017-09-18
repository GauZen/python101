.. _sec_comments:

********
Comments
********

Once your programs grow longer and the logic gets more and more complicated it
is a *very* good idea to place *meaningful* comments in your code. This makes
it easier for the future you and your collaborators or supervisors to actually
understand why your implementation is as it is.

In the very beginning your comments may be used to outline what the code block
following the comment is actually doing. Once you get more familiar with Python
the content of the comment should change from *what* the code is doing to *why*
it is doing it.

To actually write a comment prepend it with the ``#`` character. So if you
write

.. testcode::

    # In the following example you should only see
    # ``Now you see me.``, and
    # ``Are you still seing me?`` in the terminal.

    print('Now you see me.')
    # print("Now you don't.")
    print('Are you still seeing me?')  # Inline comments are nice as well!

into a file and execute it you should only see

.. testoutput::

    Now you see me.
    Are you still seeing me?


Summary
=======

.. highlights::

    * You can use comments by prepending ``#``
    * Comments are useful to explain why you did something the way you did it


Exercises
=========

#. If you encounter some more complicated code-blocks in the future comment
   them. Admittedly this is not directly an exercise, but a sincere request.
#. Really, comment your code for others and your future self. You will forget
   why you coded something the way you did. Still not really an exercise.
