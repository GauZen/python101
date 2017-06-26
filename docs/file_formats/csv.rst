.. _sec_comma-separated-values:

**********************
Comma-separated values
**********************

:Filename extension: ``.csv``

We may know comma-separated values (CSV) file mostly by working with people who
use spreadsheet software like Microsoft Excel. As the native file format of
such software might be cumbersome to read, we kindly ask for a CSV export of
those spreadsheets.

Typically a CSV file is a plain text format which contains one record per line
with several delimiter separated fields. The sequence of the fields is the same
for every records.

Note that CSV files are not standardized, and as such a lot of different
flavors exist. The delimiter, for example, does not necessary have to be a
comma, it could also be a simple space. If the delimiter is part of a field
value, for example, in a string, an escape character is required, which depends
on the flavor of the CSV implementation. Comments are also treated differently
in each implementation, with some allowing comments in the header via ``#``,
and others not supporting them at all

Hence, CSV files may be used for very simple files, but may proof unsuitable
for complex data.

Let us take a look at a CSV file that is the result of an atomistic simulation
which is stored in a file:



.. testsetup:: csv_file

    from io import StringIO

    _files = {
        'md_result.csv': StringIO(
            '# Atom types:\n'
            '# - He: Helium\n'
            '# - Ar: Argon\n'
            '# Potentials:\n'
            '# - He: Lennard-Jones potential with epsilon/k_B = 10.22 K, sigma = 256 pm\n'
            '# - Ar: Lennard-Jones potential with epsilon/k_B = 120 K, sigma = 341 pm\n'
            '# Simulation box size: 100 µm x 200 µm x 300 µm\n'
            '# Periodic boundary conditions in all directions\n'
            '# Step: 0\n'
            '# Time: 0 s\n'
            '# All quantities are given in SI units\n'
            'atom_id type x-position y-position z-position x-velocity y-velocity z-velocity\n'
            '0 He 5.7222e-07 4.8811e-09 2.0415e-07 -2.9245e+01 1.0045e+02 1.2828e+02\n'
            '1 He 9.7710e-07 3.6371e-07 4.7311e-07 -1.9926e+02 2.3275e+02 -5.3438e+02\n'
            '2 Ar 6.4989e-07 6.7873e-07 9.5000e-07 -1.5592e+00 -3.7876e+02 8.4091e+01\n'
            '3 Ar 5.9024e-08 3.7138e-07 7.3455e-08 3.4282e+02 1.5682e+02 -3.8991e+01\n'
            '4 He 7.6746e-07 8.3017e-08 4.8520e-07 -3.0450e+01 -3.7975e+02 -3.3632e+02\n'
            '5 Ar 1.7226e-07 4.6023e-07 4.7356e-08 -3.1151e+02 -4.2939e+02 -6.9474e+02\n'
            '6 Ar 9.6394e-07 7.2845e-07 8.8623e-07 -8.2636e+01 4.5098e+01 -1.0626e+01\n'
            '7 He 5.4450e-07 4.6373e-07 6.2270e-07 1.5889e+02 2.5858e+02 -1.5150e+02\n'
            '8 He 7.9322e-07 9.4700e-07 3.5194e-08 -1.9703e+02 1.5674e+02 -1.8520e+02\n'
            '9 Ar 2.7797e-07 1.6487e-07 8.2403e-07 -3.8650e+01 -6.9632e+02 2.1642e+02\n'
            '10 He 1.1842e-07 6.3244e-07 5.0958e-07 -1.4963e+02 4.2288e+02 -7.6309e+01\n'
            '11 Ar 2.0359e-07 8.3369e-07 9.6348e-07 4.8457e+02 -2.6741e+02 -3.5254e+02\n'
            '12 He 5.1019e-07 2.2470e-07 2.3846e-08 -2.3192e+02 -9.9510e+01 3.2770e+01\n'
            '13 Ar 3.5383e-07 8.4581e-07 7.2340e-07 -3.0395e+02 4.7316e+01 2.2253e+02\n'
            '14 He 3.8515e-07 2.8940e-07 5.6028e-07 2.3308e+02 2.5418e+02 4.2983e+02\n'
            '15 He 1.5842e-07 9.8225e-07 5.7859e-07 1.9963e+02 2.0311e+02 -4.2560e+02\n'
            '16 He 3.6831e-07 7.6520e-07 2.9884e-07 6.6341e+01 2.2232e+02 -9.7653e+01\n'
            '17 He 2.8696e-07 1.5129e-07 6.4060e-07 9.0358e+01 -6.7459e+01 -6.4782e+01\n'
            '18 He 1.0325e-07 9.9012e-07 3.4381e-07 7.1108e+01 1.1060e+01 1.5912e+01\n'
            '19 Ar 4.3929e-07 7.5363e-07 9.9974e-07 2.3919e+02 1.7383e+02 3.3529e+02')
    }

    class open:
        def __init__(
                self, file, mode='r', buffering=-1, encoding=None, errors=None,
                newline=None, closefd=True, opener=None):
            try:
                self.stringio = _files[file]
            except KeyError:
                self.stringio = StringIO()

        def read(self, size=None):
            return self.stringio.read(size)

        def write(self, s):
            return self.stringio.write(s)

        def close(self):
            self.stringio.seek(0)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.close()

        def __iter__(self):
            return self.stringio

        def __next__(self):
            return next(self.stringio)


.. testcode:: csv_file

    with open('md_result.csv', 'r') as f:
        print(f.read())


.. testoutput:: csv_file

    # Atom types:
    # - He: Helium
    # - Ar: Argon
    # Potentials:
    # - He: Lennard-Jones potential with epsilon/k_B = 10.22 K, sigma = 256 pm
    # - Ar: Lennard-Jones potential with epsilon/k_B = 120 K, sigma = 341 pm
    # Simulation box size: 100 µm x 200 µm x 300 µm
    # Periodic boundary conditions in all directions
    # Step: 0
    # Time: 0 s
    # All quantities are given in SI units
    atom_id type x-position y-position z-position x-velocity y-velocity z-velocity
    0 He 5.7222e-07 4.8811e-09 2.0415e-07 -2.9245e+01 1.0045e+02 1.2828e+02
    1 He 9.7710e-07 3.6371e-07 4.7311e-07 -1.9926e+02 2.3275e+02 -5.3438e+02
    2 Ar 6.4989e-07 6.7873e-07 9.5000e-07 -1.5592e+00 -3.7876e+02 8.4091e+01
    3 Ar 5.9024e-08 3.7138e-07 7.3455e-08 3.4282e+02 1.5682e+02 -3.8991e+01
    4 He 7.6746e-07 8.3017e-08 4.8520e-07 -3.0450e+01 -3.7975e+02 -3.3632e+02
    5 Ar 1.7226e-07 4.6023e-07 4.7356e-08 -3.1151e+02 -4.2939e+02 -6.9474e+02
    6 Ar 9.6394e-07 7.2845e-07 8.8623e-07 -8.2636e+01 4.5098e+01 -1.0626e+01
    7 He 5.4450e-07 4.6373e-07 6.2270e-07 1.5889e+02 2.5858e+02 -1.5150e+02
    8 He 7.9322e-07 9.4700e-07 3.5194e-08 -1.9703e+02 1.5674e+02 -1.8520e+02
    9 Ar 2.7797e-07 1.6487e-07 8.2403e-07 -3.8650e+01 -6.9632e+02 2.1642e+02
    10 He 1.1842e-07 6.3244e-07 5.0958e-07 -1.4963e+02 4.2288e+02 -7.6309e+01
    11 Ar 2.0359e-07 8.3369e-07 9.6348e-07 4.8457e+02 -2.6741e+02 -3.5254e+02
    12 He 5.1019e-07 2.2470e-07 2.3846e-08 -2.3192e+02 -9.9510e+01 3.2770e+01
    13 Ar 3.5383e-07 8.4581e-07 7.2340e-07 -3.0395e+02 4.7316e+01 2.2253e+02
    14 He 3.8515e-07 2.8940e-07 5.6028e-07 2.3308e+02 2.5418e+02 4.2983e+02
    15 He 1.5842e-07 9.8225e-07 5.7859e-07 1.9963e+02 2.0311e+02 -4.2560e+02
    16 He 3.6831e-07 7.6520e-07 2.9884e-07 6.6341e+01 2.2232e+02 -9.7653e+01
    17 He 2.8696e-07 1.5129e-07 6.4060e-07 9.0358e+01 -6.7459e+01 -6.4782e+01
    18 He 1.0325e-07 9.9012e-07 3.4381e-07 7.1108e+01 1.1060e+01 1.5912e+01
    19 Ar 4.3929e-07 7.5363e-07 9.9974e-07 2.3919e+02 1.7383e+02 3.3529e+02

Note that the first row that is not a comment holds the field names. This will
be important for later. Using the :mod:`csv` from the Python standard library
we can read it in nicely:

.. testcode:: csv_file

    import csv

    number_of_rows_to_skip = 12
    with open('md_result.csv', 'r', newline='') as f:
        # skip the first rows
        for _ in range(number_of_rows_to_skip):
            next(f)

        csv_reader = csv.reader(f, delimiter=' ')
        for row in csv_reader:
            print(row)

Which then results in the following output:

.. testoutput:: csv_file

    ['0', 'He', '5.7222e-07', '4.8811e-09', '2.0415e-07', '-2.9245e+01', '1.0045e+02', '1.2828e+02']
    ['1', 'He', '9.7710e-07', '3.6371e-07', '4.7311e-07', '-1.9926e+02', '2.3275e+02', '-5.3438e+02']
    ['2', 'Ar', '6.4989e-07', '6.7873e-07', '9.5000e-07', '-1.5592e+00', '-3.7876e+02', '8.4091e+01']
    ['3', 'Ar', '5.9024e-08', '3.7138e-07', '7.3455e-08', '3.4282e+02', '1.5682e+02', '-3.8991e+01']
    ['4', 'He', '7.6746e-07', '8.3017e-08', '4.8520e-07', '-3.0450e+01', '-3.7975e+02', '-3.3632e+02']
    ['5', 'Ar', '1.7226e-07', '4.6023e-07', '4.7356e-08', '-3.1151e+02', '-4.2939e+02', '-6.9474e+02']
    ['6', 'Ar', '9.6394e-07', '7.2845e-07', '8.8623e-07', '-8.2636e+01', '4.5098e+01', '-1.0626e+01']
    ['7', 'He', '5.4450e-07', '4.6373e-07', '6.2270e-07', '1.5889e+02', '2.5858e+02', '-1.5150e+02']
    ['8', 'He', '7.9322e-07', '9.4700e-07', '3.5194e-08', '-1.9703e+02', '1.5674e+02', '-1.8520e+02']
    ['9', 'Ar', '2.7797e-07', '1.6487e-07', '8.2403e-07', '-3.8650e+01', '-6.9632e+02', '2.1642e+02']
    ['10', 'He', '1.1842e-07', '6.3244e-07', '5.0958e-07', '-1.4963e+02', '4.2288e+02', '-7.6309e+01']
    ['11', 'Ar', '2.0359e-07', '8.3369e-07', '9.6348e-07', '4.8457e+02', '-2.6741e+02', '-3.5254e+02']
    ['12', 'He', '5.1019e-07', '2.2470e-07', '2.3846e-08', '-2.3192e+02', '-9.9510e+01', '3.2770e+01']
    ['13', 'Ar', '3.5383e-07', '8.4581e-07', '7.2340e-07', '-3.0395e+02', '4.7316e+01', '2.2253e+02']
    ['14', 'He', '3.8515e-07', '2.8940e-07', '5.6028e-07', '2.3308e+02', '2.5418e+02', '4.2983e+02']
    ['15', 'He', '1.5842e-07', '9.8225e-07', '5.7859e-07', '1.9963e+02', '2.0311e+02', '-4.2560e+02']
    ['16', 'He', '3.6831e-07', '7.6520e-07', '2.9884e-07', '6.6341e+01', '2.2232e+02', '-9.7653e+01']
    ['17', 'He', '2.8696e-07', '1.5129e-07', '6.4060e-07', '9.0358e+01', '-6.7459e+01', '-6.4782e+01']
    ['18', 'He', '1.0325e-07', '9.9012e-07', '3.4381e-07', '7.1108e+01', '1.1060e+01', '1.5912e+01']
    ['19', 'Ar', '4.3929e-07', '7.5363e-07', '9.9974e-07', '2.3919e+02', '1.7383e+02', '3.3529e+02']

But as you can see all the numbers are read in as strings. This is due to CSV
files not preserving the type information. A quick hack might be the following:

.. testcode:: csv_file

    import csv

    number_of_rows_to_skip = 12
    possible_types = (int, float, str)

    with open('md_result.csv', 'r', newline='') as f:
        # skip the first rows
        for _ in range(number_of_rows_to_skip):
            next(f)

        csv_reader = csv.reader(f, delimiter=' ')
        for row in csv_reader:
            for i, entry in enumerate(row):
                for possible_type in possible_types:
                    try:
                        entry = possible_type(entry)
                    except ValueError:
                        continue
                    except:
                        raise
                    else:
                        row[i] = entry
                        break
            print(row)

Here we define an order of types to check for, in this example we first check
whether the entry can be cast to an integer, then to a float, and then to a
string. If a casting operation succeeds, we set the entry of the row to the new
value and exit the loop that checks for the types. Now the output is closer to
what we would like.

.. testoutput:: csv_file

    [0, 'He', 5.7222e-07, 4.8811e-09, 2.0415e-07, -29.245, 100.45, 128.28]
    [1, 'He', 9.771e-07, 3.6371e-07, 4.7311e-07, -199.26, 232.75, -534.38]
    [2, 'Ar', 6.4989e-07, 6.7873e-07, 9.5e-07, -1.5592, -378.76, 84.091]
    [3, 'Ar', 5.9024e-08, 3.7138e-07, 7.3455e-08, 342.82, 156.82, -38.991]
    [4, 'He', 7.6746e-07, 8.3017e-08, 4.852e-07, -30.45, -379.75, -336.32]
    [5, 'Ar', 1.7226e-07, 4.6023e-07, 4.7356e-08, -311.51, -429.39, -694.74]
    [6, 'Ar', 9.6394e-07, 7.2845e-07, 8.8623e-07, -82.636, 45.098, -10.626]
    [7, 'He', 5.445e-07, 4.6373e-07, 6.227e-07, 158.89, 258.58, -151.5]
    [8, 'He', 7.9322e-07, 9.47e-07, 3.5194e-08, -197.03, 156.74, -185.2]
    [9, 'Ar', 2.7797e-07, 1.6487e-07, 8.2403e-07, -38.65, -696.32, 216.42]
    [10, 'He', 1.1842e-07, 6.3244e-07, 5.0958e-07, -149.63, 422.88, -76.309]
    [11, 'Ar', 2.0359e-07, 8.3369e-07, 9.6348e-07, 484.57, -267.41, -352.54]
    [12, 'He', 5.1019e-07, 2.247e-07, 2.3846e-08, -231.92, -99.51, 32.77]
    [13, 'Ar', 3.5383e-07, 8.4581e-07, 7.234e-07, -303.95, 47.316, 222.53]
    [14, 'He', 3.8515e-07, 2.894e-07, 5.6028e-07, 233.08, 254.18, 429.83]
    [15, 'He', 1.5842e-07, 9.8225e-07, 5.7859e-07, 199.63, 203.11, -425.6]
    [16, 'He', 3.6831e-07, 7.652e-07, 2.9884e-07, 66.341, 222.32, -97.653]
    [17, 'He', 2.8696e-07, 1.5129e-07, 6.406e-07, 90.358, -67.459, -64.782]
    [18, 'He', 1.0325e-07, 9.9012e-07, 3.4381e-07, 71.108, 11.06, 15.912]
    [19, 'Ar', 4.3929e-07, 7.5363e-07, 9.9974e-07, 239.19, 173.83, 335.29]

But programming with this still requires you to know exactly which field number
corresponds to which entry. And maybe your format may differ from file to file,
so that your hardcoded indices lead to wrong results. It would be better if we
could somehow access the fields by names, e.g., ``row['id']`` to get the id of
the record. This is where :class:`csv.DictReader` comes in.

.. doctest:: csv_file
    :pyversion: >= 3.6

    >>> import csv
    >>> number_of_rows_to_skip = 11
    >>> with open('md_result.csv', 'r', newline='') as f:
    ...     # skip the first rows
    ...     for _ in range(number_of_rows_to_skip):
    ...         next(f)
    ...
    ...     csv_reader = csv.DictReader(f, delimiter=' ')
    ...     for row in csv_reader:
    ...         print(row)
    ...
    OrderedDict([('atom_id', '0'), ('type', 'He'), ('x-position', '5.7222e-07'), ('y-position', '4.8811e-09'), ('z-position', '2.0415e-07'), ('x-velocity', '-2.9245e+01'), ('y-velocity', '1.0045e+02'), ('z-velocity', '1.2828e+02')])
    OrderedDict([('atom_id', '1'), ('type', 'He'), ('x-position', '9.7710e-07'), ('y-position', '3.6371e-07'), ('z-position', '4.7311e-07'), ('x-velocity', '-1.9926e+02'), ('y-velocity', '2.3275e+02'), ('z-velocity', '-5.3438e+02')])
    OrderedDict([('atom_id', '2'), ('type', 'Ar'), ('x-position', '6.4989e-07'), ('y-position', '6.7873e-07'), ('z-position', '9.5000e-07'), ('x-velocity', '-1.5592e+00'), ('y-velocity', '-3.7876e+02'), ('z-velocity', '8.4091e+01')])
    OrderedDict([('atom_id', '3'), ('type', 'Ar'), ('x-position', '5.9024e-08'), ('y-position', '3.7138e-07'), ('z-position', '7.3455e-08'), ('x-velocity', '3.4282e+02'), ('y-velocity', '1.5682e+02'), ('z-velocity', '-3.8991e+01')])
    OrderedDict([('atom_id', '4'), ('type', 'He'), ('x-position', '7.6746e-07'), ('y-position', '8.3017e-08'), ('z-position', '4.8520e-07'), ('x-velocity', '-3.0450e+01'), ('y-velocity', '-3.7975e+02'), ('z-velocity', '-3.3632e+02')])
    OrderedDict([('atom_id', '5'), ('type', 'Ar'), ('x-position', '1.7226e-07'), ('y-position', '4.6023e-07'), ('z-position', '4.7356e-08'), ('x-velocity', '-3.1151e+02'), ('y-velocity', '-4.2939e+02'), ('z-velocity', '-6.9474e+02')])
    OrderedDict([('atom_id', '6'), ('type', 'Ar'), ('x-position', '9.6394e-07'), ('y-position', '7.2845e-07'), ('z-position', '8.8623e-07'), ('x-velocity', '-8.2636e+01'), ('y-velocity', '4.5098e+01'), ('z-velocity', '-1.0626e+01')])
    OrderedDict([('atom_id', '7'), ('type', 'He'), ('x-position', '5.4450e-07'), ('y-position', '4.6373e-07'), ('z-position', '6.2270e-07'), ('x-velocity', '1.5889e+02'), ('y-velocity', '2.5858e+02'), ('z-velocity', '-1.5150e+02')])
    OrderedDict([('atom_id', '8'), ('type', 'He'), ('x-position', '7.9322e-07'), ('y-position', '9.4700e-07'), ('z-position', '3.5194e-08'), ('x-velocity', '-1.9703e+02'), ('y-velocity', '1.5674e+02'), ('z-velocity', '-1.8520e+02')])
    OrderedDict([('atom_id', '9'), ('type', 'Ar'), ('x-position', '2.7797e-07'), ('y-position', '1.6487e-07'), ('z-position', '8.2403e-07'), ('x-velocity', '-3.8650e+01'), ('y-velocity', '-6.9632e+02'), ('z-velocity', '2.1642e+02')])
    OrderedDict([('atom_id', '10'), ('type', 'He'), ('x-position', '1.1842e-07'), ('y-position', '6.3244e-07'), ('z-position', '5.0958e-07'), ('x-velocity', '-1.4963e+02'), ('y-velocity', '4.2288e+02'), ('z-velocity', '-7.6309e+01')])
    OrderedDict([('atom_id', '11'), ('type', 'Ar'), ('x-position', '2.0359e-07'), ('y-position', '8.3369e-07'), ('z-position', '9.6348e-07'), ('x-velocity', '4.8457e+02'), ('y-velocity', '-2.6741e+02'), ('z-velocity', '-3.5254e+02')])
    OrderedDict([('atom_id', '12'), ('type', 'He'), ('x-position', '5.1019e-07'), ('y-position', '2.2470e-07'), ('z-position', '2.3846e-08'), ('x-velocity', '-2.3192e+02'), ('y-velocity', '-9.9510e+01'), ('z-velocity', '3.2770e+01')])
    OrderedDict([('atom_id', '13'), ('type', 'Ar'), ('x-position', '3.5383e-07'), ('y-position', '8.4581e-07'), ('z-position', '7.2340e-07'), ('x-velocity', '-3.0395e+02'), ('y-velocity', '4.7316e+01'), ('z-velocity', '2.2253e+02')])
    OrderedDict([('atom_id', '14'), ('type', 'He'), ('x-position', '3.8515e-07'), ('y-position', '2.8940e-07'), ('z-position', '5.6028e-07'), ('x-velocity', '2.3308e+02'), ('y-velocity', '2.5418e+02'), ('z-velocity', '4.2983e+02')])
    OrderedDict([('atom_id', '15'), ('type', 'He'), ('x-position', '1.5842e-07'), ('y-position', '9.8225e-07'), ('z-position', '5.7859e-07'), ('x-velocity', '1.9963e+02'), ('y-velocity', '2.0311e+02'), ('z-velocity', '-4.2560e+02')])
    OrderedDict([('atom_id', '16'), ('type', 'He'), ('x-position', '3.6831e-07'), ('y-position', '7.6520e-07'), ('z-position', '2.9884e-07'), ('x-velocity', '6.6341e+01'), ('y-velocity', '2.2232e+02'), ('z-velocity', '-9.7653e+01')])
    OrderedDict([('atom_id', '17'), ('type', 'He'), ('x-position', '2.8696e-07'), ('y-position', '1.5129e-07'), ('z-position', '6.4060e-07'), ('x-velocity', '9.0358e+01'), ('y-velocity', '-6.7459e+01'), ('z-velocity', '-6.4782e+01')])
    OrderedDict([('atom_id', '18'), ('type', 'He'), ('x-position', '1.0325e-07'), ('y-position', '9.9012e-07'), ('z-position', '3.4381e-07'), ('x-velocity', '7.1108e+01'), ('y-velocity', '1.1060e+01'), ('z-velocity', '1.5912e+01')])
    OrderedDict([('atom_id', '19'), ('type', 'Ar'), ('x-position', '4.3929e-07'), ('y-position', '7.5363e-07'), ('z-position', '9.9974e-07'), ('x-velocity', '2.3919e+02'), ('y-velocity', '1.7383e+02'), ('z-velocity', '3.3529e+02')])

.. note::

    If you are not using at least Python 3.6 the :class:`~csv.DictReader`
    returns regular :class:`dict` instead of its ordered variant,
    :class:`~collections.OrderedDict`.

Now that the fields are in an :class:`~collections.OrderedDict`, the routine to
cast the field entries is slightly different:

.. doctest:: csv_file
    :pyversion: >= 3.6

    >>> number_of_rows_to_skip = 11
    >>> with open('md_result.csv', 'r', newline='') as f:
    ...     # skip the first rows
    ...     for _ in range(number_of_rows_to_skip):
    ...         next(f)
    ...
    ...     csv_reader = csv.DictReader(f, delimiter=' ')
    ...     for row in csv_reader:
    ...         for key, entry in row.items():
    ...             for possible_type in possible_types:
    ...                 try:
    ...                     entry = possible_type(entry)
    ...                 except ValueError:
    ...                     continue
    ...                 except:
    ...                     raise
    ...                 else:
    ...                     row[key] = entry
    ...                     break
    ...         print(row)
    ...
    OrderedDict([('atom_id', 0), ('type', 'He'), ('x-position', 5.7222e-07), ('y-position', 4.8811e-09), ('z-position', 2.0415e-07), ('x-velocity', -29.245), ('y-velocity', 100.45), ('z-velocity', 128.28)])
    OrderedDict([('atom_id', 1), ('type', 'He'), ('x-position', 9.771e-07), ('y-position', 3.6371e-07), ('z-position', 4.7311e-07), ('x-velocity', -199.26), ('y-velocity', 232.75), ('z-velocity', -534.38)])
    OrderedDict([('atom_id', 2), ('type', 'Ar'), ('x-position', 6.4989e-07), ('y-position', 6.7873e-07), ('z-position', 9.5e-07), ('x-velocity', -1.5592), ('y-velocity', -378.76), ('z-velocity', 84.091)])
    OrderedDict([('atom_id', 3), ('type', 'Ar'), ('x-position', 5.9024e-08), ('y-position', 3.7138e-07), ('z-position', 7.3455e-08), ('x-velocity', 342.82), ('y-velocity', 156.82), ('z-velocity', -38.991)])
    OrderedDict([('atom_id', 4), ('type', 'He'), ('x-position', 7.6746e-07), ('y-position', 8.3017e-08), ('z-position', 4.852e-07), ('x-velocity', -30.45), ('y-velocity', -379.75), ('z-velocity', -336.32)])
    OrderedDict([('atom_id', 5), ('type', 'Ar'), ('x-position', 1.7226e-07), ('y-position', 4.6023e-07), ('z-position', 4.7356e-08), ('x-velocity', -311.51), ('y-velocity', -429.39), ('z-velocity', -694.74)])
    OrderedDict([('atom_id', 6), ('type', 'Ar'), ('x-position', 9.6394e-07), ('y-position', 7.2845e-07), ('z-position', 8.8623e-07), ('x-velocity', -82.636), ('y-velocity', 45.098), ('z-velocity', -10.626)])
    OrderedDict([('atom_id', 7), ('type', 'He'), ('x-position', 5.445e-07), ('y-position', 4.6373e-07), ('z-position', 6.227e-07), ('x-velocity', 158.89), ('y-velocity', 258.58), ('z-velocity', -151.5)])
    OrderedDict([('atom_id', 8), ('type', 'He'), ('x-position', 7.9322e-07), ('y-position', 9.47e-07), ('z-position', 3.5194e-08), ('x-velocity', -197.03), ('y-velocity', 156.74), ('z-velocity', -185.2)])
    OrderedDict([('atom_id', 9), ('type', 'Ar'), ('x-position', 2.7797e-07), ('y-position', 1.6487e-07), ('z-position', 8.2403e-07), ('x-velocity', -38.65), ('y-velocity', -696.32), ('z-velocity', 216.42)])
    OrderedDict([('atom_id', 10), ('type', 'He'), ('x-position', 1.1842e-07), ('y-position', 6.3244e-07), ('z-position', 5.0958e-07), ('x-velocity', -149.63), ('y-velocity', 422.88), ('z-velocity', -76.309)])
    OrderedDict([('atom_id', 11), ('type', 'Ar'), ('x-position', 2.0359e-07), ('y-position', 8.3369e-07), ('z-position', 9.6348e-07), ('x-velocity', 484.57), ('y-velocity', -267.41), ('z-velocity', -352.54)])
    OrderedDict([('atom_id', 12), ('type', 'He'), ('x-position', 5.1019e-07), ('y-position', 2.247e-07), ('z-position', 2.3846e-08), ('x-velocity', -231.92), ('y-velocity', -99.51), ('z-velocity', 32.77)])
    OrderedDict([('atom_id', 13), ('type', 'Ar'), ('x-position', 3.5383e-07), ('y-position', 8.4581e-07), ('z-position', 7.234e-07), ('x-velocity', -303.95), ('y-velocity', 47.316), ('z-velocity', 222.53)])
    OrderedDict([('atom_id', 14), ('type', 'He'), ('x-position', 3.8515e-07), ('y-position', 2.894e-07), ('z-position', 5.6028e-07), ('x-velocity', 233.08), ('y-velocity', 254.18), ('z-velocity', 429.83)])
    OrderedDict([('atom_id', 15), ('type', 'He'), ('x-position', 1.5842e-07), ('y-position', 9.8225e-07), ('z-position', 5.7859e-07), ('x-velocity', 199.63), ('y-velocity', 203.11), ('z-velocity', -425.6)])
    OrderedDict([('atom_id', 16), ('type', 'He'), ('x-position', 3.6831e-07), ('y-position', 7.652e-07), ('z-position', 2.9884e-07), ('x-velocity', 66.341), ('y-velocity', 222.32), ('z-velocity', -97.653)])
    OrderedDict([('atom_id', 17), ('type', 'He'), ('x-position', 2.8696e-07), ('y-position', 1.5129e-07), ('z-position', 6.406e-07), ('x-velocity', 90.358), ('y-velocity', -67.459), ('z-velocity', -64.782)])
    OrderedDict([('atom_id', 18), ('type', 'He'), ('x-position', 1.0325e-07), ('y-position', 9.9012e-07), ('z-position', 3.4381e-07), ('x-velocity', 71.108), ('y-velocity', 11.06), ('z-velocity', 15.912)])
    OrderedDict([('atom_id', 19), ('type', 'Ar'), ('x-position', 4.3929e-07), ('y-position', 7.5363e-07), ('z-position', 9.9974e-07), ('x-velocity', 239.19), ('y-velocity', 173.83), ('z-velocity', 335.29)])

As long as the field names are consistent across files you can write code that
needs less maintenance.

Another way of reading CSV files is by using the :func:`~numpy.loadtxt`
function of NumPy. By specifying the data type as you would for
:ref:`structured_arrays` the type conversion is done for you, while retaining
the dictionary like behavior. You can also specify a comment character that
should be ignored and the amount of rows to skip:

.. testcode:: csv_file

    csv_dtype = [
        ('atom_id', np.int32),
        ('type', np.string_, 2),
        ('position', np.float64, 3),
        ('velocity', np.float64, 3)
    ]
    with open('md_result.csv', 'r') as f:
        md_data = np.loadtxt(f, dtype=csv_dtype, skiprows=12)
    print(md_data)

.. testoutput:: csv_file

    [ ( 0, b'He', [  5.72220000e-07,   4.88110000e-09,   2.04150000e-07], [ -29.245 ,  100.45  ,  128.28  ])
     ( 1, b'He', [  9.77100000e-07,   3.63710000e-07,   4.73110000e-07], [-199.26  ,  232.75  , -534.38  ])
     ( 2, b'Ar', [  6.49890000e-07,   6.78730000e-07,   9.50000000e-07], [  -1.5592, -378.76  ,   84.091 ])
     ( 3, b'Ar', [  5.90240000e-08,   3.71380000e-07,   7.34550000e-08], [ 342.82  ,  156.82  ,  -38.991 ])
     ( 4, b'He', [  7.67460000e-07,   8.30170000e-08,   4.85200000e-07], [ -30.45  , -379.75  , -336.32  ])
     ( 5, b'Ar', [  1.72260000e-07,   4.60230000e-07,   4.73560000e-08], [-311.51  , -429.39  , -694.74  ])
     ( 6, b'Ar', [  9.63940000e-07,   7.28450000e-07,   8.86230000e-07], [ -82.636 ,   45.098 ,  -10.626 ])
     ( 7, b'He', [  5.44500000e-07,   4.63730000e-07,   6.22700000e-07], [ 158.89  ,  258.58  , -151.5   ])
     ( 8, b'He', [  7.93220000e-07,   9.47000000e-07,   3.51940000e-08], [-197.03  ,  156.74  , -185.2   ])
     ( 9, b'Ar', [  2.77970000e-07,   1.64870000e-07,   8.24030000e-07], [ -38.65  , -696.32  ,  216.42  ])
     (10, b'He', [  1.18420000e-07,   6.32440000e-07,   5.09580000e-07], [-149.63  ,  422.88  ,  -76.309 ])
     (11, b'Ar', [  2.03590000e-07,   8.33690000e-07,   9.63480000e-07], [ 484.57  , -267.41  , -352.54  ])
     (12, b'He', [  5.10190000e-07,   2.24700000e-07,   2.38460000e-08], [-231.92  ,  -99.51  ,   32.77  ])
     (13, b'Ar', [  3.53830000e-07,   8.45810000e-07,   7.23400000e-07], [-303.95  ,   47.316 ,  222.53  ])
     (14, b'He', [  3.85150000e-07,   2.89400000e-07,   5.60280000e-07], [ 233.08  ,  254.18  ,  429.83  ])
     (15, b'He', [  1.58420000e-07,   9.82250000e-07,   5.78590000e-07], [ 199.63  ,  203.11  , -425.6   ])
     (16, b'He', [  3.68310000e-07,   7.65200000e-07,   2.98840000e-07], [  66.341 ,  222.32  ,  -97.653 ])
     (17, b'He', [  2.86960000e-07,   1.51290000e-07,   6.40600000e-07], [  90.358 ,  -67.459 ,  -64.782 ])
     (18, b'He', [  1.03250000e-07,   9.90120000e-07,   3.43810000e-07], [  71.108 ,   11.06  ,   15.912 ])
     (19, b'Ar', [  4.39290000e-07,   7.53630000e-07,   9.99740000e-07], [ 239.19  ,  173.83  ,  335.29  ])]

So this makes it really convenient to work with, e.g., the velocity may easily
be computed like this:

.. testcode:: csv_file

    print(np.linalg.norm(md_data['velocity'], axis=1))

With the output

.. testoutput:: csv_file

    [ 165.53317168  615.98627785  387.98565049  378.99652094  508.18147093
      874.11550713   94.73885146  339.20775124  312.54965765  730.20064455
      455.01614782  656.20167982  254.48575481  379.66301803  551.07856763
      512.09488281  251.72091508  130.04611632   73.70117372  447.04374406]
