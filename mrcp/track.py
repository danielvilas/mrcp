from mrcp.panel import *
from mrcp.points import *
import math

class Track(BaseElement):
    def __init__(self, pos=Point(0,0), color=COLOR_TRACK_DEFAULT, end=Point(0,0)) -> None:
        super().__init__(pos=pos, color=color)
        self._end=end

        dx=end._x- pos._x
        dy=end._y -pos._y

        if pos._pos==None and end._pos==None:
            if dx == 0 and dy ==0:
                return
            elif dx==0 and dy >0:
                pos._pos='t'
                end._pos='b'
            elif dx==0 and dy <0:
                pos._pos='b'
                end._pos='t'
            elif dy==0 and dx>0:
                pos._pos='l'
                end._pos='r'
            elif dy==0 and dx<0:
                pos._pos='r'
                end._pos='l'
        elif pos._pos == None:
            pos._pos='c'
        elif end._pos == None:
            end.pos_='c'

    def paint(self):
        if isinstance(self._end, tuple):
            print("track end is tuple")
            self._end=Point(0,0)
        if isinstance(self._pos, tuple):
            print("track pos is tuple")
            self._pos=Point(0,0)
    
        end = self._end.toCoords()
        x0,y0=end
        start = self._pos.toCoords()
        xf,yf=start
        dx=xf-x0
        dy=yf-y0
        if dx==0 and dy == 0 :return
        mx=0
        my=0
        t=TRACK_SIZE/2
        if dx==0:
            mx=t
            my=0
        elif dy==0:
            mx=0
            my=t
        else:
            d=math.sqrt(dx*dx+dy*dy)
            dux=dx/d
            duy=dy/d
            mx=t*duy
            my=-t*dux
        points=[(x0-mx,y0-my),(xf-mx,yf-my),(xf+mx,yf+my),(x0+mx,y0+my),(x0-mx,y0-my)]

        color = self._color
        dwg = self._panel._dwg
        layer = self._panel._tLayer
        poly=dwg.polyline(points=points,fill=color,stroke="none")
        layer.add(poly)


        # line = dwg.line(start=start, end=end, stroke="cyan", stroke_width=1)
        # layer.add(line)

        return super().paint()