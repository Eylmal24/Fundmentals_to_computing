#
# Name: Echo Trimble Rosy Lwin Malachi Milton-Brewer 
# Class: CSCI 1411-00X
# Due Date:
# Description: 
# Status:


def main():
     # first, ask the user for their first and last names
    firstName = input("Enter your first name ")
    lastName = input("Enter your last name ")

       # now ask them for the temperature they wish to convert
    fahren = (int)(input("what is the temperature in Fahreneit? "))

    # next we convert using the standard F to C formula
    celsius = (fahren-32)*(5/9)

       # finally, print out the conversion
    print("Below is the Conversion of 32 degress plus the next 10 degrees")
    print(firstName," ",lastName, "Fahrenheit tempture ", fahren, celsius, "degrees")
    print(firstName," ",lastName, "Fahrenheit tempture  ",fahren +1, (fahren+1-32*(5/9), "degrees"))
    print(firstName," ",lastName, "Fahrenheit tempture  ",fahren +2, (fahren+2-32)*(5/9), "degrees")
    print(firstName," ",lastName, "Fahrenheit tempture  ",fahren +3, (fahren+3-32)*(5/9), "degrees")
    print(firstName," ",lastName, "Fahrenheit tempture  ",fahren +4, (fahren+4-32)*(5/9), "degrees")
    print(firstName," ",lastName, "Fahrenheit tempture  ",fahren +5, (fahren+5-32)*(5/9), "degrees")
    print(firstName," ",lastName, "Fahrenheit tempture  ",fahren +6, (fahren+6-32)*(5/9), "degrees")
    print(firstName," ",lastName, "Fahrenheit tempture  ",fahren +7, (fahren+7-32)*(5/9), "degrees")
    print(firstName," ",lastName, "Fahrenheit tempture  ",fahren +8, (fahren+8-32)*(5/9), "degrees")
    print(firstName," ",lastName, "Fahrenheit tempture  ",fahren +9, (fahren+9-32)*(5/9), "degrees")
    print(firstName," ",lastName, "Fahrenheit tempture  ",fahren +10,(fahren+10-32)*(5/9), "degrees")
