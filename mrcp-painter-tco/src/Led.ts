import { PainterTco, TcoPainterHint } from "./PainterTco";
import { tcoPoint } from "./Point";
import { t_TcoBasicHint } from "./Types";

export type t_LedHint=t_TcoBasicHint

const defaultLedHint:t_LedHint={
    pos:undefined,
    type:undefined,
    color:undefined
}
export class TcoLedHint extends TcoPainterHint<t_LedHint>{
    constructor(hint:t_LedHint){
        super({...defaultLedHint, ...hint})
        
    }
    paintSelf(paper: PainterTco) {
        if(this.hint.color==undefined)
            this.hint.color=paper.options.ledColor;

        /* Evitar pintar dos veces (tiene que ver con el grabado laser)
        found = searchLed(self._config,self._panel, self._pos)

        if found != self:
            # there is another wich is not self
            # only the first will be painted
            return
        */
        let p_pos= tcoPoint(this.hint.pos)
        let [x,y] = p_pos.toCoords(paper.options)
        let dwg = paper.paper;
        let cutLayer = paper.layers.cut;
        let ledLayer = paper.layers.led;
        let trackLayer = paper.layers.track;
        let circle = dwg.circle(x,y, paper.options.ledSize/2).attr({stroke:"none",fill:this.hint.color})
        ledLayer.add(circle)

        circle = dwg.circle(x,y, paper.options.ledSize/2).attr({fill: "none",stroke: paper.options.cutColor,strokeWidth: 0.2}) 
        cutLayer.add(circle)

        circle = dwg.circle(x,y, paper.options.ledSize/2+paper.options.ledMargin).attr({fill: "none",stroke: paper.options.engraveColor,strokeWidth: 0.2});
        cutLayer.add(circle)

        circle = dwg.circle(x,y, paper.options.ledSize/2).attr({stroke:"white",fill:this.hint.color, strokeWidth: 0.2})
        trackLayer.add(circle)
    }

}