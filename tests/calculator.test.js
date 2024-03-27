const Calculator = require('../scripts/hello.js');

describe('Calculator', () => {
  let calculator;

  beforeEach(() => {
    calculator = new Calculator();
  });

  test('adds two positive numbers', () => {
    expect(calculator.add(2, 3)).toBe(5);
  });

  test('adds a positive and a negative number', () => {
    expect(calculator.add(5, -3)).toBe(2);
  });

  test('multiplies two positive numbers', () => {
    expect(calculator.multiply(5, 3)).toBe(15);
  });

  test('multiplies a positive and a negative number', () => {
    expect(calculator.multiply(5, -3)).toBe(-15);
  });
});
