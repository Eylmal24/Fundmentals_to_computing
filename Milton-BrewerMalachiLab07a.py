# Malachi
# Milton-Brewer
# Date: 03/10/2022 

def main():
    print("This program creates a file of emails and usernames from a file of names")

    infile = open("in.txt", "r")

    outfileName = input("What file should the usernames go in? ")
    
    outfile = open(outfileName, "w")

    for line in infile:
        first, last = line.split()
        email = (first + "." + last).lower() + "@ucdenver.edu" 
        uname = (last[:]+first[0]).lower()
        print(email + " " + uname, file=outfile)
    infile.close() 
    outfile.close()
    print("Emails and usernames have been written to", outfileName)
main()
