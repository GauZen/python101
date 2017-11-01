.. _sec_shell:

**************
The Unix shell
**************

.. epigraph::

    "The Linux philosophy is 'Laugh in the face of danger'. Oops. Wrong One.
    'Do it yourself'. Yes, that's it."

    ---Linus Torvalds

We could try to think of a neat way of defining what a *Unix shell* is, but
thankfully Wikipedia_ comes to the rescue:

.. pull-quote::

    A Unix shell is a command-line interpreter or shell that provides a
    traditional Unix-like command line user interface. Users direct the
    operation of the computer by entering commands as text for a command line
    interpreter to execute, or by creating text scripts of one or more such
    commands.

To put it in simpler terms, instead of pointing and clicking on colorful icons
to perform actions like opening a directory or a program, you type commands in
a terminal. The most commonly used commands are outlined in the following
sections.

.. note::

    If you do not have any prior experience with command line interfaces
    (CLIs), working with one might seem daunting at first. This is perfectly
    normal. It takes time to get used to the Unix shell. The key to mastering
    the Unix shell is to use it. *A lot.*

.. _Wikipedia: https://en.wikipedia.org/wiki/Unix_shell


``pwd``
=======

This command is used to show the path to the current working directory. It is
usually used to see where you currently are.

.. code-block:: shell

    $ pwd


``ls``
======

This command is used to show the contents of the directory you specify as
argument.

.. code-block:: shell

    $ ls <directory>

If you do not provide anything besides ``ls`` it prints the contents
of the current working directory.

.. code-block:: shell

    $ ls

A single ``.`` in place of ``<directory>`` also results in the contents of the
current working directory to be printed, as ``.`` is an explicit way of
specifying the current working directory.

For a more verbose version you may use the ``-l`` options:

.. code-block:: shell

    $ ls -l

.. note::

    If you have some spaces in some of your file names you have to enclose
    the whole filename like this: ``"<filename>"``


``cd``
======

This command is used to change the directory to the one specified as argument.
If no argument is provided you are changing to your home directory.

.. code-block:: shell

    $ cd <directory>

To get to the parent directory use

.. code-block:: shell

    $ cd ..


.. note::

    In a lot of cases ``bash``---the shell you are using---provides rather
    intelligent *autocompletion*. To use this start typing the name of a file
    or directory and hit the ``tab`` button. If there is a unique completion
    option it is completed automatically. Else hitting tab another time will
    give you a list of options that starts with whatever you typed until then.


``cat``
=======

This command is used to print the contents of the files specified as arguments.

.. code-block:: shell

    $ cat <file1> <file2> ... <fileN>


``cp``
======

This command is used to copy files. For example

.. code-block:: shell

    $ cp <file1> <file2>

copies ``<file1>`` to ``<file2>``. If you want to copy a lot of files to
another directory use

.. code-block:: shell

    $ cp <file1> <file2> ... <fileN> <directory1>/

Copying a whole directory requires you to use the ``-r`` option:

.. code-block:: shell

    $ cp -r <directory1> <directory2>


``mv``
======

This command is used to move files. For example

.. code-block:: shell

    $ mv <file1> <file2>

essentially renames ``<file1>`` to ``<file2>``. To move several files into a
directory use

.. code-block:: shell

    $ mv <file1> <file2> ... <fileN> <directory1>/

As opposed to ``cp`` the ``mv`` command can move whole directories without
using the ``-r`` option:

.. code-block:: shell

    $ mv <directory1> <directory2>


``touch``
=========

This command is used to create an empty file. Using

.. code-block:: shell

    $ touch <file1>

hence results in an empty file with the name ``<file>``.

.. note::

    If you want to copy something from the Terminal you can not do this via the
    key combination :kbd:`Ctrl + C` as this is reserved for cancelling the
    running program. Instead use :kbd:`Ctrl + Shift + C`. For pasting you also
    have to use :kbd:`Ctrl + Shift + V`.


``mkdir``
=========

This command is used to create a directory. Using

.. code-block:: shell

    $ mkdir <directory>

thus creates a directory with the name ``<directory>``.


``rm``
======

This command is used to delete files and directories. Hence

.. code-block:: shell

    $ rm <file>

deletes ``<file>``.

.. warning::

    If you delete files or directories on a modern, graphical operating system
    the files and directories usually do not get deleted immediately, but are
    copied to an intermediate directory that is usually called ``trash bin``.
    This could be considered a safety measure against accidentally deleting
    important files. This "safety net" does not exist for the ``rm`` command.
    Whatever you delete via ``rm`` is permanently deleted.


``grep``
========

If you want to see whether some text is contained within a file you can use
``grep``:

.. code-block:: shell

    $ grep <pattern> <file>

with ``<pattern>`` being the text you are looking for.


``find``
========

Find files in a directory hierarchy. This program is rather extensive and can
perform complex search operations. In its simplest form it may be used like
this:

.. code-block:: shell

    $ find <path> -name "<pattern>"

It is important to put ``<pattern>`` into quotation marks to make sure the
shell is not expanding some special characters. Special characters can, e.g.,
be the wildcard character ``*``, which matches everything. Hence, the command

.. code-block:: shell

    $ find . -name "*.py"

finds all Python files below the current directory.


Summary
=======

.. highlights::

    ``pwd``
        Print the path to the directory you are currently in.

    ``ls <directory>``
        List the contents of directory specified by ``<directory>``. If you do
        not specify a directory it defaults to your current directory.

    ``cd <directory>``
        Change the directory to ``<directory>``. If you do not specify a
        directory you go to your home directory. If you want to go back to your
        last directory you can use ``cd -``.

    ``cat <file1> <file2> ... <fileN>``
        Read the files specified and print their content to the terminal.

    ``cp <file1> <file2>``
        Copy the first argument to the second argument. If you want to copy a
        directory you have to use it with the ``-r`` option:
        ``cp -r <directory1> <directory2>``.

    ``mv <file1/directory1> <file2/directory2>``
        Move the first argument to the second argument. It is basically like
        renaming the first argument.

    ``touch <file>``
        Create an empty file at ``<file>``.

    ``mkdir <directory>``
        Create a directory at ``<directory>``.

    ``rm <file1> <file2> ... <fileN>``
        Delete the files specified. If you want to delete a directory and its
        contents you have to use it with the ``-r`` option: ``rm -r <file1>``.

    ``grep <pattern> <file>``
        Search for ``<pattern>`` in ``<file>``.

    ``find <path> -name "<pattern>"``
        Find all files in ``<path>`` and below whose name is matching
        ``<pattern>``.


Exercises
=========

#. Create an empty file called ``my_first_file.txt``

#. Open the file with your text editor and fill it with something other than
   ``asdf``. Save and close afterwards.

#. Print the content of the file to the terminal.

#. Make a new directory named ``my_first_directory``

#. Copy the file ``my_first_file.txt`` into this directory.

#. Remove the old file.

#. Print the content of the file ``my_first_file.txt`` in the directory
   ``my_first_directory`` to the terminal.

#. Print your current working directory.

#. Enter the directory ``my_first_directory``.

#. Print your current working directory.

#. Enter the parent directory.

#. List the content of your current working directory.

#. Delete the directory ``my_first_directory``.

#. List the content of your current working directory.
