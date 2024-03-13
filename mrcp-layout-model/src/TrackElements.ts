import { Hint, t_BasicHint } from "./Hints";
import { Layout } from "./Layout";



export type t_BaseElement = {
    id: string;
    type: 'element' | 'track' | 'leftTurnOut' | 'rightTurnout'
    millestone?: string
    hints?: { [ns: string]: t_BasicHint[] }
    childs?: t_BaseElement[]
}

export type t_TrackElement = t_BaseElement & {
    connections?: { [key: string]: string }
}

export class BaseElement {
    public constructor(layout: Layout, element: t_BaseElement) {
        this._element = element;
        this._layout = layout;
        this._hints = {}

        this._childs=[]
    }

    protected _element: t_TrackElement;
    protected _layout: Layout;
    protected _hints: { [ns: string]: Hint[] }
    protected _childs: BaseElement[];

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

    public pack(): t_BaseElement {
        this._element.hints = {}
        
        Object.keys(this._hints).map((ns) => {
            this._element.hints[ns] = []
            this._hints[ns].map((hint, i) => {
                this._element.hints[ns][i] = hint.pack();
            })
        })
        
        return this._element;
    }

    public addHint(hint: Hint) {
        let ns = hint.ns;
        if (this._hints[ns] == undefined)
            this._hints[ns] = []
        this._hints[ns].push(hint)
        hint.element = this
    }

    public hints(ns: string): Hint[] {
        return this._hints[ns];
    }

    public addChild(child:BaseElement){
        this._childs.push(child)
    }
    public getChilds():BaseElement[]{
        return this._childs;
    }
}
export class TrackElement extends BaseElement {
    
    protected _connections:{ [key: string]: TrackElement }

    public constructor(layout: Layout, element: t_TrackElement) {
        super(layout, element)
        this._connections={}
    }

    public get_connection(key:string): TrackElement {
        return this._connections[key];
    }
    public addConnection(key:string,track:TrackElement) {
        this._connections[key]=track;
    }
}
