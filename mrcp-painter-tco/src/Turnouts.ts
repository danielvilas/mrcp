import { TcoLedHint, t_LedHint } from "./Led"
import { PainterTco, PainterTcoOptions, TcoPainterHint } from "./PainterTco"
import { TcoPoint, tcoPoint } from "./Point"
import { TcoSwitchHint } from "./Switch"
import { TcoTrackHint, initTrack, paintTrack, t_track } from "./Track"
import { t_TcoBasicHint } from "./Types"

export type t_BaseTurnOutHint = t_TcoBasicHint&{
    right?:boolean
    up?:boolean
    vertical?:boolean
}

const defBaseToHint:t_BaseTurnOutHint={
    pos:undefined,
    type:undefined,
    right:true,
    up:true,
    vertical:false
}

export type t_HalfTurnOutHint = t_TcoBasicHint&t_BaseTurnOutHint&{
    thrownTrackColor?:string, 
    closedColor?:string
    thrownColor?:string
}

export type t_TurnOutHint=t_HalfTurnOutHint 

const defaultHalfToHint:t_HalfTurnOutHint={
    pos:undefined,
    type:undefined,
    right:true,
    up:true,
    vertical:false
}

export class TcoTurnOutHint extends TcoPainterHint<t_TurnOutHint>{
    private halfTurnOut:TcoHalfTurnOutHint
    private outCurve:TcoOutCurveHint
    private track:t_track

    constructor(hint:t_HalfTurnOutHint){
        super({...defaultHalfToHint, ...hint})
    
        this.halfTurnOut=new TcoHalfTurnOutHint({...this.hint});
        this.outCurve=new TcoOutCurveHint({...this.hint});
        this.track={pos:undefined,end:undefined,color:this.hint.color}
    }
    paintSelf(paper: PainterTco) {
        let pos = tcoPoint(this.hint.pos)
        if(this.hint.color==undefined)
            this.hint.color=paper.options.trackColor;
        if(this.hint.vertical){
            if(this.hint.up){
                this.halfTurnOut.hint.pos =pos.move({x:0, y:4})
            }else{
                this.halfTurnOut.hint.pos = this.hint.pos
            }
        }else{
            if(this.hint.right){
                this.halfTurnOut.hint.pos = this.hint.pos
            }else{
                this.halfTurnOut.hint.pos = pos.move({x:4, y:0})
            }
        }
        this.halfTurnOut.paintSelf(paper)

        let dx = 0
        let dy = 0
        if (this.hint.vertical){
            dx = -1
            dy = 4
            if (this.hint.right){
                dx = 1
            }
            if (this.hint.up){
                dy = 4
            }
        }else{
            dx = 0
            dy = 1
            if (this.hint.right){
                dx = 4
            }
            if (this.hint.up){
                dy = -1
            }
        }
        this.outCurve.hint.pos=pos.move({x:dx,y:dy})

        this.outCurve.paintSelf(paper)

        let start:TcoPoint
        let end:TcoPoint
        if (this.hint.vertical){
            start = pos.move( {x:0, y:4})
            end = pos.move( {x:0, y:8})
            if (this.hint.up){
                start = pos.move( {x:0, y:0})
                end = pos.move( {x:0, y:4})
            }
            start.point.pos='top'
            end.point.pos='top'
        }else{ 
            start = pos.move({x:0, y:0})
            end = pos.move({x:4, y:0})
            if (this.hint.right){
                start = pos.move({x:4, y:0})
                end = pos.move({x:8, y:0})
            }
            start.point.pos='left'
            end.point.pos='left'
        }
        this.track.pos=start
        this.track.end=end
        initTrack(this.track)
        paintTrack(paper,this.track)
    }

}

export class TcoHalfTurnOutHint extends TcoPainterHint<t_HalfTurnOutHint>{

    private mainTrack:t_track
    private thrownTrack:t_track
    private switch:TcoSwitchHint
    private ledCl:TcoLedHint
    private ledTh:TcoLedHint
    constructor(hint:t_HalfTurnOutHint){
        super({...defaultHalfToHint, ...hint})
        
        this.mainTrack={pos:undefined,end:undefined,color:this.hint.color}
        this.thrownTrack={pos:undefined,end:undefined,color:this.hint.thrownTrackColor}
        this.switch=new TcoSwitchHint({type:"Switch",pos:undefined,color:this.hint.color,vertical:!this.hint.vertical})
        
        if(this.hint.closedColor!="none"){
            this.ledCl = new TcoLedHint({type:"Led.Closed",pos:undefined,color:this.hint.closedColor})
        }
        if(this.hint.closedColor!="none")
            this.ledTh = new TcoLedHint({type:"Led.Thrown",pos:undefined,color:this.hint.thrownColor})
        
    }

    setColors(cfg:PainterTcoOptions){
        if (this.hint.color == undefined)
            this.hint.color = cfg.trackColor
        if (this.thrownTrack.color == undefined)
            this.thrownTrack.color = cfg.trackColor
        if(this.ledCl &&  this.ledCl.hint.color == undefined)
            this.ledCl.hint.color= cfg.closedLedColor
        if(this.ledTh && this.ledTh.hint.color == undefined)
            this.ledTh.hint.color= cfg.thrownLedColor
    }

    paintSelf(paper: PainterTco) {
        //throw new Error("Method not implemented.")
        this.setColors(paper.options)


        if (this.hint.vertical)
            this.paintVertical(paper)
        else
            this.paintHorizontal(paper)

        initTrack(this.thrownTrack);
        paintTrack(paper,this.thrownTrack)
        initTrack(this.mainTrack);
        paintTrack(paper,this.mainTrack)

        /*self._switch.paint()*/
        this.switch.paintSelf(paper)
        //console.log("painting leds")
        if(this.ledCl!=undefined) this.ledCl.paintSelf(paper)
        if(this.ledTh!=undefined) this.ledTh.paintSelf(paper)

    }

    paintVertical(paper:PainterTco){
        let dx = -1
        if(this.hint.right)
            dx = 1
        let pos = tcoPoint(this.hint.pos)
        //left

        let swPoint = pos.move({x:0,y:2})
        swPoint.point.pos='top'
        //this.switch.point.pos=swPoint

        let thPoint = pos.move({x:dx,y:3})
        thPoint.point.pos='bottom'
    
        let clPoint = pos.move({x:0,y:3})
        clPoint.point.pos='bottom'
        let stPoint = pos.move({x:0,y:0})
        stPoint.point.pos='top'


        if(this.hint.up){
            //swPoint = pointH(pos=pos, delta=(2, 0))
            //swStart = pointH(pos=pos, delta=(2, 0), adjust=(-5, -7.5))
            thPoint = pos.move({x:dx,y:0})
            thPoint.point.pos='top'
            clPoint = pos.move({x:0,y:0})
            clPoint.point.pos='top'
            stPoint = pos.move({x:0,y:3})
            stPoint.point.pos='bottom'
        }
        let cutLayer = paper.layers.cut
        let ledLayer = paper.layers.led

        this.drawHalfTurnout(paper, stPoint, cutLayer, ledLayer, swPoint, thPoint, clPoint)

    }

    paintHorizontal(paper:PainterTco){
        let dy = 1
        if(this.hint.up)
            dy = -1
        let pos = tcoPoint(this.hint.pos)
        // left
        let swPoint = pos.move({x:2,y:0})
        swPoint.point.pos='left'
        //self._switch._pos=swPoint
        

        let thPoint = pos.move({x:0,y:dy})
        thPoint.point.pos='left'
        let clPoint = pos.move({x:0,y:0})
        clPoint.point.pos='left'
        let stPoint = pos.move({x:3,y:0})
        stPoint.point.pos='right'
        if(this.hint.right){
            //swPoint = pointH(pos=pos, delta=(2, 0))
            //#swStart = pointH(pos=pos, delta=(2, 0), adjust=(-5, -7.5))
            thPoint = pos.move({x:3,y:dy})
            thPoint.point.pos='right'
            clPoint = pos.move({x:3,y:0})
            clPoint.point.pos='right'
            stPoint = pos.move({x:0,y:0})
            stPoint.point.pos='left'
        }
        let cutLayer = paper.layers.cut
        let ledLayer = paper.layers.led

        //let swSize = paper.options.SWITH_SIZE
        this.drawHalfTurnout(paper, stPoint, cutLayer, ledLayer, swPoint, thPoint, clPoint)
    }


    drawHalfTurnout(paper:PainterTco,stPoint:TcoPoint,cutLayer:Snap.Paper,ledLayer:Snap.Paper,swPoint:TcoPoint,thPoint:TcoPoint,clPoint:TcoPoint):void{
        this.mainTrack.pos=stPoint
        this.mainTrack.end=clPoint

        this.thrownTrack.pos=swPoint
        this.thrownTrack.end=thPoint

        if(this.ledTh)this.ledTh.hint.pos=thPoint
        if(this.ledCl)this.ledCl.hint.pos=clPoint

        this.switch.hint.pos=swPoint

    }
}


export class TcoOutCurveHint extends TcoPainterHint<t_BaseTurnOutHint>{
    private tracks:t_track[]=[{pos:{x:0,y:0},end:{x:0,y:0}},{pos:{x:0,y:0},end:{x:0,y:0}}];
    constructor(hint:t_HalfTurnOutHint){
        super({...defBaseToHint, ...hint})
    }

    paintSelf(paper: PainterTco) {
        if (this.hint.color ==undefined)
            this.hint.color= paper.options.trackColor
        
        let dy = 1
        if(this.hint.up)
            dy = -1
        let pos = tcoPoint(this.hint.pos)

        let thHalfPoint:TcoPoint
        let thPoint:TcoPoint
        let thEnd:TcoPoint
        if (this.hint.vertical){
            thHalfPoint =pos.move({x:0, y:0})
            thPoint = pos.move({x:-1, y:2*dy})
            thEnd = pos.move( {x:-1, y:4*dy})
            if (this.hint.right){
                thHalfPoint = pos.move({x:0, y:0})
                thPoint = pos.move( {x:1, y:2*dy})
                thEnd = pos.move({x:1, y:4*dy})
            }
            thEnd.point.pos='top'
            thPoint.point.pos='top'
            thHalfPoint.point.pos='top'
        }else{
            thHalfPoint = pos.move({x:4, y:0})
            thPoint = pos.move({x:2, y:dy})
            thEnd = pos.move( {x:0, y:dy})
            if (this.hint.right){
                thHalfPoint = pos.move({x:0, y:0})
                thPoint = pos.move({x:2, y:dy})
                thEnd = pos.move({x:4, y:dy})
            }
            thEnd.point.pos='left'
            thPoint.point.pos='left'
            thHalfPoint.point.pos='left'
        }
        
        this.tracks[0].pos=thPoint
        this.tracks[0].end=thEnd
        this.tracks[1].pos=thHalfPoint
        this.tracks[1].end=thPoint
       
        let layer=paper.layers.track;
        let circle= paper.circle(thPoint,paper.options.trackSize/2).attr({stroke:"none",fill:this.hint.color})
        layer.add(circle)
        
        this.tracks.map((track)=>{
            if(track.color==undefined)track.color=this.hint.color;
            initTrack(track);
            paintTrack(paper,track)
        })
    }
}