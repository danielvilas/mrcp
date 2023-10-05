import { Layout, TrackElement } from "mrcp-layout-model";
import { PainterTco, PainterTcoOptions, TcoPoint,TcoHalfTurnOutHint, TcoOutCurveHint } from "mrcp-painter-tco";

var l:Layout;

function halfPartsHorizontal(){
    let turn:TrackElement = l.createElement("hth-1");
    turn.addHint(new TcoHalfTurnOutHint({type:'halfTurnOut',pos:new TcoPoint({x:1,y:5}),up:true,right:true}))
    turn= l.createElement("hth-2");
    turn.addHint(new TcoHalfTurnOutHint({type:'halfTurnOut',pos:new TcoPoint({x:1,y:1}),up:false,right:true}))

    turn= l.createElement("hth-3");
    turn.addHint(new TcoHalfTurnOutHint({type:'halfTurnOut',pos:new TcoPoint({x:6,y:5}),up:true,right:false}))
    turn= l.createElement("hth-4");
    turn.addHint(new TcoHalfTurnOutHint({type:'halfTurnOut',pos:new TcoPoint({x:6,y:1}),up:false,right:false}))


    turn= l.createElement("hth-5");
    turn.addHint(new TcoOutCurveHint({type:'outCurve',pos:new TcoPoint({x:1,y:9}),up:true,right:true}))
    turn= l.createElement("hth-6");
    turn.addHint(new TcoOutCurveHint({type:'outCurve',pos:new TcoPoint({x:6,y:9}),up:true,right:false}))

    turn= l.createElement("hth-7");
    turn.addHint(new TcoOutCurveHint({type:'outCurve',pos:new TcoPoint({x:1,y:10}),up:false,right:true}))
    turn= l.createElement("hth-8");
    turn.addHint(new TcoOutCurveHint({type:'outCurve',pos:new TcoPoint({x:6,y:10}),up:false,right:false}))
}

function halfPartsVertical(){
    let turn:TrackElement = l.createElement("htv-1");
    turn.addHint(new TcoHalfTurnOutHint({type:'halfTurnOut',pos:new TcoPoint({x:1,y:14}),up:false,right:true, vertical:true}))
    turn= l.createElement("htv-2");
    turn.addHint(new TcoHalfTurnOutHint({type:'halfTurnOut',pos:new TcoPoint({x:5,y:14}),up:false,right:false, vertical:true}))

    turn= l.createElement("htv-3");
    turn.addHint(new TcoHalfTurnOutHint({type:'halfTurnOut',pos:new TcoPoint({x:1,y:19}),up:true,right:true, vertical:true}))
    turn= l.createElement("htv-4");
    turn.addHint(new TcoHalfTurnOutHint({type:'halfTurnOut',pos:new TcoPoint({x:5,y:19}),up:true,right:false, vertical:true}))


    turn= l.createElement("htv-5");
    turn.addHint(new TcoOutCurveHint({type:'outCurve',pos:new TcoPoint({x:10,y:23}),up:true,right:true, vertical:true}))
    turn= l.createElement("htv-6");
    turn.addHint(new TcoOutCurveHint({type:'outCurve',pos:new TcoPoint({x:9,y:23}),up:true,right:false, vertical:true}))

    turn= l.createElement("htv-7");
    turn.addHint(new TcoOutCurveHint({type:'outCurve',pos:new TcoPoint({x:10,y:14}),up:false,right:true, vertical:true}))
    turn= l.createElement("htv-8");
    turn.addHint(new TcoOutCurveHint({type:'outCurve',pos:new TcoPoint({x:9,y:14}),up:false,right:false, vertical:true}))
}


function build_to_layout(){
    l = new Layout("Test Layout");
    halfPartsHorizontal()
    halfPartsVertical()
//    verticalTurnout()
//    horizontalTurnout()
//    horizontalLadder()
//    verticalLadder()
}

export async function turnouts_demo():Promise<void>{
    build_to_layout();
    console.log("Packed: ")
    console.log(l.toJson())


    let opts:PainterTcoOptions={
        name:"TestTurnouts",
        format: 'svg',
        outFile:'turnouts.svg',
        size:{height:24,width:41},
        sizeInGrid:true,
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