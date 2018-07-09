from pci.epipolardsm import *

from pci.geocodedem import *

from multiprocessing import *

import csv, glob, os, sys

def extract_dem( p ):
  demopts = "epitracking computepyramid"
  tag = "dem" + str( p['interval'][0] ) + "_"
  dem = p["left"].replace( "el_", tag )
  print "Extracting epipolar dem '%s'" % dem
  epipolardsm( p['left'], p['right'], p['interval'], dem, u"NONE", demopts )
  print "'%s' done" % dem

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

  it = csv.reader( open( sys.argv[1], 'r' ) )

  epipolars = []

  for row in it:
    l, r = row
    epipolars.append( { "left" : l, "right" : r, "interval" : [ interval ] } )

  threads = len( epipolars )
  max_cpu = int( 0.75 * cpu_count() )

  if threads > max_cpu:
    threads = max_cpu

  p = Pool( threads )
  p.map( extract_dem, epipolars )

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
