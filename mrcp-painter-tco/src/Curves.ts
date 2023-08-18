import {t_BasicHint, TrackElement} from 'mrcp-layout-model'
import { t_TcoBase, tcoPoint, TcoPoint } from './Point'
import { PainterTco, TcoPainterHint } from './PainterTco'
import { initTrack, paintTrack, t_track } from './Track'

export type t_CurveHint = t_BasicHint&t_TcoBase&{
    left:boolean
    up:boolean
    radius:number
}

export class TcoCurveHint extends TcoPainterHint<t_CurveHint>{
    constructor(hint:t_CurveHint){
        super(hint)
    }

    paintSelf(paper: PainterTco) {
        let el:TrackElement = this.element;
        let end = tcoPoint(this.hint.pos).move({x:2,y:0})

        let track:t_track={
            pos:this.hint.pos,
            color:this.hint.color,
            end:end
        }
        initTrack(track);
        paintTrack(paper,track)
        console.log("painting: "+el.id)
    }
}