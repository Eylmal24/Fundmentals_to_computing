# Malachi 
# Milton-Brewer
# Date: 03/20/2022


def fahrenToCel(fahren):
    result = (fahren - 32) * (5.0 / 9.0);
    return result

def fahrenToCelList(fahrenList):
    for i in range(len(fahrenList)):
        fahren = fahrenList[i]
        celsius = (fahren - 32) * (5.0 / 9.0)
        fahrenList[i] = round(celsius,2)


def main():
    fval = float(input("Please enter the temperature in Fahrenheite: "))  
    cval = fahrenToCel(fval)
    print("Equivalent temperature in Celcius is {0:0.2f} ".format(cval))
    
    fahrenheiteList = []
    for i in range(5):
        fahren = float(input("Enter temperature in Fahrenheit: "))
        fahrenheiteList.append(fahren)

    fahrenToCelList(fahrenheiteList)
    print("The converted temperature list")
    print(fahrenheiteList)
main()
