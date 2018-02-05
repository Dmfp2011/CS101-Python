#####################################################
#####################################################
##  CS 101
##  Program 2
##  Dylan Pembrook
##  dmpfzf@mail.umkc.edu
##
##  Problem: Tracking luggage
##  
##  Algorithm:
##  1)Import random
##  2) Ask user how many trials they wish to run
##  If trials<=0, ask user to enter a value >0
##  3)Luggage always starts at Mci, (40%Lvs, 30%Sea, 30%Hnl)
##  *Random number (1-10) if random number is 1,2,3,4 package is going to Lvs
##  If random number is 5, 6, 7 package is going to Sea
##  If random number is 8,9,10 package is going to Hnl
##  If the package goes to Lvs, (30%Mci, 50%Sea, 20%Hnl)
##  *Random number (1-10) chosen, if random number is 1, 2, 3 package will go to Mci
##  If random number is 4, 5, 6, 7, 8 package will go to Sea
##  If random number is 9, 10 package will go to Hnl
##  If the package goes to Sea, (10%Mci, 60%Lvs, 30%Hnl)
##  *Random number (1-10) chosen, if random number is (1) package will go to Mci
##  If random number is (2, 3, 4, 5, 6, 7) package will go to Lvs
##  If random number is (8, 9, 10) package will go to Hnl
##  Once package reaches Hnl, that trial is over.
##  *Keep track of how many times the luggage hops
##  4)Repeat step 3 for the number of trials
##  5) Ask user if they want detailed output, answer must be, “Y, YES, N, NO”
##  *If answer is not approved, ask user to input correct answer*
##  6) If the user wants detailed output, continue with step 7
##  *if the user does not want detailed output, skip step 8*
##  7) Print the journey for each trial
##  8) Print % of the time package was on time (hop<=2)
##  9) Print the max number of hops
##  10)	Ask user if they want to run program again
##  *input must be, “Y, YES, N, NO”*
##  11) If user inputs incorrect input, ask user to input correct response
##  12) If user wishes to run program again, repeat all previous steps
##  13)	If user wishes not to run program, exit program
##
##  Error Handling:
##  1)if trials<=0, ask user to input value greater than zero
##  2) if user enters something other than Y, YES, N, or No, ask user to
##  enter appropriate variable
##
##
####################################################
####################################################

import random

#While loop for whether or not the user wants to run the program again
run_again=True
while run_again:

#Asking user for input regarding number of trials
#Error handling if trials<=0
    print("="*70)
    trials=int(input("how many rounds do you want to run lost luggage?"))

    while trials<=0:
        print("you must enter a value greater than 0")
        print()
        trials=int(input("how many rounds do you want to run lost luggage?"))

#Setting our constants
    on_time=0
    max_hops=0
    hops=0
    mci=random.randint(1,10)
    trial_count=trials
    input_counter=0
    routes=""
    detail_count=0

#Asking the user if they would like detailed output
#Error handling if the user enters a value other than Y,YES,N,or NO
    detailed_output=input("Would you like detailed output?")
    while detail_count == 0:
        if detailed_output.upper() in ("Y","YES","N","NO"):
            if detailed_output.upper()in ("Y","YES"):
                detail_count=1
            elif detailed_output.upper()in ("N","NO"):
                detail_count=1
        else:
            print()
            print("Please enter valid input(Y,YES,N,or NO")
            detailed_output=input("Would you like detailed output?")

        
    while trials >0:
#Random numbers generated to determine where the package will go if package leaves from MCI
        if mci in range (1,5):
            mci,sea,lvs=0,0,random.randint(1,10)
            hops+=1
            routes+="MCI->"
        elif mci in range (5,8):
            mci,lvs,sea=0,0,random.randint(1,10)
            hops+=1
            routes+="MCI->"
        elif mci in range (8,11):
            mci=random.randint(1,10)
            trials-=1
            hops+=1
            routes+="MCI->HNL"
            if detailed_output.upper() in ("Y", "YES"):
                print(routes)
                routes=""
            else:
                routes=""
#Calculating if package was on time
            if hops<3:
                on_time+=1
#Calculating max number of hops
            if hops>max_hops:
                max_hops=hops
                hops=0
            else:
                hops=0
#Random numbers generated to determine where the package will go if package leaves from LVS
        elif lvs in range (1,4):
            lvs,sea,mci=0,0,random.randint(1,10)
            hops+=1
            routes+="LVS->"
        elif lvs in range (4,9):
            lvs,mci,sea=0,0,random.randint(1,10)
            hops+=1
            routes+="LVS->"
        elif lvs in range (9,11):
            lvs,sea,mci=0,0,random.randint(1,10)
            trials-=1
            hops+=1
            routes+="LVS->HNL"
            if detailed_output.upper() in ("Y", "YES"):
                print(routes)
                routes=""
            else:
                routes=""
#Calculating if package was on time
            if hops<3:
                on_time+=1
#Calculating max number of hops
            if hops>max_hops:
                max_hops=hops
                hops=0
            else:
                hops=0
#Random numbers generated to determine where the package will go if package leaves from SEA
        elif sea in range (1,2):
            sea,lvs,mci=0,0,random.randint(1,10)
            hops+=1
            routes+="SEA->"
        elif sea in range (2,8):
            sea,mci,lvs=0,0,random.randint(1,10)
            hops+=1
            routes+="SEA->"
        elif sea in range (8,11):
            sea,lvs,mci=0,0,random.randint(1,10)
            trials-=1
            hops+=1
            routes+="SEA->HNL"
            if detailed_output.upper() in ("Y", "YES"):
                print(routes)
                routes=""
            else:
                routes=""
#Calculating if package was on time
            if hops<3:
                on_time+=1
#Calculating max number of hops
            if hops>max_hops:
                max_hops=hops
                hops=0
            else:
                hops=0
#Output for max number of hops and number of times the package was on time
    print()
    print("max number of hops was", max_hops)
    print("The package was on time",100*(on_time/trial_count),"%of the time.) (",on_time,"/",trial_count,")")

#Asking user if they want to play again
#Error handling if user enters a value other than Y,YES,N,or NO
    print()
    again=input("Would you like to run program again?")

    while input_counter==0:
        if again.upper() in ("Y","YES","N","NO"):
            if again.upper()in ("Y","YES"):
                run_again=True
                input_counter+=1
                print()
            elif again.upper()in ("N","NO"):
                run_again=False
                input_counter+=1
        else:
            print()
            print("Please enter valid input(Y,YES,N,or NO")
            again=input("Would you like to run program again?")
print()
print("Thank you for flying with Genreic Airlines!")
