from mrcp.panel import *
from mrcp.points import *
from mrcp.config import *

class Led(BaseElement):
    def __init__(self, pos=Point(0, 0), color=None) -> None:
        super().__init__(pos=pos, color=color)


    def paint(self):
        if(self._color is None):
            self._color=self._config.LED_COLOR

        found = searchLed(self._config,self._panel, self._pos)

        #print("Found", found, self)
        if found != self:
            # there is another wich is not self
            # only the first will be painted
            return

        pos = self._pos.toCoords(self._config)
        dwg = self._panel._dwg
        cutLayer = self._panel._cLayer
        ledLayer = self._panel._lLayer
        color = self._color
        circle = dwg.circle(center=pos, r=self._config.LED_SIZE/2, fill=color)
        ledLayer.add(circle)
        circle = dwg.circle(center=pos, r=self._config.LED_SIZE/2, stroke=self._config.COLOR_CUT,
                            stroke_width=0.2, fill="none")
        cutLayer.add(circle)
        circle = dwg.circle(center=pos, r=self._config.LED_SIZE/2+self._config.LED_MARGIN, stroke=self._config.COLOR_ENGRAVE,
                    stroke_width=0.2, fill="none")
        cutLayer.add(circle)

        circle = dwg.circle(center=pos, r=self._config.LED_SIZE/2, stroke="none",
                            stroke_width=0.2, fill="white")
        self._panel._tLayer.add(circle)
        return super().paint()

def searchLed(config, panel,pos=Point(0,0)) -> Led:
    pos = pos.toCoords(config)
    for obj in panel._paintable:
        if isinstance(obj,Led):
            if pos == obj._pos.toCoords(config):
                return obj
    return None