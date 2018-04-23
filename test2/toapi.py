#!/usr/bin/env python

import hug

@hug.get('/toapi3')
def say_hi():
    return 'say hi from toapi.py'
