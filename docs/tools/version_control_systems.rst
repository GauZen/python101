.. _sec_version_control_systems:

=======================
Version control systems
=======================

Even if you have no prior experience with programming, you may already be
familiar with some kind of version control, whether on purpose or not. Over the
course of your studies it is very likely you have had to write some sort of
papers, maybe even while collaborating with others. Does the following comic
strip resonate with you?

.. figure:: /images/phd101212s.gif
    :align: center
    :target: http://phdcomics.com/comics.php?f=1531
    :scale: 60 %

    "Piled Higher and Deeper" by Jorge Cham
    (www.phdcomics.com)

This gives you a way of keeping track of changes, as you can compare two
versions of the same document. Depending on the software you use you either
have to compare the changes "manually" by skimming the whole document, or you
can get a view highlighting the differences (see, for example,
:ref:`subsec_diff`).

Another way of having versions of a file usually comes with cloud file storage
services like Dropbox or Google Drive. Those services keep a version history of
the synced files available for restoring files you want to revert to older
versions or which you deleted accidentally.

    But why would we want to keep track of changes to our code?
    Would the latest working version not suffice at all times?

If we keep track of changes to our code we do not have to be afraid to simply
tinker with our code. Maybe we get an awesome idea for a new feature or how to
speed up your code. As we hack away we realize that the idea is not really that
awesome and we wish to go back to our previous working state. If we are then in
the unlucky state that the "undo" action of our text editor is unable to revert
all the changes we made, we have to fall back to another solution, e.g., the
aforementioned naive version control schemes. If we worked on a copy of the
last working version "reverting" is simple---we just delete the fresh copy.
Reverting our file back using the version history of a cloud file storage
service requires may require us to go to their website and check quite a few
versions of this file, as we have not had any way of controlling which state of
the file represents a meaningful increment. This leads us to the first feature
we would like our version control system to have:

.. note::

    We want to have control over what changes in our document/code form a
    logical unit that represents a meaningful increment.

More complicated documents or code libraries may be split up into several files
to emphasize the structure while separating logical units like chapters or
classes, respectively. When using the copy-and-rename scheme we would copy and
rename the directory containing all the files. The drawback of this is the
redundancy, as not all the files may change within the same increment. When
using the version history of cloud file storage services, on the other hand, we
do not run into the problem of data redundancy, but we are unable to track
which versions of the files belong together.

.. note::

    We want to be able to not only track the changes of a file, but the
    cohesive changes across multiple files, i.e., we want to track changes of a
    project instead of files.

These two ways of keeping track of file versions come with a variety of
advantages and disadvantages that we are going to address in the following
while we introduce git_ as the right tool for the job with regards to version
control systems.


During our coding sessions there will be times when we wish we could take some
of the changes to a working script back and start from the last working
checkpoint. Or we find a bug that was introduced somewhere down the road. Or
we accidentally delete an important file. In the past we may have used the
"undo" command in our text editors or the history tracking of cloud file
hosting services like Dropbox. But this is not sufficient for proper source
code management. Let us work out the advantages of version control systems as
another tool in our toolbox over file versioning by, e.g., appending version
numbers to the filename---d


Best practices
==============

.. rubric:: What not to put into version control

- config files with sensitive information, e.g., passwords, private keys
- editor backups
- generated files, e.g., executables, HTML documentation
- OS specific files, e.g., ``Thumbs.db``, ``.DS_Store``


SVN
===


Git
===

One of the most popular version control systems at the time of writing this
tutorial is git_. It was created by Linus Torvalds for development of the Linux
kernel, which is one of the most widely distributed software repositories.

Let us introduce the most important commands by creating a new project: a
collection of recipes.


Initializing a git repository---``git init``
--------------------------------------------

First of all we create a new directory that represents
the root of our project via

.. code-block:: shell

    mkdir recipes

and subsequently we enter it

.. code-block:: shell

    cd recipes

At this point we can use the command

.. code-block:: shell

    git init

to initialize the ``recipes`` directory as a new git repository. We should see
the following output in your console

.. code-block:: text

    Initialized empty Git repository in <path_before_recipes>/recipes/.git/

If we now view the contents of the ``recipes`` directory via

.. code-block:: shell

    ls -A

we should see a new directory called ``.git``, whose content we can inspect
using

.. code-block:: shell

    ls .git

resulting in the output

.. code-block:: text

    branches  config  description  HEAD  hooks  info  objects  refs

This directory is where git stores all the information about all versions of
the files associated with the project. At this point we should neither modify
nor delete any files in this directory, as it may lead to corruption of our
repository.


Knowing what's what---``git status``
------------------------------------




.. _git: https://git-scm.com/


Ignoring files
--------------

Useful gitignore templates
^^^^^^^^^^^^^^^^^^^^^^^^^^

The official github group supplies a nice list of `global gitignore templates`_
as well as `project specific gitignore templates`_.

.. _global gitignore templates: https://github.com/github/gitignore/tree/master/Global
.. _project specific gitignore templates: https://github.com/github/gitignore
