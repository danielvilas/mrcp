import { TrackElement, t_TrackElement } from "./TrackElements";

export type t_Layout = {
    name:string;
    elements?:t_TrackElement[]
}

export class Layout{
    public constructor(name:string){
        this._layout={
            name:name,
            elements:[]
        }
        this._elements={}
    }

    private _layout: t_Layout;
    private _elements: {[key:string]:TrackElement};


    //Accessors
    public get name(): string {
        return this._layout.name;
    }
    public set name(value: string) {
        this._layout.name = value;
    }

    public element(id:string,element:TrackElement=undefined):TrackElement{
        if(element!=undefined){
            this._elements[id]=element;
        }
        return this._elements[id];
    }

    // Layout Methods
    public pack():{[key:string]:any}{
        this._layout.elements=[];
        Object.keys(this._elements).map((key)=>{
            this._layout.elements.push(this._elements[key].pack());
        })
        return this._layout;
    }
    public toJson():string{
        return JSON.stringify(this.pack());
    }

    public createElement(id:string):TrackElement{
        let e=new TrackElement(this,{id:id,type:'element'});
        this._elements[id]=e;
        return e;
    }

    public get elements():TrackElement[]{
        let ret= []
        Object.keys(this._elements).map((key)=>ret.push(this._elements[key]));
        return ret
    }

}