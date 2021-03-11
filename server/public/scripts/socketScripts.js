var socket = io.connect('/');

// Show the dim value in the Dash

// making the emitter object
let emitter = {};

// getting the divs with controlsItemInner this is a div that has controls for each control module
let controlItemInner = document.querySelectorAll('.controlsItemInner');

Array.prototype.forEach.call(controlItemInner, (div) => {
    //looping through divs and getting the sliders
    div.querySelector('input[type=range]').addEventListener('click', (event) => {
        // Showing the Dim Value
        div.querySelector('span').innerHTML = event.target.value;

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

    let doubleToggle = div.querySelectorAll('input[type=checkbox]');
    Array.prototype.forEach.call(doubleToggle, (toggle) => {
        toggle.addEventListener('click', (event) => {
            // getting the ID of the control by it's classname
            let controlId = event.target.className.split(' ')[0];
            console.log(controlId);
            let dimval = event.target.checked ? 1 : 0;
            div.querySelector('input[type=range]').value = event.target.checked ? 100 : 0;

            div.querySelector('span').innerHTML = dimval * 100;
            Object.assign(emitter, {
                [controlId]: dimval,
            });

            // custom message and values are now being emitted
            socket.emit('rangeChanged', JSON.stringify(emitter));
        });
    });
});