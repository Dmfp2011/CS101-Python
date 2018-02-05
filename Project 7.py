#####################################################
#####################################################
##  CS 101
##  Program 7
##  Dylan Pembrook
##  dmpfzf@mail.umkc.edu
##
##  Problem: Sentiment Analysis
##  
##  Algorithm: Ask the user if they would like to get a sentiment or to quit
##      If quit, exit the program
##      Error handling for if the user enters anything other than 1 or Q
##      Ask the user which file they wish to get the words from
##      Error handling for if the file does not exist
##      Ask the user how they would like the sentiment sorted.
##      Error handling for if the user enters anything other than 1, 2, 3, or 4
##      Create a dictionary for each of the words in the file. Have the value to the words be a list
##      of the scores of the movie associated with that word. Ex: {“Horrible”:[0,1,4,2]}
##      Create a for loop to iterate through each of the scores for the word
##      and figure out the average score, assign that to a variable.
##      Calculate the standard deviation for the word as well, assign that to a variable.
##      Output the word, occurrence, Avg Score, and STD to a table depending on the user’s choice for sorting.
##      Repeat for each word in the word list.
##      Once the table has been fully filled out, repeat the first step and start the process over again.
##
##  Error Handling: If user enters anything into the main menu other than 1 or Q
##      If the user enters anything other than 1, 2, 3, or 4 for the display type
##      If the file does not exist
####################################################
####################################################

def main_menu():
    """Displays the main menu and checks whether or not the user enters the correct answer"""
    while True:
        print("           Python Sentiment Analysis")
        print()
        print("  1. Get sentiment for all words in a file")
        print("  Q. Quit")
        choice=input("===>")
        if choice=="1":
            return choice
        elif choice.upper()=="Q":
            return choice
        print("You must choose one of the valid choice of 1, Q")
        print()
        print()


def file_open():
    """Prints off the menu for which sentiment display the user wants"""
    while True:
        choice=input("Enter the name of the file with words to score")
        try:
            in_file=open(choice)
            in_file.close()
            return choice
        except IOError:
            print("Could not find the file you specified",choice)

def dict_list_creator(choice):
    """Creates a dictionary of the words in the word list and an empty list"""
    word_list={}
    in_file=open(choice)
    line=in_file.readlines()
    for word in line:
        word=word.strip()
        word_list[word]=[]
    return word_list

def display():
    """prints up the display to choose the graph layout"""
    while True:
        print("    Sort Options")
        print("1. Sort by Avg Ascending")
        print("2. Sort by Avg Descending")
        print("3. Sort by Standard Deviation Ascending")
        print("4. Sort by Standard Deviation Descending")
        print()
        choice_two=input("===>")
        if choice_two in ("1","2","3","4"):
            return choice_two
        print("You must choose one of the valid choices of 1,2,3,4")

def main_prog(word_dictionary):
    """counts the number of times the word appears in a review and adds that to a list"""
    main_file=open("movieReviews.txt")
    main_file_read=main_file.readlines()
    for word in main_file_read:
        for value in word_dictionary:
            if value.upper() in str(word[1:]).upper():
                word_dictionary[value].append(int(word[0]))

def occurance(word_dictionary):
    """calculates the number of occurences the word has"""
    occur={}
    for value in word_dictionary:
        occur[value]=len(word_dictionary[value])
    return occur

def average(word_dictionary):
    """Calculates the average of the scores for the word"""
    avg_dict={}
    for value in word_dictionary:
        score=0
        for lst in word_dictionary[value]:
            score+=lst
            average_total=score/len(word_dictionary[value])
            avg_dict[value]=average_total
    return avg_dict

def standard_deviation(word_dictionary,avg_dict):
    """"Calculates the standard deviation for the words"""
    std_dict={}
    for value in word_dictionary:
        std=0
        for lst in word_dictionary[value]:
            std+=(lst-avg_dict[value])**2
            std_total=std/len(word_dictionary[value])
            std_dict[value]=std_total
    return std_dict
    

def table(word_dictionary,occurance,avg,std,choice):
    """prints up a nice pretty table for the user to awe at"""
    print("{}{:>18}{:>12}{:>17}".format("Word","Occurrence","Avg Score","Std"))
    print("="*51)
    #if the user wants AVG ascending
    if choice=="1":
        for value in word_dictionary:
            print("{:<0}{:>18}{:>10.4f}{:>19.4f}".format(value,occurance[value],avg[value],std[value]))
    #if the user wants AVG decending
    elif choice=="2":
        for value in word_dictionary:
             print("{:<0}{:>18}{:>10.4f}{:>19.4f}".format(value,occurance[value],avg[value],std[value]))
    #if the user wants the STD ascending
    elif choice=="3":
        for value in word_dictionary:
             print("{:<0}{:>18}{:>10.4f}{:>19.4f}".format(value,occurance[value],avg[value],std[value]))
    #if the user wants the STD decending
    elif choice=="4":
        for value in word_dictionary:
             print("{:<0}{:>18}{:>10.4f}{:>19.4f}".format(value,occurance[value],avg[value],std[value]))
    

#####################################################################
#Main bulk of program
loop=True
while loop:
    menu=main_menu()
    #if the user wants to continue with the program
    if menu=="1":
        #Tests the file the user inputs
        sentiment=file_open()
        #creats a dictionary from the word list
        dicts=dict_list_creator(sentiment)
        #puts up the choice for sorting method
        display_choice=display()
        #counts up the scores for the words
        word=main_prog(dicts)
        #counts the occurances of said words
        occur=occurance(dicts)
        #calculates the average of the scores
        average_dictionary=average(dicts)
        #Calculates the standard deviation of the words
        std_avg_calc=standard_deviation(dicts,average_dictionary)
        #displays the table of all the info
        table(dicts,occur,average_dictionary,std_avg_calc,display_choice)
    #if the user wants to quit
    else:
        loop=False
