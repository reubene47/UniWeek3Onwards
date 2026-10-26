print("Program started!\n")

while True:
    char = input("Please enter a standard character: ")

    if len(char) > 1:
        char = input("Please enter a standard character: ")
    else:
        break

char_ord = ord(char)
print(f"The ASCII code for {char} is {char_ord}")

print("Program ended!")