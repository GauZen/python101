.. _sec_version_control_systems:

***********************
Version control systems
***********************

`Version control`_ is a component of software engineering that deals with the
management of changes to documents, code, etc. Among the simplest examples are
versions of programs. Either a date-based approach is taken or an incrementing
set of numbers is used to indicate different versions. As there may be several
changes between single versions of code a more fine grained solution may be
taken to enable more control over the changes to your code. Version control
systems are designed for this very task and are thus an important tool for each
computational scientist. So why exactly would you like to use a version control
system then?

#. Storing versions
       If you have ever been in the situation of writing a thesis you may have
       given your "final" draft to someone. Afterwards you made a revision
       based on the suggestions. Then you handed it in and maybe got some more
       suggestions, which lead to further changes. And besides the "final"
       changes your document probably evolved over many days, and passages and
       the overall structure changed.

       - How would you store the intermediate versions of such documents? Do
         you store the changed file? Or maybe the whole project? Either you can
         only view one file at a time or have an unnecessary amount of data
         duplication.

       - How would you name these versions? Do you include the date in the
         filename? What if you have several versions a day? Date and time? That
         takes a lot of discipline.

       - How do you know the changes from the previous changes? If you store the
         whole document it is still hard to make out the parts that changed,
         let alone for a whole project. An option would be to store the changes
         in an additional file like ``CHANGES`` or in a ``README`` file. Again,
         this takes a lot of discipline.

       A version control systems takes care of all of that for you. You only
       have one specific version on your disk---the one you are working on. The
       other versions are hidden inside the version control system and can be
       retrieved at any time. A version control system, furthermore, is able to
       show you the exact changes between two arbitrary versions of your
       project.

#. Restoring earlier versions
       Besides the previously mentioned benefit of being able to view changes
       among versions, being able to restore previous versions of your code
       have further advantages. Say you have been working on a new feature in
       your project. At one point it may turn out that it leads nowhere. With
       a version control system you can simply restore the version which did
       not yet have any changes connected to this feature and you can start
       from a clean slate.

       Similarly, if your code has worked before, but does not at the current
       version, you may use, e.g., a `binary search`_ within the changes that
       are versioned by the version control system to isolate the changes which
       introduced the bug.

       .. _binary search: https://en.wikipedia.org/wiki/Binary_search_algorithm



.. _version control: https://en.wikipedia.org/wiki/Version_control


Best practices
==============

Descriptive commit messages
---------------------------


What not to put into version control
------------------------------------

There are some things that you should not put into version control, i.e.,

- config files with sensitive information, e.g., passwords, private keys,
- editor backups,
- generated files, e.g., executables, HTML documentation, and
- OS specific files, e.g., ``Thumbs.db``, ``.DS_Store``.


SVN
===


Git
===

`Git`_ is a version control system created by `Linus Torvalds`_, the
creator of Linux_,


.. _git: https://git-scm.com/
.. _Linus Torvalds: https://en.wikipedia.org/wiki/Linus_Torvalds
.. _Linux: https://en.wikipedia.org/wiki/Linux


Ignoring files
--------------

Useful gitignore templates
^^^^^^^^^^^^^^^^^^^^^^^^^^

The official github group supplies a nice list of `global gitignore templates`_
as well as `project specific gitignore templates`_.

.. _global gitignore templates: https://github.com/github/gitignore/tree/master/Global
.. _project specific gitignore templates: https://github.com/github/gitignore
