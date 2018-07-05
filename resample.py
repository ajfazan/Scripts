from pci.resamp import resamp

import sys
import os

if not os.path.isfile( sys.argv[1] ):
  print "First input argument must be a raster file"
  exit( 1 )

if not os.path.isdir( sys.argv[2] ):
  print "Second input argument must be a directory"
  exit( 2 )

gsd = []

out = os.path.splitext( os.path.basename( sys.argv[1] ) )[0] + ".pix"
out = sys.argv[2] + os.path.sep + out

if os.path.exists( out ):
  try:
    os.remove( out )
  except OSError as e:
    print "Unable to remove %s: %s" % ( out, e )
    exit( -1 )

try:
  gsd = float( sys.argv[3] )
except ValueError as e:
  print "Float conversion error:", e
  exit( -1 )

resamp( sys.argv[1], [ 1 ], [], u"ALL",
        out, u"PIX", u"TILED256", [ gsd, gsd ], u"CUBIC" )
