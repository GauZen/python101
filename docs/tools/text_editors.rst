.. _sec_text_editors:

============
Text editors
============

The features a good text editor should have:

- `Unicode`_ support
      A good text editor should support Unicode. This is the de facto standard
      for cross-platform compatibility of text files. With Unicode support you
      can be sure that the text file you edited on your Unix machine can be
      worked with properly on, e.g., a Windows machine.
- `syntax highlighting`_
      In our case, the main objective of using a text editor is to write code.
      Choosing a text editor that supports syntax highlighting for the
      programming language we use helps us to comprehend the written code
      easier by applying different colors and/or weights to the text depending
      on whether the piece of text is, e.g., a string, a type declaration, or
      a keyword.
- `snippets`_
      Every programming language has certain structures for building blocks
      like, e.g., if-conditionals or for-loops. Typing them out each and every
      time is a waste of time. Good text editors allow the use of so-called
      snippets.
- hackability
      Each programmer has a different taste with regards to how they want to
      accomplish certain actions in text editors. Different shortcuts might be
      required, or a custom layout of the editor. A good text editor allows you
      to customize it to your needs, not require you to adapt to its way (at
      least to a certain amount).
- `package manager`_
      To be truly hackable a good text editor supports third-party packages
      that extend or alter the functionality of the text editor.

To gain more insight about the performance of different text editors take a
look at this `editor performance comparison`_.

In the following a brief introduction to the text editors I recommend is given.

.. _Unicode: https://en.wikipedia.org/wiki/Unicode
.. _syntax highlighting: https://en.wikipedia.org/wiki/Syntax_highlighting
.. _snippets: https://en.wikipedia.org/wiki/Snippet_(programming)
.. _package manager: https://en.wikipedia.org/wiki/Package_manager
.. _editor performance comparison: https://github.com/jhallen/joes-sandbox/tree/master/editor-perf


Atom
====

`Atom`_ is a text editor made by GitHub.

**Advantages**

- support for different encodings
- highly hackable
- `open-source <https://github.com/atom/atom>`_
- easy to learn

**Disadvantages**

- slower than the other presented editors
- less memory efficient than the other presented editors
- may not be installed on all machines you have to work with

.. _Atom: https://atom.io/


Sublime Text 3
==============

`Sublime Text`_ is a text editor made by a small team of developers. Proper
support for packages is supplied by`Package Control`_.

**Advantages**

- fast
- relatively memory efficient
- support for different encodings
- highly hackable
- easy to learn

**Disadvantages**

- closed-source
- may not be installed on all machines you have to work with
- if used for free a pop-up every ten times you save a file
- a license costs $70 at the time of writing

.. _Sublime Text: https://www.sublimetext.com/
.. _Package Control: https://packagecontrol.io/


Visual Studio Code
==================

`Visual Studio Code`_ is a text editor made by Microsoft.

**Advantages**

- support for different encodings
- highly hackable
- `open-source <https://github.com/Microsoft/vscode>`_
- easy to learn

**Disadvantages**

- may not be installed on all machines you have to work with

.. _Visual Studio Code: https://code.visualstudio.com/


Vim
===

`Vim`_ is a text editor made by the community lead by Bram Moolenaar. Support
for packages is built-in as of vim 8, but due to backward compatibility the
most popular package manager is `vim-plug`_.

**Advantages**

- `open-source <https://github.com/vim/vim>`_
- fast
- memory efficient
- may very well be installed on all Unix machines you have to work with

**Disadvantages**

- takes time to get used to
- hard to master

.. _Vim: http://www.vim.org/
.. _vim-plug: https://github.com/junegunn/vim-plug


Emacs
=====

`Emacs`_ is a text editor made by the community lead by the Free Software
Foundation.

**Advantages**

- `open-source <http://git.savannah.gnu.org/cgit/emacs.git>`_
- fast
- memory efficient
- may be installed on all Unix machines you have to work with

**Disadvantages**

- takes time to get used to
- hard to master

.. _Emacs: https://www.gnu.org/software/emacs/
