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

let inputs = document.querySelectorAll('input');

let emitter = {};

Array.prototype.forEach.call(inputs, (input) => {
    input.addEventListener('click', (event) => {
        if (event.target.attributes.type.value === 'checkbox') {
            let controlId = event.target.id;
            let controlValue = event.target.checked;
            Object.assign(emitter, {
                [controlId]: controlValue,
            });
        } else if (event.target.attributes.type.value === 'range') {
            let controlId = event.target.id;
            let controlValue = event.target.value;
            Object.assign(emitter, {
                [controlId]: controlValue,
            });
        }
        stringEmit = JSON.stringify(emitter);
        console.log(stringEmit, 'emit');
        socket.emit('rangeChanged', stringEmit);
    });
});