#exception handling 
#code to open and read file
#should handle the 'file not found error'

import sys
#variables
name=""
filename=input("Please enter file name (C:\\Users\\User\\source\\repos):")
READ='r'
#open and read
try:
    with open (filename,mode=READ) as file:
        print(file.read())

except FileNotFoundError:
    print(sys.exc_info()[0])  #you can throw an exception like this if you do not know
                              #the error


                              #or you can simply TEST the programme,find the name
                              #of the error  and place it after the except line






       

      


