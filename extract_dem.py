from pci.epipolardsm import *

import csv, glob, os, sys

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
  epipolars.append( { "left" : l, "right" : r } )

demopts = "smalltiles epitracking noglobal computepyramid"

for p in epipolars:
  tag = "dem" + str( interval ) + "_"
  dem = p["left"].replace( "el_", tag )
  epipolardsm( p['left'], p['right'], [ interval ], dem, u"MEDIUM", demopts )

pattern = "dem" + str( interval ) + "_*.pix"

r = geocodedem( pattern, [ 5 ], [ 4 ], [], [], [ -32768 ], u"YES", u"",
                sys.argv[3], u"", [], [], [ gsd, gsd ], u"SCORE" )

if r == 0:
  for f in glob.glob( pattern ):
    os.remove( f )
