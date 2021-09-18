
from mrcp.panel import *
from mrcp.points import *
from mrcp.config import *
from mrcp.curve import OutCurve


class HalfTurnout(BaseElement):
    def __init__(self, pos=(0, 0), color="Black", up=True, right=True, vertical=False) -> None:
        super().__init__(pos=pos, color=color)
        self._up = up
        self._right = right
        self._vertical = vertical

    def paint(self):
        super().paint()
        if self._vertical:
            self.paintVertical()
        else:
            self.paintHorizontal()

    def paintVertical(self):
        dx = -1
        if(self._right):
            dx = 1
        pos = self._pos
        # left
        swPointH = pointV(pos=pos, delta=(0, 2))
        swStart = pointV(pos=pos, delta=(0, 2), adjust=(-7.5, -5))

        thPointH = pointV(pos=pos, delta=(dx, 4))
        clPointH = pointV(pos=pos, delta=(0, 4))
        stPointH = pointV(pos)
        if(self._up):
            #swPointH = pointH(pos=pos, delta=(2, 0))
            #swStart = pointH(pos=pos, delta=(2, 0), adjust=(-5, -7.5))
            thPointH = pointV(pos=pos, delta=(dx, 0))
            clPointH = pointV(pos=pos)
            stPointH = pointV(pos, (0, 4))

        dwg = self._panel._dwg
        layer = self._panel._tLayer
        cutLayer = self._panel._cLayer
        ledLayer = self._panel._lLayer

        swSize = SWITH_SIZE_H
        self.drawHalfTurnout(dwg, self._color, stPointH, layer, cutLayer,
                             ledLayer, swPointH, swStart, thPointH, clPointH, swSize)

    def paintHorizontal(self):
        dy = 1
        if(self._up):
            dy = -1
        pos = self._pos
        # left
        swPointH = pointH(pos=pos, delta=(2, 0))
        swStart = pointH(pos=pos, delta=(2, 0), adjust=(-5, -7.5))

        thPointH = pointH(pos=pos, delta=(0, dy))
        clPointH = pointH(pos=pos)
        stPointH = pointH(pos, (4, 0))
        if(self._right):
            #swPointH = pointH(pos=pos, delta=(2, 0))
            #swStart = pointH(pos=pos, delta=(2, 0), adjust=(-5, -7.5))
            thPointH = pointH(pos=pos, delta=(4, dy))
            clPointH = pointH(pos=pos, delta=(4, 0))
            stPointH = pointH(pos)

        dwg = self._panel._dwg
        layer = self._panel._tLayer
        cutLayer = self._panel._cLayer
        ledLayer = self._panel._lLayer

        swSize = SWITH_SIZE
        self.drawHalfTurnout(dwg, self._color, stPointH, layer, cutLayer,
                             ledLayer, swPointH, swStart, thPointH, clPointH, swSize)

    def drawHalfTurnout(self, dwg, color, stPointH, layer, cutLayer, ledLayer, swPointH, swStart, thPointH, clPointH, swSize=SWITH_SIZE):
        # Tracks
        # hSegment(dwg,pos=pos,color=color,layer=layer,length=1)
        line = dwg.line(start=stPointH, end=clPointH,
                        stroke=color, stroke_width=5)
        layer.add(line)

        line = dwg.line(start=swPointH, end=thPointH,
                        stroke=color, stroke_width=5)
        layer.add(line)
        # Switch
        circle = dwg.circle(center=swPointH, r=5/2, fill="white")
        layer.add(circle)
        circle = dwg.circle(center=swPointH, r=5/2, stroke="red",
                            stroke_width=0.2, fill="none")
        cutLayer.add(circle)

        rect = dwg.rect(insert=swStart, size=swSize, stroke="red",
                        stroke_width=0.2, fill="none")
        cutLayer.add(rect)

        # Thrown Led
        circle = dwg.circle(center=thPointH, r=3/2, fill="green")
        ledLayer.add(circle)
        circle = dwg.circle(center=thPointH, r=3/2, stroke="red",
                            stroke_width=0.2, fill="none")
        cutLayer.add(circle)
        # Closed Led
        circle = dwg.circle(center=clPointH, r=3/2, fill="green")
        ledLayer.add(circle)
        circle = dwg.circle(center=clPointH, r=3/2, stroke="red",
                            stroke_width=0.2, fill="none")
        cutLayer.add(circle)


class LadderStep(HalfTurnout):
    def __init__(self, pos=(0, 0), color="Black", up=True, right=True, vertical=False) -> None:
        super().__init__(pos=pos, color=color, up=up, right=right, vertical=vertical)

    def paintVertical(self):
        dx = 1
        if(self._right):
            dx = -1
        if self._up:
            dx = dx*-1

        pos = self._pos
        swPointH = pointV(pos=pos, delta=(0, 2))
        swStart = pointV(pos=pos, delta=(0, 2), adjust=(-7.5, -5))
        # Down
        thPointH = pointV(pos=pos, delta=(0, 4))
        clPointH = pointV(pos=pos, delta=(-dx, 4))
        stPointH = pointV(pos, (dx, -0))

        if(self._up):
            #swPointH = pointH(pos=pos, delta=(2, 0))
            #swStart = pointH(pos=pos, delta=(2, 0), adjust=(-5, -7.5))
            thPointH = pointV(pos=pos, delta=(0, 0))
            clPointH = pointV(pos=pos, delta=(dx, 0))
            stPointH = pointV(pos, (-dx, 4))

        dwg = self._panel._dwg
        layer = self._panel._tLayer
        cutLayer = self._panel._cLayer
        ledLayer = self._panel._lLayer
        swSize = SWITH_SIZE_H
        self.drawHalfTurnout(dwg, self._color, stPointH, layer, cutLayer,
                             ledLayer, swPointH, swStart, thPointH, clPointH, swSize)

    def paintHorizontal(self):
        dy = 1
        if(self._up):
            dy = -1

        if not self._right:
            dy = dy*-1
        pos = self._pos

        # left
        swPointH = pointH(pos=pos, delta=(2, 0))
        swStart = pointH(pos=pos, delta=(2, 0), adjust=(-5, -7.5))

        thPointH = pointH(pos=pos, delta=(0, 0))
        clPointH = pointH(pos=pos, delta=(0, -dy))
        stPointH = pointH(pos, (4, dy))

        if(self._right):
            #swPointH = pointH(pos=pos, delta=(2, 0))
            #swStart = pointH(pos=pos, delta=(2, 0), adjust=(-5, -7.5))
            thPointH = pointH(pos=pos, delta=(4, 0))
            clPointH = pointH(pos=pos, delta=(4, dy))
            stPointH = pointH(pos, (0, -dy))

        dwg = self._panel._dwg
        layer = self._panel._tLayer
        cutLayer = self._panel._cLayer
        ledLayer = self._panel._lLayer

        swSize = SWITH_SIZE
        self.drawHalfTurnout(dwg, self._color, stPointH, layer, cutLayer,
                             ledLayer, swPointH, swStart, thPointH, clPointH, swSize)


class Turnout(BaseElement):
    def __init__(self, pos=(0, 0), color="Black", up=True, right=True, vertical=False) -> None:
        super().__init__(pos=pos, color=color)
        self._up = up
        self._right = right
        self._vertical = vertical
        self._halfTurnout = HalfTurnout(
            pos=pos, color=color, up=up, right=right, vertical=vertical)
        self._outCurve = OutCurve(
            pos=pos, color=color, right=right, up=up, vertical=vertical)

    def paint(self):
        super().paint()
        if(self._vertical):
            if(self._up):
                self._halfTurnout._pos = movePoint(self._pos, (0, 4))
            else:
                self._halfTurnout._pos = self._pos
        else:
            if(self._right):
                self._halfTurnout._pos = self._pos
            else:
                self._halfTurnout._pos = movePoint(self._pos, (4, 0))

        self._halfTurnout.paint()

        dx = 0
        dy = 0
        if self._vertical:
            dx = -1
            dy = 4
            if self._right:
                dx = 1
            if self._up:
                dy = 4
        else:
            dx = 0
            dy = 1
            if self._right:
                dx = 4
            if self._up:
                dy = -1

        self._outCurve._pos = movePoint(self._pos, (dx, dy))
        self._outCurve.paint()

        # TODO move to obj
        start = (0, 0)
        end = (0, 0)
        if self._vertical:
            start = pointV(pos=self._pos, delta=(0, 4))
            end = pointV(pos=self._pos, delta=(0, 8))
            if self._up:
                start = pointV(pos=self._pos, delta=(0, 0))
                end = pointV(pos=self._pos, delta=(0, 4))

        else:
            start = pointH(pos=self._pos, delta=(0, 0))
            end = pointH(pos=self._pos, delta=(4, 0))
            if self._right:
                start = pointH(pos=self._pos, delta=(4, 0))
                end = pointH(pos=self._pos, delta=(8, 0))

        line = self._panel._dwg.line(
            start=start, end=end, stroke=self._color, stroke_width=5)
        self._panel._tLayer.add(line)

    def attach(self, panel):
        self._halfTurnout.attach(panel)
        self._outCurve.attach(panel)
        return super().attach(panel)


class CurveTurnOut_2_3(BaseElement):
    def __init__(self, pos=(0, 0), color="Black", up=True, right=True, vertical=False) -> None:
        super().__init__(pos=pos, color=color)
        self._up = up
        self._right = right
        self._vertical = vertical
        self._halfTurnout = HalfTurnout(
            pos=pos, color=color, up=up, right=right, vertical=vertical)

    def attach(self, panel):
        self._halfTurnout.attach(panel)
        return super().attach(panel)


    def paintCurves(self,dwg,layer,thPoint,thEnd,clPoint,clEnd,diag1Start,diag1End,diag2Start,diag2End,outR2,outR3,color):
        line = dwg.line(start=thPoint, end=thEnd, stroke=color, stroke_width=5)
        layer.add(line)
        line = dwg.line(start=clPoint, end=clEnd, stroke=color, stroke_width=5)
        layer.add(line)
        line = dwg.line(start=diag1Start, end=diag1End,
                        stroke=color, stroke_width=5)
        layer.add(line)
        line = dwg.line(start=diag2Start, end=diag2End,
                        stroke=color, stroke_width=5)
        layer.add(line)
        line = dwg.line(start=diag2End, end=outR2, stroke=color, stroke_width=5)
        layer.add(line)
        line = dwg.line(start=diag1End, end=outR3, stroke=color, stroke_width=5)
        layer.add(line)
        circle = dwg.circle(center=diag1End, r=5/2, stroke="none", fill=color)
        layer.add(circle)
        circle = dwg.circle(center=diag2End, r=5/2, stroke="none", fill=color)
        layer.add(circle)
        circle = dwg.circle(center=diag1Start, r=5/2, stroke="none", fill=color)
        layer.add(circle)
        circle = dwg.circle(center=diag2Start, r=5/2, stroke="none", fill=color)
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

        thEnd = pointH(pos, (6*dx+eX, 2*dy))
        #self._panel.markC(thEnd)
        thPoint = pointH(pos, (4*dx+eX, dy))
        #self._panel.markC(thPoint)
        clPoint = pointH(pos, (4*dx+eX, 0))
        #self._panel.markC(clPoint)

        dh=-1
        if(self._right):
            dh = 0

        clEnd = pointC(pos, (7*dx+eX+dh, 0))
        #self._panel.markC(clEnd)
        
        diag1Start = clEnd
        diag1End = pointC(pos, (9*dx+eX+dh, 2*dy))
        #self._panel.markC(diag1End)
        diag2Start = thEnd
        
        diag2End = pointV(pos, (dx*7, 4*dy))
        #self._panel.markC(diag2End)
        outR2 = pointV(pos, (7*dx, 6*dy))
        outR3 = pointV(pos, (9*dx, 6*dy))
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

        thEnd = pointV(pos, (2*dx, 6*dy+eY))
        thPoint = pointV(pos, (dx, 4*dy+eY))
        clPoint = pointV(pos, (0, 4*dy+eY))
        clEnd = pointC(pos, (0, 7*dy+eY))

        diag1Start = clEnd
        diag1End = pointC(pos, (2*dx, 9*dy+eY))
        diag2Start = thEnd
        
        dh=1
        if(self._right):
            dh = 0

        diag2End = pointH(pos, (dx*4+dh, 7*dy+eY))
        outR2 = pointH(pos, (6*dx+dh, 7*dy+eY))
        outR3 = pointH(pos, (6*dx+dh, 9*dy+eY))
        self.paintCurves(dwg,layer,thPoint,thEnd,clPoint,clEnd,diag1Start,diag1End,diag2Start,diag2End,outR2,outR3,self._color)

    def paint(self):
        super().paint()
        if self._vertical:
            self.paintVertical()
        else:
            self.paintHorizontal()
