#note that literals are case sensitive when it comes to assessing variable values
secret_word = "Power"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
   
   if guess_count < guess_limit :
    guess = input("Enter guess: ")
    guess_count += 1
    
   else:
       out_of_guess = True 
    
    
if out_of_guess:
       
       print("Out of guesses, better luck next time") 
    
else:
       
       print("You win the game") 
   