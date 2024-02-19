response = input("Greeting: ").strip().lower()
if response.startswith("hello"):
    print("$0")
elif response.startswith("h"):
    print("$20")
else:
    print("$100")
