import random

wordList = ['Undertaker', 'Rock', 'Paper', 'Scissors', 'Yellow', 'Marie', 'Dwight']
life = 5
valid = False
selectedWord = random.choice(wordList)
selected_word_length = len(selectedWord)
count = 0
display_word = []
display_string = ""
tempString = selectedWord
selectedWord = selectedWord.lower()

while count < selected_word_length:
    display_word.append("_")
    count += 1
print(display_word)
print(display_string)

while life > 0:
    if selectedWord == display_string:
        break
    inputChar = input("Enter a letter: \n")
    inputChar = inputChar.lower()
    for i in range(len(selectedWord)):
        if selectedWord[i] == inputChar and display_word[i] != inputChar:
            valid = True
            display_word[i] = inputChar
    if valid:
        display_string = "".join(display_word)
        print(display_string)
    if not valid:
        life = life - 1
        print("Wrong letter. Try again.")
    valid = False

if life == 0:
    print("You lose!")
    print("The word was: " + tempString)
else:
    print("You win!")