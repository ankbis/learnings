import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import App from './App';

describe('App', () => {
  test('renders the todo list', () => {
    const { getByText } = render(<App />);
    const headerElement = getByText(/Todo List/i);
    expect(headerElement).toBeInTheDocument();
  });

  test('adds a new todo', () => {
    const { getByPlaceholderText, getByText } = render(<App />);
    const inputElement = getByPlaceholderText(/Add a new todo/i);
    fireEvent.change(inputElement, { target: { value: 'Buy groceries' } });
    fireEvent.submit(inputElement.form);
    const todoElement = getByText(/Buy groceries/i);
    expect(todoElement).toBeInTheDocument();
  });

  test('toggles todo completion', () => {
    const { getByText } = render(<App />);
    const todoElement = getByText(/Buy groceries/i);
    const checkboxElement = todoElement.previousSibling;
    fireEvent.click(checkboxElement);
    expect(todoElement).toHaveStyle('text-decoration: line-through');
  });
});
