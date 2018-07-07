import os
import random
from Timer import *
#guessed_tries = 0
 
def loadListOFCountries(): #load .txt file with countries
    with open('countries_and_capitals.txt', 'rt') as countries:
        lista = []
        for line in countries.readlines():
            line= line.strip()
            lista.append(line)
            #pick_random_line_from_list = random.choice(lista)
    return lista

def dash(): #hides capital name from the player
    for letter in capital: #convert string (capital name) into list of strings
        spelled_capital.append(letter)
    print('Capital: ', end='')
    for x in capital: #hides capital. Prints "-" for every letter 
        print('-', end='')
    print('\n')

def letters(life, guessed_tries, score): #handle player guesses
    draw_hangman(life)

    player_guess = input('\nPick a letter or capital: ').upper()
    guessed_tries += 1
    if len(player_guess) > 1: #if more then one letter is entered by Player
        if wrong_ans: print('Not in word: ', wrong_ans)
        if player_guess == capital: #if answer is correct
            score += 1000
            win(score, guessed_tries)
            exit()
        else: #if long answer is wrong
            os.system('clear')
            if wrong_ans: print('Not in word: ', wrong_ans)
            life -= 2
            if life == -1: life = 0
            score -= 200
            if score < 0: score = 0
    else: #if only one letter is entered by Player, do this:
        try: #check if letter is guessed correctly
            foundIndexNumber = spelled_capital.index(player_guess)
            os.system('clear')
            print('Not in word: ', wrong_ans)
            try:   #if player guessed this letter earlier, do nothing
                if player_guess in ans: 
                    os.system('clear')
                    if wrong_ans: print('Not in word: ', wrong_ans)
                else: #if player now guessed new letter add this letter to the list
                    score += 100
                    ans.append(player_guess) 
                    os.system('clear')
                    if wrong_ans: print('Not in word: ', wrong_ans) 
            except ValueError:
                os.system('clear')
                print('Not in word: ', wrong_ans)
        except ValueError: #letter not guessed correctly = error
            score -= 10
            if score < 0: score = 0
            life -= 1
            if player_guess not in wrong_ans:
                wrong_ans.append(player_guess) #add letter that was not guessed correctly to the list
                os.system('clear')
                print('Not in word: ', wrong_ans)
            else:
                os.system('clear')
                print('Not in word: ', wrong_ans)
    if not wrong_ans:  print('\n', end='')

    print('Country:', choosen_country[0])
    print('Capital: ', end='')
    dashes = 0
    for x in capital: #hides capital. Prints "-" for every letter 
        if x in ans:
            print(x, end='')
        else:
            print('-', end='')    
            dashes += 1

    if dashes == 0: #if every letter is visible = you won
        print('\n')
        print('Lives:', life)
        draw_hangman(life)
        #T.stop()
        win(score, guessed_tries)
        #print('\nYOU WON CONGRATULATIONS')
        exit()
    else:
        pass
    print('\n')
    print('Lives:', life)
    return life, guessed_tries, score

def info_player(score, guessed_tries): #ask player for name and surname
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    #guessed_tries += 1
    person = open("person.txt", "w")
    print("Time: ", datetime.datetime.now(), file = person)
    print(name + " " + surname, file = person)
    print("Guessed word: " + capital, file = person)
    print("Guessed tries: " + str(guessed_tries), file = person)
    print("Score: " + str(score), file = person)

def win(score, guessed_tries): #handle player win event
    print("\nYOU WON CONGRATULATION")
    print("Guessed tries: " + str(guessed_tries))
    print("Score: ", score)
    #score += 1000
    #guessed_tries -= 1
    T.stop()
    info_player(score, guessed_tries)

def win_two(life, ile, score, guessed_tries): #not used currently
    life -= 2
    print("Life: ", life)
    print("Test nr. ", ile)
    print("Score: ", score)
    guessed_tries += 1
    print("Guessed tries: " + str(guessed_tries))

def draw_hangman(life): #This function draws Hangman in terminal
    
    Hangman = ["/\\","""
	  |
     /\\""","""
      |
      |
     /\\""","""
      |
      |
      |
     /\\""","""
      |/
      |
      |
      |
     /\\""","""
       -
      |/
      |
      |
      |
     /\\""","""
       --
      |/
      |
      |
      |
     /\\""","""
       ---
      |/
      |
      |
      |
     /\\""","""
       ---
      |/  |
      |
      |
      |
     /\\""","""
       ---
      |/  |
      |   O
      |
      |
     /\\""","""
       ---
      |/  |
      |   O
      |   |
      |
     /\\""","""
       ---
      |/  |
      |   O
      |  /|\\
      |
     /\\""","""
       ---
      |/  |
      |   O
      |  /|\\
      |  /\\
     /\\"""]
    #if life == 5:
    #print(Hangman[7])
    #if life == 4:
     #   print(Hangman[8])
    #else:
    if life == 5:
        print(Hangman[7])
    if life == 4:
        print(Hangman[8])
    if life == 3:
        print(Hangman[9])
    if life == 2:
        print(Hangman[10])
    if life == 1:
        print(Hangman[11])
    if life == 0:
        print(Hangman[12])
    if life == -1:
        print(Hangman[12])
    
    

while True:
    os.system('clear') # clears terminal
    life = 5
    ans = [] #lista odpowiedzi gracza (poszczegolne litery)    
    pick_random_line_from_list = random.choice(loadListOFCountries())
    choosen_country = pick_random_line_from_list.split('|')
    wrong_ans = []
    if not wrong_ans:
        print('\n', end='')
    
    print('Country:', choosen_country[0]) #shows country name to the Player
    delete_space = choosen_country[1]
    capital = delete_space[:0] + delete_space[(1):]
    capital = capital.upper() #change all letters in capital to upper case
    spelled_capital = [] 
    wrong_ans = []

    dash()
    print('Lives:', life)

    T = Timer()
    T.start()
    score = 0
    guessed_tries = 0
    
    while life > 0: #run this loop if player is alive
        life, guessed_tries, score = letters(life, guessed_tries, score)
    
    #T.stop()
    draw_hangman(life)
    print('\nNumber of tries:', str(guessed_tries))
    print('score:', score)
    T.stop() #player is dead, stop timer
    print('       .-* GAME OVER *-.\n\n\n')
    info_player(score, guessed_tries)
    again = input('Run again? (Y/N): ').upper()
    if again == 'Y':
        life = 5
        guessed_tries = 0
        continue
    else:
        print('Exiting...')
        exit()
