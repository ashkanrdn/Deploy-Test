var socket = io.connect('/');

// Show the dim value in the Dash

// making the emitter object
let emitter = {
    LEDGrowMain: 0,
    LEDGrowSup1: 0,
    LEDGrowSup2: 0,
    LEDGrowMainPwr: 0,
};

//////////////////////////////////////////////////////// Light Controls \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
// getting the divs with controlsItemInner this is a div that has controls for each control module
let controlItemInner = document.querySelectorAll('.controlsItemInner.lightingCtrl');

Array.prototype.forEach.call(controlItemInner, (div) => {
    //looping through divs and getting the sliders
    if (div.querySelector('input[type=range]') !== null) {
        div.querySelector('input[type=range]').addEventListener('click', (event) => {
            // Showing the Dim Value
            div.querySelector('span').innerHTML = 'Dim: ' + event.target.value + ' %';
            // getting the ID of the control by it's classname
            let controlId = event.target.className;
            // remapping the value to be between 0 - 1
            let controlValue = event.target.value * 0.01;
            // we make the check box off if the dimmer is 0 and off it is not
            div.querySelector('input[type=checkbox]').checked = event.target.value < 1 ? false : true;

            let dimval = event.target.value < 1 ? 0 : 100;
            // The message object
            Object.assign(emitter, {
                [controlId]: controlValue,
            });

            // custom message and values are now being emitted
            socket.emit('rangeChanged', JSON.stringify(emitter));
        });
    }
    // getting all the checkboxes whitin the div
    div.querySelector('input[type=checkbox]').addEventListener('click', (event) => {
        // getting the ID of the control by it's classname
        let controlId = event.target.className.split(' ')[0];
        // setting dimval if it is check or not
        let dimval = event.target.checked ? 1 : 0;

        // if the div has range slider change it values accordingly
        if (div.querySelector('input[type=range]') !== null) {
            div.querySelector('input[type=range]').value = event.target.checked ? 100 : 0;

            div.querySelector('span').innerHTML = dimval * 100;
        }

        Object.assign(emitter, {
            [controlId]: dimval,
        });

        // custom message and values are now being emitted
        socket.emit('rangeChanged', JSON.stringify(emitter));
    });
});

// sepratly for the main power
let LEDMain = document.getElementById('LEDGrowMainID');
let LEDMainPwr = document.getElementById('LEDGrowPowerID');
LEDMain.addEventListener('change', (toggle) => {
    ischecked = toggle.target.checked;
    if (ischecked) {
        LEDMainPwr.checked = true;
        Object.assign(emitter, {
            LEDGrowMainPwr: 1,
        });
        socket.emit('rangeChanged', JSON.stringify(emitter));
    }
});

//////////////////////////////////////////////////////// Irrigation Controls \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

let controlItemInnerIRG = document.querySelectorAll('.controlsItemInner.IRGCtrl');
Irrigation = {};
Array.prototype.forEach.call(controlItemInnerIRG, (div) => {
    let IRGToggle = div.querySelectorAll('input[type=checkbox]');

    Array.prototype.forEach.call(IRGToggle, (toggle) => {
        toggle.addEventListener('change', (toggleChanged) => {
            let controlId = toggleChanged.target.className.split(' ')[0];
            let pumpVal = toggleChanged.target.checked ? 1 : 0;

            Object.assign(Irrigation, {
                [controlId]: pumpVal,
            });
            socket.emit('IRGChanged', JSON.stringify(Irrigation));
        });
    });
});

//////////////////////////////////////////////////////// Irrigation Control Water Cycles\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

let controlItemInnerIRGCycle = document.querySelectorAll('.controlsItemInner.IRGCycles');
IRGCycles = { IRGWtrCycleTime: 3 };
Array.prototype.forEach.call(controlItemInnerIRGCycle, (div) => {
    div.querySelector('input[type=range].IRGWtrCycleTime').addEventListener('click', (event) => {
        // Showing the Dim Value

        div.querySelector('span').innerHTML = 'Time interval: ' + event.target.value + ' sec';
        // getting the ID of the control by it's classname
        let controlId = event.target.className;
        // remapping the value to be between 0 - 1
        let controlValue = event.target.value;

        // The message object
        Object.assign(IRGCycles, {
            [controlId]: controlValue,
        });

        // custom message and values are now being emitted
        // socket.emit('IRGCycleChanged', JSON.stringify(IRGCycles));
    });

    let IRGToggle = div.querySelectorAll('button[type="button"].IRGWtrCycle');

    Array.prototype.forEach.call(IRGToggle, (toggle) => {
        toggle.addEventListener('click', (toggleChanged) => {
            let controlId = toggleChanged.target.className.split(' ')[0];
            let pumpVal = toggleChanged.target.checked ? 1 : 0;

            Object.assign(IRGCycles, {
                [controlId]: pumpVal,
            });
            socket.emit('IRGCycleChanged', JSON.stringify(IRGCycles));
            console.log(IRGCycles);
        });
    });
});

//////////////////////////////////////////////////////// Irrigation Control Nutr Cycles\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
let controlItemInnerIRGCycleNutr = document.querySelectorAll('.controlsItemInner.IRGCyclesNutr');
console.log(controlItemInnerIRGCycleNutr);
IRGCyclesNutr = { IRGNutrCycleTime: 3 };
Array.prototype.forEach.call(controlItemInnerIRGCycleNutr, (div) => {
    div.querySelector('input[type=range].IRGNutrCycleTime').addEventListener('click', (event) => {
        // Showing the Dim Value

        div.querySelector('span').innerHTML = 'Time interval: ' + event.target.value + ' sec';
        // getting the ID of the control by it's classname
        let controlId = event.target.className;
        // remapping the value to be between 0 - 1
        let controlValue = event.target.value;

        // The message object
        Object.assign(IRGCyclesNutr, {
            [controlId]: controlValue,
        });

        // custom message and values are now being emitted
        // socket.emit('IRGCycleChanged', JSON.stringify(IRGCycles));
    });

    let IRGToggle = div.querySelectorAll('button[type="button"].IRGNutrCycle');

    Array.prototype.forEach.call(IRGToggle, (toggle) => {
        toggle.addEventListener('click', (toggleChanged) => {
            let controlId = toggleChanged.target.className.split(' ')[0];
            let pumpVal = toggleChanged.target.checked ? 1 : 0;

            Object.assign(IRGCyclesNutr, {
                [controlId]: pumpVal,
            });
            socket.emit('IRGCycleChangedNutr', JSON.stringify(IRGCyclesNutr));
            console.log(IRGCyclesNutr);
        });
    });
});

//////////////////////////////////////////////////////// ARM CONTROLS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

let controlItemInnerARM = document.querySelectorAll('.controlsItemInner.swingCtrl');

ArmCtrl = {};
ArmCtrlLoc = {};
Array.prototype.forEach.call(controlItemInnerARM, (div) => {
    div.querySelector('input[type=range]').addEventListener('click', (event) => {
        // Showing the Dim Value
        div.querySelector('span').innerHTML = 'Position: ' + event.target.value;
        // getting the ID of the control by it's classname
        let controlId = event.target.className;
        // remapping the value to be between 0 - 1
        let controlValue = event.target.value;

        // The message object
        Object.assign(ArmCtrlLoc, {
            [controlId]: controlValue,
        });
        console.log(ArmCtrlLoc);
        // custom message and values are now being emitted
        socket.emit('ArmLocChanged', JSON.stringify(ArmCtrlLoc));
    });

    // ---------------------------------------------------------
    let ARMToggle = div.querySelectorAll('button[type="button"][name="calibrate"]');
    Array.prototype.forEach.call(ARMToggle, (toggle) => {
        toggle.addEventListener('click', (toggleChanged) => {
            let controlId = toggleChanged.target.className.split(' ')[0];
            let armVal = toggleChanged.target.checked ? 1 : 0;
            Object.assign(ArmCtrl, {
                [controlId]: armVal,
            });
            console.log(ArmCtrl);
            socket.emit('ArmCalibrate', JSON.stringify(ArmCtrl));
        });
    });
    // ---------------------------------------------------------

    let ARMBtn = div.querySelectorAll(' button[type="button"][name="pulsate"]');
    console.log(ARMBtn);
    Array.prototype.forEach.call(ARMBtn, (btn) => {
        console.log(btn);
        btn.addEventListener('mousedown', (btnChanged) => {
            let controlId = btnChanged.target.className.split(' ')[0];
            Object.assign(ArmCtrl, {
                [controlId]: true,
            });
            socket.emit('ArmChanged', JSON.stringify(ArmCtrl));
        });
        // ---------------------------------------------------------

        btn.addEventListener('mouseup', (btnChanged) => {
            let controlId = btnChanged.target.className.split(' ')[0];
            Object.assign(ArmCtrl, {
                [controlId]: false,
            });
            socket.emit('ArmChanged', JSON.stringify(ArmCtrl));
        });
    });
});


//////////////////////////////////////////////////////// AIR CONTROLS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

let controlItemInnerAIR = document.querySelectorAll('.controlsItemInner.AirCtrl');
Air = {};
Array.prototype.forEach.call(controlItemInnerAIR, (div) => {
    let AIRToggle = div.querySelectorAll('input[type=checkbox]');

    Array.prototype.forEach.call(AIRToggle, (toggle) => {
        toggle.addEventListener('change', (toggleChanged) => {
            let controlId = toggleChanged.target.className.split(' ')[0];

            let AirVal = toggleChanged.target.checked ? 1 : 0;

            Object.assign(Air, {
                [controlId]: AirVal,
            });
            socket.emit('AirChanged', JSON.stringify(Air));
        });
    });
});