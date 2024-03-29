from typing import Tuple
from mrcp.points import Point, pointC, pointH
import svgwrite
from svgwrite.extensions import Inkscape
from mrcp.config import *
import sys

class BaseElement(object):
    def __init__(self,pos=Point(0,0),color=None) -> None:
        super().__init__()
        self._pos=pos
        self._color=color
        self._panel=None
        self._config=None

    def attach(self,panel):
        self._panel=panel
        self._config=panel._config
        panel.register(self)
    
    def paint(self):
        pass

class Panel(object):
    def __init__(self, name, width, height, config=None, sizeInGrid=False):
        
        if config is None:
            config=Config()
        self._config=config
        if(sizeInGrid is True):
            width=width*config.GRID_SIZE
            height=height*config.GRID_SIZE

        svgWidht = '{}cm'.format(width/10)
        svgHeight = '{}cm'.format(height/10)
        print("Panel: "+name+" "+ svgWidht + ' ' + svgHeight)
        
        self._dwg = svgwrite.Drawing(name, size=(svgWidht, svgHeight),
                                     profile='full', debug=True)
        # set user coordinate space
        self._dwg.viewbox(width=width, height=height)
        self._inkscape = Inkscape(self._dwg)
        
        self._gLayer = self._inkscape.layer(label="Grid", locked=True)
        self._dwg.add(self._gLayer)        
        
        self._tLayer = self._inkscape.layer(label="Track", locked=True)
        self._dwg.add(self._tLayer)
        self._cLayer = self._inkscape.layer(label="Cut", locked=True)
        self._dwg.add(self._cLayer)
        self._lLayer = self._inkscape.layer(label="Led", locked=True)
        self._dwg.add(self._lLayer)
        self._oLayer = self._inkscape.layer(label="Outs", locked=True)
        self._dwg.add(self._oLayer)
        self._elements=[]
        self._mark=False
        self._size=(width, height)
        self._paintable=[]

    def grid(self, size=None):
        if size == None:
            size=self._size
        layer = self._gLayer
        patternSmall = self._dwg.defs.add(self._dwg.pattern(
            size=(self._config.GRID_SIZE, self._config.GRID_SIZE), patternUnits="userSpaceOnUse"))
        path = 'M {} 0 L 0 0 0 {}'.format(self._config.GRID_SIZE, self._config.GRID_SIZE)
        patternSmall.add(self._dwg.path(d=path, stroke=svgwrite.rgb(
            0, 0, 200, '%'), stroke_width=0.1, fill="none"))

        patternBig = self._dwg.defs.add(self._dwg.pattern(
            size=(self._config.GRID_SIZE*4, self._config.GRID_SIZE*4), patternUnits="userSpaceOnUse"))

        path = 'M {} 0 L 0 0 0 {}'.format(self._config.GRID_SIZE*4, self._config.GRID_SIZE*4)
        patternBig.add(self._dwg.rect(
            size=(self._config.GRID_SIZE*4, self._config.GRID_SIZE*4), fill=patternSmall.get_paint_server()))
        patternBig.add(self._dwg.path(d=path, stroke=svgwrite.rgb(
            0, 0, 200, '%'), stroke_width=0.2, fill="none"))
        layer.add(self._dwg.rect(size=size, fill="white"))
        layer.add(self._dwg.rect(size=size, fill=patternBig.get_paint_server()))

    def margin(self,margin=10,radius=0):
        width, height = self._size
        rectSize=(width-2*margin,height-2*margin)
        rect = self._dwg.rect(insert=(margin,margin),size=rectSize,fill="none", stroke_width=0.2, stroke=self._config.COLOR_ENGRAVE)
        self._oLayer.add(rect)

    def register(self, element:BaseElement):
        if element in self._paintable:
            print("twice register of",element)
            return
        self._paintable.append(element)
        # if element in self._elements:
        #     print("Register a element")
        # else:
        #     print("Register a sub-element")

    
    def add(self, element:BaseElement, pos=None):
        self._elements.append(element)
        element.attach(self)
        if pos != None:
            if isinstance(pos,Tuple):
                frame = sys._getframe(1)
                print("Converting Tuple to Pos: ", pos," ",frame.f_code.co_name,frame.f_code.co_filename,frame.f_lineno)
                x,y=pos
                pos= Point(x,y)
            element._pos=pos
            if self._mark: self.mark(pos)

    def paint(self):
        for element in self._elements:
            element.paint()
        self._oLayer.add(self._dwg.rect(size=self._size, fill="none",stroke=self._config.COLOR_CUT,stroke_width=0.2))
        
    
    def markStart(self,mark=True):
        self._mark=mark

    def mark(self,point=Point(0,9)):
        if isinstance(point, Tuple):
            print("Converting Tuple to Pos: ", point," ",sys._getframe(1).f_code.co_name)
            x,y=point
            point= Point(x,y)
        point=point.toCoords(self._config)
        circle = self._dwg.circle(center=point, r=0.5, stroke="red",
                            stroke_width=0.2, fill="yellow")
        self._lLayer.add(circle)
    def markC(self,point=(0,9)):
        circle = self._dwg.circle(center=point, r=0.5, stroke="red",
                            stroke_width=0.2, fill="yellow")
        self._lLayer.add(circle)


    def markPoint(self,point:Point):
        self.markC(point.toCoords(self._config))