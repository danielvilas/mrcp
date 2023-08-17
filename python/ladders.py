import mrcp
from mrcp.points import *

def myPanel(name, endContra=False):
    panel = mrcp.Panel(name, 215, 120)
    panel.grid()
    panel.markStart()
    ladder = mrcp.Ladder(color="gray", up=True, right=True,vertical=False)
    ladder.addStep(color="blueviolet")
    ladder.addStep(thrownColor='red',closedColor='cyan')
    panel.add(ladder,Point(1,10))
    ladder.addStep()
    if endContra:
        ladder.endContraTurnout(thrownColor='red',closedColor='cyan')

    ladder = mrcp.Ladder(color="gray", up=False, right=True,vertical=False,thrownColor='red',closedColor='cyan')
    ladder.addStep()
    ladder.addStep()
    panel.add(ladder,Point(1,13))
    ladder.addStep()
    if endContra:
        ladder.endContraTurnout()

    ladder = mrcp.Ladder(color="gray", up=True, right=False,vertical=False)
    ladder.addStep()
    ladder.addStep()
    panel.add(ladder,Point(38,10))
    ladder.addStep()
    if endContra:
        ladder.endContraTurnout()

    ladder = mrcp.Ladder(color="gray", up=False, right=False,vertical=False)
    ladder.addStep()
    ladder.addStep()
    panel.add(ladder,Point(38,13))
    ladder.addStep()
    if endContra:
        ladder.endContraTurnout()

    panel.paint()
    panel._dwg.save()


if __name__ == '__main__':
    myPanel("Ladders_contra.svg",True)
    myPanel("Ladders.svg",False)
