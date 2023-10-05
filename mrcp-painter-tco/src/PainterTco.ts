import { Layout } from 'mrcp-layout-model'
import {t_BasicHint, BasicHint} from 'mrcp-layout-model'
import * as fs from 'fs'
import * as path from 'path';

import {JSDOM} from 'jsdom'
declare global {
    namespace NodeJS {
        interface Global {
            document: Document;
            window: Window;
            navigator: Navigator;
        }
    }
}

const jsEnv = new JSDOM('<!doctype html><html><body></body></html>');
global.window= jsEnv.window.document.defaultView;
global.document=jsEnv.window.document

import Snap = require("snapsvg")
import xmlserializer=require('xmlserializer')
type Size={width: number; height: number;}
import * as cts from './constants'
import { TcoPoint, tcoPoint } from './Point';
import { t_TcoBasicHint, t_TcoPlaces, t_TcoPoint } from './Types';

export type PainterTcoOptions = {
    name:string
    format?: 'svg'|'png'
    size?:Size
    sizeInGrid?:boolean
    outFile?:string
    grid?:boolean
    markStart?:boolean,
    gridBase?:number,
    trackSize?:number,
    trackColor?:string
}

export const PainterTcoDefaultOptions:PainterTcoOptions={
    name:undefined,
    format: 'svg',
    size:{height:100,width:100},
    outFile:"out.svg",
    sizeInGrid:false,
    grid:false,
    markStart:false,
    gridBase:5,
    trackSize:3,
    trackColor:"black"
}


const panelLayersKind=['grid','track','cut','led','outs']
export type PanelLayersKind='grid'|'track'|'cut'|'led'|'outs'
export type PanelLayers={[key in PanelLayersKind]?:Snap.Paper}

export class PainterTco {

    public constructor(_options:PainterTcoOptions) {
        this._options={...PainterTcoDefaultOptions, ..._options}
    }

    private _options: PainterTcoOptions;
    private svg:string

    private _layers: PanelLayers;
    private _paper: Snap.Paper;

    public paint(layout:Layout): void {
        this._layers={};
        if(this._options.sizeInGrid){
            this.options.size.width=this.options.size.width*this.options.gridBase
            this.options.size.height=this.options.size.height*this.options.gridBase
        }
        let paper = Snap(this.options.size.width/10+"cm",this.options.size.height/10+"cm");
        this._paper=paper;
        paper.attr({viewBox:[0,0,this.options.size.width,this.options.size.height].join(',')})
        panelLayersKind.map((value)=>{
            let grp = paper.group();
            grp.attr({id:value});
            paper.add(grp);
            this.layers[value]=grp;
        });
        
        if(this.grid)this.paintGrid();
        let elments= layout.elements
        elments.map((el)=>{
            let h=el.hints(cts.ns);
            if(h.length>0 && h[0] instanceof TcoPainterHint){
                let th:TcoPainterHint<t_TcoBasicHint>=h[0] as TcoPainterHint<t_TcoBasicHint>;
                th.paint(this)
            }
        })

        this.svg = xmlserializer.serializeToString(paper.node);        
    }

    private paintGrid():void {
        let paper=this.paper;
        let layer= this.layers.grid;


        layer.add(paper.rect(0,0,this.options.size.width,this.options.size.height).attr({fill: "white"}))

        var smallPattern = paper.path("M "+this.options.gridBase+" 0 L 0 0 0 "+this.options.gridBase).attr({
                     fill: "none",
                     stroke: "#0000C8",
                     strokeWidth: 0.1
            }).pattern(0, 0, this.options.gridBase, this.options.gridBase);
        
        var bigPattern = paper.rect(0,0,this.options.gridBase*4,this.options.gridBase*4).attr({fill:smallPattern
            }).pattern(0, 0, this.options.gridBase*4, this.options.gridBase*4);

        bigPattern.add(paper.path("M "+this.options.gridBase*4+" 0 L 0 0 0 "+this.options.gridBase*4).attr({
            fill: "none",
            stroke: "#0000C8",
            strokeWidth: 0.2
        }))
        layer.add(paper.rect(0,0,this.options.size.width,this.options.size.height).attr({fill: bigPattern}))

    }

    public grid(grid=true){
        this.options.grid=grid;
    }
    public markStart(markStart=true){
        this.options.markStart=markStart;
    }

    public async save():Promise<void>{
        console.log(this.svg);
        return new Promise<void>((resolve,reject)=>{
            fs.writeFile(path.resolve(this.options.outFile), this.svg, function (err) {
                if (err) reject( err);
                console.log('Saved!');
                resolve();
            });
        });
    }

    public get options(): PainterTcoOptions {
        return this._options;
    }

    public get layers(): PanelLayers {
        return this._layers;
    }
    
    public get paper(): Snap.Paper {
        return this._paper;
    }

    public circle(point:(TcoPoint|t_TcoPoint),r:number,pos?:t_TcoPlaces):Snap.Element{
        let [x,y] = tcoPoint(point).toCoords(this.options,pos);
        return this.paper.circle(x,y,r);
    }
    
    public markPoint(point:(t_TcoPoint | TcoPoint)){    
        let circle=this.circle(point,0.5).attr({stroke:"red",strokeWidth:0.2,fill:"yellow"})
        this.layers.led.add(circle)
    }
}

export abstract class TcoPainterHint<T extends (t_TcoBasicHint)> extends BasicHint<T>{
    constructor(hint:T){
        super(cts.ns,hint)
        this.dirty=true;
    }

    protected dirty:boolean

    public paint(paper:PainterTco):void{
        if(!this.dirty)return;
        this.paintSelf(paper);
        if(paper.options.markStart){
            paper.markPoint(this.hint.pos)
        }
        this.dirty=false
    }

    abstract paintSelf(paper:PainterTco);
}

export function endPainterProcess():void{
    jsEnv.window.close();
    global.window.close();
}

