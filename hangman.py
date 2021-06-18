
from logo import logo

from art import stages

import random

print(logo)

word_list = ['otter','cat','camel','horse','baboon']

chosen_word = random.choice(word_list)

display = []

for i in chosen_word:
    display += "_"
print(display)

stages.reverse()

lives = 6

end_of_game = False
 
while not end_of_game:
            
    guess = input('Guess a letter? ').lower()
                        
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
        
    if guess not in chosen_word:
        print("You chose the letter {} which is not in this word. You lost a life.".format(guess))
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lost!!!')
            
    if '_' not in display:                           
        end_of_game = True                
        print("You won!!!")
    
    print(stages[lives])










