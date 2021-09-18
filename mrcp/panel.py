from mrcp.points import pointC, pointH
from mrcp.config import GRID_SIZE
import svgwrite
from svgwrite.extensions import Inkscape

class BaseElement(object):
    def __init__(self,pos=(0,0),color="black") -> None:
        super().__init__()
        self._pos=pos
        self._color=color
        self._panel=None

    def attach(self,panel):
        self._panel=panel
    
    def paint(self):
        pass

class Panel(object):
    def __init__(self, name, width, height):
        svgWidht = '{}cm'.format(width/10)
        svgHeight = '{}cm'.format(height/10)
        print(svgWidht + ' ' + svgHeight)

        self._dwg = svgwrite.Drawing(name, size=(svgWidht, svgHeight),
                                     profile='full', debug=True)
        # set user coordinate space
        self._dwg.viewbox(width=width, height=height)
        self._inkscape = Inkscape(self._dwg)
        self.grid((width, height))
        self._tLayer = self._inkscape.layer(label="Track", locked=True)
        self._dwg.add(self._tLayer)
        self._cLayer = self._inkscape.layer(label="Cut", locked=True)
        self._dwg.add(self._cLayer)
        self._lLayer = self._inkscape.layer(label="Led", locked=True)
        self._dwg.add(self._lLayer)
        self._elements=[]
        self._mark=False

    def grid(self, size):
        layer = self._inkscape.layer(label="GridLayer", locked=True)
        self._dwg.add(layer)
        patternSmall = self._dwg.defs.add(self._dwg.pattern(
            size=(GRID_SIZE, GRID_SIZE), patternUnits="userSpaceOnUse"))
        path = 'M {} 0 L 0 0 0 {}'.format(GRID_SIZE, GRID_SIZE)
        patternSmall.add(self._dwg.path(d=path, stroke=svgwrite.rgb(
            0, 0, 200, '%'), stroke_width=0.1, fill="none"))

        patternBig = self._dwg.defs.add(self._dwg.pattern(
            size=(GRID_SIZE*4, GRID_SIZE*4), patternUnits="userSpaceOnUse"))

        path = 'M {} 0 L 0 0 0 {}'.format(GRID_SIZE*4, GRID_SIZE*4)
        patternBig.add(self._dwg.rect(
            size=(20, 20), fill=patternSmall.get_paint_server()))
        patternBig.add(self._dwg.path(d=path, stroke=svgwrite.rgb(
            0, 0, 200, '%'), stroke_width=0.2, fill="none"))
        layer.add(self._dwg.rect(size=size, fill="white"))
        layer.add(self._dwg.rect(size=size, fill=patternBig.get_paint_server()))

    def add(self, element:BaseElement, pos=None):
        self._elements.append(element)
        element.attach(self)
        if pos != None:
            element._pos=pos
            if self._mark: self.mark(pos)

    def paint(self):
        for element in self._elements:
            element.paint()
    
    def markStart(self,mark=True):
        self._mark=mark

    def mark(self,point=(0,9)):
        point=pointC(point)
        circle = self._dwg.circle(center=point, r=0.5, stroke="red",
                            stroke_width=0.2, fill="yellow")
        self._lLayer.add(circle)
    def markC(self,point=(0,9)):
        circle = self._dwg.circle(center=point, r=0.5, stroke="red",
                            stroke_width=0.2, fill="yellow")
        self._lLayer.add(circle)
