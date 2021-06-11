import random

lives =  3

letter = ["the","next","clue","is","in","Arkham","Assylum"]

def anagram_game():
    global lives
    random.shuffle(letter)
    print(letter)

    print("Solve the anagram")
    guess=input("Type your guess here")

    if guess.lower()=="the next clue is in arkham assylum":
        print ("yes")
    elif guess.lower!="the next clue is in arkham assylum" and lives >1:
        lives -=1
        print (f"No, and you have lost a life. You have {lives} left")
        anagram_game()
    else:
        print("Out of lives dead")

anagram_game()
