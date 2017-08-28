#!/usr/bin/env python

import somemodule as sm


# somemodule is very tidy:
print dir(sm)

# yet all internal functions can be inspected if need be:
print "namespace:", sm.internal
print "function: ", sm.internal.double
print "function: ", sm.internal.triple

# or used:
assert sm.internal.double(3) == 6
assert sm.internal.triple(3) == 9

# but the important function of somemodule is easy to find:
assert sm.important(10) == 50


