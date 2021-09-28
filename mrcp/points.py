from mrcp.config import *
import sys

def pointC(pos=(0,0),delta=(0,0), adjust=(0,0)):
    if isinstance(pos, Point):
        frame = sys._getframe(1)
        print("Converting Point to Tuple: (", pos._x,",",pos._y,") ",frame.f_code.co_name,frame.f_code.co_filename,frame.f_lineno)
        return pos.move(delta).toCoords(adjust)
    x, y =pos
    dx, dy = delta
    ax, ay= adjust
    ay=ay+2.5
    ax=ax+2.5
    xf=(x+dx)*GRID_SIZE+ax
    yf=(y+dy)*GRID_SIZE+ay
    return (xf,yf)

def pointH(pos=(0,0),delta=(0,0),adjust=(0,0)):
    if isinstance(pos, Point):
        frame = sys._getframe(1)
        print("Converting Point to Tuple: (", pos._x,",",pos._y,") ",frame.f_code.co_name,frame.f_code.co_filename,frame.f_lineno)
        pos=(pos._x,pos._y)
    ax,ay=adjust
    return pointC(pos,delta,(ax-2.5,ay))


def pointV(pos=(0,0),delta=(0,0), adjust=(0,0)):
    if isinstance(pos, Point):
        frame = sys._getframe(1)
        print("Converting Point to Tuple: (", pos._x,",",pos._y,") ",frame.f_code.co_name,frame.f_code.co_filename,frame.f_lineno)
        pos=(pos._x,pos._y)
    ax,ay=adjust
    return pointC(pos,delta,(ax,ay-2.5))

def movePoint(pos=(0,0),delta=(0,0)):
    if isinstance(pos,Point):
        pos=(pos._x,pos._y)
    if isinstance(delta,Point):
        delta=(delta._x,delta._y)
    x, y =pos
    dx, dy = delta
    return Point(x+dx,y+dy)

class Point(object):
    def __init__(self,x,y, pos=None) -> None:
        super().__init__()
        self._x=x
        self._y=y
        self._pos=pos

    def move(self, delta=(0,0)):
        dx,dy=delta
        return Point(self._x+dx,self._y+dy, self._pos)

    def toCoords(self,adjust=(0,0),place=None):
        if place is None and self._pos != None:
            place = self._pos
        ax,ay=adjust
        if place==None or place=='c':
            ax+=GRID_SIZE/2
            ay+=GRID_SIZE/2
        elif place=='t' or place=='v':
            ax+=GRID_SIZE/2
        elif place=='l' or place=='h':
            ay+=GRID_SIZE/2
        elif place=='b':
            ax+=GRID_SIZE/2
            ay+=GRID_SIZE
        elif place=='r':
            ay+=GRID_SIZE/2
            ax+=GRID_SIZE
        elif place=='bl':
            ay+=GRID_SIZE
        elif place=='br':
            ay+=GRID_SIZE
            ax+=GRID_SIZE
        elif place=='tl':
            ay+=0
        elif place=='tr':
            ax+=GRID_SIZE
        xf=(self._x)*GRID_SIZE+ax
        yf=(self._y)*GRID_SIZE+ay
        return (xf,yf)

        