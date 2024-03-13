import { BaseElement, t_BasicHint } from "mrcp-layout-model"
import { TcoPoint, tcoPoint } from "./Point"
import { PainterTco, TcoPainterHint } from "./PainterTco"
import { t_TcoBase, t_TcoPoint } from "./Types"

export type t_track=t_TcoBase&{
    end:t_TcoPoint | TcoPoint
}

export type t_TrackHint=t_BasicHint & t_track

export class TcoTrackHint extends TcoPainterHint<t_TrackHint>{
    constructor(hint:t_TrackHint){
        super(hint)
        initTrack(hint);
    }

    paintSelf(paper: PainterTco) {
        let el:BaseElement = this.element;
        paintTrack(paper,this.hint)
        console.log("painting: "+el.id)
    }
}

export function initTrack(track:t_track){
    let pos = track.pos = tcoPoint(track.pos).point;
    let end = track.end = tcoPoint(track.end).point;


    let dx=end.x- pos.x
    let dy=end.y -pos.y
    if (pos.pos==undefined && end.pos==undefined){
        if (dx == 0 && dy ==0){
            return
        }else if( dx==0 && dy >0){
            pos.pos='top'
            end.pos='bottom'
        }else if( dx==0 && dy <0){
            pos.pos='bottom'
            end.pos='top'
        }else if( dy==0 && dx>0){
            pos.pos='left'
            end.pos='right'
        }else if( dy==0 && dx<0){
            pos.pos='right'
            end.pos='left'
        }
    }else if(pos.pos == undefined){
        pos.pos='center'
    }else if(end.pos == undefined){
        end.pos='center'
    }
}

export function paintTrack(paper:PainterTco,track:t_track):void{
    let start=tcoPoint(track.pos);
    let end=tcoPoint(track.end);
  
    let [x0,y0]=end.toCoords(paper.options)
    let[xf,yf]=start.toCoords(paper.options)
    let dx=xf-x0
    let dy=yf-y0
    
    if (dx==0 && dy == 0) return
    let mx=0
    let my=0
    let t=paper.options.trackSize/2

    if (dx==0){
        mx=t
        my=0
    }else if(dy==0){
        mx=0
        my=t
    }else{
        let d=Math.sqrt(dx*dx+dy*dy)
        let dux=dx/d
        let duy=dy/d
        mx=t*duy
        my=-t*dux
    }
    let points=[x0-mx,y0-my, 
        xf-mx,yf-my,
        xf+mx,yf+my, 
        x0+mx,y0+my, 
        x0-mx,y0-my]

    let color = track.color
    let layer = paper.layers.track
    let poly = paper.paper.polyline(points).attr({fill:color,stroke:"none"})
    layer.add(poly)
}