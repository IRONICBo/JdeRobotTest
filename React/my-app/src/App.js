import React, { useState } from "react";

function TaskForm({ addTask }) {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  function handleSubmit(event) {
    event.preventDefault();
    if (!name) return;
    addTask({ name, description });
    setName("");
    setDescription("");
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input
          type="text"
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
      </label>
      <label>
        Description:
        <textarea
          value={description}
          onChange={(event) => setDescription(event.target.value)}
        />
      </label>
      <button type="submit">Add Task</button>
    </form>
  );
}

function TaskList({ tasks, editTask, deleteTask, completeTask }) {
  return (
    <ul>
      {tasks.map((task) => (
        <li key={task.id}>
          <div>
            <h3>{task.name}</h3>
            <p>{task.description}</p>
          </div>
          <div>
            <button onClick={() => editTask(task)}>Edit</button>
            <button onClick={() => deleteTask(task)}>Delete</button>
            <button onClick={() => completeTask(task)}>Complete</button>
          </div>
        </li>
      ))}
    </ul>
  );
}

function App() {
  const [tasks, setTasks] = useState([]);
  const [editingTask, setEditingTask] = useState(null);

  function addTask(task) {
    setTasks([...tasks, { id: Date.now(), ...task }]);
  }

  function editTask(task) {
    setEditingTask(task);
  }

  function saveTask(task) {
    const updatedTasks = tasks.map((t) =>
      t.id === task.id ? { ...t, ...task } : t
    );
    setTasks(updatedTasks);
    setEditingTask(null);
  }

  function deleteTask(task) {
    const filteredTasks = tasks.filter((t) => t.id !== task.id);
    setTasks(filteredTasks);
  }

  function completeTask(task) {
    const completedTasks = tasks.map((t) =>
      t.id === task.id ? { ...t, completed: true } : t
    );
    setTasks(completedTasks);
  }

  return (
    <div>
      <h1>Task List</h1>
      <TaskForm addTask={addTask} />
      <TaskList
        tasks={tasks}
        editTask={editTask}
        deleteTask={deleteTask}
        completeTask={completeTask}
      />
      {editingTask && (
        <TaskForm addTask={saveTask} initialValues={editingTask} />
      )}
    </div>
  );
}

export default App;
