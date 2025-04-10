import Lab7.string_package.math_utils as math_utils 
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))
op = input("Enter operation (add, subtract, multiply, divide, power, mod): ")

operations ={
    'add': math_utils.add(x,y),
    'subtract': math_utils.subtract(x,y),
    'multiply': math_utils.multiply(x,y),
    'divide': math_utils.divide(x,y),
    'power': math_utils.power(x,y),
    'mod': math_utils.mod(x,y)
}

if op in operations:
    result = operations[op]
    print(f"The result of {op}({x}, {y}) is: {result}")
else:
    print("Invalid operation. Please choose from add, subtract, multiply, divide, power, or mod.")