def read_data (file_name):
    #Function Name: read data
    #Description: read a set of numbers from an input file
    #Paramater:file_name - name of the input file
    #Returns list of numbers
    inputfile = open(file_name, 'r' )
    list_of_numbers = []
    for line in inputfile:
        num = int(line)
        list_of_numbers.append(num)
    inputfile.close()
    return list_of_numbers 
def compute_sum (list_of_numbers):
    #Function Name: compute sum
    #Description: calculate sums of a list
    #Paramater:list_of_numbers
    #Returns Sum
    Sum = sum(list_of_numbers)
    return Sum

def compute_mean (list_of_numbers):
    #Function Name: compute mean
    #Description: calculate mean of a list
    #Paramater:compute_sum
    #Returns mean
    Sum = compute_sum (list_of_numbers)
    Length = len(list_of_numbers)
    mean = Sum/Length
    return mean

def compute_sd (list_of_numbers):
    import math
    mean = compute_mean (list_of_numbers)
    Sum = 0
    for line in list_of_numbers:
        num = int(line)
        deviation = mean - num
        square = deviation*deviation
    size = len(list_of_numbers)
    result = Sum/(size-1)
    value = math.sqrt(result)
    return value
