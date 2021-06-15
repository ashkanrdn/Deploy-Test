var socket = io.connect('/');


let LED_Values = {};
let IRG_Values = {};
let ARM_Values = {};
let AIR_Values = {};
let Schedule_Values = {};




// querying controllers
let LEDcontrols = document.querySelectorAll('.controlsItemInner.LEDCtrl');
let LEDMain = document.getElementById('LEDGrowMainID');
let LEDMainPwr = document.getElementById('LEDGrowPowerID');

let ARMControls = document.querySelectorAll('.controlsItemInner.ARMCtrl');

let IRGControls = document.querySelectorAll('.controlsItemInner.IRGCtrl');
let IRGCycleWtrControls = document.querySelectorAll('.controlsItemInner.IRGCyclesWtr');
let IRGCycleNutrControls = document.querySelectorAll('.controlsItemInner.IRGCyclesNutr');

let AIRControls = document.querySelectorAll('.controlsItemInner.AirCtrl');

let ScheduleControls = document.querySelectorAll('.controlsItemInner.ScheduleCtrl');





//////////////////////////////////////////////////////// Light Controls \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
// getting the divs with controlsItemInner ID this is a div that has controls for each control module

Array.prototype.forEach.call(LEDcontrols, (div) => {
    //LED sliders
    if (div.querySelector('input[type=range]') !== null) {
        div.querySelector('input[type=range]').addEventListener('click', (event) => {
            // Display Dim Value
            div.querySelector('span').innerHTML = 'Dim: ' + event.target.value + ' %';
            // we make the check box off if the dimmer is 0 and off it is not
            div.querySelector('input[type=checkbox]').checked = event.target.value < 1 ? false : true;
            // getting the ID of the control by it's classname
            let controlId = event.target.className;
            // remapping the value to be between 0 - 1
            let controlValue = event.target.value * 0.01;
            let dimval = event.target.value < 1 ? 0 : 100;
            // The message object
            Object.assign(LED_Values, {
                [controlId]: controlValue,
            });
            // Emitting the dashValues to socket server
            socket.emit('LEDchanged', JSON.stringify(LED_Values));
        });
    }
    // LED on/off
    div.querySelector('input[type=checkbox]').addEventListener('click', (event) => {
        let controlId = event.target.className.split(' ')[0];
        let controlValue = event.target.checked ? 1 : 0;
        // if the div has range slider display the dynamic dimming value t
        if (div.querySelector('input[type=range]') !== null) {
            div.querySelector('input[type=range]').value = event.target.checked ? 100 : 0;
            div.querySelector('span').innerHTML = controlValue * 100;
        }
        Object.assign(LED_Values, {
            [controlId]: controlValue,
        });
        // custom message and values are now being emitted
        socket.emit('LEDchanged', JSON.stringify(LED_Values));
    });
});


LEDMain.addEventListener('change', (toggle) => {
    ischecked = toggle.target.checked;
    if (ischecked) {
        LEDMainPwr.checked = true;
        Object.assign(LED_Values, {
            LEDGrowMainPwr: 1,
        });
        socket.emit('rangeChanged', JSON.stringify(LED_Values));
    }
});

//////////////////////////////////////////////////////// Irrigation Controls \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Array.prototype.forEach.call(IRGControls, (div) => {
    let IRGToggle = div.querySelectorAll('input[type=checkbox]');
    Array.prototype.forEach.call(IRGToggle, (toggle) => {
        toggle.addEventListener('change', (toggleChanged) => {
            let controlId = toggleChanged.target.className.split(' ')[0];
            let controlValue = toggleChanged.target.checked ? 1 : 0;
            Object.assign(IRG_Values, {
                [controlId]: controlValue,
            });
            socket.emit('IRGChanged', JSON.stringify(IRG_Values));
        });
    });
});
//////////////////////////////////////////////////////// Irrigation Control Water Cycles\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Array.prototype.forEach.call(IRGCycleWtrControls, (div) => {
    div.querySelector('input[type=range].IRGWtrCycleTime').addEventListener('click', (event) => {
        // Showing the Dim Value
        div.querySelector('span').innerHTML = 'Time interval: ' + event.target.value + ' sec';
        // getting the ID of the control by it's classname
        let controlId = event.target.className;
        // remapping the value to be between 0 - 1
        let controlValue = event.target.value;
        // The message object
        Object.assign(IRG_Values, {
            [controlId]: controlValue,
        });
    });
    let IRGToggle = div.querySelectorAll('button[type="button"].IRGWtrCycle');
    Array.prototype.forEach.call(IRGToggle, (toggle) => {
        toggle.addEventListener('click', (toggleChanged) => {
            let controlId = toggleChanged.target.className.split(' ')[0];
            let controlValue = toggleChanged.target.checked ? 1 : 0;
            Object.assign(IRG_Values, {
                [controlId]: controlValue,
            });
            socket.emit('IRGCycleWtr', JSON.stringify(IRG_Values));
        });
    });
});

//////////////////////////////////////////////////////// Irrigation Control Nutr Cycles\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Array.prototype.forEach.call(IRGCycleNutrControls, (div) => {
    div.querySelector('input[type=range].IRGNutrCycleTime').addEventListener('click', (event) => {
        // Showing the Dim Value
        div.querySelector('span').innerHTML = 'Time interval: ' + event.target.value + ' sec';
        // getting the ID of the control by it's classname
        let controlId = event.target.className;
        // remapping the value to be between 0 - 1
        let controlValue = event.target.value;
        // The message object
        Object.assign(IRG_Values, {
            [controlId]: controlValue,
        });

    });

    let IRGToggle = div.querySelectorAll('button[type="button"].IRGNutrCycle');
    Array.prototype.forEach.call(IRGToggle, (toggle) => {
        toggle.addEventListener('click', (toggleChanged) => {
            let controlId = toggleChanged.target.className.split(' ')[0];
            let controlValue = toggleChanged.target.checked ? 1 : 0;
            Object.assign(IRG_Values, {
                [controlId]: controlValue,
            });
            socket.emit('IRGCycleNutr', JSON.stringify({ IRGWtrCycle: 0, IRGNutrCycle: 0 }));
        });
    });
});

//////////////////////////////////////////////////////// ARM CONTROLS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



Array.prototype.forEach.call(ARMControls, (div) => {
    div.querySelector('input[type=range]').addEventListener('click', (event) => {
        // Showing the Dim Value
        div.querySelector('span').innerHTML = 'Position: ' + event.target.value;
        // getting the ID of the control by it's classname
        let controlId = event.target.className;
        // remapping the value to be between 0 - 1
        let controlValue = event.target.value;
        // The message object
        Object.assign(ARM_Values, {
            [controlId]: controlValue,
        });
        // custom message and values are now being emitted
        socket.emit('ARMLoc', JSON.stringify(ARM_Values));
    });

    // ----------------------- Calibrate -----------------------
    let ARM_Calibrate_Toggle = div.querySelectorAll('button[type="button"][name="calibrate"]');
    Array.prototype.forEach.call(ARM_Calibrate_Toggle, (toggle) => {
        toggle.addEventListener('click', (toggleChanged) => {
            let controlId = toggleChanged.target.className.split(' ')[0];
            let controlValue = toggleChanged.target.checked ? 1 : 0;
            Object.assign(ARM_Values, {
                [controlId]: controlValue,
            });
            socket.emit('ARMCalibrate', JSON.stringify(ARM_Values));
        });
    });
    // ----------------------- Pulsate Left / Right -----------------------
    let ARM_Pulsate_Button = div.querySelectorAll(' button[type="button"][name="pulsate"]');
    Array.prototype.forEach.call(ARM_Pulsate_Button, (btn) => {
        btn.addEventListener('mousedown', (btnChanged) => {
            let controlId = btnChanged.target.className.split(' ')[0];
            Object.assign(ARM_Values, {
                [controlId]: true,
            });
            socket.emit('ARMChanged', JSON.stringify(ARM_Values));
        });
        btn.addEventListener('mouseup', (btnChanged) => {
            let controlId = btnChanged.target.className.split(' ')[0];
            Object.assign(ARM_Values, {
                [controlId]: false,
            });
            socket.emit('ARMChanged', JSON.stringify(ARM_Values));
        });
    });
});


//////////////////////////////////////////////////////// AIR CONTROLS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


Array.prototype.forEach.call(AIRControls, (div) => {
    let AIRToggle = div.querySelectorAll('input[type=checkbox]');
    Array.prototype.forEach.call(AIRToggle, (toggle) => {
        toggle.addEventListener('change', (toggleChanged) => {
            let controlId = toggleChanged.target.className.split(' ')[0];
            let controlValue = toggleChanged.target.checked ? 1 : 0;
            Object.assign(AIR_Values, {
                [controlId]: controlValue,
            });
            socket.emit('AIRChanged', JSON.stringify(AIR_Values));
        });
    });
});


//////////////////////////////////////////////////////// SCHEDULE CONTROLS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
function IRGWtrSeq() {

    setTimeout(() => {
        socket.emit('IRGCycleWtr', JSON.stringify({ IRGWtrCycle: 5 }));


        console.log(new Date().toLocaleString(), 'wtr')


    }, 10000);


}

function IRGNutrSeq() {
    setTimeout(() => {
        console.log(new Date().toLocaleString(), 'nutr')
        socket.emit('IRGCycleNutr', JSON.stringify({ IRGNutrCycle: 5 }));
    }, 5000);
}

function mySeq() {
    IRGNutrSeq();
    console.log(new Date().toLocaleString())
    IRGWtrSeq();
}

let IRGInterval = setInterval(mySeq, 30000)



function myStopFunction() {
    clearInterval(IRGInterval);
}


Array.prototype.forEach.call(ScheduleControls, (div) => {



    let ScheduleButton = div.querySelectorAll('button[type="button"][name="scheduler"]');
    Array.prototype.forEach.call(ScheduleButton, (btn) => {
        btn.addEventListener('click', (toggleChanged) => {
            console.log('Hi')
            IRGInterval


        });
    });


    let cancelScheduleButton = div.querySelectorAll('button[type="button"][name="cancelScheduler"]');
    Array.prototype.forEach.call(cancelScheduleButton, (btn) => {
        btn.addEventListener('click', (toggleChanged) => {
            myStopFunction()
            console.log('Bye')


        });
    });
});