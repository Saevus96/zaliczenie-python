#imports
from datetime import datetime

#function to count days between two dates
def countDays(date1, date2):
    date1 = datetime.strptime(date1, "%d.%m.%Y")
    date2 = datetime.strptime(date2, "%d.%m.%Y")
    return abs((date2 - date1).days)

# Add first date
print("Podaj pierwsza date")
date1 = input()
print("Podaj druga date")
# Add second date
date2 = input()

print(countDays(date1, date2))