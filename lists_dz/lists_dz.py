abc='proGrammeriMine'
abcc=list(abc)
print(abc,abcc)
while True:
    print()
    print("1-функция len")
    print("2-функция capitalize")
    print("3-функция isalpha")
    print("4-функция upper")
    print("5-функция lower")
    print("6-функция isspace")
    print("7-функция swapcase")
    print("8-функция split")
    print("9-функция isalnum")
    print("10-функция replace")
    valik = int(input(""))
    print()
    if valik == 1:
        print("Всего ",len(abcc)," симболов") #Выводит длину строки
    elif valik == 2:
        print(abc.capitalize()) #Делает первую букву большой, а другие маленькие
    elif valik == 3:
        if abc.isalpha()==True: #Состоит ли строка из букв
            print("Есть буквы")
        else:
            print("Нету букв")
    elif valik == 4:
        print(abc.upper()) #Заглавные буквы
    elif valik == 5:
        print(abc.lower()) #Маленькие буквы
    elif valik == 6:
        if abc.isspace()==True: #проверка на пробелы
            print("В строке присутствуют пробелы")
        else:
            print("В строке нет пробелов")
    elif valik == 7:
        print(abc.swapcase())# Переводит символы нижнего регистра в верхний, а верхнего – в нижний
    elif valik == 8:
        print(abc.split()) # Pаздвляет слова между собой
    elif valik == 9:
        if abc.isalnum()==True: # Состоит ли строка из цифр или букв
            print("Состоит из букв")
        else:
            print("Состоит из букв и цифр")
    elif valik == 10:
        print(abc.replace("proGrammeriMine","Olen programmeerija")) # Замена слова на другое
    else:
        print("Ошибка!") 
