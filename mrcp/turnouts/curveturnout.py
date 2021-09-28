from mrcp.panel import *
from mrcp.points import *
from .halfturnout import *


class CurveTurnOut_2_3(BaseElement):
    def __init__(self, pos=(0, 0), color=COLOR_TRACK_DEFAULT, up=True, right=True, vertical=False) -> None:
        super().__init__(pos=pos, color=color)
        self._up = up
        self._right = right
        self._vertical = vertical
        self._halfTurnout = HalfTurnout(
            pos=pos, color=color, up=up, right=right, vertical=vertical)
        self._tracks=[Track(color=color),Track(color=color),Track(color=color),
                      Track(color=color),Track(color=color),Track(color=color)]

    def attach(self, panel):
        self._halfTurnout.attach(panel)
        for track in self._tracks:
            track.attach(panel)

        return super().attach(panel)


    def paintCurves(self,dwg,layer,thPoint,thEnd,clPoint,clEnd,diag1Start,diag1End,diag2Start,diag2End,outR2,outR3,color):

        self._tracks[0]._pos=thPoint
        self._tracks[0]._end=thEnd
        self._tracks[1]._pos=diag2Start
        self._tracks[1]._end=diag2End
        self._tracks[2]._pos=diag2End
        self._tracks[2]._end=outR2


        self._tracks[3]._pos=clPoint
        self._tracks[3]._end=clEnd
        self._tracks[4]._pos=diag1Start
        self._tracks[4]._end=diag1End
        self._tracks[5]._pos=diag1End
        self._tracks[5]._end=outR3


        if isinstance(thEnd, tuple):
            print("tuple thEnd on paintCurves")
        else:
            thEnd=thEnd.toCoords()
        if isinstance(thPoint, tuple):
            print("tuple thPoint on paintCurves")
        else:
            thPoint=thPoint.toCoords()

        if isinstance(diag1Start, tuple):
            print("tuple diag1Start on paintCurves")
        else:
            diag1Start=diag1Start.toCoords()
        if isinstance(diag2Start, tuple):
            print("tuple diag2Start on paintCurves")
        else:
            diag2Start=diag2Start.toCoords()
        if isinstance(clPoint, tuple):
            print("tuple clPoint on paintCurves")
        else:
            clPoint=clPoint.toCoords()
        if isinstance(clEnd, tuple):
            print("tuple clEnd on paintCurves")
        else:
            clEnd=clEnd.toCoords()

        if isinstance(diag1End, tuple):
            print("tuple diag1End on paintCurves")
        else:
            diag1End=diag1End.toCoords()
        if isinstance(diag2End, tuple):
            print("tuple diag2End on paintCurves")
        else:
            diag2End=diag2End.toCoords()


        if isinstance(outR2, tuple):
            print("tuple outR2 on paintCurves")
        else:
            outR2=outR2.toCoords()
        if isinstance(outR3, tuple):
            print("tuple outR3 on paintCurves")
        else:
            outR3=outR3.toCoords()


        circle = dwg.circle(center=diag1End, r=TRACK_SIZE/2, stroke="none", fill=color)
        layer.add(circle)
        circle = dwg.circle(center=diag2End, r=TRACK_SIZE/2, stroke="none", fill=color)
        layer.add(circle)
        circle = dwg.circle(center=diag1Start, r=TRACK_SIZE/2, stroke="none", fill=color)
        layer.add(circle)
        circle = dwg.circle(center=diag2Start, r=TRACK_SIZE/2, stroke="none", fill=color)
        layer.add(circle)

    def paintHorizontal(self):
        self._halfTurnout._pos = self._pos
        eX=0
        if not self._right:
            self._halfTurnout._pos =movePoint(self._pos,(-3,0))
            eX=1
        self._halfTurnout.paint()

        dx = -1
        if(self._right):
            dx = 1
        pos= self._pos
        dwg=self._panel._dwg
        layer=self._panel._tLayer

        dy=1
        if self._up:
            dy=-1
        
        thEnd = pos.move((6*dx+eX, 2*dy))
        thEnd._pos='l'

        thPoint = pos.move((4*dx+eX, dy))
        thPoint._pos='l'

        clPoint = pos.move((4*dx+eX, 0))
        clPoint._pos='l'

        dh=-1
        if(self._right):
            dh = 0

        clEnd = pos.move((7*dx+eX+dh, 0))
        clEnd._pos='c'
        
        diag1Start = clEnd
        diag1End = pos.move((9*dx+eX+dh, 2*dy))
        diag1End._pos='c'
        diag2Start = thEnd
        
        diag2End = pos.move((dx*7, 4*dy))
        diag2End._pos='t'
        outR2 = pos.move((7*dx, 6*dy))
        outR2._pos='t'
        outR3 = pos.move((9*dx, 6*dy))
        outR3._pos='t'
       # self._panel.markC(outR3)
        self.paintCurves(dwg,layer,thPoint,thEnd,clPoint,clEnd,diag1Start,diag1End,diag2Start,diag2End,outR2,outR3,self._color)

    def paintVertical(self):

        self._halfTurnout._pos = self._pos
        eY=0
        if self._up:
            self._halfTurnout._pos =movePoint(self._pos,(0,-3))
            eY=1
        self._halfTurnout.paint()

        dx = -1
        if(self._right):
            dx = 1
        pos= self._pos
        dwg=self._panel._dwg
        layer=self._panel._tLayer

        dy=1
        if self._up:
            dy=-1
        
        thEnd = pos.move((2*dx, 6*dy+eY))
        thEnd._pos='t'

        thPoint = pos.move((dx, 4*dy+eY))
        thPoint._pos='t'
        
        clPoint = pos.move((0, 4*dy+eY))
        clPoint._pos='t'

        clEnd=pos.move((0, 7*dy+eY))
        clEnd._pos='c'

        diag1Start = clEnd
        diag1End = pos.move((2*dx, 9*dy+eY))
        diag1End._pos='c'
        diag2Start = thEnd
        
        dh=1
        if(self._right):
            dh = 0

        diag2End = pos.move((dx*4+dh, 7*dy+eY))
        diag2End._pos='l'
        outR2 = pos.move((6*dx+dh, 7*dy+eY))
        outR2._pos='l'
        outR3 = pos.move((6*dx+dh, 9*dy+eY))
        outR3._pos='l'
        self.paintCurves(dwg,layer,thPoint,thEnd,clPoint,clEnd,diag1Start,diag1End,diag2Start,diag2End,outR2,outR3,self._color)

    def paint(self):
        super().paint()
        if self._vertical:
            self.paintVertical()
        else:
            self.paintHorizontal()
        for track in self._tracks:
            track.paint()