def dateConvert(date):
    dlist = date.split("/")
    monthList = ["January", "Feburary", "March", "April", "May", "June", "July",
                  "August", "September", "October", "Novermber", "December"]
    month, day, year = int(dlist[0]), int(dlist[1]), int(dlist[2])
    dateString = str(monthList[month - 1]) + " " + str(day) + "," +str(year)
    return dateString


def main():
    date = input("Enter date :")
    print(dateConvert(date))

main()

