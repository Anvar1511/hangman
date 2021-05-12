# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:23:58 2021

@author: Anvar
"""

import random
words_list = ["baxt", "salomatlik", "boylik"]
chosen_word = random.choice(words_list)

display = []
word_len = len(chosen_word)

for _ in range(word_len):
    display+="_"
print(display) 


end_of_game = False
while not end_of_game: 
    guess = input("Guess a letter: ").lower()
        
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position]=letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")
