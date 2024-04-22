import React from 'react';

function TodoItem({ todo, toggleTodo, deleteTodo }) {
  const handleToggle = () => {
    toggleTodo(todo.id);
  };

  const handleDelete = () => {
    deleteTodo(todo.id);
  };

  return (
    <li>
      <input type="checkbox" checked={todo.completed} onChange={handleToggle} />
      <span style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}>{todo.text}</span>
      <button onClick={handleDelete}>Delete</button>
    </li>
  );
}

export default TodoItem;
