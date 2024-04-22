import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import TodoItem from './TodoItem';

const mockTodo = { id: 1, text: 'Buy groceries', completed: false };

test('renders todo text', () => {
  const { getByText } = render(<TodoItem todo={mockTodo} />);
  expect(getByText('Buy groceries')).toBeInTheDocument();
});

test('toggles todo completion', () => {
  const toggleTodo = jest.fn();
  const { getByRole } = render(<TodoItem todo={mockTodo} toggleTodo={toggleTodo} />);
  const checkboxElement = getByRole('checkbox');
  fireEvent.click(checkboxElement);
  expect(toggleTodo).toHaveBeenCalledWith(1);
});

test('deletes todo', () => {
  const deleteTodo = jest.fn();
  const { getByRole } = render(<TodoItem todo={mockTodo} deleteTodo={deleteTodo} />);
  const deleteButton = getByRole('button', { name: 'Delete' });
  fireEvent.click(deleteButton);
  expect(deleteTodo).toHaveBeenCalledWith(1);
});
