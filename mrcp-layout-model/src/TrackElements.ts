import { Hint, t_BasicHint } from "./Hints";
import { Layout } from "./Layout";



export type t_TrackElement ={
    id:string;
    type:'element'|'leftTurnOut'|'rightTurnout'
    millestone?:string
    connections?:{[key:string]:string}
    hints?:{[ns:string]:t_BasicHint[]}
}

export class TrackElement{
    
    public constructor(layout:Layout,element:t_TrackElement){
        this._element=element;
        this._layout=layout;
        this._hints={};
    }
    
    private _element: t_TrackElement;
    private _layout: Layout;
    private _hints:{[ns:string]:Hint[]}

    // Accesors
    public get id(): string {
        return this._element.id;
    }
    public set id(value: string) {
        this._element.id = value;
    }
    public get layout(): Layout {
        return this._layout;
    }
    public set layout(value: Layout) {
        this._layout = value;
    }

    // methods
    public pack():t_TrackElement{
        this._element.hints={}
        Object.keys(this._hints).map((ns)=>{
            this._element.hints[ns]=[]
            this._hints[ns].map((hint,i)=>{
                this._element.hints[ns][i]=hint.pack();
            })
        })
        return this._element;
    }

    public addHint(hint:Hint){
        let ns= hint.ns;
        if(this._hints[ns]==undefined)
            this._hints[ns]=[]
        this._hints[ns].push(hint)
        hint.element=this
    }

    public hints(ns:string):Hint[]{
        return this._hints[ns];
    }

}