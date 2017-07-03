.. _sec_javascript-object-notation:

**************************
JavaScript Object Notation
**************************

:Filename extension: ``.json``

The JavaScript Object Notation (JSON) format was derived from JavaScript. It
is, however, a language-independent format with many programming languages
offering support for simple generation and parsing of JSON files, among them
Python.

.. testsetup:: json_file

    from io import StringIO

    _files = {
        'md_result.json': StringIO(
            '{\n'
            '  "potentials": {\n'
            '    "Ar": {\n'
            '      "type": "Lennard-Jones",\n'
            '      "parameters": {\n'
            '        "sigma": {\n'
            '          "unit": "pm",\n'
            '          "magnitude": 341\n'
            '        },\n'
            '        "epsilon/k_B": {\n'
            '          "unit": "K",\n'
            '          "magnitude": 120\n'
            '        }\n'
            '      }\n'
            '    },\n'
            '    "He": {\n'
            '      "type": "Lennard-Jones",\n'
            '      "parameters": {\n'
            '        "sigma": {\n'
            '          "unit": "pm",\n'
            '          "magnitude": "256"\n'
            '        },\n'
            '        "epsilon/k_B": {\n'
            '          "unit": "K",\n'
            '          "magnitude": "10.22"\n'
            '        }\n'
            '      }\n'
            '    }\n'
            '  },\n'
            '  "atoms": [\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        -29.245,\n'
            '        100.45,\n'
            '        128.28\n'
            '      ],\n'
            '      "atom_id": 0,\n'
            '      "position": [\n'
            '        5.7222e-07,\n'
            '        4.8811e-09,\n'
            '        2.0415e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        -199.26,\n'
            '        232.75,\n'
            '        -534.38\n'
            '      ],\n'
            '      "atom_id": 1,\n'
            '      "position": [\n'
            '        9.771e-07,\n'
            '        3.6371e-07,\n'
            '        4.7311e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "Ar",\n'
            '      "velocity": [\n'
            '        -1.5592,\n'
            '        -378.76,\n'
            '        84.091\n'
            '      ],\n'
            '      "atom_id": 2,\n'
            '      "position": [\n'
            '        6.4989e-07,\n'
            '        6.7873e-07,\n'
            '        9.5e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "Ar",\n'
            '      "velocity": [\n'
            '        342.82,\n'
            '        156.82,\n'
            '        -38.991\n'
            '      ],\n'
            '      "atom_id": 3,\n'
            '      "position": [\n'
            '        5.9024e-08,\n'
            '        3.7138e-07,\n'
            '        7.3455e-08\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        -30.45,\n'
            '        -379.75,\n'
            '        -336.32\n'
            '      ],\n'
            '      "atom_id": 4,\n'
            '      "position": [\n'
            '        7.6746e-07,\n'
            '        8.3017e-08,\n'
            '        4.852e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "Ar",\n'
            '      "velocity": [\n'
            '        -311.51,\n'
            '        -429.39,\n'
            '        -694.74\n'
            '      ],\n'
            '      "atom_id": 5,\n'
            '      "position": [\n'
            '        1.7226e-07,\n'
            '        4.6023e-07,\n'
            '        4.7356e-08\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "Ar",\n'
            '      "velocity": [\n'
            '        -82.636,\n'
            '        45.098,\n'
            '        -10.626\n'
            '      ],\n'
            '      "atom_id": 6,\n'
            '      "position": [\n'
            '        9.6394e-07,\n'
            '        7.2845e-07,\n'
            '        8.8623e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        158.89,\n'
            '        258.58,\n'
            '        -151.5\n'
            '      ],\n'
            '      "atom_id": 7,\n'
            '      "position": [\n'
            '        5.445e-07,\n'
            '        4.6373e-07,\n'
            '        6.227e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        -197.03,\n'
            '        156.74,\n'
            '        -185.2\n'
            '      ],\n'
            '      "atom_id": 8,\n'
            '      "position": [\n'
            '        7.9322e-07,\n'
            '        9.47e-07,\n'
            '        3.5194e-08\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "Ar",\n'
            '      "velocity": [\n'
            '        -38.65,\n'
            '        -696.32,\n'
            '        216.42\n'
            '      ],\n'
            '      "atom_id": 9,\n'
            '      "position": [\n'
            '        2.7797e-07,\n'
            '        1.6487e-07,\n'
            '        8.2403e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        -149.63,\n'
            '        422.88,\n'
            '        -76.309\n'
            '      ],\n'
            '      "atom_id": 10,\n'
            '      "position": [\n'
            '        1.1842e-07,\n'
            '        6.3244e-07,\n'
            '        5.0958e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "Ar",\n'
            '      "velocity": [\n'
            '        484.57,\n'
            '        -267.41,\n'
            '        -352.54\n'
            '      ],\n'
            '      "atom_id": 11,\n'
            '      "position": [\n'
            '        2.0359e-07,\n'
            '        8.3369e-07,\n'
            '        9.6348e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        -231.92,\n'
            '        -99.51,\n'
            '        32.77\n'
            '      ],\n'
            '      "atom_id": 12,\n'
            '      "position": [\n'
            '        5.1019e-07,\n'
            '        2.247e-07,\n'
            '        2.3846e-08\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "Ar",\n'
            '      "velocity": [\n'
            '        -303.95,\n'
            '        47.316,\n'
            '        222.53\n'
            '      ],\n'
            '      "atom_id": 13,\n'
            '      "position": [\n'
            '        3.5383e-07,\n'
            '        8.4581e-07,\n'
            '        7.234e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        233.08,\n'
            '        254.18,\n'
            '        429.83\n'
            '      ],\n'
            '      "atom_id": 14,\n'
            '      "position": [\n'
            '        3.8515e-07,\n'
            '        2.894e-07,\n'
            '        5.6028e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        199.63,\n'
            '        203.11,\n'
            '        -425.6\n'
            '      ],\n'
            '      "atom_id": 15,\n'
            '      "position": [\n'
            '        1.5842e-07,\n'
            '        9.8225e-07,\n'
            '        5.7859e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        66.341,\n'
            '        222.32,\n'
            '        -97.653\n'
            '      ],\n'
            '      "atom_id": 16,\n'
            '      "position": [\n'
            '        3.6831e-07,\n'
            '        7.652e-07,\n'
            '        2.9884e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        90.358,\n'
            '        -67.459,\n'
            '        -64.782\n'
            '      ],\n'
            '      "atom_id": 17,\n'
            '      "position": [\n'
            '        2.8696e-07,\n'
            '        1.5129e-07,\n'
            '        6.406e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "He",\n'
            '      "velocity": [\n'
            '        71.108,\n'
            '        11.06,\n'
            '        15.912\n'
            '      ],\n'
            '      "atom_id": 18,\n'
            '      "position": [\n'
            '        1.0325e-07,\n'
            '        9.9012e-07,\n'
            '        3.4381e-07\n'
            '      ]\n'
            '    },\n'
            '    {\n'
            '      "type": "Ar",\n'
            '      "velocity": [\n'
            '        239.19,\n'
            '        173.83,\n'
            '        335.29\n'
            '      ],\n'
            '      "atom_id": 19,\n'
            '      "position": [\n'
            '        4.3929e-07,\n'
            '        7.5363e-07,\n'
            '        9.9974e-07\n'
            '      ]\n'
            '    }\n'
            '  ],\n'
            '  "step": 0,\n'
            '  "boundary_conditions": [\n'
            '    "periodic",\n'
            '    "periodic",\n'
            '    "periodic"\n'
            '  ],\n'
            '  "system_size": [\n'
            '    {\n'
            '      "unit": "\u00b5m",\n'
            '      "magnitude": 100\n'
            '    },\n'
            '    {\n'
            '      "unit": "\u00b5m",\n'
            '      "magnitude": 200\n'
            '    },\n'
            '    {\n'
            '      "unit": "\u00b5m",\n'
            '      "magnitude": 300\n'
            '    }\n'
            '  ],\n'
            '  "time": {\n'
            '    "unit": "s",\n'
            '    "magnitude": 0\n'
            '  },\n'
            '  "atom_types": {\n'
            '    "Ar": "Argon",\n'
            '    "He": "Helium"\n'
            '  }\n'
            '}')
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


.. doctest:: json_file

    >>> with open('md_result.json', 'r') as f:
    ...     print(f.read())
    ...
    {
      "potentials": {
        "Ar": {
          "type": "Lennard-Jones",
          "parameters": {
            "sigma": {
              "unit": "pm",
              "magnitude": 341
            },
            "epsilon/k_B": {
              "unit": "K",
              "magnitude": 120
            }
          }
        },
        "He": {
          "type": "Lennard-Jones",
          "parameters": {
            "sigma": {
              "unit": "pm",
              "magnitude": "256"
            },
            "epsilon/k_B": {
              "unit": "K",
              "magnitude": "10.22"
            }
          }
        }
      },
      "atoms": [
        {
          "type": "He",
          "velocity": [
            -29.245,
            100.45,
            128.28
          ],
          "atom_id": 0,
          "position": [
            5.7222e-07,
            4.8811e-09,
            2.0415e-07
          ]
        },
        {
          "type": "He",
          "velocity": [
            -199.26,
            232.75,
            -534.38
          ],
          "atom_id": 1,
          "position": [
            9.771e-07,
            3.6371e-07,
            4.7311e-07
          ]
        },
        {
          "type": "Ar",
          "velocity": [
            -1.5592,
            -378.76,
            84.091
          ],
          "atom_id": 2,
          "position": [
            6.4989e-07,
            6.7873e-07,
            9.5e-07
          ]
        },
        {
          "type": "Ar",
          "velocity": [
            342.82,
            156.82,
            -38.991
          ],
          "atom_id": 3,
          "position": [
            5.9024e-08,
            3.7138e-07,
            7.3455e-08
          ]
        },
        {
          "type": "He",
          "velocity": [
            -30.45,
            -379.75,
            -336.32
          ],
          "atom_id": 4,
          "position": [
            7.6746e-07,
            8.3017e-08,
            4.852e-07
          ]
        },
        {
          "type": "Ar",
          "velocity": [
            -311.51,
            -429.39,
            -694.74
          ],
          "atom_id": 5,
          "position": [
            1.7226e-07,
            4.6023e-07,
            4.7356e-08
          ]
        },
        {
          "type": "Ar",
          "velocity": [
            -82.636,
            45.098,
            -10.626
          ],
          "atom_id": 6,
          "position": [
            9.6394e-07,
            7.2845e-07,
            8.8623e-07
          ]
        },
        {
          "type": "He",
          "velocity": [
            158.89,
            258.58,
            -151.5
          ],
          "atom_id": 7,
          "position": [
            5.445e-07,
            4.6373e-07,
            6.227e-07
          ]
        },
        {
          "type": "He",
          "velocity": [
            -197.03,
            156.74,
            -185.2
          ],
          "atom_id": 8,
          "position": [
            7.9322e-07,
            9.47e-07,
            3.5194e-08
          ]
        },
        {
          "type": "Ar",
          "velocity": [
            -38.65,
            -696.32,
            216.42
          ],
          "atom_id": 9,
          "position": [
            2.7797e-07,
            1.6487e-07,
            8.2403e-07
          ]
        },
        {
          "type": "He",
          "velocity": [
            -149.63,
            422.88,
            -76.309
          ],
          "atom_id": 10,
          "position": [
            1.1842e-07,
            6.3244e-07,
            5.0958e-07
          ]
        },
        {
          "type": "Ar",
          "velocity": [
            484.57,
            -267.41,
            -352.54
          ],
          "atom_id": 11,
          "position": [
            2.0359e-07,
            8.3369e-07,
            9.6348e-07
          ]
        },
        {
          "type": "He",
          "velocity": [
            -231.92,
            -99.51,
            32.77
          ],
          "atom_id": 12,
          "position": [
            5.1019e-07,
            2.247e-07,
            2.3846e-08
          ]
        },
        {
          "type": "Ar",
          "velocity": [
            -303.95,
            47.316,
            222.53
          ],
          "atom_id": 13,
          "position": [
            3.5383e-07,
            8.4581e-07,
            7.234e-07
          ]
        },
        {
          "type": "He",
          "velocity": [
            233.08,
            254.18,
            429.83
          ],
          "atom_id": 14,
          "position": [
            3.8515e-07,
            2.894e-07,
            5.6028e-07
          ]
        },
        {
          "type": "He",
          "velocity": [
            199.63,
            203.11,
            -425.6
          ],
          "atom_id": 15,
          "position": [
            1.5842e-07,
            9.8225e-07,
            5.7859e-07
          ]
        },
        {
          "type": "He",
          "velocity": [
            66.341,
            222.32,
            -97.653
          ],
          "atom_id": 16,
          "position": [
            3.6831e-07,
            7.652e-07,
            2.9884e-07
          ]
        },
        {
          "type": "He",
          "velocity": [
            90.358,
            -67.459,
            -64.782
          ],
          "atom_id": 17,
          "position": [
            2.8696e-07,
            1.5129e-07,
            6.406e-07
          ]
        },
        {
          "type": "He",
          "velocity": [
            71.108,
            11.06,
            15.912
          ],
          "atom_id": 18,
          "position": [
            1.0325e-07,
            9.9012e-07,
            3.4381e-07
          ]
        },
        {
          "type": "Ar",
          "velocity": [
            239.19,
            173.83,
            335.29
          ],
          "atom_id": 19,
          "position": [
            4.3929e-07,
            7.5363e-07,
            9.9974e-07
          ]
        }
      ],
      "step": 0,
      "boundary_conditions": [
        "periodic",
        "periodic",
        "periodic"
      ],
      "system_size": [
        {
          "unit": "µm",
          "magnitude": 100
        },
        {
          "unit": "µm",
          "magnitude": 200
        },
        {
          "unit": "µm",
          "magnitude": 300
        }
      ],
      "time": {
        "unit": "s",
        "magnitude": 0
      },
      "atom_types": {
        "Ar": "Argon",
        "He": "Helium"
      }
    }

Which can easily be read with the :mod:`json` module of the Python standard
library:

.. doctest:: json_file

    >>> import json
    >>> with open('md_result.json', 'r') as f:
    ...     md_data = json.load(f)
    ...
    >>> print(md_data)
    {'potentials': {'He': {'parameters': {'sigma': {'magnitude': '256', 'unit': 'pm'}, 'epsilon/k_B': {'magnitude': '10.22', 'unit': 'K'}}, 'type': 'Lennard-Jones'}, 'Ar': {'parameters': {'sigma': {'magnitude': 341, 'unit': 'pm'}, 'epsilon/k_B': {'magnitude': 120, 'unit': 'K'}}, 'type': 'Lennard-Jones'}}, 'time': {'magnitude': 0, 'unit': 's'}, 'boundary_conditions': ['periodic', 'periodic', 'periodic'], 'atom_types': {'He': 'Helium', 'Ar': 'Argon'}, 'system_size': [{'magnitude': 100, 'unit': 'µm'}, {'magnitude': 200, 'unit': 'µm'}, {'magnitude': 300, 'unit': 'µm'}], 'atoms': [{'position': [5.7222e-07, 4.8811e-09, 2.0415e-07], 'atom_id': 0, 'type': 'He', 'velocity': [-29.245, 100.45, 128.28]}, {'position': [9.771e-07, 3.6371e-07, 4.7311e-07], 'atom_id': 1, 'type': 'He', 'velocity': [-199.26, 232.75, -534.38]}, {'position': [6.4989e-07, 6.7873e-07, 9.5e-07], 'atom_id': 2, 'type': 'Ar', 'velocity': [-1.5592, -378.76, 84.091]}, {'position': [5.9024e-08, 3.7138e-07, 7.3455e-08], 'atom_id': 3, 'type': 'Ar', 'velocity': [342.82, 156.82, -38.991]}, {'position': [7.6746e-07, 8.3017e-08, 4.852e-07], 'atom_id': 4, 'type': 'He', 'velocity': [-30.45, -379.75, -336.32]}, {'position': [1.7226e-07, 4.6023e-07, 4.7356e-08], 'atom_id': 5, 'type': 'Ar', 'velocity': [-311.51, -429.39, -694.74]}, {'position': [9.6394e-07, 7.2845e-07, 8.8623e-07], 'atom_id': 6, 'type': 'Ar', 'velocity': [-82.636, 45.098, -10.626]}, {'position': [5.445e-07, 4.6373e-07, 6.227e-07], 'atom_id': 7, 'type': 'He', 'velocity': [158.89, 258.58, -151.5]}, {'position': [7.9322e-07, 9.47e-07, 3.5194e-08], 'atom_id': 8, 'type': 'He', 'velocity': [-197.03, 156.74, -185.2]}, {'position': [2.7797e-07, 1.6487e-07, 8.2403e-07], 'atom_id': 9, 'type': 'Ar', 'velocity': [-38.65, -696.32, 216.42]}, {'position': [1.1842e-07, 6.3244e-07, 5.0958e-07], 'atom_id': 10, 'type': 'He', 'velocity': [-149.63, 422.88, -76.309]}, {'position': [2.0359e-07, 8.3369e-07, 9.6348e-07], 'atom_id': 11, 'type': 'Ar', 'velocity': [484.57, -267.41, -352.54]}, {'position': [5.1019e-07, 2.247e-07, 2.3846e-08], 'atom_id': 12, 'type': 'He', 'velocity': [-231.92, -99.51, 32.77]}, {'position': [3.5383e-07, 8.4581e-07, 7.234e-07], 'atom_id': 13, 'type': 'Ar', 'velocity': [-303.95, 47.316, 222.53]}, {'position': [3.8515e-07, 2.894e-07, 5.6028e-07], 'atom_id': 14, 'type': 'He', 'velocity': [233.08, 254.18, 429.83]}, {'position': [1.5842e-07, 9.8225e-07, 5.7859e-07], 'atom_id': 15, 'type': 'He', 'velocity': [199.63, 203.11, -425.6]}, {'position': [3.6831e-07, 7.652e-07, 2.9884e-07], 'atom_id': 16, 'type': 'He', 'velocity': [66.341, 222.32, -97.653]}, {'position': [2.8696e-07, 1.5129e-07, 6.406e-07], 'atom_id': 17, 'type': 'He', 'velocity': [90.358, -67.459, -64.782]}, {'position': [1.0325e-07, 9.9012e-07, 3.4381e-07], 'atom_id': 18, 'type': 'He', 'velocity': [71.108, 11.06, 15.912]}, {'position': [4.3929e-07, 7.5363e-07, 9.9974e-07], 'atom_id': 19, 'type': 'Ar', 'velocity': [239.19, 173.83, 335.29]}], 'step': 0}

So parsing a JSON file results in a composition of dictionaries, lists,
strings, integers, and floats.

Writing JSON files is equally simple:

.. doctest:: json_file

    >>> with open('my_md_result.json', 'w') as f:
    ...     json.dump(md_data, f, indent=2)
    ...

with the ``indent`` keyword resulting in the file not written in a very
condensed manner, but with newlines and an indentation of 2. Note that the
following Python types can be converted out-of-the-box:

+----------------------------------------+--------+
| Python                                 | JSON   |
+========================================+========+
| :class:`dict`                          | object |
+----------------------------------------+--------+
| :class:`list`, :class:`tuple`          | array  |
+----------------------------------------+--------+
| :class:`str`                           | string |
+----------------------------------------+--------+
| :class:`int`, :class:`float`,          | number |
| :class:`int`- & :class:`float`-derived |        |
| :class:`~enum.Enum`\ s                 |        |
+----------------------------------------+--------+
| :data:`True`                           | true   |
+----------------------------------------+--------+
| :data:`False`                          | false  |
+----------------------------------------+--------+
| :data:`None`                           | null   |
+----------------------------------------+--------+
