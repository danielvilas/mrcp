from mrcp.curve import OutCurve
from mrcp.turnouts import HalfTurnout, LadderStep
from mrcp.panel import *
from mrcp.points import *

class Ladder(BaseElement):
    def __init__(self, pos=(0, 0), color=None,thrownTrackColor=None, up=True, right=True, vertical=False,closedColor=None,thrownColor=None) -> None:
        super().__init__(pos=pos, color=color)
        if thrownTrackColor== None:
            thrownTrackColor=color      
        self._up = up
        self._right = right
        self._vertical = vertical
        self._steps=[]
        start=HalfTurnout(color=color,thrownTrackColor=thrownTrackColor,up=up,right=right,vertical=vertical,closedColor=closedColor,thrownColor=thrownColor)
        self._steps.append(start)
        self._endCurve=True
        self._closedColor=closedColor
        self._thrownColor=thrownColor

    def attach(self, panel):
        for element in self._steps:
            if element._panel == None:
                element.attach(panel)
        return super().attach(panel)

    def paint(self):
        if self._color is None:
            self._color= self._config.COLOR_TRACK_DEFAULT

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
            if element._color is None:
                element._color = self._config.COLOR_TRACK_DEFAULT
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
    
    def addStep(self,color=None,closedColor=None,thrownColor=None):

        if closedColor == None:
            closedColor=self._closedColor
        if thrownColor == None:
            thrownColor=self._thrownColor
        if color == None:
            color=self._color

        step = LadderStep(color=color, up=self._up,right=self._right,vertical=self._vertical,closedColor=closedColor,thrownColor=thrownColor)
        self._steps.append(step)
        if self._panel != None:
            step.attach(self._panel)

    def endContraTurnout(self,color=None, closedColor=None,thrownColor=None):
        if closedColor == None:
            closedColor=self._closedColor
        if thrownColor == None:
            thrownColor=self._thrownColor
        if color == None:
            color=self._color

        step = HalfTurnout(color=color, up=not self._up,right=not self._right,vertical=self._vertical,closedColor=closedColor,thrownColor=thrownColor)
        self._steps.append(step)
        if self._panel != None:
            step.attach(self._panel)
        self._endCurve=False