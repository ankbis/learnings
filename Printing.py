print("hello world")

var1 = 10

print(var1)

var2 = var1 + 15

print(var2)

if(var2 > 20):
    print("I am inside if")

var3 = "Ankush " * var1

print(var3)

#This is a comment

print(type(var1))
print(type(var3))

print(5 / 2)
print(6 / 2)

print(5 // 2)
print(7 // 2)

print(min(1,2,3))
print(max(7,4,5))

print(abs(32))
print(abs(-32))

print(float(10))
print(int(50.05))
print(int('100') + 5)

print(round(-2.01))


def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
        among a, b and c.

        >>> least_difference(1, 5, -5)
        4
        """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)

help(least_difference)

print(1, 2, 3, sep=' < ')


def greet(who="Ankush"):
    print("Hello, ", who)

    greet()
    greet(who="Nam")
    greet("Bisht")
