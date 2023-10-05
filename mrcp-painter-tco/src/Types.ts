import { t_BasicHint } from "mrcp-layout-model"
import { TcoPoint } from "./Point"

export type t_TcoPlaces='center'|'top'|'bottom'|'left'|'right'|'top-left'|'top-rigth'|'bottom-left'|'bottom-right'

export type t_TcoBase={
    pos: t_TcoPoint | TcoPoint
    color?:string
}

export type t_TcoPoint={
    x:number,
    y:number,
    pos?:t_TcoPlaces
}

export type t_TcoBasicHint = t_TcoBase & t_BasicHint