.. _sec_shell:

==============
The Unix Shell
==============

.. epigraph::

    "The Linux philosophy is 'Laugh in the face of danger'. Oops. Wrong One.
    'Do it yourself'. Yes, that's it."

    -- Linus Torvalds

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

.. code-block:: console

    $ pwd


``ls``
======

This command is used to show the contents of the directory you specify as
argument.

.. code-block:: console

    $ ls directory1

If you do not provide anything besides ``ls`` it prints the contents
of the current working directory.

.. code-block:: console

    $ ls

For a more verbose version you may use the ``-l`` options:

.. code-block:: console

    $ ls -l

.. note::

    If you have some spaces in some of your file names you have to enclose
    the whole filename like this: ``"{filename}"``


``cd``
======

This command is used to change the directory to the one specified as argument.
If no argument is provided you are changing to your home directory.

.. code-block:: console

    $ cd directory1

To get to the parent directory use

.. code-block:: console

    $ cd ..


.. note::

    In a lot of cases ``bash`` -- the shell you are using -- provides rather
    intelligent *autocompletion*. To use this start typing the name of a file
    or directory and hit the ``tab`` button. If there is a unique completion
    option it is completed automatically. Else hitting tab another time will
    give you a list of options that starts with whatever you typed until then.


``cat``
=======

This command is used to print the contents of the files specified as arguments.

.. code-block:: console

    $ cat file1 file2 ... fileN


``cp``
======

This command is used to copy files. For example

.. code-block:: console

    $ cp file1 file2

copies ``file1`` to ``file2``. If you want to copy a lot of files to another
directory use

.. code-block:: console

    $ cp file1 file2 ... fileN directory1/

Copying a whole directory requires you to use the ``-r`` option:

.. code-block:: console

    $ cp -r directory1 directory2


``mv``
======

This command is used to move files. For example

.. code-block:: console

    $ mv file1 file2

essentially renames ``file1`` to ``file2``. To move several files into a
directory use

.. code-block:: console

    $ mv file1 file2 ... fileN directory1/

As opposed to ``cp`` the ``mv`` command can move whole directories without
using the ``-r`` option:

.. code-block:: console


``touch``
=========

This command is used to create an empty file. Using

.. code-block:: console

    $ touch file1

hence results in an empty file with the name ``file1``.

.. note::

    If you want to copy something from the Terminal you can not do this via the
    key combination ``Ctrl + C`` as this is reserved for cancelling the running
    program. Instead use ``Ctrl + Shift + C``. For pasting you also have to use
    ``Ctrl + Shift + V``.


``rm``
======

This command is used to delete files and directories. Hence

.. code-block:: console

    $ rm file1

deletes ``file1``.

.. warning::

    If you delete files or directories on a modern, graphical operating system
    the files and directories usually do not get deleted immediately, but are
    copied to an intermediate directory that is usually called ``trash bin``.
    This could be considered a safety measure against accidentally deleting
    important files. This "safety net" does not exist for the ``rm`` command.
    Whatever you delete via ``rm`` is permanently deleted.


Summary
=======

.. highlights::

    ``pwd``
        Print the path to the directory you are currently in.

    ``ls $1``
        List the contents of directory specified by ``$1``. If you do not
        specify a directory it defaults to your current directory.

    ``cd $1``
        Change the directory to ``$1``. If you do not specify a directory you
        go to your home directory. If you want to go back to your last
        directory you can use ``cd -``.

    ``cat $1 $2 ... $n``
        Read the files specified and print their content to the terminal.

    ``cp $1 $2``
        Copy the first argument to the second argument. If you want to copy a
        directory you have to use it with the ``-r`` option: ``cp -r $1 $2``.

    ``mv $1 $2``
        Move the first argument to the second argument. It is basically like
        renaming the first argument.

    ``touch $1``
        Create an empty file at ``$1``.

    ``rm $1 $2 ... $n``
        Delete the files specified. If you want to delete a directory and its
        contents you have to use it with the ``-r`` option: ``rm -r $1``.


Tasks
=====

#. Create an empty file called ``my_first_file.txt``

#. Open the file with your text editor and fill it with something other and
   ``asdf``. Save and close afterwards.

#. Print the content of the file to the terminal.

#. Make a new directory named ``my_first_folder``

#. Copy the file ``my_first_file.txt`` into this directory.

#. Remove the old file.

#. Print the content of the file ``my_first_file.txt`` in the directory
   ``my_first_directory`` to the terminal.

#. Print your current working directory.

#. Enter the directory ``my_first_directory``.

#. Print your current working directory.

#. Enter the parent directory.

#. Delete the directory ``my_first_directory``.
