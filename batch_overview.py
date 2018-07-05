from pci.pyramid import *

import glob
import sys
import os

if not os.path.isdir( sys.argv[1] ):
  print "Input argument '%s' is not a directory" % sys.argv[1]
  exit( -1 )

os.chdir( sys.argv[1] )

files = []
for ext in ( "*.pix", "*.tif" ):
  files.extend( map( unicode, glob.glob( ext ) ) )

for f in files:
  pyramid( f, [], u"YES", [ -2 ], u"AVERAGE" )
