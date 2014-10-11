#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 04: Merging Two Dictionaries """

import data

data.BANDS['Buckingham Nicks'] = {
    'Lindsey Buckingham': ['guitar', 'vocals'],
    'Stevie Nicks': ['vocals', 'tambourine']
}

data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])
print data.BANDS['Fleetwood Mac']