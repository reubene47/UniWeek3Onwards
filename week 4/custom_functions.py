# === Task 3 ===

# def listen():
#     sound = input("Please enter a sound: ")
#     print(f"That was a loud {sound}!")

# listen()

# === Task 4 ===

# def identify():
#     vision = input("What lies before us?")

#     if vision == "a large boulder":
#         print("It's time to run!")
#     else:
#         print("We will be fine")

# identify()

# === Task 5 ===

# def escape_by(plan):
#     if plan == "jumping over":
#         print("We cannot escape that way! The boulder is too big!")
#     elif plan == "running around":
#         print("We cannot escape that way! The boulder is moving too fast!")
#     elif plan == "cross bridge ahead":
#         print("That might just work! Let's go!")
#     else:
#         print("We cannot escape that way! The boulder is in the way!")

# escape_by("jumping over")
# escape_by("running around")
# escape_by("cross bridge ahead")

# === Task 6 ===

# def cross_bridge(steps):
#     if steps >= 0 and steps <= 5:
#         for step in range(steps):
#             print("Crossed step")
#         print("We must keep going!")
#     elif steps > 5:
#         for step in range(steps):
#             print("Crossed step")
#         print("The bridge is collapsing!")
#     else:
#         print("We must keep going!")

# cross_bridge(3)
# cross_bridge(6)

# === Task 7 ===

# def climb_ladder(steps_remaining, steps_crossed):
#     if steps_remaining > steps_crossed:
#         print("Still some way to go!")
#     else:
#         print("We are almost there!")

# climb_ladder(5, 2)
# climb_ladder(2, 5)

# === Task 8 ===

# def display_ladder(steps):
#     for step in range(steps):
#         print("| |\n***")

# def create_ladder():
#     steps = int(input("How many steps remain?"))

#     display_ladder(steps)

# create_ladder()

# === Task 9 ===

def sum_weights(character_weight, inventory_weight):
    total_weight = character_weight + inventory_weight
    return total_weight

def calc_avg_weight(character_weight, inventory_weight):
    avg_weight = sum_weights(character_weight, inventory_weight) / 2
    return avg_weight

def run():
    character_weight = int(input("What is the weight of the character?"))
    inventory_weight = int(input("What is the weight of their inventory?"))

    calculate = input("What would you like to calculate? (sum or average)")

    if calculate == "sum":
        print(sum_weights(character_weight, inventory_weight))
    elif calculate == "average":
        print(calc_avg_weight(character_weight, inventory_weight))
    else:
        print("Can't do that")

run()