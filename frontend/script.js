async function addTask() {
    let input = document.getElementById("taskInput");
    let task = input.value;

    if (task === "") {
        return;
    }

    await fetch("http://18.61.130.115:5000/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            task: task
        })
    });

    input.value = "";

    location.reload();
}

async function loadTasks() {
    let response = await fetch("http://18.61.130.115:5000/tasks");
    let tasks = await response.json();

    let list = document.getElementById("taskList");

    tasks.forEach(function(task) {
        let item = document.createElement("li");
        item.textContent = task.task;
        list.appendChild(item);
    });
}

loadTasks();
#jenkins wehook test
