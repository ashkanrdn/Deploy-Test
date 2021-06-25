var app = require("./app");
var socket = require("socket.io");
const mongoose = require("mongoose");

const ControlsState = require("./models/ControlsStateModel");

// Connect to mongodb
const dbURI = "mongodb+srv://ashkan:12345ashkan@amps.sytdb.mongodb.net/amps-db?retryWrites=true&w=majority";

mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true });
let port = 3000;

// Connecting to the mongo cluster
mongoose
    .connect(dbURI, { useUnifiedTopology: true, useNewUrlParser: true, useFindAndModify: false, useCreateIndex: true })
    .then(
        (result) =>
        (server = app.listen(port, () => {
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
                console.log("LEDchanged Changed: " + state);
                // let stateTemp = JSON.parse(state)
                // console.log(stateTemp.LEDGrowMainPwr)
                    // Figure out the proper data add
                // const controlsState = new ControlsState({ conTopic: state.LEDGrowMainPwr });
                // controlsState.save()
                io.emit("LEDchanged",state);
            });

            // _________________ AIR _________________
            socket.on("AIRChanged", (state) => {
                console.log("AIRChanged Changed: " + state);
                io.emit("AIRChanged", state);
            });

            // _________________ IRG _________________
            socket.on("IRGChanged", (state) => {
                console.log("IRGChanged Changed: " + state);
                io.emit("IRGChanged", state);
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
                console.log("ArmChanged Changed: " + state);
                io.emit("ARMChanged", state);
            });

            // ARM Calibrate
            socket.on("ARMCalibrate", (state) => {
                console.log("ArmCalibrate");
                io.emit("ARMCalibrate", state);
            });

            // ARM Location
            socket.on("ARMLoc", (state) => {
                console.log("ArmLoc Changed: " + state);
                io.emit("ARMLoc", state);
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