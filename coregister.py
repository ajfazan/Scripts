from pci.inscoreg import inscoreg

from pci.api import datasource as handle

import sys
import os

def get_channels( img ):
  try:
    dataset = handle.open_dataset( img )
    return range( 1, dataset.chans_count + 1 )
  except:
    print "Unable to open dataset %s" % img
    return range( 1, 5 )

if not os.path.isfile( sys.argv[1] ):
  print "First input argument must be a reference image file"
  exit( 1 )

if not os.path.isfile( sys.argv[2] ):
  print "Second input argument must be an image file"
  exit( 2 )

if not os.path.isdir( sys.argv[3] ):
  print "Third input argument must be a directory"
  exit( 3 )

out = os.path.splitext( os.path.basename( sys.argv[2] ) )[0] + ".pix"
out = os.path.join( sys.argv[3], out )

if os.path.exists( out ):
  try:
    os.remove( out )
  except OSError as e:
    print "Unable to remove %s: %s" % ( out, e )
    exit( -1 )

num_pts = 256
try:
  nump_ts = int( sys.argv[4] )
except ValueError as e:
  print "Integer conversion error:", e
  exit( -1 )

min_score = 0.75
try:
  min_score = float( sys.argv[5] )
except ValueError as e:
  print "Float conversion error:", e
  exit( -1 )

radius = 40
try:
  radius = int( sys.argv[6] )
except ValueError as e:
  print "Integer conversion error:", e
  exit( -1 )

match_channel = 1
try:
  match_channel = int( sys.argv[7] )
except ValueError as e:
  print "Integer conversion error:", e
  exit( -1 )

inscoreg( sys.argv[1], [ 1 ], sys.argv[2], [ match_channel ],
  get_channels( sys.argv[2] ), [ num_pts ], [ min_score ], [ radius ], out )
