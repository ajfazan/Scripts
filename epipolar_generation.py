from pci.epipolar import *

import sys
import os

if not os.path.isdir( sys.argv[1] ):
  print "First input argument must be a directory"
  exit( 1 )

if not os.path.isdir( sys.argv[3] ):
  print "Third input argument must be a directory"
  exit( 3 )

channels = []
try:
  channels = [ int( n ) for n in sys.argv[2].split( "," ) ]
except ValueError as e:
  print "Conversion error [STRING >> INT]", e
  exit( 2 )

epipolar( sys.argv[1], channels, [], [], u"FILE", u"MAX", [ 80 ], [ 1 ],
          sys.argv[3], [ 0.0 ], u"", u"", [ 4096 ], [] )
