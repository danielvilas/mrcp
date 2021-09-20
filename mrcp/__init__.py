try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import svgwrite
from mrcp.panel import Panel
from mrcp.config import *
from mrcp.curve import *
from mrcp.turnouts import *
from mrcp.ladder import *

print ("MRCP")

