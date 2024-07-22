name = input("Enter your name: ")
while name == "":
    print("You did not inter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")