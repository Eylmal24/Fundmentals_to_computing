# Malachi
# Milton-Brewer
# Date: 03/10/2022 

def main():
    FileName = input ("Enter the input file name: ")
    
    inFile = open(FileName, "r")

    outfileName = input("Enter the output file name: ")

    outfile = open(outfileName, "w")
    
    for line in inFile:
        information = line.split(" ")
        firstName = information[0]
        gpa = information[1]
        average = 0
        count = 0
        for x in information[1::]:
            count = count + 1
            average = average +int(x)
        average = average / count
        score = average
        print(firstName , score, file=outfile)
    
    inFile.close()
    outfile.close()
    print(outfileName, "has been written in, good bye.")
main()
