import { PainterTcoOptions } from "./PainterTco"

export type t_TcoPlaces='center'|'top'|'bottom'|'left'|'right'|'top-left'|'top-rigth'|'bottom-left'|'bottom-right'

export type t_TcoBase={
    pos: t_TcoPoint | TcoPoint
    color:string
}

export type t_TcoPoint={
    x:number,
    y:number,
    pos?:t_TcoPlaces
}

export class TcoPoint{
    private _point: t_TcoPoint;
    constructor (point:t_TcoPoint={x:0,y:0}){
        this._point=point;
    }

    public get point(): t_TcoPoint {
        return this._point;
    }

    public set point(value: t_TcoPoint) {
        this._point = value;
    }

    public move(delta:TcoPoint|t_TcoPoint):TcoPoint{
        let _delta=tcoPoint(delta)._point
        let ret = new TcoPoint({x:this._point.x+_delta.x,
            y:this._point.y+_delta.y,
            pos:this._point.pos
            })
        //TODO handle pos updates,...
        return ret 
    }

    public toCoords(config:PainterTcoOptions,place?:t_TcoPlaces):[number,number]{
        if( place == undefined && this._point.pos != undefined){
            place = this._point.pos
        }
        //ax,ay=adjust
        let ax=0, ay=0;
        if (place==undefined || place=='center'){
            ax+=config.gridBase/2
            ay+=config.gridBase/2
        }else if( place=='top'){
            ax+=config.gridBase/2
        }else if( place=='left'){
            ay+=config.gridBase/2
        }else if( place=='bottom'){
            ax+=config.gridBase/2
            ay+=config.gridBase
        }else if( place=='right'){
            ay+=config.gridBase/2
            ax+=config.gridBase
        }else if( place=='bottom-left'){
            ay+=config.gridBase
        }else if( place=='bottom-right'){
            ay+=config.gridBase
            ax+=config.gridBase
        }else if( place=='top-left'){
            ay+=0
        }else if( place=='top-rigth'){
            ax+=config.gridBase
        }
        let xf=(this._point.x)*config.gridBase+ax
        let yf=(this._point.y)*config.gridBase+ay
        return [xf,yf]
    }
}

export function tcoPoint(inPoint:TcoPoint|t_TcoPoint|[x:number,y:number]):TcoPoint{
    if(inPoint instanceof TcoPoint)
        return inPoint;
    // if(inPoint is t_tcoPoint)
    if(Array.isArray(inPoint)){
        return new TcoPoint({x:inPoint[0],y:inPoint[1]})
    }else{
        return new TcoPoint(inPoint)
    }
}