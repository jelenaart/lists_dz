abc='proGrammeriMine'
abcc=list(abc)
print(abc,abcc)
while True:
    print()
    print("1-Function len")
    print("2-Function capitalize")
    print("3-Function isalpha")
    print("4-Function upper")
    print("5-Function lower")
    print("6-Function isspace")
    print("7-Function swapcase")
    print("8-Function split")
    print("9-Function isalnum")
    print("10-Function replace")
    valik = int(input(""))
    print()
    if valik == 1:
        print("Vsego ",len(abcc)," symvolov") # Dlina stroki
    elif valik == 2:
        print(abc.capitalize()) # Delaet pervyu bukvu bolshoi a drugie malenkie
    elif valik == 3:
        if abc.isalpha()==True: # Sostoit li stroka iz bukv
            print("Estˇ bukvi")
        else:
            print("Nety bukv")
    elif valik == 4:
        print(abc.upper()) # S zaglavnoi
    elif valik == 5:
        print(abc.lower()) #S malenkoi
    elif valik == 6:
        if abc.isspace()==True: # proverka na probeli
            print("V stroke estˇ probeli ")
        else:
            print("V stroke nety probelov")
    elif valik == 7:
        print(abc.swapcase())# Perevodit bolshie bukvi v malenkie a malenkie v bolshie
    elif valik == 8:
        print(abc.split()) # Razdelyaet slova mejdu soboi
    elif valik == 9:
        if abc.isalnum()==True: # Sostoit li stroka iz bukv ili cifr
            print("Sostoit iz bukv")
        else:
            print("Sostoit iz bukv i cifr")
    elif valik == 10:
        print(abc.replace("proGrammeriMine","Olen programmeerija")) # Zamena slova
    else:
        print("Error!") 
