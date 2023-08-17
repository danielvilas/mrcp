import { Layout } from "./Layout";



export type t_TrackElement ={
    id:string;
    type:'element'|'leftTurnOut'|'rightTurnout'
    millestone?:string
    connections?:{[key:string]:string}
}

export class TrackElement{
    
    public constructor(layout:Layout,element:t_TrackElement){
        this._element=element;
        this._layout=layout;
    }
    
    private _element: t_TrackElement;
    private _layout: Layout;

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
        return this._element;
    }
}