camel_case = input("camelCase: ")
print("snake_case: ", end="")
for c in camel_case:
    if c.isupper():
        print("_", end="")
        print(c.lower(), end="")
    else:
        print(c, end="")
print()
