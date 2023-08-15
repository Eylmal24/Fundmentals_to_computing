def discount_percentage(Quantity):
    discount = 0
    if Quantity >= 100:
        discount = 50  
    elif Quantity >= 50:
        discount = 40
    elif Quantity >= 20:
        discount = 30
    elif Quantity >= 10:
        discount = 20
    else:
        discount = 0

    return discount


def main():
    
    try:
        Quantity = int (input ('what is the Quantity of packages: '))
        percent = discount_percentage(Quantity)
        amount = (Quantity * 99)
        discount_amount = (amount * percent/100)
        total_amount = (amount - discount_amount)
        if Quantity < 0:
            print("error")
        else:
            print ("discount", percent, "discount amount", discount_amount, "total", total_amount)
     

    # If the input is a non-numerical string then display an error message
    except ValueError as err:
        print ('One of you score is non-numerical')
        print ('Please try again with correct scotes')
    # Catch unexpected errors
    #except:
     #   print ('Unknown error')
