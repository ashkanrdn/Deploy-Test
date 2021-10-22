var socket = io.connect("/");

// Creating an interface for scheduling, adding the scheduled task to a quee, making the socket commuincate with pi app
// fuguring out how to make an api route to pull all the database so shop can tap into
// setup logging for python
// setup paper trail for logging stuff

// let testToggle = document.getElementById("LEDGrowPower");
// console.log(testToggle);
// console.log("hi");
// testToggle.addEventListener("change", (toggleChanged) => {
//     console.log("Hi");
// let controlId = toggleChanged.target.className.split(" ")[0];
// let controlValue = toggleChanged.target.checked ? 1 : 0;
// Object.assign(All_Control_Values.AIR_Values, {
//     [controlId]: controlValue,
// });
// socket.emit("AIRChanged", JSON.stringify(All_Control_Values));
// });

// socket.emit("scheduleWTR", "Hello");

//Select DOM
const scheduleInput = document.querySelector(".schedule-input");
const scheduleButton = document.querySelector(".schedule-button");
const scheduleList = document.querySelector(".schedule-list");
const filterOption = document.querySelector(".filter-schedule");

//Event Listeners
document.addEventListener("DOMContentLoaded", getschedules);
scheduleButton.addEventListener("click", addSchedule);
scheduleList.addEventListener("click", deleteschedule);
filterOption.addEventListener("click", filterschedule);

//Functions

function addSchedule(e) {
    //Prevent natural behaviour
    e.preventDefault();
    //Create schedule div
    const scheduleDiv = document.createElement("div");
    scheduleDiv.classList.add("schedule");
    //Create list
    const newSchedule = document.createElement("li");
    newschedule.innerText = scheduleInput.value;
    //Save to local - do this last
    //Save to local
    saveLocalschedules(scheduleInput.value);
    //
    newschedule.classList.add("schedule-item");
    scheduleDiv.appendChild(newschedule);
    scheduleInput.value = "";
    //Create Completed Button
    const completedButton = document.createElement("button");
    completedButton.innerHTML = `<i class="fas fa-check"></i>`;
    completedButton.classList.add("complete-btn");
    scheduleDiv.appendChild(completedButton);
    //Create trash button
    const trashButton = document.createElement("button");
    trashButton.innerHTML = `<i class="fas fa-trash"></i>`;
    trashButton.classList.add("remove-schedule");
    scheduleDiv.appendChild(trashButton);
    //attach final schedule
    scheduleList.appendChild(scheduleDiv);
}
v;

function deleteschedule(e) {
    const item = e.target;

    if (item.classList[0] === "remove-schedule") {
        // e.target.parentElement.remove();
        const schedule = item.parentElement;
        schedule.classList.add("fall");
        //at the end
        removeLocalschedules(schedule);
        schedule.addEventListener("transitionend", (e) => {
            schedule.remove();
        });
    }
    if (item.classList[0] === "complete-btn") {
        const schedule = item.parentElement;
        schedule.classList.toggle("completed");
        console.log(schedule);
    }
}

function filterschedule(e) {
    const schedules = scheduleList.childNodes;
    schedules.forEach(function(schedule) {
        switch (e.target.value) {
            case "all":
                schedule.style.display = "flex";
                break;
            case "completed":
                if (schedule.classList.contains("completed")) {
                    schedule.style.display = "flex";
                } else {
                    schedule.style.display = "none";
                }
                break;
            case "uncompleted":
                if (!schedule.classList.contains("completed")) {
                    schedule.style.display = "flex";
                } else {
                    schedule.style.display = "none";
                }
        }
    });
}

function saveLocalschedules(schedule) {
    let schedules;
    if (localStorage.getItem("schedules") === null) {
        schedules = [];
    } else {
        schedules = JSON.parse(localStorage.getItem("schedules"));
    }
    schedules.push(schedule);
    localStorage.setItem("schedules", JSON.stringify(schedules));
}

function removeLocalschedules(schedule) {
    let schedules;
    if (localStorage.getItem("schedules") === null) {
        schedules = [];
    } else {
        schedules = JSON.parse(localStorage.getItem("schedules"));
    }
    const scheduleIndex = schedule.children[0].innerText;
    schedules.splice(schedules.indexOf(scheduleIndex), 1);
    localStorage.setItem("schedules", JSON.stringify(schedules));
}

function getschedules() {
    let schedules;
    if (localStorage.getItem("schedules") === null) {
        schedules = [];
    } else {
        schedules = JSON.parse(localStorage.getItem("schedules"));
    }
    schedules.forEach(function(schedule) {
        //Create schedule div
        const scheduleDiv = document.createElement("div");
        scheduleDiv.classList.add("schedule");
        //Create list
        const newschedule = document.createElement("li");
        newschedule.innerText = schedule;
        newschedule.classList.add("schedule-item");
        scheduleDiv.appendChild(newschedule);
        scheduleInput.value = "";
        //Create Completed Button
        const completedButton = document.createElement("button");
        completedButton.innerHTML = `<i class="fas fa-check"></i>`;
        completedButton.classList.add("complete-btn");
        scheduleDiv.appendChild(completedButton);
        //Create trash button
        const trashButton = document.createElement("button");
        trashButton.innerHTML = `<i class="fas fa-trash"></i>`;
        trashButton.classList.add("remove-schedule");
        scheduleDiv.appendChild(trashButton);
        //attach final schedule
        scheduleList.appendChild(scheduleDiv);
    });
}

// _______________________________   DAY PICKER _______________________

var dayOption = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
var daySelected = [true, false, true, true, true, false, false];
var indexSelected = [];
var dayFormated = "";
var checked;

daySelected.map((value, i) => {
    if (value) {
        console.log(value);
        checked = "checked";
    } else {
        checked = "";
    }
    $(".day").append(
        '<label><input onclick="tickDay(' + i + ')" type="checkbox"' + this.checked + ">" + dayOption[i] + "</label>"
    );
});
formatSelectedDays();

function tickDay(i) {
    this.daySelected[i] = !this.daySelected[i];
    this.formatSelectedDays();
}

function formatSelectedDays() {
    var result = "";
    var indexSelected = [];

    this.daySelected.map((value, i) => {
        if (this.daySelected[i]) indexSelected.push(i);
    });

    var head = "";
    var count_range = 0;
    indexSelected.map((value, i) => {
        if (i == 0) {
            head = this.dayOption[indexSelected[i]];
        } else {
            if (indexSelected[i] == indexSelected[i - 1] + 1) {
                //check next
                count_range++;
            } else {
                if (count_range <= 1) {
                    if (count_range === 0) {
                        result += head + ", ";
                    } else {
                        result += head + " - " + this.dayOption[indexSelected[i - 1]] + ", ";
                    }
                } else {
                    result += head + " - " + this.dayOption[indexSelected[i - 1]] + ", ";
                }
                count_range = 0;
                head = this.dayOption[indexSelected[i]];
            }
        }
    });
    if (count_range < 1) {
        result += head;
    } else {
        result += head + " - " + this.dayOption[indexSelected[indexSelected.length - 1]];
    }
    if (result === "") {
        result = "Choose day";
    }
    this.dayFormated = result;
    $(".result").html("<h4>" + result + "</h4>");
}