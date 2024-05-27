const Calculator = require('./calculator');

describe('Calculator', () => {
  let calculator;

  beforeEach(() => {
    calculator = new Calculator();
  });

  test('adds two positive numbers', () => {
    expect(calculator.add(2, 3)).toBe(5);
  });

  test('adds two negative numbers', () => {
    expect(calculator.add(-2, -3)).toBe(-5);
  });

  test('multiplies two positive numbers', () => {
    expect(calculator.multiply(4, 5)).toBe(20);
  });

  test('multiplies two negative numbers', () => {
    expect(calculator.multiply(-4, -5)).toBe(20);
  });
});
