#ALGORITHM FROM http://www.algorytm.org/algorytmy-arytmetyczne/zamiana-z-i-na-system-rzymski.html
#Roman numbers table

convertedNumber = list()
def converToRomanNumbers(number):
    romanNumbers = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }
    if(len(str(number))>5):
        print("To large number")
        return 0
    for key in romanNumbers.keys():
        if(number>=key):
            convertedNumber.append(romanNumbers[key])            
            converToRomanNumbers(number-key)
            break
print("Podaj liczbe arabska, max 5 cyfr w liczbie")
number = input()
converToRomanNumbers(int(number))
print(''.join(convertedNumber))
