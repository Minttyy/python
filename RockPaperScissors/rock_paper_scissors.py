import random

list = [
    [1,'✊'],
    [2,'✋'],
    [3,'✌'],
    [4,'🖖'],
    [5,'🦎']
]

# Display
print("===================")
print("Rock Paper Scissors")
print("===================")

for i in range(len(list)):
    print(f'{i+1}) {list[i][1]}')

# Chosen
player = int(input('Pick a number:'))
computer = random.choices(list)

for i in range(len(list)):
    if player == i+1:
        chosen = list[i][1]

print(f"You chose: {chosen}")
print(f"CPU chose: {computer[0][1]}")

# Logic
computer_number = computer[0][0]

if player == computer_number:
    print("No winners here! You are tied!")
elif (player == 2 and computer_number == 1) or (player == 1 and computer_number == 3) or (player == 3 and computer_number == 2):
    # Normal
    print("The player won!")
elif (player == 1 and computer_number == 5) or (player == 5 and computer_number == 4) or (player == 4 and computer_number == 3):
    # Additional `1`
    print("The player won!")
elif (player == 3 and computer_number == 5) or (player == 5 and computer_number == 2) or (player == 2 and computer_number == 4) or (player == 4 and computer_number == 1):
    # Additional `2`
    print("The player won!")
else:
    print("The CPU won! You have lost!")


