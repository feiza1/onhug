#!/usr/bin/env python

import hug


@hug.get('/')
def say_hi():
    return 'say hi from something'


@hug.get('/toapi')
def say_hi2():
    return 'say hi from something2'


