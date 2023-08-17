from mrcp.points import Point
from mrcp.turnouts import CurveTurnOut_2_3
import mrcp


def fullCurve(panel,pos=Point(10,10),radius=2):
    curve1=mrcp.Curve(radius=radius,left=True,up=True,color="gray")
    panel.add(curve1,pos)
    curve1=mrcp.Curve(radius=radius,left=False,up=True,color="gray")
    panel.add(curve1,pos=mrcp.movePoint(pos,Point(2,0)))
    curve1=mrcp.Curve(radius=radius,left=True,up=False,color="gray")
    panel.add(curve1,pos=mrcp.movePoint(pos,Point(0,2)))
    curve1=mrcp.Curve(radius=radius,left=False,up=False,color="gray")
    panel.add(curve1,pos=mrcp.movePoint(pos,Point(2,2)))

def r1r4_curves(panel):
    fullCurve(panel,radius=1)
    fullCurve(panel,radius=2)
    fullCurve(panel,radius=3)
    fullCurve(panel,radius=4)

def vertical23(panel):
    curve= CurveTurnOut_2_3(color="gray",up=False,right=True,vertical=True)
    panel.add(curve,Point(24,12))
    curve= CurveTurnOut_2_3(color="gray",up=False,right=False,vertical=True)
    panel.add(curve,Point(37,12))
    curve= CurveTurnOut_2_3(color="gray",up=True,right=True,vertical=True)
    panel.add(curve,Point(24,10))
    curve= CurveTurnOut_2_3(color="gray",up=True,right=False,vertical=True)
    panel.add(curve,Point(37,10))

def horizontal23(panel):
    curve= CurveTurnOut_2_3(color="gray",up=False,right=True,vertical=False)
    panel.add(curve,Point(20,24))
    curve= CurveTurnOut_2_3(color="gray",up=True,right=True,vertical=False)
    panel.add(curve,Point(20,37))
    curve= CurveTurnOut_2_3(color="gray",up=False,right=False,vertical=False)
    panel.add(curve,Point(18,24))
    curve= CurveTurnOut_2_3(color="gray",up=True,right=False,vertical=False)
    panel.add(curve,Point(18,37))

def myPanel(name):
    panel = mrcp.Panel(name, 200, 200)
    panel.grid()
    panel.markStart()

    r1r4_curves(panel)
    vertical23(panel)
    horizontal23(panel)


    panel.paint()
    panel._dwg.save()


if __name__ == '__main__':
    myPanel("curves.svg")
