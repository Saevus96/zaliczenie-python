#imports
import re

#function to clean cpp file
def cleanCpp(cppFileNameRead, cppFileNameWrite):
    fileRead = open(cppFileNameRead, "r")
    fileWrite = open(cppFileNameWrite, "w")
    #declare tags to clean /* *\ // and multiline comments clean
    x = re.compile(r"(/\*.*?\*/|//[^\r\n]*$)",
        re.DOTALL | re.MULTILINE
    )
    #read text from file
    text =""
    for line in fileRead:
        text += line

    #convert text from file and write the converted text to new file
    result = x.sub("", text)
    fileWrite.write(result)
    fileRead.close()
    fileWrite.close()

print("podaj nazwe pliku cpp do czyszczenia komentarzy")
cppFileNameRead = input()
print("podaj nazwe pliku cpp do ktorego mam zapisac wyczyszczony kod")
cppFileNameWrite = input()

cleanCpp(cppFileNameRead, cppFileNameWrite)