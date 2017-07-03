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

As the data we store tends to get quite large we can leverage the compression
options HDF5 offers. H5Py makes keeps this simple and enables compression when
a ``compression`` keyword is supplied, followed by a number in the range of 1
to 9 indicating the cpu-time/compression trade-off, from "least compression" to
"densest compression."

.. code-block:: python

    my_array = np.array(5*5*3*3*3).reshape(5, 5, 3, 3, 3)

    with h5py.File('my_file.h5', 'w') as f:
        group = f.create_group('my_group')
        dset = group.create_dataset('my_dataset', data=my_array, compression=9)


Attributes
==========

Each group and dataset may have attributes. Attributes are metadata that can be
assigned in a dictionary-like fashion using the ``attributes`` attribute of the
group or dataset object.

.. code-block:: python

    md_dtype = [
        ('atom_id', np.int32),
        ('type', np.string_, 2),
        ('position', np.float64, 3),
        ('velocity', np.float64, 3)
    ]
    md_data = np.array(
        [
            (0, 'He', (5.7222e-07, 4.8811e-09, 2.0415e-07), (-29.245, 100.45, 128.28))
            (1, 'He', (9.7710e-07, 3.6371e-07, 4.7311e-07), (-199.26, 232.75, -534.38))
            (2, 'Ar', (6.4989e-07, 6.7873e-07, 9.5000e-07), (-1.5592, -378.76, 84.091))
            (3, 'Ar', (5.9024e-08, 3.7138e-07, 7.3455e-08), (342.82, 156.82, -38.991))
            (4, 'He', (7.6746e-07, 8.3017e-08, 4.8520e-07), (-30.45, -379.75, -336.32))
            (5, 'Ar', (1.7226e-07, 4.6023e-07, 4.7356e-08), (-311.51, -429.39, -694.74))
            (6, 'Ar', (9.6394e-07, 7.2845e-07, 8.8623e-07), (-82.636, 45.098, -10.626))
            (7, 'He', (5.4450e-07, 4.6373e-07, 6.2270e-07), (158.89, 258.58, -151.5))
            (8, 'He', (7.9322e-07, 9.4700e-07, 3.5194e-08), (-197.03, 156.74, -185.2))
            (9, 'Ar', (2.7797e-07, 1.6487e-07, 8.2403e-07), (-38.65, -696.32, 216.42))
            (10, 'He', (1.1842e-07, 6.3244e-07, 5.0958e-07), (-149.63, 422.88, -76.309))
            (11, 'Ar', (2.0359e-07, 8.3369e-07, 9.6348e-07), (484.57, -267.41, -352.54))
            (12, 'He', (5.1019e-07, 2.2470e-07, 2.3846e-08), (-231.92, -99.51, 32.77))
            (13, 'Ar', (3.5383e-07, 8.4581e-07, 7.2340e-07), (-303.95, 47.316, 222.53))
            (14, 'He', (3.8515e-07, 2.8940e-07, 5.6028e-07), (233.08, 254.18, 429.83))
            (15, 'He', (1.5842e-07, 9.8225e-07, 5.7859e-07), (199.63, 203.11, -425.6))
            (16, 'He', (3.6831e-07, 7.6520e-07, 2.9884e-07), (66.341, 222.32, -97.653))
            (17, 'He', (2.8696e-07, 1.5129e-07, 6.4060e-07), (90.358, -67.459, -64.782))
            (18, 'He', (1.0325e-07, 9.9012e-07, 3.4381e-07), (71.108, 11.06, 15.912))
            (19, 'Ar', (4.3929e-07, 7.5363e-07, 9.9974e-07), (239.19, 173.83, 335.29))
        ],
        dtype=md_dtype)
    # - He: Lennard-Jones potential with epsilon/k_B = 10.22 K, sigma = 256 pm
    # - Ar: Lennard-Jones potential with epsilon/k_B = 120 K, sigma = 341 pm
    with h5py.File('md_results.h5') as f:
        f.attrs['units'] = 'All quantities are in SI units.'
        f.attrs['atom-types'] = np.array(
            [
                ('He', 'Helium'),
                ('Ar', 'Argon')
            ],
            dtype=[(), ()])
        f.attrs['He potential'] = 'Lennard-Jones'
        f.attrs['Ar potential'] = 'Lennard-Jones'
        f.attrs['system size'] = np.array([100e-6, 200e-6, 300e-6])
        f.attrs['boundary conditions'] = np.array(
            ['periodic', 'periodic', 'periodic'])
        dset = f.create_dataset('0000', data=md_data, compression=9)
        dset.attrs['step'] = 0
        dset.attrs['time'] = 0

