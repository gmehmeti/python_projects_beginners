
# Role the dice game
import random as rn

while True:
    cmd = input("Roll the dice? (y/n): ").lower()
    if cmd == "n":
        print("Thank you for playing!")
        exit(0) # break
    elif (cmd == "y"):
        first = rn.randint(1,6)
        second = rn.randint(1,6)
        print(f"({first}, {second})")
    else:
        print("Invalid choice!")
        continue
