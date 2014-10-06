==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #07
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-10-06T09:00:00-0400
:Due-Date: 2014-10-14T09:00:00-0400


Instructions
============

The following tasks will either have you interacting with existing files in
the starter repo or creating new ones on the fly. Don't forget to add your
interpreter directive, utf-8 encoding, and a short docstring with any new files
that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requires
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the official Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.


Task 07: Iterating Dictionaries
--------------------------------

It is often very useful to iterate through a dictionary object separating the iteration into key and value pairs. In
this task you will need to use your new knowledge of dictionary iteration using the ``iteritems()`` method.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_07.py``

#.  Declare a variable named ``DATA`` as a dictionary object. Assign it these key value pairs. This example data for
    your to work with.

#. Create a function named ``iter_dict_funky_sum()``.

    #.  Declare a running total integer variable.

    #.  Use a ``for`` loop on to extract the key and value pairs from ``DATA``.

    #.  Assign and append the product of the value minus the key to the running total variable.

    #.  Return the funky total.

``DATA`` Example
^^^^^^^^^^^^^^^^

.. code-block::

    DATA = {
        2: 7493945,
        76: 4654320,
        3: 4091979,
        90: 1824881,
        82: 714422,
        45: 1137701,
        10: 374362,
        0: 326226,
        -15: 417203,
        -56: 333525,
        67: 323451,
        99: 321696,
        21: 336753,
        -100: 361237,
        55: 1209714,
        5150: 1771800,
        42: 4714011,
        888: 14817667,
        3500: 13760234,
        712: 10903322,
        7: 10443792,
        842: 11716264,
        18584: 10559923,
        666: 9275602,
        70: 11901200,
        153: 12074784,
        8: 4337229
    }


Output Example
^^^^^^^^^^^^^^

.. code-block::

    >>> import task_07
    >>> task_07.iter_dict_funky_sum(task_07.DATA)
    140166242
    >>>


Task 09: Merging Data Using a Dictionary Key
--------------------------------------------

As a Python programmer, you may at some point face a situation where you are tasked with merging data from multiple
data sources. This is usually done with some kind of key values shared between the data sets.

For this task you will be working to merge Internet bandwidth data collected from three of the routers used by SPS at
our main campus. The Chief Information Officer (CIO) wants a report showing hourly average download traffic for each
router between 9/15/2014 and 9/20/2014. The network administrator has dumped the data for each router into a CSV file.

Since we have yet to cover file IO operations in class, a ``task_09_utility.py`` module has been provided. It
includes a helper function for retrieving data from the CSV files in the form as a list of dictionary objects. A
second helper function provides a way to convert a dictionary into a sorted list.


Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_09.py``

#.  Import the ``task_09_utility.py`` file.

#.  Instantiate a list variable named ``DATA_FILES`` and assign it three dictionary objects each with a key value ``data`` and values of:

    *   'task_09_data/router_01.csv'
    *   'task_09_data/router_02.csv'
    *   'task_09_data/router_03.csv'

#.  Create a function named ``load_data()`` that accepts the ``DATA_FILES`` list object as a parameter.

    #.  Loop through the list
    
    #.  Set an incremental integer key using a counter within your loop. Example (1, 2, 3, ...)
    
    #.  You must pass the file path to the function using the ``data`` key used in ``DATA_FILES``. Assign the value using the ``task_09_utility.get_data()`` function. 
    
    #.  Return a dictionary object.
    
#.  Create a function named ``merge_data()`` that accepts a dictionary object created by the ``load_data()`` function.

    #.  Declare an empty dictionary variable to hold your merged data.

    #.  Use a loop that extracts the key and value pair using the dictionary object ``iteritems()`` method.
    
    #.  Use string slicing to extract the day of the month and the hour to create a key for the merged data.
    
    #.  Use an ``if`` conditional to check if the candidate key is already present in the declared container dictionary variable.

    #.  Assign the key a value of a list containing the ``clock`` and ``value_avg`` keys from the input dictionary.
    
    #.  Make sure to handle situations where dates are missing from any of the data sources. Assign a value of zero for any missing data.

    #.  Convert the container dictionary to a sorted list using ``task_09_utility.sort_dict()``.

    #.  Return the sorted list.

Output Example
^^^^^^^^^^^^^^

.. note::

    This is only example output. It has been truncated for brevity.

.. code-block::

    $ python task_09.py
    [['2014-09-15 00:00:00', 0, '137640', '141366'],
     ['2014-09-15 01:00:00', 0, '123755', '115611'],
     ['2014-09-15 02:00:00', 0, '135569', '114956'],
     ['2014-09-15 03:00:00', 0, '303295', '288066'],
     ['2014-09-15 04:00:00', 0, '140800', '110984'],
     ['2014-09-15 05:00:00', 0, '132150', '126002'],
     ...
     ['2014-09-18 04:00:00', '174456', '108466', '131256'],
     ['2014-09-18 05:00:00', '819066', '111762', '124666'],
     ['2014-09-18 06:00:00', '2118101', '505801', '803900'],
     ['2014-09-18 07:00:00', '767654', '943558', '1816370'],
     ['2014-09-18 08:00:00', '14522464', '5843934', '5233635'],
     ['2014-09-18 09:00:00', '23170931', '10404840', '11715033'],
     ['2014-09-18 10:00:00', '24114328', '14417230', '9235289'],
     ['2014-09-18 11:00:00', '23617824', '10295080', '7452332'],
     ['2014-09-18 12:00:00', '19077509', '13409772', '10086040'],
     ['2014-09-18 13:00:00', '25239127', '12299642', '11995444'],
     ['2014-09-18 14:00:00', '11978037', '8246122', '11055365'],
     ['2014-09-18 15:00:00', '31212115', '14750547', '11313491'],
     ['2014-09-18 16:00:00', '6526768', '6700765', '10439742'],
     ['2014-09-18 17:00:00', '11898908', '8920453', '3764985'],
     ['2014-09-18 18:00:00', '3044609', '2299610', '888989'],
     ['2014-09-18 19:00:00', '1978930', '2880184', '284551'],
     ['2014-09-18 20:00:00', '1662631', '1355832', '863157'],
     ['2014-09-18 21:00:00', '559190', '1358866', '384384'],
     ['2014-09-18 22:00:00', '155978', '177637', '190171'],
     ['2014-09-18 23:00:00', '128770', '114094', '167008'],
     ['2014-09-19 00:00:00', '277428', '198593', 0],
     ['2014-09-19 01:00:00', '120651', '124192', 0],
     ...
     ['2014-09-19 21:00:00', '132568', '129424', 0],
     ['2014-09-19 22:00:00', '357205', '107939', 0],
     ['2014-09-19 23:00:00', '141285', '107529', 0]]
    

Example of DATA_FILES
^^^^^^^^^^^^^^^^^^^^^

Note how this is a list of dictionary objects.

.. code-block::

    >>> import task_09
    >>> task_09.DATA_FILES
    [{'data': 'task_09_data/router_01.csv'}, {'data': 'task_09_data/router_02.csv'}, {'data': 'task_09_data/router_03.csv'}]
    >>> 

Example of using ``task_09_utility.get_data()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    >>> import task_09_utility
    >>> task_09_utility.get_data('task_09_data/router_01.csv')
    [{'value_min': '106288', 'value_avg': '143334', 'num': '9', 'value_max': '280576', 'clock': '2014-09-15 22:00:00'}, {'value_min': '93728', 'value_avg': '111313', 'num': '9', 'value_max': '124728', 'clock': '2014-09-15 23:00:00'}, {'value_min': '100056', 'value_avg': '135149', 'num': '11', 'value_max': '310760', 'clock': '2014-09-16 00:00:00'}, ....


Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Lesson 01.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
