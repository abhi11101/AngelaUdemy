print("Welcome to the TrueLove program.")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_name = (name1 + name2).lower()

tens_digit = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")
tens_digit *= 10

ones_digit = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")

score = tens_digit + ones_digit

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Score is {score}")
