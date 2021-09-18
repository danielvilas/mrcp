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