## if user press s then April->march->february 
## if user press d then April->may->june->july

from datetime import datetime
import calendar

def clearScreen():
    import Student_login as s
    s.clearScreen()

def getCurrYear():
    return datetime.now().year

def getCurrMonth():
    return datetime.now().month

def prepareCal(y , m):
    print( calendar.month(y , m) )

def main():
    clearScreen()
    year = getCurrYear()
    month = getCurrMonth()
    prepareCal(year , month)

    while True:
        input_command = input("Enter 's' or 'd' \n")
        if input_command == 's':
            month = month - 1

            if month == 0:
                month = 12
                year = year-1

            clearScreen()
            prepareCal(year , month)
            
        elif input_command == 'd':
            month = month+1

            if month == 13:
                month = 1
                year = year+1

            clearScreen()
            prepareCal(year , month)
        else:
            clearScreen()
            prepareCal(year , month)


if __name__ == '__main__':
    main()