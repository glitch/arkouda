
import sys

from context import arkouda as ak

ak.verbose = False
if len(sys.argv) > 1:
    ak.connect(server=sys.argv[1], port=int(sys.argv[2]), access_token=sys.argv[3] if len(sys.argv)>=4 else None)
else:
    ak.connect()

ak.shutdown()
sys.exit()
