var app = require('./app');
var socket = require('socket.io');
const mongoose = require('mongoose');



let port = 3000
    // Server start
var server = app.listen(port, function() {
    console.log('listening for requests on port ' + port);
});

// Socket setup & pass server
var io = socket(server);

io.on('connection', (socket) => {
    console.log('AMPS Unit Connected');

    // _________________ LED _________________
    socket.on('LEDchanged', (rangeX) => {
        console.log('LEDchanged Changed: ' + rangeX);
        io.emit('LEDchanged', rangeX);
    });

    // _________________ AIR _________________
    socket.on('AIRChanged', (state) => {
        console.log('AIRChanged Changed: ' + state);
        io.emit('AIRChanged', state);
    });

    // _________________ IRG _________________
    socket.on('IRGChanged', (state) => {
        console.log('IRGChanged Changed: ' + state);
        io.emit('IRGChanged', state);
    });

    // IRG Cycles
    socket.on('IRGCycleWtr', (state) => {
        console.log('IRG Cycle Changed: ' + state);
        io.emit('IRGCycleWtr', state);
    });

    socket.on('IRGCycleNutr', (state) => {
        console.log('IRG Cycle Nutr Changed: ' + state);
        io.emit('IRGCycleNutr', state);
    });

    // _________________ ARM _________________
    // ARM Controls
    socket.on('ARMChanged', (state) => {
        console.log('ArmChanged Changed: ' + state);
        io.emit('ARMChanged', state);
    });

    // ARM Calibrate
    socket.on('ARMCalibrate', (state) => {
        console.log('ArmCalibrate');
        io.emit('ARMCalibrate', state);
    });

    // ARM Location
    socket.on('ARMLoc', (state) => {
        console.log('ArmLoc Changed: ' + state);
        io.emit('ARMLoc', state);
    });


    socket.on('disconnect', () => {
        console.log('user disconnected');
    });
});