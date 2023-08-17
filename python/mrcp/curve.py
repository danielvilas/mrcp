from mrcp.panel import *
from mrcp.points import *
from mrcp.track import *

class Curve(BaseElement):
    def __init__(self, pos=(0,0), color=None,radius=2,left=True, up=True) -> None:
        super().__init__(pos=pos, color=color)
        self._radius=radius
        self._left=left
        self._up=up
        self._tracks=[Track(color=color),Track(color=color),Track(color=color)]

    def attach(self, panel):
        for track in self._tracks:
            track.attach(panel)
        return super().attach(panel)

    def paint(self):
        if self._color is None:
            self._color= self._config.COLOR_TRACK_DEFAULT
        delta1=1+2*self._radius;
        delta2=2*(self._radius-1);

        dx=1;
        dsy=0;
        dsx=0;
        dy=1;

        if self._left:
            dx=-1;
            dsx=1

        if self._up:
            dy=-1
            dsy=1
        
        #pa=pointC(self._pos,(dx*delta1,dy*delta2))
        pa=self._pos.move((dx*delta1,dy*delta2))
        pa._pos='c'
        #sa=pointV(self._pos,(dx*delta1,dsy))
        sa=self._pos.move((dx*delta1,dsy))
        sa._pos='t'
        #pb=pointC(self._pos,(dx*delta2,dy*delta1))
        pb=self._pos.move((dx*delta2,dy*delta1))
        pb._pos='c'
        #sb=pointH(self._pos,(dsx,dy*delta1))
        sb=self._pos.move((dsx,dy*delta1))
        sb._pos='l'
        self._tracks[0]._pos=sa
        self._tracks[0]._end=pa
        self._tracks[0].paint()

        self._tracks[1]._pos=pa
        self._tracks[1]._end=pb
        self._tracks[1].paint()

        self._tracks[2]._pos=pb
        self._tracks[2]._end=sb
        self._tracks[2].paint()
    
        circle=self._panel._dwg.circle(center=pa.toCoords(self._config,place='c'),r=self._config.TRACK_SIZE/2,stroke="none", fill=self._color)
        self._panel._tLayer.add(circle)
        circle=self._panel._dwg.circle(center=pb.toCoords(self._config,place='c'),r=self._config.TRACK_SIZE/2,stroke="none", fill=self._color)
        self._panel._tLayer.add(circle)


class OutCurve(BaseElement):
    def __init__(self, pos=(0,0), color=None,right=True, up=True, vertical=False) -> None:
        super().__init__(pos=pos, color=color)
        self._right=right
        self._up=up
        self._vertical=vertical
        self._tracks=[Track(color=color),Track(color=color)]
    def attach(self, panel):
        for track in self._tracks:
            track.attach(panel)

        return super().attach(panel)


    def paint(self):
        if self._color is None:
            self._color= self._config.COLOR_TRACK_DEFAULT
        super().paint()
        dy = 1
        if(self._up):
            dy = -1
        pos = self._pos

        thHalfPoint =Point(0,0)
        thPoint = Point(0,0)
        thEnd = Point(0,0)
        if self._vertical:
            thHalfPoint =pos.move(delta=(0, 0))
            thPoint = pos.move(delta=(-1,2*dy))
            thEnd = pos.move( delta=(-1, 4*dy))
            if self._right:
                thHalfPoint = pos.move(delta=(0, 0))
                thPoint = pos.move( delta=(1, 2*dy))
                thEnd = pos.move(delta=(1,4*dy))
            thEnd._pos='t'
            thPoint._pos='t'
            thHalfPoint._pos='t'
        else:
            thHalfPoint = pos.move(delta=(4, 0))
            thPoint = pos.move(delta=(2, dy))
            thEnd = pos.move( delta=(0, dy))
            if self._right:
                thHalfPoint = pos.move(delta=(0, 0))
                thPoint = pos.move(delta=(2, dy))
                thEnd = pos.move( delta=(4, dy))
            thEnd._pos='l'
            thPoint._pos='l'
            thHalfPoint._pos='l'
        
        self._tracks[0]._pos=thPoint
        self._tracks[0]._end=thEnd
        self._tracks[1]._pos=thHalfPoint
        self._tracks[1]._end=thPoint

        circle = self._panel._dwg.circle(center=thPoint.toCoords(self._config), r=self._config.TRACK_SIZE/2, fill=self._color)
        self._panel._tLayer.add(circle)
        for track in self._tracks:
            track.paint()

