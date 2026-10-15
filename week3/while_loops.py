import os
import subprocess

# === Task 1 ===

# apples_num = int(input("How many apples should I remove?"))

# while apples_num > 0:
#     print("Removed apple.")
#     apples_num -= 1

# === Task 2 ===

# subprocess.run(["cls"], shell=True)

# obstacles_input = int(input("How many obstacles should I avoid?\n"))

# obstacles = 0

# print("")

# while obstacles < obstacles_input:
#     obstacles += 1
#     print(f"Avoiding... Done! {obstacles} obstacles avoided.")
# print("\nAll obstacles have been avoided.")

# === Task 3 ===

# subprocess.run(["cls"], shell=True)

# bars = int(input("How many bars should be charged?\n"))

# bars_charged = 1

# print("")

# while bars_charged < bars:
#     print(f"Charging: {"█" * bars_charged}")
#     bars_charged += 1
# print("\nThe battery is fully charged.")

# === Task 4 ===

# subprocess.run(["cls"], shell=True)

# phrase = input("Please enter a phrase:\n")
# phrase_chars = len(phrase)

# print("Hi " * phrase_chars)

# === Task 5 ===

# subprocess.run(["cls"], shell=True)

# print("Calculating the sum of the first 100 numbers...")

# num = 1
# total = 0

# while num <= 100:
#     total = total + num
#     num = num + 1
# print(f"...Done! The answer is {total}")

# === Task 6 ===

subprocess.run(["cls"], shell=True)

current = 1
total = 0

amount = int(input("How many numbers should I sum up? "))
print("")

while current <= amount:
    num = int(input(f"Please enter number {current} of {amount}: "))
    total = total + num
    current = current + 1
print(f"\nThe answer is {total}")