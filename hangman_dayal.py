import time
import random

def main():
    global word
    global count
    global limit
    global display
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
                      "plants"]
    word = random.choice(words_to_guess)
    count = 0
    limit = 5
    display = "_" * len(word)
    print(display)
def hangman():
    global word
    global display
    global count
    global limit

    userdata = input("enter your guess: ")
    if len(userdata) >=2 or userdata == "" or userdata <= "9":
        print("enter a valid letter")
        hangman()
    elif userdata in word:
        index=word.find(userdata)
        word= word[0:index] + "_" + word[index+1:]
        display=display[:index] + userdata + display[index+1:]

        if word == '_' * len(word):
            print("you have won")
            exit()
        print(display)
        hangman()
    else:
        count+=1
        if count==limit:
            print("Your have been hanged")
        else:
            print('You have '+str(limit-count)+' more chances')
            hangman()

main()
hangman()