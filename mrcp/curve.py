from mrcp.panel import *
from mrcp.points import *

class Curve(BaseElement):
    def __init__(self, pos=(0,0), color=COLOR_TRACK_DEFAULT,radius=2,left=True, up=True) -> None:
        super().__init__(pos=pos, color=color)
        self._radius=radius
        self._left=left
        self._up=up

    def paint(self):
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
        
        pa=pointC(self._pos,(dx*delta1,dy*delta2))
        sa=pointV(self._pos,(dx*delta1,dsy))
        pb=pointC(self._pos,(dx*delta2,dy*delta1))
        sb=pointH(self._pos,(dsx,dy*delta1))
        line=self._panel._dwg.line(start=sa,end=pa,stroke=self._color, stroke_width=TRACK_SIZE)
        self._panel._tLayer.add(line)
        line=self._panel._dwg.line(start=pa,end=pb,stroke=self._color, stroke_width=TRACK_SIZE)
        self._panel._tLayer.add(line)
        line=self._panel._dwg.line(start=pb,end=sb,stroke=self._color, stroke_width=TRACK_SIZE)
        self._panel._tLayer.add(line)
        circle=self._panel._dwg.circle(center=pa,r=TRACK_SIZE/2,stroke="none", fill=self._color)
        self._panel._tLayer.add(circle)
        circle=self._panel._dwg.circle(center=pb,r=TRACK_SIZE/2,stroke="none", fill=self._color)
        self._panel._tLayer.add(circle)


class OutCurve(BaseElement):
    def __init__(self, pos=(0,0), color=COLOR_TRACK_DEFAULT,right=True, up=True, vertical=False) -> None:
        super().__init__(pos=pos, color=color)
        self._right=right
        self._up=up
        self._vertical=vertical

    def paint(self):
        super().paint()
        dy = 1
        if(self._up):
            dy = -1
        pos = self._pos
        layer = self._panel._tLayer
        dwg = self._panel._dwg

        thHalfPointH =(0,0)
        thPointH = (0,0)
        thEnd = (0,0)
        if self._vertical:
            thHalfPointH = pointV(pos=pos, delta=(0, 0))
            thPointH = pointV(pos=pos, delta=(-1,2*dy))
            thEnd = pointV(pos=pos, delta=(-1, 4*dy))
            if self._right:
                thHalfPointH = pointV(pos=pos, delta=(0, 0))
                thPointH = pointV(pos=pos, delta=(1, 2*dy))
                thEnd = pointV(pos=pos, delta=(1,4*dy))   
        else:
            thHalfPointH = pointH(pos=pos, delta=(4, 0))
            thPointH = pointH(pos=pos, delta=(2, dy))
            thEnd = pointH(pos=pos, delta=(0, dy))
            if self._right:
                thHalfPointH = pointH(pos=pos, delta=(0, 0))
                thPointH = pointH(pos=pos, delta=(2, dy))
                thEnd = pointH(pos=pos, delta=(4, dy))

        line = dwg.line(start=thPointH, end=thEnd, stroke=self._color, stroke_width=TRACK_SIZE)
        layer.add(line)
        line = dwg.line(start=thHalfPointH, end=thPointH,
                    stroke=self._color, stroke_width=TRACK_SIZE)
        layer.add(line)
        circle = dwg.circle(center=thPointH, r=TRACK_SIZE/2, fill=self._color)
        layer.add(circle)

