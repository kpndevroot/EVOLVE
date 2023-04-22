let taskList = document.getElementById("taskList");
let taskInput = document.getElementById("task");

function addTask() {
  let task = taskInput.value;
  if (task !== "") {
    let li = document.createElement("li");
    li.innerText = task;
    li.onclick = function () {
      this.classList.toggle("completed");
    };
    taskList.appendChild(li);
    taskInput.value = "";
  }
}
