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

    panel = mrcp.Panel(name, 200, 140)
    panel.grid()
    panel.margin(margin=7) # The box is 6mm, +1 extra
    dwg = panel._dwg
    tLayer = panel._tLayer


# Up Yard, tracks
    panel.add(Track(Point(9,4),color=upYardColor,end=Point(16,4)))
    panel.add(Track(Point(21,4),color=upYardColor,end=Point(35,4)))
    panel.add(Track(Point(17,6),color=upYardColor,end=Point(35,6)))
    panel.add(Track(Point(13,8),color=mainTrackColor,end=Point(22,8)))
# Up Yard, ladder

    ladder = mrcp.Ladder(color=mainTrackColor,thrownTrackColor=upYardColor,up=True,right=True)
    panel.add(ladder,Point(9,8))
    ladder.addStep(color=upYardColor)
    ladder.endContraTurnout(color=upYardColor)

# Up Yard, service track
    turn= mrcp.Turnout(color=mainTrackColor,thrownTrackColor=stopLine,up=False,right=True)
    panel.add(turn,Point(23, 8))


# Down Station, tracks
    panel.add(Track(Point(9,23),color=mainTrackColor,end=Point(30,23)))
    panel.add(Track(Point(9,21),color=mainTrackColor,end=Point(26,21)))
    panel.add(Track(Point(27,19),color=stopLine,end=Point(30,19)))
    panel.add(Track(Point(16,19),color=stopLine,end=Point(22,19)))
# Down Station, exit track

    turn= mrcp.HalfTurnout(color=mainTrackColor,up=True,right=False)
    panel.add(turn,Point(27,21))
    turn= mrcp.HalfTurnout(color=stopLine,up=False,right=True)
    panel.add(turn,Point(23, 19))


# curve
    curve=mrcp.CurveTurnOut_2_3(color=mainTrackColor,up=False,right=True,vertical=True)
    panel.add(curve,pos=Point(3,14))
    curve=mrcp.CurveTurnOut_2_3(color=mainTrackColor,up=False,right=False,vertical=True)
    panel.add(curve,pos=Point(36,14))

    curve = mrcp.Curve(radius=2, color=mainTrackColor, left=True, up=True)
    panel.add(curve, pos=Point(8, 13))
    curve = mrcp.Curve(radius=2, color=mainTrackColor, left=False, up=True)
    panel.add(curve, pos=Point(31, 13))

    curve = mrcp.Curve(radius=1, color=stopLine, left=False, up=True)
    panel.add(curve, pos=Point(31, 13))
    curve = mrcp.Curve(radius=1, color=stopLine, left=False, up=False)
    panel.add(curve, pos=Point(31, 16))
# Close curve
    panel.add(Track(Point(34,14),color=stopLine,end=Point(34,15)))

# Occupancy leds
# Main Line
    panel.add(Led(color=occupancyColorMain),Point(5,9,'bl'))
    panel.add(Led(color=occupancyColorMain),Point(6,20,'l'))
    panel.add(Led(color=occupancyColorMain),Point(4,22,'c'))
    panel.add(Led(color=occupancyColorMain),Point(13,23,'c'))
    panel.add(Led(color=occupancyColorMain),Point(13,21,'c'))
    panel.add(Led(color=occupancyColorMain),Point(19,23,'c'))
    panel.add(Led(color=occupancyColorMain),Point(19,21,'c'))
    panel.add(Led(color=occupancyColorMain),Point(24,23,'r'))
    panel.add(Led(color=occupancyColorMain),Point(24,21,'r'))
    panel.add(Led(color=occupancyColorMain),Point(28,8,'r'))
    panel.add(Led(color=occupancyColorMain),Point(21,8,'c'))
    panel.add(Led(color=occupancyColorMain),Point(16,8,'r'))
    panel.add(Led(color=occupancyColorMain),Point(35,10,'tl'))
    panel.add(Led(color=occupancyColorMain),Point(34,20,'l'))
    panel.add(Led(color=occupancyColorMain),Point(35,22,'c'))
    


    #StopLine
    panel.add(Led(color=occupancyColorStopLine),Point(19,19,'c'))
    panel.add(Led(color=occupancyColorStopLine),Point(28,19,'r'))
    panel.add(Led(color=occupancyColorStopLine),Point(33,18,'tl'))
    panel.add(Led(color=occupancyColorStopLine),Point(33,12,'tl'))
    panel.add(Led(color=occupancyColorStopLine),Point(28,10,'r'))

    #Upper Yard
    panel.add(Led(color=occupancyColorYard),Point(31,6,'c'))
    panel.add(Led(color=occupancyColorYard),Point(31,4,'c'))
    panel.add(Led(color=occupancyColorYard),Point(26,6,'r'))
    panel.add(Led(color=occupancyColorYard),Point(26,4,'r'))
    panel.add(Led(color=occupancyColorYard),Point(21,6,'c'))
    panel.add(Led(color=occupancyColorYard),Point(21,4,'c'))
    panel.add(Led(color=occupancyColorYard),Point(12,4,'r'))

    panel.paint()
    dwg.save()


if __name__ == '__main__':
    myPanel("panel.svg")
