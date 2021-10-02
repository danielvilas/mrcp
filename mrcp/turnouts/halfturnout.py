from mrcp.track import Track
from mrcp.panel import *
from mrcp.points import *
from mrcp.config import *
from mrcp.switch import *
from mrcp.led import *

class HalfTurnout(BaseElement):
    def __init__(self, pos=(0, 0), color=COLOR_TRACK_DEFAULT, thrownTrackColor=None, up=True, right=True, vertical=False,closedColor=CLOSED_LED_COLOR,thrownColor=THROWN_LED_COLOR) -> None:
        super().__init__(pos=pos, color=color)
        if thrownTrackColor==None:
            thrownTrackColor=color;

        self._up = up
        self._right = right
        self._vertical = vertical
        self._mainTrack= Track(color=color)
        self._thrownTrack=Track(color=thrownTrackColor)
        self._switch=Switch(color=color, vertical=not vertical)
        self._ledCl= Led(color=closedColor)
        self._ledTh= Led(color=thrownColor)


    def paint(self):
        super().paint()
        if self._vertical:
            self.paintVertical()
        else:
            self.paintHorizontal()
        self._thrownTrack.paint()
        self._mainTrack.paint()
        self._switch.paint()
        self._ledCl.paint()
        self._ledTh.paint()

    def attach(self, panel):
        self._mainTrack.attach(panel)
        self._thrownTrack.attach(panel)
        self._switch.attach(panel)
        self._ledCl.attach(panel)
        self._ledTh.attach(panel)
        return super().attach(panel)

    def paintVertical(self):
        dx = -1
        if(self._right):
            dx = 1
        pos = self._pos
        # left

        swPoint = pos.move(delta=(0, 2))
        swPoint._pos='t'
        self._switch._pos=swPoint

        thPoint = pos.move((dx, 3))
        thPoint._pos='b'
    
        clPoint = pos.move((0,3))
        clPoint._pos='b'
        stPoint = pos.move()
        stPoint._pos='t'


        if(self._up):
            #swPoint = pointH(pos=pos, delta=(2, 0))
            #swStart = pointH(pos=pos, delta=(2, 0), adjust=(-5, -7.5))
            thPoint = pos.move((dx, 0))
            thPoint._pos='t'
            clPoint = pos.move()
            clPoint._pos='t'
            stPoint = pos.move((0, 3))
            stPoint._pos='b'

        dwg = self._panel._dwg
        layer = self._panel._tLayer
        cutLayer = self._panel._cLayer
        ledLayer = self._panel._lLayer

        swSize = SWITH_SIZE_H
        self.drawHalfTurnout(dwg, stPoint, cutLayer, ledLayer, swPoint, thPoint, clPoint)

    def paintHorizontal(self):
        dy = 1
        if(self._up):
            dy = -1
        pos = self._pos
        # left
        swPoint = pos.move((2,0))
        swPoint._pos='l'
        self._switch._pos=swPoint
        

        thPoint = pos.move((0,dy))
        thPoint._pos='l'
        clPoint = pos.move()
        clPoint._pos='l'
        stPoint = pos.move((3,0))
        stPoint._pos='r'
        if(self._right):
            #swPoint = pointH(pos=pos, delta=(2, 0))
            #swStart = pointH(pos=pos, delta=(2, 0), adjust=(-5, -7.5))
            thPoint = pos.move((3,dy))
            thPoint._pos='r'
            clPoint = pos.move((3, 0))
            clPoint._pos='r'
            stPoint = pos.move()
            stPoint._pos='l'

        dwg = self._panel._dwg
        cutLayer = self._panel._cLayer
        ledLayer = self._panel._lLayer

        swSize = SWITH_SIZE
        self.drawHalfTurnout(dwg, stPoint, cutLayer, ledLayer, swPoint, thPoint, clPoint)

    def drawHalfTurnout(self, dwg, stPoint, cutLayer, ledLayer, swPoint, thPoint, clPoint):
        self._mainTrack._pos=stPoint
        self._mainTrack._end=clPoint

        self._thrownTrack._pos=swPoint
        self._thrownTrack._end=thPoint

        self._ledTh._pos=thPoint
        self._ledCl._pos=clPoint

        if isinstance(stPoint, tuple):
            print("tuple stPoint on drawHalfTurnout")
        
        if isinstance(clPoint, tuple):
            print("tuple clPoint on drawHalfTurnout")
        else:
            clPoint=clPoint.toCoords()
        if isinstance(swPoint, tuple):
            print("tuple swPoint on drawHalfTurnout")
        else:
            swPoint=swPoint.toCoords()
        if isinstance(thPoint, tuple):
            print("tuple thPoint on drawHalfTurnout")
        else:
            thPoint=thPoint.toCoords()


        # Thrown Led

        # Closed Led
    