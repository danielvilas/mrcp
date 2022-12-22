from mrcp.config import *
import sys

def pointC(config,pos=(0,0),delta=(0,0), adjust=(0,0)):
    if isinstance(pos, Point):
        frame = sys._getframe(1)
        print("Converting Point to Tuple: (", pos._x,",",pos._y,") ",frame.f_code.co_name,frame.f_code.co_filename,frame.f_lineno)
        return pos.move(delta).toCoords(adjust)
    x, y =pos
    dx, dy = delta
    ax, ay= adjust
    ay=ay+config.GRID_SIZE/2
    ax=ax+config.GRID_SIZE/2
    xf=(x+dx)*config.GRID_SIZE+ax
    yf=(y+dy)*config.GRID_SIZE+ay
    return (xf,yf)

def pointH(config,pos=(0,0),delta=(0,0),adjust=(0,0)):
    if isinstance(pos, Point):
        frame = sys._getframe(1)
        print("Converting Point to Tuple: (", pos._x,",",pos._y,") ",frame.f_code.co_name,frame.f_code.co_filename,frame.f_lineno)
        pos=(pos._x,pos._y)
    ax,ay=adjust
    return pointC(pos,delta,(ax-config.GRID_SIZE/2,ay))


def pointV(config,pos=(0,0),delta=(0,0), adjust=(0,0)):
    if isinstance(pos, Point):
        frame = sys._getframe(1)
        print("Converting Point to Tuple: (", pos._x,",",pos._y,") ",frame.f_code.co_name,frame.f_code.co_filename,frame.f_lineno)
        pos=(pos._x,pos._y)
    ax,ay=adjust
    return pointC(pos,delta,(ax,ay-config.GRID_SIZE/2))

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

    def toCoords(self,config,adjust=(0,0),place=None):
        if place is None and self._pos != None:
            place = self._pos
        ax,ay=adjust
        if place==None or place=='c':
            ax+=config.GRID_SIZE/2
            ay+=config.GRID_SIZE/2
        elif place=='t' or place=='v':
            ax+=config.GRID_SIZE/2
        elif place=='l' or place=='h':
            ay+=config.GRID_SIZE/2
        elif place=='b':
            ax+=config.GRID_SIZE/2
            ay+=config.GRID_SIZE
        elif place=='r':
            ay+=config.GRID_SIZE/2
            ax+=config.GRID_SIZE
        elif place=='bl':
            ay+=config.GRID_SIZE
        elif place=='br':
            ay+=config.GRID_SIZE
            ax+=config.GRID_SIZE
        elif place=='tl':
            ay+=0
        elif place=='tr':
            ax+=config.GRID_SIZE
        xf=(self._x)*config.GRID_SIZE+ax
        yf=(self._y)*config.GRID_SIZE+ay
        return (xf,yf)

        