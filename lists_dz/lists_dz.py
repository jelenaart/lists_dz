abc='proGrammeriMine'
abcc=list(abc)
print(abc,abcc)
while True:
    print()
    print("1-������� len")
    print("2-������� capitalize")
    print("3-������� isalpha")
    print("4-������� upper")
    print("5-������� lower")
    print("6-������� isspace")
    print("7-������� swapcase")
    print("8-������� split")
    print("9-������� isalnum")
    print("10-������� replace")
    valik = int(input(""))
    print()
    if valik == 1:
        print("����� ",len(abcc)," ��������") #������� ����� ������
    elif valik == 2:
        print(abc.capitalize()) #������ ������ ����� �������, � ������ ���������
    elif valik == 3:
        if abc.isalpha()==True: #������� �� ������ �� ����
            print("���� �����")
        else:
            print("���� ����")
    elif valik == 4:
        print(abc.upper()) #��������� �����
    elif valik == 5:
        print(abc.lower()) #��������� �����
    elif valik == 6:
        if abc.isspace()==True: #�������� �� �������
            print("� ������ ������������ �������")
        else:
            print("� ������ ��� ��������")
    elif valik == 7:
        print(abc.swapcase())# ��������� ������� ������� �������� � �������, � �������� � � ������
    elif valik == 8:
        print(abc.split()) # P�������� ����� ����� �����
    elif valik == 9:
        if abc.isalnum()==True: # ������� �� ������ �� ���� ��� ����
            print("������� �� ����")
        else:
            print("������� �� ���� � ����")
    elif valik == 10:
        print(abc.replace("proGrammeriMine","Olen programmeerija")) # ������ ����� �� ������
    else:
        print("������!") 
