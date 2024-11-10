answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.strip()
if answer.lower().replace("-", " ") == "forty two":
    print("Yes")
elif answer == "42":
    print("Yes")
else:
    print("No")