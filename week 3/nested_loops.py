# === Task 13 ===

# rows = int(input("How many rows should I have?"))
# columns = int(input("How many columns should I have?"))

# print("Here I go:")

# emoji = ":-)"

# for i in range(rows):
#     print(emoji * columns)

# print("\nDone!")

# === Task 14 ===

sequence = input("Please enter a sequence\n")

marker = input("Please enter the character for the marker\n")

# Find markers
is_counting = False
count = 0
for character in sequence:
   if (is_counting == False) and (character == marker):
    print("Found first marker")
    is_counting = True
   elif (is_counting == True) and (character == marker):
    print("Found last marker")
   elif is_counting:
    count += 1
# Display result
print(f"The distance between the markers is {count}")