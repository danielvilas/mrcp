from mrcp.track import Track
import mrcp


from mrcp.points import *

def myPanel(name):

    panel = mrcp.Panel(name, 200, 120)
    dwg = panel._dwg
    tLayer = panel._tLayer


# Up Yard, tracks
    panel.add(Track(Point(8,2),color="gray",end=Point(15,2)))
    panel.add(Track(Point(20,2),color="gray",end=Point(35,2)))
    panel.add(Track(Point(16,4),color="gray",end=Point(35,4)))
    panel.add(Track(Point(12,6),color="gray",end=Point(23,6)))
# Up Yard, ladder

    # turn= mrcp.HalfTurnout(color="cyan",up=True,right=True)
    # panel.add(turn,(8,6))
    # turn=mrcp.LadderStep(color="cyan",up=True,right=True)
    # panel.add(turn,(12,4))
    # turn= mrcp.HalfTurnout(color="cyan",up=False,right=False)
    # panel.add(turn,(16,2))
    ladder = mrcp.Ladder(color="gray",up=True,right=True)
    panel.add(ladder,Point(8,6))
    ladder.addStep()
    ladder.endContraTurnout()

# Up Yard, service track
    turn= mrcp.Turnout(color="gray",up=False,right=True)
    panel.add(turn,Point(24, 6))


# Down Station, tracks
    panel.add(Track(Point(8,21),color="gray",end=Point(31,21)))
    panel.add(Track(Point(8,19),color="gray",end=Point(27,19)))
    panel.add(Track(Point(28,17),color="gray",end=Point(31,17)))
    panel.add(Track(Point(16,17),color="gray",end=Point(23,17)))
# Down Station, exit track

    turn= mrcp.HalfTurnout(color="gray",up=True,right=False)
    panel.add(turn,Point(28,19))
    turn= mrcp.HalfTurnout(color="gray",up=False,right=True)
    panel.add(turn,Point(24, 17))


# curve
    #vSegment(dwg,pos=(0,12),layer=tLayer, color="gray",length=2)


    curve=mrcp.CurveTurnOut_2_3(color="gray",up=False,right=True,vertical=True)
    panel.add(curve,pos=Point(2,12))
    curve=mrcp.CurveTurnOut_2_3(color="gray",up=False,right=False,vertical=True)
    panel.add(curve,pos=Point(37,12))

    curve = mrcp.Curve(radius=2, color="gray", left=True, up=True)
    panel.add(curve, pos=Point(7, 11))
    curve = mrcp.Curve(radius=2, color="gray", left=False, up=True)
    panel.add(curve, pos=Point(32, 11))
    curve = mrcp.Curve(radius=1, color="gray", left=False, up=True)
    panel.add(curve, pos=Point(32, 11))
    curve = mrcp.Curve(radius=1, color="gray", left=False, up=False)


    panel.add(curve, pos=Point(32, 14))


# Close curve
    panel.add(Track(Point(35,12),color="gray",end=Point(35,13)))

    panel.paint()
    dwg.save()


if __name__ == '__main__':
    myPanel("panel.svg")
