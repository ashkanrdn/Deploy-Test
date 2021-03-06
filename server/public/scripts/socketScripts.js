var socket = io.connect('/');

// };
// document.getElementById('myonoffswitch').addEventListener('change', function() {
//     socket.emit('stateChanged', this.checked);
//     console.log(this.checked);
// });
// document.getElementById('myRange').addEventListener('click', function() {
//     socket.emit('rangeChanged', this.value);
//     console.log(this.value);
// });

let sliders = document.querySelectorAll('.sliderDom');

Array.prototype.forEach.call(sliders, (slider) => {
    slider.querySelector('input').addEventListener('click', (event) => {
        // 1. apply our value to the span
        slider.querySelector('span').innerHTML = event.target.value;
    });
});

let inputs = document.querySelectorAll('input');

let emitter = {};

Array.prototype.forEach.call(inputs, (input) => {
    input.addEventListener('click', (event) => {
        if (event.target.value) {
            // socket.emit('rangeChanged',{event.value,} );

            let controlId = event.target.id;
            let controlValue = event.target.value;

            Object.assign(emitter, {
                [controlId]: controlValue,
            });

            console.log(emitter, 'emit');
        } else {
            let controlId = event.target.id;
            let controlValue = event.target.checked;

            Object.assign(emitter, {
                [controlId]: controlValue,
            });
        }

        stringEmit = JSON.stringify(emitter);
        console.log(stringEmit, 'emit');
        socket.emit('rangeChanged', stringEmit);
    });
});