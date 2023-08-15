"""
Author: Malachi Milton-Brewer
Date: 04/19/22
This program will perform the following tasks:
   1) It will ask user for word - as a string
   
   2) It will count every single word .
   3) The file will ask for a file
   4) the file will be processed and count every time the word was used.
   5) the output will be how many time the word was use or an error if depending on the word
"""
def main():
    inputFileName = input ("please enter the name of the file with names and grades in it: ")
    processFile(inputFileName)
    
    """
    Function Name: main
    Description: Ask the user for a number greater than 2. It will
               use a loop to iterate from 2 to the given number
               and disply all the numbers which are prime. It will
                use is_prime function to check if the number is prime.
                It will also display an error message if the input is
                invalid (see program description)
    Parameter: none
    """

def processFile(FileName):
    """
   Function Name: main
   Description: takes an a file as a peramenter and asks for a word. This word is than checked with
   the file and 
   Parameter: none
   """
    infile = open(FileName,'r')
    line = infile.readline()
    count = 0
    xStr = input("enter word here :")
    while line != "":
        for xStr in line.split(" "):
            count = count + 1
        line = infile.readline()

    else :
        print(xStr, "was found", count, "times"  ) 
  
    # except ValueError as err:
     #   print ('Your score is non-numerical')
      #  print ('Please try again with correct scotes')
