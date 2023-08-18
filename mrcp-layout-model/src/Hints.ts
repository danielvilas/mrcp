import { TrackElement } from "./TrackElements";

export abstract class Hint{

    constructor(ns?:string){
        this._ns=ns;
    }
    private _ns: string;
    private _element: TrackElement;
    
    //Get Set
    public get element(): TrackElement {
        return this._element;
    }
    public set element(value: TrackElement) {
        this._element = value;
    }

    public get ns(): string {
        return this._ns;
    }
    public set ns(value: string) {
        this._ns = value;
    }

    //Methods
    public abstract pack():t_BasicHint;

}

export type t_BasicHint={
    type:string; 
}

export class BasicHint<T extends t_BasicHint> extends Hint{
    constructor(ns?:string,hint?:T){
        super(ns);
        this._hint=hint;
    }
    
    private _hint: T;
    
    public get hint(): T {
        return this._hint;
    }
    public set hint(value: T) {
        this._hint = value;
    }

    public pack(): t_BasicHint {
        return this._hint;
    }

}