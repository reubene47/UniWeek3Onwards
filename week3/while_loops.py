# apples_num = int(input("How many apples should I remove?"))

# while apples_num > 0:
#     print("Removed apple.")
#     apples_num -= 1

import os
import subprocess

subprocess.run(["cls"], shell=True)

obstacles_input = int(input("How many obstacles should I avoid?\n"))

obstacles = 0

print("")

while obstacles < obstacles_input:
    obstacles += 1
    print(f"Avoiding... Done! {obstacles} obstacles avoided.")
print("\nAll obstacles have been avoided.")

