var socket = io.connect('/');

// Show the dim value in the Dash

//////////////////////////////////////////////////////// Irrigation Control Nutr Cycles\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
let controlItemInnerIRGCycleNutr = document.querySelectorAll('.controlsItemInner.waterSchedule');

IRGCyclesNutr = { IRGNutrCycleTime: 3 };
Array.prototype.forEach.call(controlItemInnerIRGCycleNutr, (div) => {
  div.querySelector('input[type=range].IRGWtrCycleTime').addEventListener('click', (event) => {
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
    socket.emit('Test', 'Testaa');
  });

  
});

