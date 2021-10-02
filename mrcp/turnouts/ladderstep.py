from mrcp.panel import *
from mrcp.points import *
from .halfturnout import *
 
class LadderStep(HalfTurnout):
    def __init__(self, pos=(0, 0), color=COLOR_TRACK_DEFAULT, up=True, right=True, vertical=False,closedColor=CLOSED_LED_COLOR,thrownColor=THROWN_LED_COLOR) -> None:
        #Interchange the color
        super().__init__(pos=pos, color=color, up=up, right=right, vertical=vertical,closedColor=thrownColor,thrownColor=closedColor)

    def paintVertical(self):
        dx = 1
        if(self._right):
            dx = -1
        if self._up:
            dx = dx*-1

        pos = self._pos
        swPoint = pos.move(delta=(0, 2))
        swPoint._pos='t'
        self._switch._pos=swPoint
        
        # Down
        thPoint = pos.move(delta=(0, 3))
        thPoint._pos='b'
        clPoint = pos.move(delta=(-dx, 3))
        clPoint._pos='b'
        stPoint = pos.move( (dx, -0))
        stPoint._pos='t'

        if(self._up):
            thPoint = pos.move( delta=(0, 0))
            thPoint._pos='t'
            clPoint = pos.move( delta=(dx, 0))
            clPoint._pos='t'
            stPoint =  pos.move((-dx, 3))
            stPoint._pos='b'

        dwg = self._panel._dwg
        
        cutLayer = self._panel._cLayer
        ledLayer = self._panel._lLayer
        self.drawHalfTurnout(dwg, stPoint, cutLayer, ledLayer, swPoint, thPoint, clPoint)

    def paintHorizontal(self):
        dy = 1
        if(self._up):
            dy = -1

        if not self._right:
            dy = dy*-1
        pos = self._pos

        # left
        swPoint = pos.move(delta=(2, 0))
        swPoint._pos='l'
        self._switch._pos=swPoint

        thPoint = pos.move(delta=(0, 0))
        thPoint._pos='l'
        clPoint = pos.move( delta=(0, -dy))
        clPoint._pos='l'
        stPoint =pos.move((3, dy))
        stPoint._pos='r'

        if(self._right):
            #swPointH = pointH(pos=pos, delta=(2, 0))
            #swStart = pointH(pos=pos, delta=(2, 0), adjust=(-5, -7.5))
            thPoint = pos.move(delta=(3, 0))
            thPoint._pos='r'
            clPoint = pos.move(delta=(3, dy))
            clPoint._pos='r'
            stPoint = pos.move( (0, -dy))
            stPoint._pos='l'

        dwg = self._panel._dwg
        
        cutLayer = self._panel._cLayer
        ledLayer = self._panel._lLayer

        swSize = SWITH_SIZE
        self.drawHalfTurnout(dwg, stPoint, cutLayer, ledLayer, swPoint, thPoint, clPoint)