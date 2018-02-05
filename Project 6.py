#####################################################
#####################################################
##  CS 101
##  Program 6
##  Dylan Pembrook
##  dmpfzf@mail.umkc.edu
##
##  Problem: Stock Market
##  
##  Algorithm: Ask the user the name of the stock to do research on or to quit
##  If the name is invalid, inform the user and prompt a correct response
##  Ask the user the stock purchase date
##  If the date is invalid, inform the user and prompt a correct date
##  Ask the user the stock sell date
##  If the date is invalid, inform the user and prompt a correct date
##  If the purchase date is greater than the sell date warn the user and prompt for both dates again
##  Ask the user how many stocks to purchase on the purchase date, number must be bigger than 0
##  If the start or stop date doesn’t exist, inform the user and restart the questions
##  Print out the stock, date, shares, price, total price for both the purchase and sell date
## 
##  Error handling: if the stock name is invalid
##  if the start date is invalid
##  if the stop date is invalid
##  if the start date is after the sell date
##  if the number of stocks is zero or less
####################################################
####################################################

def stock_name():
    """Gets the name of the stock the user wishes to use"""
    stock_loop=True
    while stock_loop:
        name_of_stock=input("Enter the name of the stock purchased. Enter quit to exit ==>")
        #Checking if the input was an empty string or QUIT
        if name_of_stock.upper()=="QUIT":
            return name_of_stock
        elif name_of_stock=="":
            print("Could not find stock. Please try another")
            print()
        else:
            #Making sure that the user input is an actual stock name
            in_file=open("stocklist.csv")
            csv_file=csv.reader(in_file)
            count=0
            for line in csv_file:
                if name_of_stock.upper() in line[0]:
                    stock_loop=False
                    count=1
                    break
            #if the stock is not on the stocklist
            if count==0:
                print("Could not find stock. Please try another")
                print()
    in_file.close()
    return name_of_stock.upper()

def stop_date():
    """Asks the user what the selling date of their stock will be"""
    while True:
        sell_date=input("Enter the date you sold the stock ==>")
        #Attempts to convert the sell date into a numerical value that is comparable
        try:
            sell_date=datetime.datetime.strptime(sell_date,"%m/%d/%Y")
            break
        except ValueError:
            print("You entered an incorrect date, please re-enter in the format MM/DD/YYYY")
    return sell_date
        
    

def start_date():
    """Asks the user what the purchase date of their stock will be"""
    while True:
        purchase_date=input("Enter the stock purchase date ==>")
        #Attempts to convert the purchase date into a numerical value that is comparable
        try:
            purchase_date=datetime.datetime.strptime(purchase_date,"%m/%d/%Y")
            break
        except ValueError:
            print("You've entered an incorrect date, please re-enter in the format MM/DD/YYY")
    return purchase_date

def shares():
    """Asks the user how many shares they purchased on the purchase date. Checks if the input
    is a number and if that number is greater than zero"""
    print()
    while True:
        try:
            stock_shares=int(input("How many stocks were purchased on the start date"))
            if stock_shares>0:
                return stock_shares
            else:
                print("You must enter a number greater than zero")
        except ValueError:
            print("You must enter a number")

def table(price_open_dict,price_close_dict,split_number):
    """prints up the table for the stock information"""
    in_file=open("stocklist.csv")
    csv_file=csv.reader(in_file)
    stock_list_dict={}
    for line in csv_file:
        stock_list_dict[line[0]]=line[1]
    #Converting all of the table info into variables for easier formatting
    purchase_dates=purchase_date.strftime("%m/%d/%Y")
    sell_dates=sell_date.strftime("%m/%d/%Y")
    buy_price=float(price_open_dict[purchase_dates])
    sell_price=float(price_close_dict[sell_dates])
    buy_total=share_num*buy_price
    sell_total=float(split_number[sell_dates])*sell_price
    print()
    #Printing up the actual table itself
    print(stock_list_dict[stock],"(",stock.lower(),")Portfolio")
    print("{}{:>12}{:>15}{:>15}{:>15}".format("Action","Date","Shares","Price","Total Price"))
    print("="*63)
    #Printing the buy line
    print("{}{:>16}{:>12}{:>17.2f}{:>15.2f}".format("Buy",purchase_dates,share_num,buy_price,buy_total))
    #Printing the sold line
    print("{}{:>15}{:>12}{:>17.2f}{:>15.2f}".format("Sold",sell_dates,float(split_number[sell_dates])*share_num,sell_price,sell_total))
    print("="*63)
    print("{:>63.2f}".format(sell_total-buy_total))
    print()

def date_check(stock,purchase_date,sell_date):
    """Puts all the dates from the afore mentioned stock into a set
    and checks them to the purchase and sell date"""
    stock+=".csv"
    stock_file=open(stock)
    stock_csv=csv.reader(stock_file)
    date_set=set({})
    #Converting the comparable date into the traditional format
    purchase_date_ordered=purchase_date.strftime("%m/%d/%Y")
    sell_date_ordered=sell_date.strftime("%m/%d/%Y")
    #Adds the dates available for the inputted stock into a set
    for line in stock_csv:
        date_set.add(line[0])
    #Checking to see if the purchase date is in the afore mentioned set
    if purchase_date_ordered not in date_set:
        print("Could not locate the start date of",purchase_date)
        if sell_date_ordered not in date_set:
            print("Could not locate the end date of",sell_date)
    #Checking to see if the sold date is in the afore mentioned set
    elif sell_date_ordered not in date_set:
        print("Could not locate the end date of",sell_date)
    #If both the dates are in the set, the loop breaks and the table can be processed
    #If either date is not in the set, the menu starts over
    else:
        loop_breaker=5
        return loop_breaker

def open_price(stock):
    """Gets a key value pair for date and open price"""
    stock+=".csv"
    stock_file=open(stock)
    price_csv=csv.reader(stock_file)
    price_open_dict={}
    #Places the key of the date and the value of the opening price into
    #A dictionary for formatting in the table
    for line in price_csv:
        price_open_dict[line[0]]=line[1]
    return price_open_dict

def close_price(stock):
    """Gets a key value pair for date and close price"""
    stock+=".csv"
    stock_file=open(stock)
    price_csv=csv.reader(stock_file)
    price_close_dict={}
    #Places the key of the date and the value of the closing price into
    #A dictionary for formatting in the table
    for line in price_csv:
        price_close_dict[line[0]]=line[4]
    return price_close_dict

def split_num(stock):
    """Gets the split number for the stock"""
    stock+=".csv"
    stock_file=open(stock)
    price_csv=csv.reader(stock_file)
    split_val_dict={}
    #Places the key of the date and the value of the split number into a dictionary
    for line in price_csv:
        split_val_dict[line[0]]=line[7]
    return split_val_dict
  

##########################################################

import csv
import datetime
outter_loop=True
while outter_loop:
    inner_loop=True
    loop_breaker=0
    while inner_loop:
        #Gets the stock name from the user
        stock=stock_name()
        if stock.upper()=="QUIT":
            outter_loop=False
            break
        else:
            #Gets the purchase and sell dates from the user and verifys them
            purchase_date=start_date()
            sell_date=stop_date()
            if purchase_date>sell_date:
                print("Could not locate the start date of",purchase_date)
                print("Could not locate the end date of",sell_date)
                print()
            else:
                #Gets the number of shares and verifys the dates to the stock
                inner_loop=False
                share_num=shares()
                loop_breaker=date_check(stock,purchase_date,sell_date)
                
    if loop_breaker==5:
        #Getting the open price, close price, number split and formats all the information into a table
        price_open_dict=open_price(stock)
        price_close_dict=close_price(stock)
        split_number=split_num(stock)
        table(price_open_dict,price_close_dict,split_number)

########################################


