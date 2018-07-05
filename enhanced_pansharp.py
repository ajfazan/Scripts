from pci.pcimod import pcimod
from pci.pansharp2 import *
from pci.ihs import *
from pci.pyramid import *

import sys
import os

if not os.path.isfile( sys.argv[1] ):
  print "First input argument must be a multispectral image file"
  exit( 1 )

if not os.path.isfile( sys.argv[2] ):
  print "Second input argument must be a panchromatic image file"
  exit( 2 )

if not os.path.isdir( sys.argv[3] ):
  print "Third input argument must be a directory"
  exit( 3 )

channels = []
try:
  channels = [ int( n ) for n in sys.argv[4].split( "," ) ]
except ValueError as e:
  print "Conversion error [STRING >> INT]", e
  exit( 2 )

out = os.path.splitext( os.path.basename( sys.argv[1] ) )[0] + ".pix"
out = out.replace( "-M2AS-", "-PSH2-" )
out = sys.argv[3] + os.path.sep + out

if os.path.exists( out ):
  try:
    os.remove( out )
  except OSError as e:
    print "Unable to remove %s: %s" % ( out, e )
    exit( -1 )

pansharp2(
  sys.argv[1], channels, channels, sys.argv[2], [ 1 ],
  out, channels, u"YES", u"FILE,0", u"OFF", u"PIX", u"TILED256"
)

l = len( channels )

pcimod( out, u"ADD", [ 0, 0, 3, 0, 0, 0 ] )

ihs( out, [ 1, 2, 3 ], list( range( l + 1, l + 4 ) ), [], u"CYLINDER" )

pyramid( out, [], u"YES", [ -2 ], u"AVERAGE" )
