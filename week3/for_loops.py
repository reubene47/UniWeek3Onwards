# === Task 7 ===

# mountains = int(input("How many mountains should I display?"))

# for i in range(1, mountains):
#     print("Displaying...")

# for mountain in range(mountains):
#  print("""
#  __
#  / \\_
#  /^ \\
#  / ^ \\_
#  _/ ^ ^ ^\\
#  / ^ ^ \\
#  """)

# print("Done!")

# === Task 8 ===

distance = int(input("How far are we from the target?\n"))

for i in range(distance):
    print(f"{distance} steps remaining")
    distance -= 1

print("Target achieved!")