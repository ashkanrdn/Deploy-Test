var socket = io.connect('/');

// Show the dim value in the Dash

let sliders = document.querySelectorAll('.sliderDom'); //getting all the slider divs
Array.prototype.forEach.call(sliders, (slider) => {
    //looping through divs and getting the sliders
    slider.querySelector('input').addEventListener('click', (event) => {
        //   apply  value to the span
        slider.querySelector('span').innerHTML = event.target.value;
    });
});

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
            let controlValue = event.target.value;
            // we assign number value
            Object.assign(emitter, {
                [controlId]: controlValue,
            });
        }
        // whenever any changes happen we emit new message
        // before emitting the object we need stringy it
        stringEmit = JSON.stringify(emitter);
        console.log(stringEmit, 'emit');
        // custom message and values are now being emitted
        socket.emit('rangeChanged', stringEmit);
    });
});