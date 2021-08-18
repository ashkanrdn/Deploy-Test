var app = require("./app");
var socket = require("socket.io");
const mongoose = require("mongoose");
const ControlsState = require("./models/ControlsStateModel");
// Connect to mongodb
const dbURI = "mongodb+srv://ashkan:12345ashkan@amps.sytdb.mongodb.net/amps-db?retryWrites=true&w=majority";
let port = 3000;
// Connecting to the mongo cluster
mongoose
    .connect(dbURI, { useUnifiedTopology: true, useNewUrlParser: true, useFindAndModify: false, useCreateIndex: true })
    .then(
        (result) =>
        (server = app.listen(process.env.PORT || 3000, () => {
            console.log("listening for requests on port " + port);
        }))
    )
    // creating socket server and socket functions
    .then((result) => {
        io = socket(server);
        // _________________ Connection Established  _________________
        io.on("connection", (socket) => {
            console.log("AMPS Unit Connected");
            // _________________ LED _________________
            socket.on("LEDchanged", (state) => {
                let stateTemp = JSON.parse(state);
                console.log("LEDChanged ==> ", stateTemp.LED_Values);
                const controlsState = new ControlsState({
                    LED_Values: {
                        LEDGrowMain: stateTemp.LED_Values.LEDGrowMain,
                        LEDGrowSup1: stateTemp.LED_Values.LEDGrowSup1,
                        LEDGrowSup2: stateTemp.LED_Values.LEDGrowSup2,
                        LEDGrowMainPwr: stateTemp.LED_Values.LEDGrowMainPwr,
                    },
                    AIR_Values: {
                        AIRMainPwr: stateTemp.AIR_Values.AIRMainPwr,
                    },
                    IRG_Values: {
                        IRGMainPump: stateTemp.IRG_Values.IRGMainPump,
                        IRGWtrSol: stateTemp.IRG_Values.IRGWtrSol,
                        IRGNutrSol: stateTemp.IRG_Values.IRGNutrSol,
                        IRGTrnsPump: stateTemp.IRG_Values.IRGTrnsPump,
                        IRGLight: stateTemp.IRG_Values.IRGLight,
                        IRGlvl5Sol: stateTemp.IRG_Values.IRGlvl5Sol,
                        IRGlvl4Sol: stateTemp.IRG_Values.IRGlvl4Sol,
                        IRGlvl3Sol: stateTemp.IRG_Values.IRGlvl3Sol,
                        IRGlvl2Sol: stateTemp.IRG_Values.IRGlvl2Sol,
                        IRGlvl1Sol: stateTemp.IRG_Values.IRGlvl1Sol,
                    },
                    ARM_Values: {
                        swingArmPWR: stateTemp.ARM_Values.swingArmPWR,
                        swingArmLoc: stateTemp.ARM_Values.swingArmLoc,
                        swingArmL: stateTemp.ARM_Values.swingArmL,
                        swingArmR: stateTemp.ARM_Values.swingArmR,
                    },
                });
                controlsState.save();
                io.emit("LEDchanged", JSON.stringify(stateTemp.LED_Values));
            });
            // _________________ AIR _________________
            socket.on("AIRChanged", (state) => {
                let stateTemp = JSON.parse(state);
                console.log("AIRChanged ==> ", stateTemp.AIR_Values);
                const controlsState = new ControlsState({
                    LED_Values: {
                        LEDGrowMain: stateTemp.LED_Values.LEDGrowMain,
                        LEDGrowSup1: stateTemp.LED_Values.LEDGrowSup1,
                        LEDGrowSup2: stateTemp.LED_Values.LEDGrowSup2,
                        LEDGrowMainPwr: stateTemp.LED_Values.LEDGrowMainPwr,
                    },
                    AIR_Values: {
                        AIRMainPwr: stateTemp.AIR_Values.AIRMainPwr,
                    },
                    IRG_Values: {
                        IRGMainPump: stateTemp.IRG_Values.IRGMainPump,
                        IRGWtrSol: stateTemp.IRG_Values.IRGWtrSol,
                        IRGNutrSol: stateTemp.IRG_Values.IRGNutrSol,
                        IRGTrnsPump: stateTemp.IRG_Values.IRGTrnsPump,
                        IRGLight: stateTemp.IRG_Values.IRGLight,
                        IRGlvl5Sol: stateTemp.IRG_Values.IRGlvl5Sol,
                        IRGlvl4Sol: stateTemp.IRG_Values.IRGlvl4Sol,
                        IRGlvl3Sol: stateTemp.IRG_Values.IRGlvl3Sol,
                        IRGlvl2Sol: stateTemp.IRG_Values.IRGlvl2Sol,
                        IRGlvl1Sol: stateTemp.IRG_Values.IRGlvl1Sol,
                    },
                    ARM_Values: {
                        swingArmPWR: stateTemp.ARM_Values.swingArmPWR,
                        swingArmLoc: stateTemp.ARM_Values.swingArmLoc,
                        swingArmL: stateTemp.ARM_Values.swingArmL,
                        swingArmR: stateTemp.ARM_Values.swingArmR,
                    },
                });
                controlsState.save();
                io.emit("AIRChanged", JSON.stringify(stateTemp.AIR_Values));
            });
            // _________________ IRG _________________
            socket.on("IRGChanged", (state) => {
                let stateTemp = JSON.parse(state);
                console.log("IRGChanged ==> ", stateTemp.IRG_Values);
                const controlsState = new ControlsState({
                    LED_Values: {
                        LEDGrowMain: stateTemp.LED_Values.LEDGrowMain,
                        LEDGrowSup1: stateTemp.LED_Values.LEDGrowSup1,
                        LEDGrowSup2: stateTemp.LED_Values.LEDGrowSup2,
                        LEDGrowMainPwr: stateTemp.LED_Values.LEDGrowMainPwr,
                    },
                    AIR_Values: {
                        AIRMainPwr: stateTemp.AIR_Values.AIRMainPwr,
                    },
                    IRG_Values: {
                        IRGMainPump: stateTemp.IRG_Values.IRGMainPump,
                        IRGWtrSol: stateTemp.IRG_Values.IRGWtrSol,
                        IRGNutrSol: stateTemp.IRG_Values.IRGNutrSol,
                        IRGTrnsPump: stateTemp.IRG_Values.IRGTrnsPump,
                        IRGLight: stateTemp.IRG_Values.IRGLight,
                        IRGlvl5Sol: stateTemp.IRG_Values.IRGlvl5Sol,
                        IRGlvl4Sol: stateTemp.IRG_Values.IRGlvl4Sol,
                        IRGlvl3Sol: stateTemp.IRG_Values.IRGlvl3Sol,
                        IRGlvl2Sol: stateTemp.IRG_Values.IRGlvl2Sol,
                        IRGlvl1Sol: stateTemp.IRG_Values.IRGlvl1Sol,
                    },
                    ARM_Values: {
                        swingArmPWR: stateTemp.ARM_Values.swingArmPWR,
                        swingArmLoc: stateTemp.ARM_Values.swingArmLoc,
                        swingArmL: stateTemp.ARM_Values.swingArmL,
                        swingArmR: stateTemp.ARM_Values.swingArmR,
                    },
                });
                controlsState.save();
                io.emit("IRGChanged", JSON.stringify(stateTemp.IRG_Values));
            });
            // IRG Cycles
            socket.on("IRGCycleWtr", (state) => {
                console.log("IRG Cycle Changed: " + state);
                io.emit("IRGCycleWtr", state);
            });
            socket.on("IRGCycleNutr", (state) => {
                console.log("IRG Cycle Nutr Changed: " + state);
                io.emit("IRGCycleNutr", state);
            });
            // _________________ ARM _________________
            // ARM Controls
            socket.on("ARMChanged", (state) => {
                let stateTemp = JSON.parse(state);
                console.log("ARMChanged ==> ", stateTemp.ARM_Values);
                const controlsState = new ControlsState({
                    LED_Values: {
                        LEDGrowMain: stateTemp.LED_Values.LEDGrowMain,
                        LEDGrowSup1: stateTemp.LED_Values.LEDGrowSup1,
                        LEDGrowSup2: stateTemp.LED_Values.LEDGrowSup2,
                        LEDGrowMainPwr: stateTemp.LED_Values.LEDGrowMainPwr,
                    },
                    AIR_Values: {
                        AIRMainPwr: stateTemp.AIR_Values.AIRMainPwr,
                    },
                    IRG_Values: {
                        IRGMainPump: stateTemp.IRG_Values.IRGMainPump,
                        IRGWtrSol: stateTemp.IRG_Values.IRGWtrSol,
                        IRGNutrSol: stateTemp.IRG_Values.IRGNutrSol,
                        IRGTrnsPump: stateTemp.IRG_Values.IRGTrnsPump,
                        IRGLight: stateTemp.IRG_Values.IRGLight,
                        IRGlvl5Sol: stateTemp.IRG_Values.IRGlvl5Sol,
                        IRGlvl4Sol: stateTemp.IRG_Values.IRGlvl4Sol,
                        IRGlvl3Sol: stateTemp.IRG_Values.IRGlvl3Sol,
                        IRGlvl2Sol: stateTemp.IRG_Values.IRGlvl2Sol,
                        IRGlvl1Sol: stateTemp.IRG_Values.IRGlvl1Sol,
                    },
                    ARM_Values: {
                        swingArmPWR: stateTemp.ARM_Values.swingArmPWR,
                        swingArmLoc: stateTemp.ARM_Values.swingArmLoc,
                        swingArmL: stateTemp.ARM_Values.swingArmL,
                        swingArmR: stateTemp.ARM_Values.swingArmR,
                    },
                });
                controlsState.save();
                io.emit("ARMChanged", JSON.stringify(stateTemp.ARM_Values));
            });
            // ARM Calibrate
            socket.on("ARMCalibrate", (state) => {
                console.log("ArmCalibrate");
                io.emit("ARMCalibrate", JSON.stringify(stateTemp.ARM_Values));
            });
            // ARM Location
            socket.on("ARMLoc", (state) => {
                let stateTemp = JSON.parse(state);

                console.log("ARMChanged ==> ", stateTemp.Arm_Values);

                const controlsState = new ControlsState({
                    LED_Values: {
                        LEDGrowMain: stateTemp.LED_Values.LEDGrowMain,
                        LEDGrowSup1: stateTemp.LED_Values.LEDGrowSup1,
                        LEDGrowSup2: stateTemp.LED_Values.LEDGrowSup2,
                        LEDGrowMainPwr: stateTemp.LED_Values.LEDGrowMainPwr,
                    },
                    AIR_Values: {
                        AIRMainPwr: stateTemp.AIR_Values.AIRMainPwr,
                    },
                    IRG_Values: {
                        IRGMainPump: stateTemp.IRG_Values.IRGMainPump,
                        IRGWtrSol: stateTemp.IRG_Values.IRGWtrSol,
                        IRGNutrSol: stateTemp.IRG_Values.IRGNutrSol,
                        IRGTrnsPump: stateTemp.IRG_Values.IRGTrnsPump,
                        IRGLight: stateTemp.IRG_Values.IRGLight,
                        IRGlvl5Sol: stateTemp.IRG_Values.IRGlvl5Sol,
                        IRGlvl4Sol: stateTemp.IRG_Values.IRGlvl4Sol,
                        IRGlvl3Sol: stateTemp.IRG_Values.IRGlvl3Sol,
                        IRGlvl2Sol: stateTemp.IRG_Values.IRGlvl2Sol,
                        IRGlvl1Sol: stateTemp.IRG_Values.IRGlvl1Sol,
                    },
                    ARM_Values: {
                        swingArmPWR: stateTemp.ARM_Values.swingArmPWR,
                        swingArmLoc: stateTemp.ARM_Values.swingArmLoc,
                        swingArmL: stateTemp.ARM_Values.swingArmL,
                        swingArmR: stateTemp.ARM_Values.swingArmR,
                    },
                });
                controlsState.save();
                io.emit("ARMLoc", JSON.stringify(stateTemp.ARM_Values));
            });
            // _________________ SCHEDULE _________________
            socket.on("scheduleWTR", (state) => {
                console.log("scheduleWTR Changed: " + state);
                io.emit("scheduleWTR", state);
            });
            // _________________ DISCONNECTION _________________
            socket.on("disconnect", () => {
                console.log("user disconnected");
            });
        });
    })
    .catch((err) => console.log(error));