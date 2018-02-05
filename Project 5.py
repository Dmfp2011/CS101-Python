#####################################################
#####################################################
##  CS 101
##  Program 5
##  Dylan Pembrook
##  dmpfzf@mail.umkc.edu
##
##  Problem: Picture Filters
##  
##  Algorithm:Ask the user if they wish to perform 1. Grayscale, 2. Vintage, Q. Quit
##	If user enters anything other than 1,2, or Q then prompt them to enter a valid input
##  Ask the user which file they wish to apply the filter to
##	If the file doesn’t exist ask user to input a valid file name
##	If the third line of the file doesn’t read “255”, inform the user that they have a bad file and prompt for a valid file name.
##  Ask the user what the name of the file to be written to is
##  If the user selected option 1), set gray = .299* red value+0.587*green value+0.114*blue value
##  This is done for each set of three values throughout the entire program (has to be between 0 and 255)
##  If the user selected option 2), set vintage=blue/2… do this for all the blue values in the program (all blues will be line[6:3]
##  For option 1&2, write the new values in the appropriate lines and close both the files
##  If the user selects Q then exit the program.
##  Repeat the first step once the file has been written
##
## 
##  Error handling:
##      If the user submits a response other than 1, 2, or Q
##      if the user submits a file that doesn't exist
##      If the first line of the file is not "P3"
##      If the third line of the file is not "255"
####################################################
####################################################

def vintage():
    """takes all the blue values in the file[6::3] and halfs that value.
    prints original red and green values and prints the new blue"""
    line=in_file.readlines()
    print(line[0].strip(), file=out_filed)
    print(line[1].strip(), file=out_filed)
    print(line[2].strip(), file=out_filed)
    cnt=0
    for value in line[3:]:
        cnt+=1
        val_int=int(value)
        if cnt%3==0:
            print(val_int//2, file=out_filed)
        else:
            print(value.strip(), file=out_filed)

def gray_scale():
    """Takes the red. green, and blue values of the code and repurposes them
    to become a grayscale version of the pixels. prints the new values
    to the out file"""
    line=in_file.readlines()
    print(line[0].strip(), file=out_filed)
    print(line[1].strip(), file=out_filed)
    print(line[2].strip(), file=out_filed)
    cnt=1
    for value in line[3:]:
        if cnt==1:
            red=int(value)*0.299
            cnt+=1
        elif cnt==2:
            green=int(value)*0.587
            cnt+=1
        elif cnt==3:
            blue=int(value)*0.114
            cnt=1
            grayscale=red+green+blue
            print(grayscale, file=out_filed)
            print(grayscale, file=out_filed)
            print(grayscale, file=out_filed)

def main_menu():
    """Prints up the main menu.
    Has error handling for bad input"""
    while True:
        print()
        print("Image Filters")
        print()
        print("1. Convert image to Grayscale")
        print("2. Convert image to Vintage")
        print("Q. Quit")
        choice=input("==>")
        if choice in ("1","2","Q","q"):
            return(choice)
            break
        else:
            print("You must enter 1,2 or Q")

def get_file(filters):
    """Gets the name of the file depending on users choice"""
    while True:
        in_file=input("What is the name of the file to "+filters+" ==>")
        try:
            test_file=open(in_file)
            line=test_file.readlines()
            if line[0].strip()!="P3":
                print("The first line should read 'P3'")
            elif line[2].strip()!="255":
                print("The third line should read '255'")
            else:
                break
        except IOError:
            print("Could not find the file specified. Try another filename.")
    test_file.close()
    return in_file

def out_file():
    """Gets the name of the out file and tests to make sure it opens"""
    while True:
        out_file=input("What is the name of the file to write to ==>")
        try:
            test_out=open(out_file,"w")
            break
        except OSError:
            print("Could not write to that out file. Try another file name.")
        except ValueError:
            print("Could not write to that out file. Try another file name.")
    test_out.close()
    return out_file
#############################################################

while True:
    choice=main_menu()
    print()
    #Itterating if the user chose Grayscale
    if choice=="1":
        #Opening the in file and the out file
        in_file=open(get_file("grayscale"))
        out_filed=open(out_file(),"w")
        #Itterating through the libes if the file
        gray_scale()

    #Itterating if the user chose Vintage
    elif choice=="2":
        #opening the in file and the out file
        in_file=open(get_file("vintage"))
        out_filed=open(out_file(),"w")
        #Itterating through the libes if the file
        vintage() 

    #Itterating if the user chose to Quit      
    else:
        break
    print("The task has been completed")

    #Closing Files
    in_file.close()
    out_filed.close()






    
