#!/usr/bin/python
#
# Jeremie Le Hen <jeremie@le-hen.org>, 2012
# This file is in the public domain.
#
# Run this is the correct directory.

import os

def visit(arg, dirname, names):
	for n in names:
		f = dirname + "/" + n
		print "%u %s" % (os.path.getmtime(f), f)

os.path.walk(".", visit, None)
