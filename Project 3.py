#####################################################
#####################################################
##  CS 101
##  Program 3
##  Dylan Pembrook
##  dmpfzf@mail.umkc.edu
##
##  Problem: Slice of life
##  
##  Algorithm:
##  rounds=int(input(“how many rounds do you want to play? (1-20)=>”))
##  while rounds<0 or rounds>20:
##	print(“you must enter a valid number for rounds between 1 and 20”)
##	rounds=int(input(“how many rounds do you want to play? (1-20)=>”))
##  difficulty=int(input(“which difficulty would you like the string? 1. easy, 2. medium, 3.hard”)
##  if difficulty not in (1,2,3):
##	print(“you must enter a valid difficulty 1. easy, 2. medium, 3.hard”)
##	difficulty=int(input(“which difficulty would you like the string? 1. easy, 2. medium, 3.hard”)
##  depending on the difficulty level, create a “word” of random letters or random casing.
##	easy=5 letters, medium= 7 letters, hard=10 letters
##  once the word is created, three random numbers are created to indicate how the slicing will occur
##  for easy and medium:
##  the first random number will be from 0 to half of the length of the word (start) (E=0 or 1)(M=0,1,2)
##	the 2nd random number will be from half of the length of the word to the length (stop) (E=2,3,4) (M=(3,4,5,6)
##`for hard:
##	the 1st number will be from 0 to half of the length of the word (start)can be negative(0,1,2,3,4,-1,-2,-3,-4,-5)
##	the 2nd number will be from half of the length to the full length of the word(stop) can be negative(5,6,7,8,9,-6,-7,-8,-9,-10)
##	the 3rd number will either be a 1 or a 2 (step) can be negative.(-2,-1,1,2)
##  once all this is implemented, the user will submit their answer to the sliced word.
##  if the answer given is correct a #right counter will increase by one. the next round will begin (round-=)
##  else: the next round will begin (round-=)
##  once all rounds are over,
##  print (“you got ”,correct,” out of”, rounds, “correct which is”, (correct/rounds)*100,”%”)
##  again=input(“would you like to play again?”)
##
##  Error handling: if the user enters a number =<0 or 20< for rounds
##  If the user enters any letter other than Y,YES,N, or NO for playing again
##  If the user enters a number other than 1,2,3 for the difficulty
##
####################################################
####################################################

import random
import string

run_again=True
while run_again==True:
    print("="*70)
    print("Welcome to the game of slice!")

#Asking user how many rounds they would like to play betwen 1-20
    start=False
    while start is False:
        rounds=int(input("how many rounds do you want to play? (1-20)=>"))
        while rounds<=0 or rounds>20:
            print("you must enter a valid number for rounds between 1 and 20")
            rounds=int(input("how many rounds do you want to play? (1-20)=>"))
        start=True
    starting_rounds=rounds
    print()

#Asking user which difficulty they wish to play the game
    condition=False
    while condition is False:
        difficulty=int(input("What difficulty would you like the slice? 1. Easy, 2. Medium, 3. Hard=>"))
        while difficulty not in (1,2,3):
            print("You must enter a valie choice, 1. Easy, 2. Medium, 3. Hard")
            difficulty=int(input("What difficulty would you like the slice? 1. Easy, 2. Medium, 3. Hard=>"))
        condition=True



#Asking user if they would like hints enabled
    print()
    hint=input("Would you like hints enabled?")
    detail_bool=False
    while detail_bool==False:
        if hint.upper() in ("Y","YES","N","NO"):
            if hint.upper()in ("Y","YES"):
                detail_hints=True
                detail_bool=True
                print()
            elif hint.upper()in ("N","NO"):
                detail_hints=False
                detail_bool=True
                print()
        else:
            print()
            print("Please enter valid input(Y,YES,N,or NO)")
            hint=input("Would you like hints enabled?")


    num_correct=0
    while rounds>0:
        
#Building up the slice parameter
        if difficulty ==1:
            word_length=5
            final_word=""
            start_slice,stop=random.randint(0,1),random.randint(2,5)

#Setting up the letters in the slice
            while word_length>0:
                letter=random.choice(string.ascii_letters)
                word_length-=1
                final_word+=letter

#Displaying the hints if they were selected
            if detail_hints==True:
                print("{:>27}".format("01234"))
                print("{:>27}".format("-54321"))
                
#Determining if the users guess was correct
            guess=input("what is the slice of '{}'[{}:{}:]? ==>".format(final_word,start_slice,stop))
            final_slice= final_word[start_slice:stop:]
            if guess==final_slice:
                num_correct+=1
                print("Correct, the word was",guess)
                print()
                rounds-=1
            else:
                print("Wrong, the word was",final_slice)
                print()
                rounds-=1

#Building a medium difficulty word
        elif difficulty==2:
            word_length=7
            final_word=""
            start_slice,stop=random.randint(0,2),random.randint(3,7)
           
#Setting up the letters in the slice
            while word_length>0:
                letter=random.choice(string.ascii_letters)
                word_length-=1
                final_word+=letter

#Displaying the hints if they were selected
            if detail_hints==True:
                print("{:>29}".format("0123456"))
                print("{:>29}".format("-7654321"))

#Determining if the users guess was correct
            guess=input("What is the slice of '{}'[{}:{}:]? ==>".format(final_word,start_slice,stop))
            final_slice= final_word[start_slice:stop:]
            if guess==final_slice:
                num_correct+=1
                print("Correct, the word was",guess)
                print()
                rounds-=1
            else:
                print("Wrong, the word was",final_slice)
                print()
                rounds-=1

#Building a hard difficulty word          
        elif difficulty==3:
            word_length=10
            final_word=""

#setting up the extra possibilities on the hard difficulty
            if random.randint(1,4)==1:
                start_slice=-random.randint(6,10)
            else:
                start_slice=random.randint(0,4)

            if random.randint(1,4)==1:
                end_slice=-random.randint(1,5)
            else:
                end_slice=random.randint(5,9)

            if random.randint(1,5)==1:
                step=2
            else:
                step=1

            if random.randint(1,4)==1:
                step=-step


#Setting up the random letters in the slice
            while word_length>0:
                letter=random.choice(string.ascii_letters)
                word_length-=1
                final_word+=letter

#Displaying the hints if they were selected
            if detail_hints==True:
                print("{:>32}".format("0123456789"))
                print("{:>32}".format("-0987654321"))

#Determining whether or not the guess was correct            
            guess=input("what is the slice of '{}'[{}:{}:{}]? ==>".format(final_word,start_slice,end_slice,step))
            final_slice= final_word[start_slice:end_slice:step]
            if guess==final_slice:
                num_correct+=1
                print("Correct, the word was",guess)
                print()
                rounds-=1
            else:
                print("Wrong, the word was",final_slice)
                print()
                rounds-=1
            

#Printing off the statistice to the game
    print("You got",num_correct,"out of",starting_rounds,"which is",100*(num_correct/starting_rounds),"%")

#Asking the user if they would like to play again
#Error handling for incorrect input
    again=input("would you like to play again?")
    again_bool=False
    while again_bool==False:
        if again.upper() in ("Y","YES","N","NO"):
            if again.upper()in ("Y","YES"):
                run_again=True
                again_bool=True
                print()
            elif again.upper()in ("N","NO"):
                run_again=False
                again_bool=True
        else:
            print()
            print("Please enter valid input(Y,YES,N,or NO)")
            again=input("Would you like to run program again?")
print("Thank you for playing!")


