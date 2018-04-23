#!/usr/bin/env python

import hug
import something
import hb
from test2 import toapi, a_hug


hug.API(__name__).extend(hb, "/hb")
hug.API(__name__).extend(something, "/something")
hug.API(__name__).extend(toapi, "/toapi")
hug.API(__name__).extend(a_hug, "/a_hug")
