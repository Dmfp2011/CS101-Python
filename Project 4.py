#####################################################
#####################################################
##  CS 101
##  Program 4
##  Dylan Pembrook
##  dmpfzf@mail.umkc.edu
##
##  Problem: File Transposition
##  
##  Algorithm:
##  Ask the user whether they want to 1. encipher a file, 2. decipher a file, or Q.  quit
##  Error handling if the enter a response other than 1,2, or Q
##  Ask the user which file they wish to encipher or decipher
##  Error handling for if the user enters a file that doesn’t exist
##  Ask the user which file they wish to write to
##  For encipher:
##  	Take each individual character of the string.
##      If the index of that character divided by 2 has a remainder of 0 (example: 4/2=2.0 5/2=2.5)
##      then the character in question is added to a new string called first.
##      If the index divided by 2 has any remainder, then the character is added to a new string called second.
##      Once the original string has been fully examined, the transposed new string is equal to first + second.
##  This process is repeated for each line of the file. Once the entirety of the file has been dealt with, the file will close
##  For decipher:
##  	Split the string in half. The first character of the first half and the first character of the second half are added to make a new string.
##      And so on and so on until both the first half and second half are used up and the new string is complete.
##      Write the new string into a new file. Continue onto the next line until there is no more lines to read. Close file(s)
##  This process is repeated for each line of the file. Once the entirety of the file has been dealt with, the file will close
##  For Quit:
##  	Exit the program
##  Repeat the first step once the new file is written.
##  
##
##  Error handling:
##      If the user submits a response other than 1, 2, or Q
##      if the user submits a file that doesn't exist
####################################################
####################################################

def transpose(file):
    """encodes the string and return the transposed value
    params:
    original: str-Original clean text string
    returns: str-Transposed string.
    Examples of transpose:
    >>>transpose("1234")
    '1324'
    >>>transpose("12345")
    '13524'
    >>>transpose("Hello World")
    'HloWrdel ol'"""
    first=""
    second=""
    file=str(file)
    for chr in range(0,len(file)):
        if chr%2==0: first+=(file[chr])
        else: second+=(file[chr])
    encipher=first+second
    return encipher

def decipher(message):
    """ Takes a transposed message and returns it back to the original.
    params:
    message:str-Transposed message
    returns:str-Unencrypted original.
    Examples of decipher
    >>>decipher("1324")
    '1234'
    >>>decipher("13524")
    '12345'
    >>>decipher("HloWrdel ol")
    'Hello World'"""
    first=""
    second=""
    original=""
    message=str(message)
    length_two=int(len(message)/2)
    #Determining the decipher for an even length word
    if len(message)%2==0:
        for chr in range(0,length_two):
            first+=(message[chr])
        for chr in range(length_two,len(message)):
            second+=(message[chr])
        for chr in range(0,length_two):
            original+=first[chr]
            original+=second[chr]
        return(original)
    #Determining the decipher for an odd length word
    elif len(message)%2!=0:
        for chr in range(0,length_two+1):
            first+=(message[chr])
        for chr in range(length_two+1,len(message)):
            second+=(message[chr])
        for chr in range(0,length_two+1):
            original+=first[chr]
            try:
                original+=second[chr]
            except IndexError:
                break
        return(original)

def main_menu():
    """Prints up the main menu.
    Has error handling for bad input"""
    while True:
        print()
        print("Transposition options")
        print()
        print("1. Encipher File")
        print("2. Decipher File")
        print("Q. Quit")
        choice=input("==>")
        if choice in ("1","2","Q","q"):
            return(choice)
            break
        else:
            print("You must enter 1,2 or Q")

def get_file(cipher):
    """Gets the name of the file depending on users choice"""
    while True:
        in_file=input("What is the name of the file to "+cipher+" ==>")
        try:
            test_file=open(in_file)
            break
        except IOError:
            print("Could not find the file specified. Try another filename.")
    return in_file
####################################################################

#Printing up the main menu
while True:
    choice=main_menu()
    print()
    #Determining if the choice was one, two, or Q
    if choice=="1":
        #Opening the in file and the out file
        in_file=open(get_file("Encipher"))
        out_file=input("What is the name of the file to write to ==>")
        out_file=open(out_file,"w")
        #Itterating through the lines of the file
        for line in in_file:
            line=line.strip()
            out_file.write(transpose(line))
            out_file.write('\n')
            
    elif choice=="2":
        #Opening the in file and the out file
        in_file=open(get_file("Decipher"))
        out_file=input("What is the name of the file to write to ==>")
        out_file=open(out_file,"w")
        #Itterating through the lines of the file
        for line in in_file:
            line=line.strip()
            out_file.write(decipher(line))
            out_file.write('\n')
            
    else:
        break
    print("The task has been completed")

    #Closing Files
    in_file.close()
    out_file.close()
