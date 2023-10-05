import { curves_demo} from './curves'
import {endPainterProcess} from 'mrcp-painter-tco'
import { turnouts_demo } from './turnouts';

async function t(){
    await curves_demo();
    await turnouts_demo();
    endPainterProcess();
    process.exit();
}


t()
