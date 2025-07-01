import random
# Define snakes and ladders as dictionaries
snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72
}
ladders = {
    6: 25,
    11: 40,
    60: 85,
    46: 90,
    17: 69
}
# Function to simulate dice roll
def roll_dice():
    return random.randint(1, 6)
# Move with snakes and ladders logic
def move_player(position, roll):
    new_position = position + roll
    if new_position > 100:
        print(f"Roll of {roll} ignored, move exceeds 100.")
        return position
    print(f"Moved to {new_position}")
    if new_position in snakes:
        print(f"Oops! Bitten by a snake! Down to {snakes[new_position]}")
        return snakes[new_position]
    elif new_position in ladders:
        print(f"Yay! Climbed a ladder! Up to {ladders[new_position]}")
        return ladders[new_position]
    return new_position
# Ask user name
user_name = input("Enter your name: ")
robot_name = "Robot"
# Randomly choose who plays first
print("\nRolling to decide who plays first...")
first = random.randint(1, 2)
if first == 1:
    turn_order = [user_name, robot_name]
else:
    turn_order = [robot_name, user_name]
print(f"\n{turn_order[0]} will go first!")
# Initialize player positions
positions = {
    user_name: 0,
    robot_name: 0
}
# Game loop
while True:
    for player in turn_order:
        print(f"\n{player}'s turn.")
        if player == user_name:
            input("Press Enter to roll the dice... ")
            roll = roll_dice()
            print(f"You rolled a {roll}")
        else:
            roll = roll_dice()
            print(f"Robot rolled a {roll}")
            current_position = positions[player]
        new_position = move_player(current_position, roll)
        positions[player] = new_position
        print(f"{player}'s new position: {positions[player]}")
        if positions[player] == 100:
            print(f"\n🎉 {player} wins the game! 🎉")
            exit()
