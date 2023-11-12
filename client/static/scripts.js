$(document).ready(function() {
    // get the temperature status element
    var temperatureStatus = $("#temperature-status");

    // function to update the temperature status
    function updateTemperatureStatus() {
        $.ajax({
            url: "/temperature",
            type: "GET",
            success: function(data) {
                temperatureStatus.text(data.temperature + " °C");
            },
            error: function() {
                temperatureStatus.text("Error");
            }
        });
    }

    function updateLightSwitch() {
    $.ajax({
        url: "/ligth/status", // This URL will need to be provided by your backend
        type: "GET",
        success: function(response) {
            // Assume the response contains a JSON object with the light status in a boolean format
            var lightSwitch = $('#light-toggle');
            if (response.light_status === true) {
                lightSwitch.prop('checked', true);
            } else {
                lightSwitch.prop('checked', false);
            }
        },
        error: function() {
            console.error("Failed to fetch the light status.");
        }
    });}

// function to update the light level
function updateLightStatus(light_status) {
    $.ajax({
        
        type: 'POST',
        url: '/update_light_status',
        data: JSON.stringify({'status': light_status}),
        contentType: 'application/json',
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

// function to update the fan speed
function updateFanStatus(fan_status) {
    $.ajax({
        type: 'POST',
        url: '/update_fan_status',
        data: JSON.stringify({'status': fan_status}),
        contentType: 'application/json',
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

// function to handle changes to the light slider
// function to handle changes to the light toggle
$('#light-toggle').on('change', function() {
    var light_status = $(this).is(':checked');

    console.log("light status changed");
    updateLightStatus(light_status);
});

// function to handle changes to the fan slider
$('#fan-toggle').on('change', function() {
    var fan_status = $(this).is(':checked');
    console.log("fan status changed");

    updateFanStatus(fan_status);
});
});