def secnd(n,sec):
    sec = n * 365 * 24 * 60 * 60
    return sec

def mints(n,mint):
    mint = n * 365 * 24 * 60
    return mint

def hours(n,hour):
    hour = n * 365 * 24
    return hour

def days(n,day):
    day = n * 365
    return day

def weeks(n,week):
    week = n * 365 / 7 
    return week

def months(n,month):
    month = n * 12
    return month
month = 0
week = 0
day= 0
hour = 0
week = 0
mint = 0
sec= 0
while True:
    try:
        n = int(input("Enter your Age :"))
    except ValueError:
        print("Please Enter Your Age in Numbers")
        continue
    option= int(input( "1. Months /n2. Weeks /n3. Days /n4. Hours/n5. minutes /n6. Seconds /n7. Exit/n Type Only 1/2/3/4/5/6/7 :"))

    if option == 1 :
        c= months(n,month)
        print(c)

    if option == 2 :
        c= weeks(n,week)
        print(c)

    if option == 3 :
        c= days(n,day)
        print(c)
    
    if option == 4 :
        c= hours(n,hour)
        print(c)

    if option == 5 :
        c= mints(n,mint)
        print(c)

    if option == 6 :
        c= secnd(n,sec)
        print(c)

    if option < 1 or option > 7:
        print("Invalid! Type Only 1/2/3/4/5/6")

    if option == 7:
        print("GoodBye ..!")
        break

            