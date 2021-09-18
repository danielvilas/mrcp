import mrcp


def halfPartsHorizontal(panel):
    turn= mrcp.HalfTurnout(color="gray",up=True,right=True)
    panel.add(turn,(1,5))
    turn= mrcp.HalfTurnout(color="gray",up=False,right=True)
    panel.add(turn,(1,1))
    
    turn= mrcp.HalfTurnout(color="gray",up=True,right=False)
    panel.add(turn,(6,5))
    turn= mrcp.HalfTurnout(color="gray",up=False,right=False)
    panel.add(turn,(6,1))
    
    #Closing curves Horizontal
    curve = mrcp.OutCurve(color="gray",up=True,right=True, vertical=False)
    panel.add(curve,(1,9))
    curve = mrcp.OutCurve(color="gray",up=True,right=False, vertical=False)
    panel.add(curve,(6,9))

    curve = mrcp.OutCurve(color="gray",up=False,right=True, vertical=False)
    panel.add(curve,(1,10))
    curve = mrcp.OutCurve(color="gray",up=False,right=False, vertical=False)
    panel.add(curve,(6,10))



def halfPartsVertical(panel):
    #Half turnout Vertical
    turn= mrcp.HalfTurnout(color="gray",up=False,right=True, vertical=True)
    panel.add(turn,(1,14))
    turn= mrcp.HalfTurnout(color="gray",up=False,right=False, vertical=True)
    panel.add(turn,(5,14))

    turn= mrcp.HalfTurnout(color="gray",up=True,right=True, vertical=True)
    panel.add(turn,(1,19))
    turn= mrcp.HalfTurnout(color="gray",up=True,right=False, vertical=True)
    panel.add(turn,(5,19))


    #Closing curves Horizontal
    curve = mrcp.OutCurve(color="gray",up=True,right=True, vertical=True)
    panel.add(curve,(10,23))
    curve = mrcp.OutCurve(color="gray",up=True,right=False, vertical=True)
    panel.add(curve,(9,23))

    curve = mrcp.OutCurve(color="gray",up=False,right=True, vertical=True)
    panel.add(curve,(10,14))
    curve = mrcp.OutCurve(color="gray",up=False,right=False, vertical=True)
    panel.add(curve,(9,14))

def verticalTurnout(panel):
    #Composites/full Turnouts Horizontal
    turn= mrcp.Turnout(color="gray",up=False,right=True, vertical=True)
    panel.add(turn,(14, 1))
    turn= mrcp.Turnout(color="gray",up=False,right=False, vertical=True)
    panel.add(turn,(20, 1))

    turn= mrcp.Turnout(color="gray",up=True,right=True, vertical=True)
    panel.add(turn,(14, 9))
    turn= mrcp.Turnout(color="gray",up=True,right=False, vertical=True)
    panel.add(turn,(20, 9))

def horizontalTurnout(panel):
    #Composites/full Turnouts Horizontal
    turn= mrcp.Turnout(color="gray",up=False,right=True)
    panel.add(turn,(23, 1))
    turn= mrcp.Turnout(color="gray",up=False,right=False)
    panel.add(turn,(32, 1))

    turn= mrcp.Turnout(color="gray",up=True,right=True)
    panel.add(turn,(23, 7))
    turn= mrcp.Turnout(color="gray",up=True,right=False)
    panel.add(turn,(32, 7))

def horizontalLadder(panel):
    #Ladder Steps
    step = mrcp.LadderStep(color="gray",up=True,right=True)
    panel.add(step,(14, 19))
    step = mrcp.LadderStep(color="gray",up=True,right=False)
    panel.add(step,(19, 19))

    step = mrcp.LadderStep(color="gray",up=False,right=True)
    panel.add(step,(14, 22))

    step = mrcp.LadderStep(color="gray",up=False,right=False)
    panel.add(step,(19, 22))

def verticalLadder(panel):

    step = mrcp.LadderStep(color="gray",up=False,right=False, vertical=True)
    panel.add(step,(30, 13))
    step = mrcp.LadderStep(color="gray",up=False,right=True, vertical=True)
    panel.add(step,(33, 13))
    step = mrcp.LadderStep(color="gray",up=True,right=False, vertical=True)
    panel.add(step,(30, 18))
    step = mrcp.LadderStep(color="gray",up=True,right=True, vertical=True)
    panel.add(step,(33, 18))

def myPanel(name):
    panel = mrcp.Panel(name, 205, 120)
    panel.markStart()

    #Half turnout Horizontal
    halfPartsHorizontal(panel)
    halfPartsVertical(panel)
    verticalTurnout(panel)
    horizontalTurnout(panel)
    horizontalLadder(panel)
    verticalLadder(panel)

    panel.paint()
    panel._dwg.save()


if __name__ == '__main__':
    myPanel("turnouts.svg")
