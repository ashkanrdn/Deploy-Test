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
const todoInput = document.querySelector(".todo-input");
const todoButton = document.querySelector(".todo-button");
const todoList = document.querySelector(".todo-list");
const filterOption = document.querySelector(".filter-todo");

//Event Listeners
document.addEventListener("DOMContentLoaded", getTodos);
todoButton.addEventListener("click", addSchedule);
todoList.addEventListener("click", deleteTodo);
filterOption.addEventListener("click", filterTodo);

//Functions

function addSchedule(e) {
    //Prevent natural behaviour
    e.preventDefault();
    //Create todo div
    const scheduleDiv = document.createElement("div");
    todoDiv.classList.add("schedule");
    //Create list
    const newSchedule = document.createElement("li");
    newTodo.innerText = todoInput.value;
    //Save to local - do this last
    //Save to local
    saveLocalTodos(todoInput.value);
    //
    newTodo.classList.add("todo-item");
    todoDiv.appendChild(newTodo);
    todoInput.value = "";
    //Create Completed Button
    const completedButton = document.createElement("button");
    completedButton.innerHTML = `<i class="fas fa-check"></i>`;
    completedButton.classList.add("complete-btn");
    todoDiv.appendChild(completedButton);
    //Create trash button
    const trashButton = document.createElement("button");
    trashButton.innerHTML = `<i class="fas fa-trash"></i>`;
    trashButton.classList.add("remove-schedule");
    todoDiv.appendChild(trashButton);
    //attach final Todo
    todoList.appendChild(todoDiv);
}
v;

function deleteTodo(e) {
    const item = e.target;

    if (item.classList[0] === "remove-schedule") {
        // e.target.parentElement.remove();
        const todo = item.parentElement;
        todo.classList.add("fall");
        //at the end
        removeLocalTodos(todo);
        todo.addEventListener("transitionend", (e) => {
            todo.remove();
        });
    }
    if (item.classList[0] === "complete-btn") {
        const todo = item.parentElement;
        todo.classList.toggle("completed");
        console.log(todo);
    }
}

function filterTodo(e) {
    const todos = todoList.childNodes;
    todos.forEach(function(todo) {
        switch (e.target.value) {
            case "all":
                todo.style.display = "flex";
                break;
            case "completed":
                if (todo.classList.contains("completed")) {
                    todo.style.display = "flex";
                } else {
                    todo.style.display = "none";
                }
                break;
            case "uncompleted":
                if (!todo.classList.contains("completed")) {
                    todo.style.display = "flex";
                } else {
                    todo.style.display = "none";
                }
        }
    });
}

function saveLocalTodos(todo) {
    let todos;
    if (localStorage.getItem("todos") === null) {
        todos = [];
    } else {
        todos = JSON.parse(localStorage.getItem("todos"));
    }
    todos.push(todo);
    localStorage.setItem("todos", JSON.stringify(todos));
}

function removeLocalTodos(todo) {
    let todos;
    if (localStorage.getItem("todos") === null) {
        todos = [];
    } else {
        todos = JSON.parse(localStorage.getItem("todos"));
    }
    const todoIndex = todo.children[0].innerText;
    todos.splice(todos.indexOf(todoIndex), 1);
    localStorage.setItem("todos", JSON.stringify(todos));
}

function getTodos() {
    let todos;
    if (localStorage.getItem("todos") === null) {
        todos = [];
    } else {
        todos = JSON.parse(localStorage.getItem("todos"));
    }
    todos.forEach(function(todo) {
        //Create todo div
        const todoDiv = document.createElement("div");
        todoDiv.classList.add("todo");
        //Create list
        const newTodo = document.createElement("li");
        newTodo.innerText = todo;
        newTodo.classList.add("todo-item");
        todoDiv.appendChild(newTodo);
        todoInput.value = "";
        //Create Completed Button
        const completedButton = document.createElement("button");
        completedButton.innerHTML = `<i class="fas fa-check"></i>`;
        completedButton.classList.add("complete-btn");
        todoDiv.appendChild(completedButton);
        //Create trash button
        const trashButton = document.createElement("button");
        trashButton.innerHTML = `<i class="fas fa-trash"></i>`;
        trashButton.classList.add("remove-schedule");
        todoDiv.appendChild(trashButton);
        //attach final Todo
        todoList.appendChild(todoDiv);
    });
}