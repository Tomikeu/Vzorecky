#Přivítaní 
print("Vítejte v aplikaci pro výpočty.")

v = input("1. Klasická kalkulačka\n2. Kalkulačka na výpočet obsahu...")

#Kalkulačka
if v == "1." or v == "1" or v == "Klasická kalkulačka" or v == "Klasicka kalkulacka":
    x = input("Napiš číslo X\n")
    y = input("Napiš číslo Y\n")
    z = input("Vyber znaménko\n1. Sčítání\n2. Odečítání\n3. Násobení\n4. Dělení\n5. Mocnina\n6. Odmocnina\n")

    x = (int(x))
    y = (int(y))

#Sčítání
    if z == "Sčítání" or "1." or "1. Sčítání" or "1" or "scitani":
        m = (x + y)
        m = (str(m))
        print("Výsledek je " + m)
#Odečítání
    elif z == "Odečítání" or "2." or "2. Odečítání" or "2" or "odecitani":
        m = (x - y)
        m = (str(m))
        print("Výsledek je " + m)
#Násobení
    elif z == "Násobení" or "3." or "3. Násobení" or "3" or "nasobeni":
        m = (x * y)
        m = (str(m))
        print("Výsledek je " + m)
#Dělení
    elif z == "Dělení" or "4." or "4. Dělení" or "4" or "deleni":
        if y == 0:
            print("y nesmí být 0")
        else:
            m = (x / y)
            m = (str(m))
            print("Výsledek je" + m)
#Mocnina
    elif z == "Mocnina" or "5." or "5. Mocnina" or "5" or "mocnina":
        m = (x ** y)
        m = (str(m))
        print("Výsledek je " + m)
#Odmocnina
    elif z == "Odmocnina" or "6." or "6. Odmocnina" or "6" or "odmocnina":
        m = (x * 1 / y)
        m = (str(m))
        print("Výsledek je " + m)

#Kalkulačna na výpočet obsahu atd..
elif v == "2." or v == "2" or v == "Kalkulačka na výpočet obsahu..." or v == "Kalkulacka na vypocet obsahu..." or v == "Kalkulačka na výpočet obsahu" or v == "Kalkulacka na vypocet obsahu":

    k = input("1. Obsah kruhu\n2. Obsah obdelníku\n3. Obvod obdelníku\n4. Objem kvadru\n")

#Obsah kruku
    if k == "1" or k == "1." or k == "obsah kruhu":
        a = input("Napiš číslo r\n")

        a = int(a)

        if a>0:
            v = (3.14 * a**2)
            v = str(v)
            c = print("Výsledek je " + v)
        else:
            print("Něco je špatně.")

#Obsah obdelníku
    elif k == "2" or k == "2." or k == "obsah obdelníku" or k == "obsah obdelniku":
    
        a = input("Délka strany a\n")
        b = input("Délka strany b\n")

        a = int(a)
        b = int(b)

        if a>0 and b>0:
            v = (a * b)
            v = str(v)
            c = print("Výsledek je " + v)
        else:
            print("Něco je špatně.")

#Obvod obdelníku
    elif k == "3" or k == "3." or k == "obvod obdelníku" or k == "obvod obdelniku":
        a = input("Délka strany a\n")
        b = input("Délka strany b\n")

        a = int(a)
        b = int(b)

        if a>0 and b>0:
            v = (2 * (a + b))
            v = str(v)
            c = print("Výsledek je " + v)
        else:
            print("Něco je špatně.")

#Objem kvádru
    elif k == "4" or k == "4." or k == "objem kvadru":
        a = input("Napiš číslo a\n")
        b = input("Napiš číslo b\n")
        c = input("Napiš číslo c\n")

        a = int(a)
        b = int(b)
        c = int(c)

        if a and b and c>0:
            v = (a * b * c)
            v = str(v)
            c = print("Výsledek je " + v)
        else:
            print("Něco je špatně.")
    else:
        print("Něco je špatně.")
else:
    print("Něco je špatně.")