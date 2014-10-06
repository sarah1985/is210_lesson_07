==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #06
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-10-06T09:00:00-0400
:Due-Date: 2014-10-14T09:00:00-0400


Overview
========

The following tasks will either have you interacting with existing files in
the starter repo or creating new ones on the fly. Don't forget to add your
interpreter directive, utf-8 encoding, and a short docstring with any new files
that you create!

Warmup Tasks
============

Task 01: Creating a Dictionary
------------------------------

Dictionaries can often be thought of as tabular data which is why they're so
commonly used to represent database data. For this task, we'll be creating
a dictionary from a table of data.

Specifications
^^^^^^^^^^^^^^

#.  Create a file, ``task_01.py``.

#   In ``task_01.py``, create a constant called ``GRADE_DATA`` that stores the
    following table, *Grades*,  as a **nested** dictionary.

    #.  The first level key of the dictionary is ``student`` which represents
        the student's name.

    #.  Second level keys of this dictionary should map to the subjects.

    #.  Do not use functions that convert data of other types to instantiate
        the dictionary. You should use some form of the ``{}`` syntax to
        construct the dictionary.

    #.  Your dictionary construction should be clean and well-indented to make
        it easy to read.

Data
^^^^
    
.. table:: Grades

    ====================== ================ =====
    student                subject          grade
    ====================== ================ =====
    Luke Skywalker         math             B
    Luke Skywalker         etiquette        B+
    Luke Skywalker         grammar          B
    Luke Skywalker         gym              A
    Han Solo               math             A-
    Han Solo               etiquette        C-
    Han Solo               grammar          B
    Han Solo               gym              B
    C-3PO                  math             C
    C-3PO                  etiquette        A+
    C-3PO                  grammar          A
    C-3PO                  gym              F
    ====================== ================ =====

Task 02: Dictionary Access
--------------------------

There are a number of ways to access data from dictionaries. Here we'll
practice a few of the most common ones.

Specifications
^^^^^^^^^^^^^^

#.  Start off by opening ``data.py`` and just taking a look at the structure of
    the ``BANDS`` dictionary.

#.  Create a file named ``task_02.py``.

#.  In ``task_02.py``, import the ``data`` module.

#.  In one line, create a new constant named ``NIGEL`` and use dictionary keys
    to assign its value value from the ``'Nigel Tufnel'`` entry of the
    ``data.BANDS`` dictionary.

#.  Create a new constant named ``BANDS_NAMES`` and use a built-in dictionary
    function to fill it with a list of band-names from ``data.BANDS``.

Task 03: Adding and Removing Keys
---------------------------------

There are a number of ways to add or remove keys to Python dictionaries. Here,
we'll cover the most common types.

Specifications
^^^^^^^^^^^^^^

#.  Create a new file named, ``task_03.py``

#.  Import the ``data`` module.

#.  With ``task_03.py``, copy ``data.BANDS`` into a new constant named
    ``CORRECTED``.

    .. tip::

        Keep in mind that the assignment operator (``=``), doesn't a
        dictionary, it just creates a new reference to it. There is a built-in
        dictionary function that creates a new copy of a dictionary.

#.  Remove the ``'David Lee Roth'`` entry from the ``'Van Halen'`` entry of
    ``CORRECTED`` with the ``del`` statement.

#.  Using the assignment syntax (``[]``), add a new entry to
    ``CORRECTED['Van Halen']`` with key ``'Sammy Hagar'`` and value
    ``['vocals']``.

Task 04: Merging Two Dictionaries
---------------------------------

The ``.update()`` method is a powerful tool for merging dictionary data as
you'll see below.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_04.py``.

#.  With ``task_04.py``, create a new top-level band entry in ``data.BANDS``
    with the key, ``'Buckingham Nicks``. The key:values of ``Buckingham Nicks``
    are:

    .. code:: python

        'Lindsey Buckingham': ['guitar', 'vocals'],
        'Stevie Nicks': ['vocals', 'tambourine']

#.  Use a built-in dictionary function to merge 
    ``data.BANDS['Buckingham Nicks']`` into 
    ``data.BANDS['Fleewood Mac']`` so that there are now five keys in
    ``data.BANDS['Fleetwood Mac']``.

Task 05: Changing the Value of a Key
------------------------------------

Changing dictionary values is nearly identical to assigning them.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_05.py``.

#.  With ``task_05.py``, import the ``data`` module.

#.  Change the value of ``data.SUPERHEROES['Logan']['alias']`` to
    ``'Wolverine'`` without altering ``data.py`` and without creating a new
    dictionary or variable.

Task 06: Getting Values with a Default
--------------------------------------

The ``.get()`` function has surprising utility when traversing data that
could be incomplete.

Specifications
^^^^^^^^^^^^^^

#.  Open ``task_06.py``

#.  Complete line 10 of ``task_06.py`` so that the ``'pet'`` key of
    ``HERO_DATA`` is added to the new ``SUPER_SIDEKICKS`` dictionary.

#.  If no pet data exists, the returned value should be ``None``

#.  Use a built-in dictionary function to achieve this objective.

#.  Restrict your edits to just line 10.

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
