import mrcp
import svgwrite
from svgwrite.extensions import Inkscape


from mrcp.points import *


def hSegment(dwg, pos=(0, 0), color="black", length=1, layer=None):
    color = "yellow"
    if layer == None:
        layer = dwg
    start = pointH(pos=pos)
    end = pointH(pos=pos, delta=(4*length, 0))

    line = dwg.line(start=start, end=end, stroke=color, stroke_width=5)
    layer.add(line)
    return


def vSegment(dwg, pos=(0, 0), color="black", length=1, layer=None):
    color = "yellow"
    if layer == None:
        layer = dwg
    start = pointV(pos=pos)
    end = pointV(pos=pos, delta=(0, 4*length))

    line = dwg.line(start=start, end=end, stroke=color, stroke_width=5)
    layer.add(line)
    return






def myPanel(name):

    panel = mrcp.Panel(name, 200, 120)
    dwg = panel._dwg
    tLayer = panel._tLayer


# Up Yard, tracks
    hSegment(dwg, pos=(8, 2), layer=tLayer, color="gray", length=2)
    hSegment(dwg, pos=(20, 2), layer=tLayer, color="gray", length=4)
    hSegment(dwg, pos=(16, 4), layer=tLayer, color="gray", length=5)
    hSegment(dwg, pos=(12, 6), layer=tLayer, color="gray", length=3)
# Up Yard, ladder

    # turn= mrcp.HalfTurnout(color="cyan",up=True,right=True)
    # panel.add(turn,(8,6))
    # turn=mrcp.LadderStep(color="cyan",up=True,right=True)
    # panel.add(turn,(12,4))
    # turn= mrcp.HalfTurnout(color="cyan",up=False,right=False)
    # panel.add(turn,(16,2))
    ladder = mrcp.Ladder(color="gray",up=True,right=True)
    panel.add(ladder,(8,6))
    ladder.addStep()
    ladder.endContraTurnout()

# Up Yard, service track
    turn= mrcp.Turnout(color="gray",up=False,right=True)
    panel.add(turn,(24, 6))


# Down Station, tracks
    hSegment(dwg, pos=(8, 21), layer=tLayer, color="gray", length=6)
    hSegment(dwg, pos=(8, 19), layer=tLayer, color="gray", length=5)
    hSegment(dwg, pos=(28, 17), layer=tLayer, color="gray", length=1)
    hSegment(dwg, pos=(16, 17), layer=tLayer, color="gray", length=2)
# Down Station, exit track

    turn= mrcp.HalfTurnout(color="gray",up=True,right=False)
    panel.add(turn,(28,19))
    turn= mrcp.HalfTurnout(color="gray",up=False,right=True)
    panel.add(turn,(24, 17))


# curve
    #vSegment(dwg,pos=(0,12),layer=tLayer, color="gray",length=2)


    curve=mrcp.CurveTurnOut_2_3(color="gray",up=False,right=True,vertical=True)
    panel.add(curve,pos=(2,12))
    curve=mrcp.CurveTurnOut_2_3(color="gray",up=False,right=False,vertical=True)
    panel.add(curve,pos=(37,12))

    curve = mrcp.Curve(radius=2, color="gray", left=True, up=True)
    panel.add(curve, pos=(7, 11))
    curve = mrcp.Curve(radius=2, color="gray", left=False, up=True)
    panel.add(curve, pos=(32, 11))
    curve = mrcp.Curve(radius=1, color="gray", left=False, up=True)
    panel.add(curve, pos=(32, 11))
    curve = mrcp.Curve(radius=1, color="gray", left=False, up=False)
    panel.add(curve, pos=(32, 14))
    panel.paint()


# Close curve
    st = pointV((35, 12))
    se = pointV((35, 12), (0, 2))
    tLayer.add(dwg.line(start=st, end=se, stroke="gray", stroke_width=5))
    dwg.save()


if __name__ == '__main__':
    myPanel("panel.svg")
