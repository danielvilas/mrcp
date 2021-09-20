from mrcp.curve import OutCurve
from mrcp.turnouts import HalfTurnout, LadderStep
from mrcp.panel import *
from mrcp.points import *

class Ladder(BaseElement):
    def __init__(self, pos=(0, 0), color=COLOR_TRACK_DEFAULT, up=True, right=True, vertical=False) -> None:
        super().__init__(pos=pos, color=color)
        self._up = up
        self._right = right
        self._vertical = vertical
        self._steps=[]
        start=HalfTurnout(color=color,up=up,right=right,vertical=vertical)
        self._steps.append(start)
        self._endCurve=True

    def attach(self, panel):
        for element in self._steps:
            if element._panel == None:
                element.attach(panel)
        return super().attach(panel)

    def paint(self):
        incX=-4
        if self._right:
            incX=4
        incY=2
        cy=-1
        if self._up :
            incY =-2
            cy=1
        ax=0
        ay=0

        for element in self._steps:
            element._pos=movePoint(self._pos,(ax,ay))
            element.paint()
            ax += incX
            ay += incY
    
        if self._endCurve:
            end = OutCurve(color=self._color,right=self._right,up=self._up)
            end.attach(self._panel)
            end._pos=movePoint(self._pos,(ax,ay+cy))
            end.paint()
        return super().paint()
    
    def addStep(self):
        step = LadderStep(color=self._color, up=self._up,right=self._right,vertical=self._vertical)
        self._steps.append(step)
        if self._panel != None:
            step.attach(self._panel)

    def endContraTurnout(self):

        step = HalfTurnout(color=self._color, up=not self._up,right=not self._right,vertical=self._vertical)
        self._steps.append(step)
        if self._panel != None:
            step.attach(self._panel)
        self._endCurve=False