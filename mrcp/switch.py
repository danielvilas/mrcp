from mrcp.panel import *
from mrcp.points import *
from mrcp.config import *

class Switch(BaseElement):
    def __init__(self, pos=Point(0, 0), color=None, vertical=False) -> None:
        super().__init__(pos=pos, color=color)
        self._vertical = vertical

    def paint(self):
        if self._color is None:
            self._color= self._config.COLOR_TRACK_DEFAULT
        super().paint()

        swPoint = self._pos
        swStart = swPoint.toCoords(self._config,adjust=(-7.5, -5))
        swSize= self._config.SWITH_SIZE_H
        if self._vertical:
            swStart = swPoint.toCoords(self._config,adjust=(-5, -7.5) )
            swSize= self._config.SWITH_SIZE

        dwg = self._panel._dwg
        cutLayer = self._panel._cLayer
        layer = self._panel._tLayer

        # Switch
        circle = dwg.circle(center=swPoint.toCoords(self._config), r=self._config.SWITH_HOLE_SIZE/2, fill="white")
        layer.add(circle)
        circle = dwg.circle(center=swPoint.toCoords(self._config), r=self._config.SWITH_HOLE_SIZE/2, stroke=self._config.COLOR_CUT,
                            stroke_width=0.2, fill="none")
        cutLayer.add(circle)
        circle = dwg.circle(center=swPoint.toCoords(self._config), r=self._config.SWITH_HOLE_MARGIN_SIZE/2, stroke=self._config.COLOR_ENGRAVE,
                    stroke_width=0.2, fill="none")
        cutLayer.add(circle)

        rect = dwg.rect(insert=swStart, size=swSize, stroke=self._config.COLOR_ENGRAVE,
                        stroke_width=0.2, fill="none")
        cutLayer.add(rect)