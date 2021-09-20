from mrcp.config import *

def pointC(pos=(0,0),delta=(0,0), adjust=(0,0)):
    x, y =pos
    dx, dy = delta
    ax, ay= adjust
    ay=ay+2.5
    ax=ax+2.5
    xf=(x+dx)*GRID_SIZE+ax
    yf=(y+dy)*GRID_SIZE+ay
    return (xf,yf)

def pointH(pos=(0,0),delta=(0,0),adjust=(0,0)):
    ax,ay=adjust
    return pointC(pos,delta,(ax-2.5,ay))


def pointV(pos=(0,0),delta=(0,0), adjust=(0,0)):
    ax,ay=adjust
    return pointC(pos,delta,(ax,ay-2.5))

def movePoint(pos=(0,0),delta=(0,0)):
    x, y =pos
    dx, dy = delta
    return (x+dx,y+dy)

class Point(object):
    def __init__(self,x,y, pos=None) -> None:
        super().__init__()
        self._x=x
        self._y=y
        self._pos=pos

    def move(self, delta=(0,0)):
        dx,dy=delta
        return Point(self._x+dx,self._y+dy, self._pos)

    def toCoords(self,adjust=(0,0)):
        ax,ay=adjust
        if self._pos==None or self._pos=='c':
            ax+=GRID_SIZE/2
            ay+=GRID_SIZE/2
        elif self._pos=='t' or self._pos=='v':
            ax+=GRID_SIZE/2
        elif self._pos=='l' or self._pos=='h':
            ay+=GRID_SIZE/2
        elif self._pos=='b':
            ax+=GRID_SIZE/2
            ay+=GRID_SIZE
        elif self._pos=='r':
            ay+=GRID_SIZE/2
            ax+=GRID_SIZE
        xf=(self._x)*GRID_SIZE+ax
        yf=(self._y)*GRID_SIZE+ay
        return (xf,yf)

        