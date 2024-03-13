import { BaseElement, TrackElement} from 'mrcp-layout-model'
import { PainterTco, TcoPainterHint } from './PainterTco'
import { initTrack, paintTrack, t_track } from './Track'
import { t_TcoBasicHint } from './Types'
import { tcoPoint } from './Point'

export type t_CurveHint = t_TcoBasicHint&{
    left:boolean
    up:boolean
    radius:number
}

export class TcoCurveHint extends TcoPainterHint<t_CurveHint>{

    private tracks:t_track[]=[{pos:{x:0,y:0},end:{x:0,y:0}},{pos:{x:0,y:0},end:{x:0,y:0}},{pos:{x:0,y:0},end:{x:0,y:0}}];
    constructor(hint:t_CurveHint){
        super(hint)
        
        
        this.tracks.map((t)=>{t.color=hint.color;t.pos=hint.pos})
    }

    paintSelf(paper: PainterTco) {
        let el:BaseElement = this.element as BaseElement;
        if (this.hint.color==undefined){
            this.hint.color=paper.options.trackColor;
        }
        let radius=this.hint.radius
        let delta1=1+2*radius;
        let delta2=2*(radius-1);

        let dx=1;
        let dsy=0;
        let dsx=0;
        let dy=1;

        if (this.hint.left){
            dx=-1;
            dsx=1
        }

        if (this.hint.up){
            dy=-1
            dsy=1
        }

        let pos= tcoPoint(this.hint.pos)

        let pa=pos.move({x:dx*delta1,y:dy*delta2})
        pa.point.pos='center'
        let sa=pos.move({x:dx*delta1,y:dsy})
        sa.point.pos='top'
        let pb=pos.move({x:dx*delta2,y:dy*delta1})
        pb.point.pos='center'
        let sb=pos.move({x:dsx,y:dy*delta1})
        sb.point.pos='left'

        this.tracks[0].pos=sa
        this.tracks[0].end=pa
        
        this.tracks[1].pos=pa
        this.tracks[1].end=pb
        
        this.tracks[2].pos=pb
        this.tracks[2].end=sb
        

        let layer=paper.layers.track;
        let circle= paper.circle(pa,paper.options.trackSize/2,'center').attr({stroke:"none",fill:this.hint.color})
        layer.add(circle)
        circle= paper.circle(pb,paper.options.trackSize/2,'center').attr({stroke:"none",fill:this.hint.color})
        layer.add(circle)
        
        this.tracks.map((track)=>{
            if(track.color==undefined)track.color=this.hint.color;
            initTrack(track);
            paintTrack(paper,track)
        })
        
        console.log("painting: "+el.id)
    }

}