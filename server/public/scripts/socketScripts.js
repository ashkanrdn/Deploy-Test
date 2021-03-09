var socket = io.connect('/');

// Show the dim value in the Dash

//selecting all the inputs
let inputs = document.querySelectorAll('input');

// making the emitter object
let emitter = {};

// getting the divs with controlsItemInner this is a div that has controls for each control module
let controlItemInner = document.querySelectorAll('.controlsItemInner');

Array.prototype.forEach.call(controlItemInner, (div) => {

    //looping through divs and getting the sliders
    div.querySelector('input[type=range]').addEventListener('click', (event) => {
        // Setting the dim value on dashboard
        div.querySelector('span').innerHTML = event.target.value;
        // if the slider is less than 1 turn toggle off
        if (event.target.value < 1) {
            div.querySelector('input[type=checkbox]').checked = false;
            // here we update the value on dashValues as well
            Object.assign(emitter, {
                [event.target.id + 'PWR']: false,
            });

        } else if (event.target.value > 1) {
            // if the slider is on make the toggle on
            div.querySelector('input[type=checkbox]').checked = true;




            Object.assign(emitter, {
                [event.target.id + 'PWR']: true,
            });
        }

        // if it is range
        let controlId = event.target.id;
        let controlValue = event.target.value * 0.01;
        // we assign number value
        console.log(controlId, controlValue)
        Object.assign(emitter, {
            [controlId]: controlValue,
        });

        stringEmit = JSON.stringify(emitter);

        // custom message and values are now being emitted
        socket.emit('rangeChanged', stringEmit);
    });

    div.querySelector('input[type=checkbox]').addEventListener('click', (event) => {
        if (event.target.checked === true) {
            div.querySelector('input[type=range]').value = 100;
            div.querySelector('span').innerHTML = div.querySelector('input[type=range]').value;

            // The ID of Slider
            let controlId = event.target.id;
            // Removing the last 3 chars (PWR) from end of the id
            let controlIdForRange = controlId.substring(0, controlId.length - 3)

            let controlValue = 1;

            Object.assign(emitter, {
                [controlIdForRange]: controlValue,
            });




        } else if (event.target.checked === false) {
            div.querySelector('span').innerHTML = 0;
            div.querySelector('input[type=range]').value = 0;
            // The ID of Slider
            let controlId = event.target.id;
            // Removing the last 3 chars (PWR) from end of the id
            let controlIdForRange = controlId.substring(0, controlId.length - 3)

            let controlValue = 0;

            Object.assign(emitter, {
                [controlIdForRange]: controlValue,
            });

        }
        // if it is checkbox we get checked value
        let controlId = event.target.id;
        let controlValue = event.target.checked;
        // then add the input ID and it value to emitter object
        Object.assign(emitter, {
            [controlId]: controlValue,
        });

        stringEmit = JSON.stringify(emitter);
        console.log(emitter)
            // custom message and values are now being emitted
        socket.emit('rangeChanged', stringEmit);
    });
});