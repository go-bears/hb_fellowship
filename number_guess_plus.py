import random

# Put your code here
print "Hi, Let's play a game!"
name = raw_input("Let's play a game! What's your name? ")
print "Hello, %s! " % name

secret_number = random.choice(range(1,101))
#print secret_number

print "I have a secret number between 1 and 100."
print "You have seven guesses to find it." 
guesses = 7
score = 0
best_score = 7

while guesses > 0:
    #start
    if guesses == 7:
        print "let's start! you have %d guesses" % guesses
        print "So the lowest number of guesses is %d" % best_score


    #confirm guess if a number
    while True:
        try:
            user_guess = int(raw_input("Guess the number: "))
            break
        except ValueError:
            print "You did not type a number! Try again."
    
    #increment guesses and scores
    guesses -= 1
    score += 1

    #keep track of number of guesses and score
    if guesses > 1:
        print "try again. you have %d left" % guesses
    
        #confirm number guess is between 1-100    
        if user_guess < 0 or user_guess > 100:
            print "You're not following the rules. You can only guess between 1 and 100. And you wasted a guess."

        #compares user_guess against secret number    
        if user_guess < secret_number:
            print "You guessed too low."
        elif user_guess > secret_number:
            print "You guessed too high.  "
        elif user_guess == secret_number:
            print "You win. Congratulations!!!!"
            print "The secret number was %d" % secret_number
            
        #checks if current score is best score
            if score < best_score:
                best_score = score
                print "Also, you found the number in only %d guesses. " % score
                print "You're best!"

            play_again = raw_input("Would you like to play again? y/n: " )
            play_again = play_again.lower()
            if play_again == 'y' or play_again == 'yes':
                print "Great!! Let's go!"
                guesses = 7
                secret_number = random.choice(range(1,101))
            elif play_again == 'n' or play_again == 'no':
                print "Thanks for playing!"
                break
            else:
                print "That doesn't make sense. I'm assuming you don't want to play anymore. Bye!"
                break

  
    else:
        print "You have no more guesses. I win!"
        play_again = raw_input("Would you like to play again? y/n: " )
        play_again = play_again.lower()
        if play_again == 'y' or play_again == 'yes':
            print "Great!! Let's go!"
            guesses = 7
            secret_number = random.choice(range(1,101))
        elif play_again == 'n' or play_again == 'no':
            print "Thanks for playing!"
            break
        else:
            print "That doesn't make sense. I'm assuming you don't want to play anymore. Bye!"
            break


    #asks to play again 






# If the user inputs a number that isn't between 1-100 as requested, mock them for their crimes and ask them to enter a valid number.
# If the user inputs something that is not a number, mock them for their crimes and ask them to enter a valid number. Hint: a good way to do this is to learn about Python,s try and except statements.
# Ask the user if they would like to play again and restart the game rather than exiting.
# Keep track of the "high score" (or is that low score?) and display that when you congratulate the user
