const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const controlSchema = new Schema({
    // Update Schema

    LED_Values: [{
        LEDGrowMain: { type: Number },
        LEDGrowSup1: { type: Number },
        LEDGrowSup2: { type: Number },
        LEDGrowMainPwr: { type: Number },
    }, ],
    AIR_Values: [{ AIRMainPwr: { type: Number } }],
    IRG_Values: [{
        IRGMainPump: { type: Number },
        IRGWtrSol: { type: Number },
        IRGNutrSol: { type: Number },
        IRGTrnsPump: { type: Number },
        IRGLight: { type: Number },
        IRGlvl5Sol: { type: Number },
        IRGlvl4Sol: { type: Number },
        IRGlvl3Sol: { type: Number },
        IRGlvl2Sol: { type: Number },
        IRGlvl1Sol: { type: Number },
    }, ],
    ARM_Values: [{
        swingArmPWR: { type: Number },
        swingArmLoc: { type: Number },
        swingArmL: { type: Boolean },
        swingArmR: { type: Boolean },
    }, ],
}, { timestamps: true });

const ControlsState = mongoose.model("ControlsState", controlSchema);

module.exports = ControlsState;