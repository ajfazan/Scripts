from pci.ortho import *

import glob
import sys
import os

if not os.path.isdir( sys.argv[1] ):
  print "First input argument '%s' is not a directory" % sys.argv[1]
  exit( 1 )

if not os.path.isfile( sys.argv[2] ):
  print "Second input argument must be a DEM file"
  exit( 2 )

if not os.path.isdir( sys.argv[3] ):
  print "Third input argument '%s' is not a directory" % sys.argv[3]
  exit( 3 )

os.chdir( sys.argv[1] )

dem = unicode( sys.argv[2] )

gsd = unicode( sys.argv[4] )

files = map( unicode, glob.glob( e ) )

for f in files:

  out = sys.argv[3] + os.path.sep + "ortho_" + f
  ortho( f, [], [], [], u"FILE", out, u"PIX", u"TILED256", [ 0.0 ], \
         [], [], [], [], [], [], \
         u"", \
         u"", gsd, u"", dem, [ 1 ], [], u"MSL", u"METER", [ 0.0, 1.0 ], \
         u"4096", [ 1 ], u"CUBIC" )

# ortho( mfile, dbic, mmseg, dbiw, srcbgd, filo, ftype, foptions, outbgd,
# ulx, uly, lrx, lry, edgeclip, tipostrn, mapunits, bxpxsz, bypxsz,
# filedem, dbec, backelev, elevref, elevunit, elfactor, proc, sampling,
# resample )
