from mrcp.panel import *
from mrcp.points import *
from mrcp.config import *

class Led(BaseElement):
    def __init__(self, pos=Point(0, 0), color=LED_COLOR) -> None:
        super().__init__(pos=pos, color=color)

    def paint(self):

        found = searchLed(self._panel, self._pos)

        #print("Found", found, self)
        if found != self:
            # there is another wich is not self
            # only the first will be painted
            return

        pos = self._pos.toCoords()
        dwg = self._panel._dwg
        cutLayer = self._panel._cLayer
        ledLayer = self._panel._lLayer
        color = self._color
        circle = dwg.circle(center=pos, r=LED_SIZE/2, fill=color)
        ledLayer.add(circle)
        circle = dwg.circle(center=pos, r=LED_SIZE/2, stroke=COLOR_CUT,
                            stroke_width=0.2, fill="none")
        cutLayer.add(circle)
        circle = dwg.circle(center=pos, r=LED_SIZE/2+LED_MARGIN, stroke=COLOR_ENGRAVE,
                    stroke_width=0.2, fill="none")
        cutLayer.add(circle)

        return super().paint()

def searchLed(panel,pos=Point(0,0)) -> Led:
    pos = pos.toCoords()
    for obj in panel._paintable:
        if isinstance(obj,Led):
            if pos == obj._pos.toCoords():
                return obj
    return None