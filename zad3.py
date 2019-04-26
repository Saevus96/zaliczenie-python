#imports
from operator import itemgetter

#function to count letters in user Text
def countLetters(userText):   
   
   #alphabet container
   char = dict()
   for i in range(32,127):    
      char[chr(i)] = 0
   
   #read user text and if add to container if character exists in alphabet container
   for key in char.keys():
      counter =0     
      for j in range(0, len(userText)):
         if(key == userText[j]):
            counter = counter+1
         char[key] = counter
   
   #Sort values in alphabet container by highest value
   char = dict(sorted(char.items(), key=itemgetter(1), reverse=True))
   afterSort = dict()
  
   #cut values equals 0
   for key in char.keys():
      if(char[key] > 1):
         afterSort[key] = char[key]
   return afterSort

#input text
print("Podaj zdanie dla obliczenia znaków: ")
userText = input()
print(countLetters(userText))