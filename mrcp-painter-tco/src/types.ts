export type t_TcoPoint={
    x:number,
    y:number,
    pos?:'center'|'top'|'bottom'|'left'|'right'|'top-left'|'top-rigth'|'bottom-left'|'bottom-right'
}

export class TcoPoint{
    private _point: t_TcoPoint;
    constructor (point:t_TcoPoint={x:0,y:0,pos:'center'}){
        this._point=point;
        if(this._point.pos==undefined)this._point.pos='center'
    }

    public get point(): t_TcoPoint {
        return this._point;
    }

    public set point(value: t_TcoPoint) {
        this._point = value;
    }

    public move(delta:TcoPoint|t_TcoPoint):TcoPoint{
        let _delta:t_TcoPoint
        if(delta instanceof TcoPoint){
            _delta=delta.point;
        }else{
            _delta=delta;
        }
        let ret = new TcoPoint({x:this._point.x+_delta.x,
            y:this._point.y+_delta.y,
            pos:this._point.pos
            })
        //TODO handle pos updates,...
        return ret 
    }

}