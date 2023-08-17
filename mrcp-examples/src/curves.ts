// Copy of curves.py in TS
import {TrackElement,Layout} from "mrcp-layout-model"
import {PainterTco, PainterTcoOptions, TcoPoint} from 'mrcp-painter-tco'


var l:Layout;

function fullCurve(radius?:number=2, pos?,TcoPoint={x:10,y:10,pos:'center'}){
    let curve:TrackElement = l.createElement("c1-"+radius);
    curve.addHint("tco",{type:'curve',pos:pos,color:"gray",left:true,up:true,radius:radius})

}

    curve1=mrcp.Curve(radius=radius,left=False,up=True,color="gray")
    panel.add(curve1,pos=mrcp.movePoint(pos,Point(2,0)))
    curve1=mrcp.Curve(radius=radius,left=True,up=False,color="gray")
    panel.add(curve1,pos=mrcp.movePoint(pos,Point(0,2)))
    curve1=mrcp.Curve(radius=radius,left=False,up=False,color="gray")
    panel.add(curve1,pos=mrcp.movePoint(pos,Point(2,2)))

function r1r4_curves():
    fullCurve(panel,radius=1)
    fullCurve(panel,radius=2)
    fullCurve(panel,radius=3)
    fullCurve(panel,radius=4)


function build_curves_layout(){
    l = new Layout("Test Layout");
    
    r1r4_curves()

}

export async function curves_demo():Promise<void>{
    build_curves_layout();

    let opts:PainterTcoOptions={
        name:"TestCurves",
        format: 'svg',
        outFile:'curves.svg',
        size:{height:200,width:200},
        grid:true
    }

    let panel= new PainterTco(opts)

    panel.grid()
    panel.markStart()

    //r1r4_curves(panel)
    //vertical23(panel)
    //horizontal23(panel)


    panel.paint(l)
    await panel.save()
    return;
}