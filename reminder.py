import datetime
from datetime import date

database={}
class reminder:
    def store(key1,value1):  
        database.update({key1:value1})
        print(database)
        return database
    def remind(data1,a): #only get year but not month and day
        year_val=datetime.datetime.now().year
        month_val=datetime.datetime.now().month
        day_val=datetime.datetime.now().day
        st=date(year_val,month_val,day_val)
    #    val=data1[a]
        for x,y in database.items():
            if st==y:
                print(f"It's {st},Happy {y}!!!")   #only prints the recent correct value if there are multiple correct one
            else:
                print(f"It's {st},nothing special but {x} is on {y}")
        
rem1=reminder
while True:
    print('[1] Store Event')
    print('[2] Remind Event')
    x=int(input("Enter your choice: "))
    if x==1:
       a=input("Enter your event: ")
       yr=int(input(f"Enter year for {a}: "))
       mt=int(input(f"Enter month for {a}: "))
       dy=int(input(f"Enter day for {a}: "))
       b=date(yr,mt,dy)
       data1=rem1.store(a,b)
    if x==2:
       rem1.remind(data1,a)
    ask=input("Continue?")
    if ask=='n':
        break
