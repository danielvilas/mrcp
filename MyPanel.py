from mrcp.track import Track
import mrcp
from mrcp.led import Led


from mrcp.points import *

mainTrackColor="gray"
upYardColor="blueviolet"
stopLine="sandybrown"

occupancyColorMain="lightcoral"
occupancyColorStopLine="mistyrose"
occupancyColorYard="lightblue"

def myPanel(name):

    panel = mrcp.Panel(name, 200, 120)
    dwg = panel._dwg
    tLayer = panel._tLayer


# Up Yard, tracks
    panel.add(Track(Point(8,2),color=upYardColor,end=Point(15,2)))
    panel.add(Track(Point(20,2),color=upYardColor,end=Point(38,2)))
    panel.add(Track(Point(16,4),color=upYardColor,end=Point(38,4)))
    panel.add(Track(Point(12,6),color=mainTrackColor,end=Point(23,6)))
# Up Yard, ladder

    # turn= mrcp.HalfTurnout(color="cyan",up=True,right=True)
    # panel.add(turn,(8,6))
    # turn=mrcp.LadderStep(color="cyan",up=True,right=True)
    # panel.add(turn,(12,4))
    # turn= mrcp.HalfTurnout(color="cyan",up=False,right=False)
    # panel.add(turn,(16,2))
    ladder = mrcp.Ladder(color=mainTrackColor,thrownTrackColor=upYardColor,up=True,right=True)
    panel.add(ladder,Point(8,6))
    ladder.addStep(color=upYardColor)
    ladder.endContraTurnout(color=upYardColor)

# Up Yard, service track
    turn= mrcp.Turnout(color=mainTrackColor,thrownTrackColor=stopLine,up=False,right=True)
    panel.add(turn,Point(24, 6))


# Down Station, tracks
    panel.add(Track(Point(8,21),color=mainTrackColor,end=Point(31,21)))
    panel.add(Track(Point(8,19),color=mainTrackColor,end=Point(27,19)))
    panel.add(Track(Point(28,17),color=stopLine,end=Point(31,17)))
    panel.add(Track(Point(16,17),color=stopLine,end=Point(23,17)))
# Down Station, exit track

    turn= mrcp.HalfTurnout(color=mainTrackColor,up=True,right=False)
    panel.add(turn,Point(28,19))
    turn= mrcp.HalfTurnout(color=stopLine,up=False,right=True)
    panel.add(turn,Point(24, 17))


# curve
    #vSegment(dwg,pos=(0,12),layer=tLayer, color=mainTrackColor,length=2)


    curve=mrcp.CurveTurnOut_2_3(color=mainTrackColor,up=False,right=True,vertical=True)
    panel.add(curve,pos=Point(2,12))
    curve=mrcp.CurveTurnOut_2_3(color=mainTrackColor,up=False,right=False,vertical=True)
    panel.add(curve,pos=Point(37,12))

    curve = mrcp.Curve(radius=2, color=mainTrackColor, left=True, up=True)
    panel.add(curve, pos=Point(7, 11))
    curve = mrcp.Curve(radius=2, color=mainTrackColor, left=False, up=True)
    panel.add(curve, pos=Point(32, 11))

    curve = mrcp.Curve(radius=1, color=stopLine, left=False, up=True)
    panel.add(curve, pos=Point(32, 11))
    curve = mrcp.Curve(radius=1, color=stopLine, left=False, up=False)
    panel.add(curve, pos=Point(32, 14))
# Close curve
    panel.add(Track(Point(35,12),color=stopLine,end=Point(35,13)))

# Occupancy leds
# Main Line
    panel.add(Led(color=occupancyColorMain),Point(4,7,'bl'))
    panel.add(Led(color=occupancyColorMain),Point(5,18,'l'))
    panel.add(Led(color=occupancyColorMain),Point(3,20,'c'))
    panel.add(Led(color=occupancyColorMain),Point(11,21,'r'))
    panel.add(Led(color=occupancyColorMain),Point(11,19,'r'))
    panel.add(Led(color=occupancyColorMain),Point(19,21,'r'))
    panel.add(Led(color=occupancyColorMain),Point(19,19,'r'))
    panel.add(Led(color=occupancyColorMain),Point(27,21,'r'))
    panel.add(Led(color=occupancyColorMain),Point(25,19,'r'))
    panel.add(Led(color=occupancyColorMain),Point(29,6,'r'))
    panel.add(Led(color=occupancyColorMain),Point(19,6,'r'))
    panel.add(Led(color=occupancyColorMain),Point(13,6,'r'))
    panel.add(Led(color=occupancyColorMain),Point(36,8,'tl'))
    panel.add(Led(color=occupancyColorMain),Point(35,18,'l'))
    panel.add(Led(color=occupancyColorMain),Point(36,20,'c'))
    


    #StopLine
    panel.add(Led(color=occupancyColorStopLine),Point(19,17,'r'))
    panel.add(Led(color=occupancyColorStopLine),Point(29,17,'r'))
    panel.add(Led(color=occupancyColorStopLine),Point(34,16,'tl'))
    panel.add(Led(color=occupancyColorStopLine),Point(34,10,'tl'))
    panel.add(Led(color=occupancyColorStopLine),Point(29,8,'r'))

    #Upper Yard
    panel.add(Led(color=occupancyColorYard),Point(35,4,'c'))
    panel.add(Led(color=occupancyColorYard),Point(35,2,'c'))
    panel.add(Led(color=occupancyColorYard),Point(27,4,'r'))
    panel.add(Led(color=occupancyColorYard),Point(27,2,'r'))
    panel.add(Led(color=occupancyColorYard),Point(19,4,'r'))
    panel.add(Led(color=occupancyColorYard),Point(19,2,'r'))
    panel.add(Led(color=occupancyColorYard),Point(11,2,'r'))

    panel.paint()
    dwg.save()


if __name__ == '__main__':
    myPanel("panel.svg")
