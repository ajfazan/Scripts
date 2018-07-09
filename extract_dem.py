from pci.epipolardsm import *

from pci.geocodedem import *

import csv, glob, os, sys

if __name__ == '__main__':

  if not os.path.isfile( sys.argv[1] ):
    print "Input argument must be a text file"
    exit( 1 )

  interval = 0
  try:
    interval = int( sys.argv[2] )
  except ValueError as e:
    print "Integer conversion error >> ", e
    exit( -1 )

  gsd = 0.0
  try:
    gsd = float( sys.argv[4] )
  except ValueError as e:
    print "Float conversion error >> ", e
    exit( -1 )

  demopts = "smalltiles epitracking noglobal computepyramid"

  it = csv.reader( open( sys.argv[1], 'r' ) )

  for row in it:
    l, r = row
    tag = "dem" + str( interval ) + "_"
    dem = l.replace( "el_", tag )
    epipolardsm( l, r, [ interval ], dem, u"NONE", demopts )

  if os.path.exists( sys.argv[3] ):
    try:
      os.remove( sys.argv[3] )
    except OSError as e:
      print "Unable to remove %s: %s" % ( sys.argv[3], e )
      exit( -1 )

  pattern = "dem" + str( interval ) + "_*.pix"

  r = geocodedem( pattern, [ 5 ], [ 4 ], [], [], [ -32768 ], u"YES", u"",
                  sys.argv[3], u"", [], [], [ gsd, gsd ], u"SCORE" )

  if r == 0:
    for f in glob.glob( pattern ):
      try:
        os.remove( f )
      except OSError as e:
        print "Unable to remove %s: %s" % ( f, e )
        exit( -1 )
