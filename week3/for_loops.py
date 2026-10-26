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

# distance = int(input("How far are we from the target?\n"))

# for i in range(distance):
#     print(f"{distance} steps remaining")
#     distance -= 1

# print("Target achieved!")

# === Task 9 ===

# brightness = int(input("What level of brightness is required?\n"))

# print("\nAdjusting brightness...\n")

# for i in range(brightness):
#     print(f"Brightness level: {"*" * brightness}")
#     brightness += 1

# === Task 10 ===

word = input("What word do you see?\n")

print("\nDisplaying index positions...")

for i in range(len(word)):
    print(f"Index {i}: {word[i]}")