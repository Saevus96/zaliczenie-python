#imports
import re

print("Podaj nazwe pliku, który mam wyczyścić")
fileNameOpen = input()
print("Podaj nazwę pliku do którego mam zapisać oczyszczony tekst")
fileNameRead = input()

htmlFileRead = open(fileNameOpen, "r")
htmlFileWrite = open(fileNameRead, "w")

#declare tags to clean <> </>
x = re.compile('<.*?>') 

#function to read line in file and clean from tags
for line in htmlFileRead:
    result = x.sub("", line)
    htmlFileWrite.write(result) 

#close files
htmlFileWrite.close()
htmlFileRead.close()