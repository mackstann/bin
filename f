#!/usr/bin/env python

import sys

fields = map(int, sys.argv[1:])

for line in sys.stdin:
    words = line.split()
    print ' '.join([ words[field-1] for field in fields if field < len(words) ])

