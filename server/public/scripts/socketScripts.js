var socket = io.connect('/');

// Show the dim value in the Dash

//selecting all the inputs
let inputs = document.querySelectorAll('input');

// making the emitter object
let emitter = {};

//looping through inputs and separating the checkbox and range
Array.prototype.forEach.call(inputs, (input) => {
    // every time user clicks on any input =>
    input.addEventListener('click', (event) => {
        // we check for the input type=>
        if (event.target.attributes.type.value === 'checkbox') {
            // if it is checkbox we get checked value
            let controlId = event.target.id;
            let controlValue = event.target.checked;
            // then add the input ID and it value to emitter object
            Object.assign(emitter, {
                [controlId]: controlValue,
            });
        } else if (event.target.attributes.type.value === 'range') {
            // if it is range
            let controlId = event.target.id;
            let controlValue = event.target.value * 0.01;
            // we assign number value
            Object.assign(emitter, {
                [controlId]: controlValue,
            });
        }
        // whenever any changes happen we emit new message
        // before emitting the object we need stringy it
        stringEmit = JSON.stringify(emitter);

        // custom message and values are now being emitted
        socket.emit('rangeChanged', stringEmit);
    });
});


// Aesthetics for when toggle is clicked slider respond to it
// if dimmer is clicked toggle is checked
let controlItemInner = document.querySelectorAll('.controlsItemInner');

Array.prototype.forEach.call(controlItemInner, (div) => {
    //looping through divs and getting the sliders
    div.querySelector('input[type=range]').addEventListener('click', (event) => {
        div.querySelector('span').innerHTML = event.target.value;
        if (event.target.value < 1) {
            div.querySelector('input[type=checkbox]').checked = false;
        } else if (event.target.value > 1) {
            div.querySelector('input[type=checkbox]').checked = true;
        }
    });

    div.querySelector('input[type=checkbox]').addEventListener('click', (event) => {
        if (event.target.checked === true) {
            div.querySelector('input[type=range]').value = 100;
            div.querySelector('span').innerHTML = div.querySelector('input[type=range]').value;
        } else if (event.target.checked === false) {
            div.querySelector('span').innerHTML = 0;

            div.querySelector('input[type=range]').value = 0;
        }
    });
});