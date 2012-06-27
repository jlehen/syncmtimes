#!/usr/bin/python
#
# Jeremie Le Hen <jeremie@le-hen.org>, 2012
# This file is in the public domain.
#
# Run this is the correct directory.

import fileinput
import getopt
import os
import sys

noexec = False
verbose = False
opts, args = getopt.getopt(sys.argv[1:], 'nv')
for o, a in opts:
	if o == "-n":
		noexec = True
	elif o == "-v":
		verbose = True

args.insert(0, sys.argv[0])
sys.argv = args
for line in fileinput.input():
	a = line.split()
	if not os.path.exists(a[1]):
		print "%s not found" % a[1]
		continue
	if verbose:
		print "Setting time for %s" % a[1]
	if noexec:
		continue
	t = int(a[0])
	os.utime(a[1], (t, t))
