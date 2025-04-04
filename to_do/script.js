document.getElementById('addTaskBtn').addEventListener('click', addTask);

function addTask() {
    let taskInput = document.getElementById('taskInput');
    let taskList = document.getElementById('taskList');

    if (taskInput.value.trim() === '') {
        alert("Please enter a task!");
        return;
    }

    let li = document.createElement('li');
    li.innerHTML = `${taskInput.value} <button onclick="removeTask(this)">Remove</button>`;
    taskList.appendChild(li);

    taskInput.value = '';
}

function removeTask(taskElement) {
    taskElement.parentElement.remove();
}
