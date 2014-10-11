#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 03: Adding and Removing Keys """

import data

CORRECTED = data.BANDS.copy()
print CORRECTED

CORRECTED['Dylan'] = {
    'Bob Dylan': ['vocals', 'guitar', 'harmonica']
}
print CORRECTED

del CORRECTED['Van Halen']['David Lee Roth']
print CORRECTED

CORRECTED['Van Halen']['Sammy Hagar'] = ['vocals']
print CORRECTED