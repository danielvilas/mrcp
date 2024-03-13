import { PainterTco, TcoPainterHint } from "./PainterTco";
import { tcoPoint } from "./Point";
import { t_TcoBasicHint } from "./Types";

export type t_SwitchHint=t_TcoBasicHint &{
    vertical?:boolean
}

const defaultLedHint:t_SwitchHint={
    pos:undefined,
    type:undefined,
    color:undefined,
    vertical:false
}
export class TcoSwitchHint extends TcoPainterHint<t_SwitchHint>{
    constructor(hint:t_SwitchHint){
        super({...defaultLedHint, ...hint})
        
    }
    paintSelf(paper: PainterTco) {
    if(this.hint.color==undefined)
        this.hint.color=paper.options.trackColor;


    let swPoint = tcoPoint(this.hint.pos)
    //let [x,y] = swPoint.toCoords(paper.options,adjust=(-7.5, -5))
    let [x,y] = swPoint.toCoords(paper.options)
    x += -7.5;
    y += -5;
    let swSize= paper.options.switchSizeH
    
    if (this.hint.vertical){
        //[x,y]= swPoint.toCoords(self._config,adjust=(-5, -7.5) )
        [x,y]= swPoint.toCoords(paper.options)
        x += -5;
        y += -7.5;
        swSize= paper.options.switchSize
    }

    let dwg = paper.paper
    let cutLayer = paper.layers.cut
    let tracklayer = paper.layers.track

    // Switch
    let [cx,cy] = swPoint.toCoords(paper.options)
    let circle = dwg.circle(cx,cy, paper.options.switchHoleSize/2).attr({fill:"white"})
    tracklayer.add(circle)

    circle = dwg.circle(cx,cy, paper.options.switchHoleSize/2).attr({stroke:paper.options.cutColor, strokeWidth:0.2, fill:"none"})
    cutLayer.add(circle)

    circle = dwg.circle(cx,cy,paper.options.switchHoleMarginSize/2).attr({stroke:paper.options.engraveColor, strokeWidth:0.2, fill: "none"})
    cutLayer.add(circle)
    
    let rect = dwg.rect(x,y,swSize.x,swSize.y).attr({stroke:paper.options.engraveColor,strokeWidth:0.2, fill:"none"})
    cutLayer.add(rect) 
    }

}