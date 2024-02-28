
import random
import hangman_art
import hangman_words

end_of_game = False
word_list = hangman_words.word_list
stages = hangman_art.stages
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    #Guessed letter previously
    if guess in display:
      print("\nYou already guessed that letter. Try again.")
      
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       
        if letter == guess:
          display[position] = letter
        
    #Then reduce 'lives' by 1. 
    if guess not in chosen_word:
      lives-=1
      if lives > 0:
       print(f"\nOops! '{guess}' isn't in the word. You lost a life!")
  
    #If lives goes down to 0 then the game should stop and it should print "You lose."   
    if lives == 0:
      end_of_game = True
      print("\nYou lose!")

    #Print the ASCII art from 'stages' that corresponds to the
    #current number of 'lives' the user has remaining.
    print(f"{stages[lives]}")
  
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win!")
        
    
    
    