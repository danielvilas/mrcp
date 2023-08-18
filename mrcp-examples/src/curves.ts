// Copy of curves.py in TS
import {TrackElement,Layout} from "mrcp-layout-model"
import {PainterTco, PainterTcoOptions, TcoPoint,TcoCurveHint} from 'mrcp-painter-tco'


var l:Layout;

const defaultPoint = new TcoPoint({x:10,y:10})

function fullCurve(radius:number=2, pos:TcoPoint=defaultPoint){
    let curve:TrackElement = l.createElement("c1-"+radius);
    curve.addHint(new TcoCurveHint({type:'curve',pos:pos,color:"gray",left:true,up:true,radius:radius}))

    //curve = l.createElement("c2-"+radius);
    //curve.addHint(new TcoCurveHint({type:'curve',pos:pos.move({x:2,y:0}),color:"gray",left:false,up:true,radius:radius}))
    
    //curve = l.createElement("c3-"+radius);
    //curve.addHint(new TcoCurveHint({type:'curve',pos:pos.move({x:0,y:2}),color:"gray",left:true,up:false,radius:radius}))
    
    //curve = l.createElement("c4-"+radius);
    //curve.addHint(new TcoCurveHint({type:'curve',pos:pos.move({x:2,y:2}),color:"gray",left:false,up:false,radius:radius}))

}
    

function r1r4_curves(){
    fullCurve(1)
    //fullCurve(2)
    //fullCurve(3)
    //fullCurve(4)
}

function build_curves_layout(){
    l = new Layout("Test Layout");
    
    r1r4_curves()

}

export async function curves_demo():Promise<void>{
    build_curves_layout();
    console.log("Packed: ")
    console.log(l.toJson())


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
    console.log("\nSvg:")
    await panel.save()
    
    return;
}