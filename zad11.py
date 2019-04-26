


print("Podaj nazwę pliku z adresem maską i bramką w formacie adres / bramka / maska")
fileName = input()
print("Podaj dla jakiego systemu wygenerować plik konfiguracyjny 1 - Windows, 2 - Linuks, 3 - Cisco")
configType = input()

#check config type compatibility
while (int(configType) >3):
    print("Zły parametr dla pliku configuracyjnego! Podaj jeszcze raz !")
    configType = input()
#open file in and config file
fileIn = open(fileName, "r")
fileOut = open("config.cfg", "w")

#loop to read fileIN and get address mask gate and write config file with specified configType
for line in fileIn:
    address = line.split(" /")[0]
    mask = line.split(" / ")[1]
    gate = line.split(" / ")[2].rstrip()

    if configType == "1":
        fileOut.write("route ADD "+address+" MASK "+ mask + " " +gate+"\n")
    elif configType == "2":
        fileOut.write("route add -net " + address +" netmask "+ mask +" gw " + gate + " dev eth1\n")
    elif configType == "3":
        fileOut.write("Router(config)#ip route " +address+" "+mask+" "+gate+"\n")

fileIn.close()
fileOut.close()
