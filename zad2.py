#imports
import calendar

#List of Months
monthList = list()
monthList ={"styczeń": 1, "luty": 2, "marzec": 3, "kwiecień": 4, "maj": 5, "czerwiec": 6,
        "lipiec": 7, "sierpień": 8, "wrzesień": 9, "październik": 10, "listopad": 11, "grudzien": 12}


print("podaj miesiąc po polsku")
m = input()
print("podaj rok")
y = input()

#search month in list 
for key in monthList.keys():
    if(key == m):
        m = monthList[key]

print(calendar.month(int(y),m))