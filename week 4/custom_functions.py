# === Task 3 ===

def listen():
    sound = input("Please enter a sound: ")
    print(f"That was a loud {sound}!")

listen()

def identify():
    vision = input("What lies before us?")

    if vision == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine")

identify()