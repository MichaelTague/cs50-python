problem = input("Expression: ")
parts = problem.split(" ")
x = float(parts[0])
op = parts[1]
y = float(parts[2])
match op:
    case "+":
        z = x + y
    case "-":
        z = x - y
    case "*":
        z = x * y
    case "/":
        z = x / y
print(f"{z:.1f}")