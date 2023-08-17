import { curves_demo} from './curves'
import {endPainterProcess} from 'mrcp-painter-tco'

async function t(){
    await curves_demo();
    endPainterProcess();
    process.exit();
}


t()
