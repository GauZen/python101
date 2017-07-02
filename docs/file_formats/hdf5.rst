.. _sec_hdf5:

**************************
Hierarchical Data Format 5
**************************

:filename extension: ``.h5``, ``.hdf5``

The file structure of HDF5 includes two major types of objects:

- Datasets
      Multidimensional arrays of a homogeneous type.

- Groups
      Container structures which can hold datasets or other groups.

In that way we end up with a data format that somewhat resembles a filesystem.


Python support for HDF5 is due to the `h5py package`_, which can be installed
via

.. code-block:: console

    pip install h5py

and be used after importing it via

.. code-block:: python

    import h5py

.. _h5py package: http://www.h5py.org


File objects
============

To open an HDF5 file the recommended way is to use

.. code-block:: python

    with h5py.File('my_file.h5', 'r') as f:
        # interact with the file object

where the first argument is the path to the HDF5 file, and the second one is
the mode in which to open the file. Available modes are

:``r``: readonly, file must exist
:``r+``: read/write, file must exist
:``w``: create file, truncate if exists
:``w-`` or ``x``: create file, fail if exists
:``a``: read/write if exists, create otherwise

with the default filemode being ``a``.

.. danger::

    Similarly to :func:`open` there is another way of opening an HDF5 file:

    .. code-block:: python

        f = h5py.File('my_file.h5', 'r')
        # interact with the file object
        f.close()

    This has the disadvantage that you have to take care of closing the file
    yourself. As the binary nature of HDF5 files essentially means that one
    corrupted bit may lead to *loss of all the data in the file.* We therefore
    strongly recommend the previously mentioned way with the context manager.

Every file object is also an HDF5 group object representing the root group of
the file.


Groups
======

The hierarchical organization of the HDF5 file format is achieved by groups.
Similarly to directories on your regular filesystem they help you with the
organization of your data within an HDF5 file. As mentioned before the file
object returned by the ``File`` initialization. Creating a new group is done by
calling the ``create_group()`` method of an HDF5 ``Group`` object:

.. code-block:: python

    with h5py.File('my_file.h5', 'w') as f:
        print('Name of group:', f.name)
        nested_group = f.create_group('nested group')
        print('Name of nested group:', nested_group.name)
        recursively_created_group = f.create_group('/this/is/deep')
        print(
            'Name of recursively created group:',
            recursively_created_group.name)

Which results in the following output:

.. code-block:: text

    Name of group: /
    Name of nested group: /nested group
    Name of recursively created group: /this/is/deep


Working with files may also be compared to working with :class:`dict` objects,
as they offer the indexing syntax to traverse groups, support iteration and the
``keys()``, ``values()`` and ``items()`` syntax:

.. code-block:: python

    with h5py.File('my_file.h5', 'w') as f:
        f.create_group('/favorite/group/one')
        f.create_group('/favorite/group/two')
        f.create_group('/favorite/group/three')
        group = f['/favorite/group']
        for subgroup_name in sorted(group):
            print(subgroup_name)
        subgroup_one = group['one']
        print(subgroup_one.name)
        for subgroup_name, subgroup in sorted(group.items()):
            print(subgroup_name, subgroup.name)


.. code-block:: text

    one
    three
    two
    /favorite/group/one
    one /favorite/group/one
    three /favorite/group/three
    two /favorite/group/two


Datasets
========

Creating a dataset is done via calling the ``create_dataset`` method on an HDF5
group. Although we can create empty datasets in HDF5 and fill them with data
later on, we much more commonly just want to store data that has been worked on
in a NumPy array. This can be done like this:

.. code-block:: python

    my_array = np.array(5*5*3*3*3).reshape(5, 5, 3, 3, 3)

    with h5py.File('my_file.h5', 'w') as f:
        group = f.create_group('my_group')
        dset = group.create_dataset('my_dataset', data=my_array)

    with h5py.File('my_file.h5', 'r') as f:
        retrieved_array = np.array(f['my_group/my_dataset'])

    print(np.allclose(my_array, retrieved_array))

Which results in the ouptut ``True``. Handling the datatypes is done
automatically both for dumping and loading the data---both for regular and
structured arrays.


Attributes
==========





Datasets
========

.. code-block:: python

    with h5py.File('my_first_hdf5_file.h5') as f:
        f.create_dataset('my_first_dataset', data=my_data)

