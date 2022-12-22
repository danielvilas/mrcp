from mrcp.points import Point
import mrcp


def halfPartsHorizontal(panel):
    turn= mrcp.HalfTurnout(color=None,up=True,right=True)
    panel.add(turn,Point(1,5))
    turn= mrcp.HalfTurnout(color=None,up=False,right=True)
    panel.add(turn,Point(1,1))
    
    turn= mrcp.HalfTurnout(color=None,up=True,right=False)
    panel.add(turn,Point(6,5))
    turn= mrcp.HalfTurnout(color=None,up=False,right=False)
    panel.add(turn,Point(6,1))
    
    #Closing curves Horizontal
    curve = mrcp.OutCurve(color=None,up=True,right=True, vertical=False)
    panel.add(curve,Point(1,9))
    curve = mrcp.OutCurve(color=None,up=True,right=False, vertical=False)
    panel.add(curve,Point(6,9))

    curve = mrcp.OutCurve(color=None,up=False,right=True, vertical=False)
    panel.add(curve,Point(1,10))
    curve = mrcp.OutCurve(color=None,up=False,right=False, vertical=False)
    panel.add(curve,Point(6,10))



def halfPartsVertical(panel):
    #Half turnout Vertical
    turn= mrcp.HalfTurnout(color=None,up=False,right=True, vertical=True)
    panel.add(turn,Point(1,14))
    turn= mrcp.HalfTurnout(color=None,up=False,right=False, vertical=True)
    panel.add(turn,Point(5,14))

    turn= mrcp.HalfTurnout(color=None,up=True,right=True, vertical=True)
    panel.add(turn,Point(1,19))
    turn= mrcp.HalfTurnout(color=None,up=True,right=False, vertical=True)
    panel.add(turn,Point(5,19))


    #Closing curves Horizontal
    curve = mrcp.OutCurve(color=None,up=True,right=True, vertical=True)
    panel.add(curve,Point(10,23))
    curve = mrcp.OutCurve(color=None,up=True,right=False, vertical=True)
    panel.add(curve,Point(9,23))

    curve = mrcp.OutCurve(color=None,up=False,right=True, vertical=True)
    panel.add(curve,Point(10,14))
    curve = mrcp.OutCurve(color=None,up=False,right=False, vertical=True)
    panel.add(curve,Point(9,14))

def verticalTurnout(panel):
    #Composites/full Turnouts Horizontal
    turn= mrcp.Turnout(color=None,up=False,right=True, vertical=True)
    panel.add(turn,Point(14, 1))
    turn= mrcp.Turnout(color=None,up=False,right=False, vertical=True)
    panel.add(turn,Point(20, 1))

    turn= mrcp.Turnout(color=None,up=True,right=True, vertical=True)
    panel.add(turn,Point(14, 9))
    turn= mrcp.Turnout(color=None,up=True,right=False, vertical=True)
    panel.add(turn,Point(20, 9))

def horizontalTurnout(panel):
    #Composites/full Turnouts Horizontal
    turn= mrcp.Turnout(color=None,up=False,right=True)
    panel.add(turn,Point(23, 1))
    turn= mrcp.Turnout(color=None,up=False,right=False)
    panel.add(turn,Point(32, 1))

    turn= mrcp.Turnout(color=None,up=True,right=True)
    panel.add(turn,Point(23, 7))
    turn= mrcp.Turnout(color=None,up=True,right=False)
    panel.add(turn,Point(32, 7))

def horizontalLadder(panel):
    #Ladder Steps
    step = mrcp.LadderStep(color=None,up=True,right=True)
    panel.add(step,Point(14, 19))
    step = mrcp.LadderStep(color=None,up=True,right=False)
    panel.add(step,Point(19, 19))

    step = mrcp.LadderStep(color=None,up=False,right=True)
    panel.add(step,Point(14, 22))

    step = mrcp.LadderStep(color=None,up=False,right=False)
    panel.add(step,Point(19, 22))

def verticalLadder(panel):

    step = mrcp.LadderStep(color=None,up=False,right=False, vertical=True)
    panel.add(step,Point(30, 13))
    step = mrcp.LadderStep(color=None,up=False,right=True, vertical=True)
    panel.add(step,Point(33, 13))
    step = mrcp.LadderStep(color=None,up=True,right=False, vertical=True)
    panel.add(step,Point(30, 18))
    step = mrcp.LadderStep(color=None,up=True,right=True, vertical=True)
    panel.add(step,Point(33, 18))

def myPanel(name):
    cfg = mrcp.Config()
    #cfg.LED_SIZE=5
    #cfg.LED_MARGIN=3
    #cfg.LED_COLOR='orange'
    #cfg.CLOSED_LED_COLOR='orange'
    #cfg.THROWN_LED_COLOR='black'
    #cfg.TRACK_SIZE=2
    #cfg.GRID_SIZE=10
    #cfg.COLOR_TRACK_DEFAULT='orange'
    #cfg.COLOR_CUT='orange'
    #cfg.COLOR_ENGRAVE='orange'
    #cfg.SWITH_HOLE_SIZE=12
    #cfg.SWITH_HOLE_MARGIN_SIZE=24
    #cfg.SWITH_SIZE=(20,15)
    #cfg.SWITH_SIZE_H=(30,10)
    panel = mrcp.Panel(name, 41, 24,config=cfg, sizeInGrid=True)
    
    
    panel.grid()
    panel.markStart()

    #Half turnout Horizontal
    halfPartsHorizontal(panel)
    halfPartsVertical(panel)
    verticalTurnout(panel)
    horizontalTurnout(panel)
    horizontalLadder(panel)
    verticalLadder(panel)
    panel.add(mrcp.Led(),Point(25,10))
    panel.paint()
    panel._dwg.save()


if __name__ == '__main__':
    myPanel("turnouts.svg")
