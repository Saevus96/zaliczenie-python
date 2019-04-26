#imports
import math

#function to sum all numbers and check her primary
def countNumbers(x,y):

    #function to check primary
    def isPrime(n):
        if(n<=1):
            return 0
        if(n == 2):
            return 1
        for i in range(2, n):
            if(n % i == 0):
                return 0
        return 1

    #open file with write access
    fileout = open("file.out", "w")

    #loop to print in file numbers, where sum of numbers is primary
    print("print values")
    for i in range(int(x), int(y)): 
        sum =0
        iLength =str(i)
        for j in range(0, (len(iLength))):
            sum = sum + int(iLength[j])
        if(isPrime(sum)):
            print(str(i)+" "+str(sum))
            fileout.write(str(i)+"\n")
    fileout.close()

#start and end of range
print("add values")
x = input()
y = input()

countNumbers(x,y)