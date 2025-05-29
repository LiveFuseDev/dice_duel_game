import random

win_messages = ["Victory is yours!", "You cheated death!", "The gods smile upon you!"]
lose_messages = ["Fate shows no mercy.", "You have been judged.", "The void awaits."]
draw_messages = ["Balance has been struck.", "Neither wins. Neither loses.", "A stalemate in the stars."]


print("🎲 Welcome to Dice Duel! 🎲")
print("Prepare yourself for a battle of luck.")
print("Roll the die and let fate decide who reigns supreme!")

input("Type Roll to decide your fate.\n").lower()

user_roll = random.randint(1, 6)
computer_roll = random.randint(1, 6)

print(f"You rolled {user_roll}")
print(f"Fate rolled {computer_roll}")

if user_roll > computer_roll:
    print(random.choice(win_messages))
elif user_roll < computer_roll:
    print(random.choice(lose_messages))
else:
    print(random.choice(draw_messages))