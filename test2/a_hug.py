#!/usr/bin/env python

import hug

@hug.get('/happy_birthday')
def happy_birthday(name='liujw', age:hug.types.number=10):
    return "happy {age} birthday {name}".format(**locals())

@hug.get('/greet/{event}')
def greet(event:str):
    greetings = 'happy'
    if event == "christmas":
        greetings = 'marry'
    elif event == 'kwanzaa':
        greetings = 'joyous'
    elif event == 'wishes':
        greetings = 'warm'
    return '{greetings} {event}'.format(**locals())


#  @hug.get('/echo', versions=1)
#  def echo(text):
    #  return text

#  @hug.get('/echo', versions=range(2, 5))
#  def echo(text):
    #  return "Echo: {text}".format(**locals())







