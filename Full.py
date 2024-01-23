#Přivítaní 
print("Vítejte v aplikaci pro výpočty.")

k = input("1. Obsah kruhu\n2. Obsah obdelníku\n3. Obvod obdelníku\n4. Objem kvadru\n")

if k == "1" or k == "1." or k == "obsah kruhu":
    a = input("Napiš číslo r\n")

    a = int(a)

    if a>0:
        v = (3.14 * a**2)
        v = str(v)
        c = print("Výsledek je " + v)
    else:
        print("Něco je špatně.")

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