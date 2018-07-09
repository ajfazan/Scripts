
from pci.fexport import *

import os, sys

def main( args ):
  if not os.path.isfile( args[1] ):
    print "Input argument must be a PIX file"
    exit( 1 )

  channels = []
  try:
    channels = [ int( n ) for n in args[2].split( "," ) ]
  except ValueError as e:
    print "Conversion error [STRING >> INT]", e
    exit( 2 )

  out = args[1].replace( ".pix", ".tif" )

  fexport( args[1], out, [], channels, [], [], [], [], u"TIF", u"TILED512 LZW" )

if __name__ == "__main__":
  main( sys.argv )
