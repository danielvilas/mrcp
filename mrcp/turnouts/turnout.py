from mrcp.panel import *
from mrcp.points import *
from .halfturnout import *
from mrcp.curve import OutCurve

class Turnout(BaseElement):
    def __init__(self, pos=(0, 0), color=COLOR_TRACK_DEFAULT, up=True, right=True, vertical=False) -> None:
        super().__init__(pos=pos, color=color)
        self._up = up
        self._right = right
        self._vertical = vertical
        self._halfTurnout = HalfTurnout(
            pos=pos, color=color, up=up, right=right, vertical=vertical)
        self._outCurve = OutCurve(
            pos=pos, color=color, right=right, up=up, vertical=vertical)
        self._track=Track(color=color)

    def paint(self):
        super().paint()
        if(self._vertical):
            if(self._up):
                self._halfTurnout._pos =self._pos.move((0, 4))
            else:
                self._halfTurnout._pos = self._pos
        else:
            if(self._right):
                self._halfTurnout._pos = self._pos
            else:
                self._halfTurnout._pos = self._pos.move((4, 0))

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

        self._outCurve._pos = self._pos.move( (dx, dy))
        self._outCurve.paint()

        # TODO move to obj
        start = (0, 0)
        end = (0, 0)
        if self._vertical:
            start = self._pos.move( delta=(0, 4))
            end = self._pos.move( delta=(0, 8))
            if self._up:
                start = self._pos.move( delta=(0, 0))
                end = self._pos.move( delta=(0, 4))
            start._pos='t'
            end._pos='t'

        else:
            start = self._pos.move(delta=(0, 0))
            end = self._pos.move(delta=(4, 0))
            if self._right:
                start = self._pos.move(delta=(4, 0))
                end = self._pos.move(delta=(8, 0))
            start._pos='l'
            end._pos='l'
        self._track._pos=start
        self._track._end=end
        self._track.paint()
        

    def attach(self, panel):
        self._halfTurnout.attach(panel)
        self._outCurve.attach(panel)
        self._track.attach(panel)
        return super().attach(panel)

