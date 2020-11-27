### Room 1 ###
### Benjamin Thiel ###
###  Entschlüsseln der Aufgabe ###
    
# gegeben ist ein String "SLYLHEQLQNTLWDNWDCRBWLNFNCLYNFQQCDPNTBIDEYOVLTCDRNLQWGTLYERQWLYCLTQN" 
# und Verschlüsselungsfunktion
# Schlüssel müssen durch kleine Rätsel gefunden werden (Wortspiele o.ä.) S1(7919) und S2(7907)
# Aufgabe: Schreiben Sie einen Code, um den Geheimtext zu entschlüsseln












def encrypt (x, a, b): 

    # Verschlüsseln nach der Fomel: Geheimtext  = Klartext  x   Schlüssel 1 + Schlüssel 2
    #                                   y       =   x       *   a           + b

    y = []
    y_str = ""
    x = x.replace(" ","")   # zuerst müssen die Leerzeichen entfernt werden
    x = x.upper()           # alles in Großbuchstaben umwandeln
    
    for i in x:             # Iteration über K
        p = (ord(i) - 65)          # Umwandeln der einzelnen Buchstaben in Zahlen anhand der Unicode-Werte (64 < x < 91)
        q = ((((p * a ) + b )  % 26) + 65)  # Hier wird gerechnet im Zahlenkörper 26 und +65, um im Unicode zu bleiben
        q = chr(q)              # Zurückwandlung in Buchstaben   
        y.append(q)             # Anhängen an Liste y
    return ( y_str.join(y))     # Liste y wird in str umgewandelt und zurückgegeben 



def decrypt (y, a, b):

    x = []
    x_str = ""
    y = y.upper()   #Sollte eigentich nicht vorkommen, aber falls lowercase eingegeben wird

    for i in y:
        p = (ord(i) - 65)
        # Hier muss gerechnet werden. Es fehlt das multiplikativ inverse Element
        lk = euklid(a, 26)
        mie = lk[1]
        if mie < 0:
            aie = abs(mie)  #additiv inverse element
            mie = 0
            while ((mie + aie) % 26) != 0:
                mie += 1
        elif mie == 0:
            print("Schlüssel 1 ist invalid, da nicht teilerfremd")
            return 0

        q = ((mie * (p - b)) % 26) + 65
        q = chr(q)
        x.append(q)
    return (x_str.join(x))

 
def euklid(a, b):         # Erweiterter Euklidscher Algorithmus zur Ermittlung der Linearkombinationen
    u, v, s, t = 1, 0, 0, 1
    while b!=0:
        q = a // b
        a, b = b, a - q * b
        u, s = s, u - q * s
        v, t = t, v - q * t
    return (a, u, v) 

again = "n"
choose = ""

while choose != "1" or choose != "2":
    choose = input("\nWas wollen Sie machen? \nVerschlüsseln (1)\nEntschlüsseln (2) \n")

    if choose == "1":
        Klartext = str(input("\nBitte einen Text zum verschlüsseln eingeben (keine Umlaute / Sonderzeichen) :")) # Dieser Text soll schlussendlich verschlüsselt werden
        
        S1 = int(input("Und jetzt der Schlüssel 1: "))     #das ist verbesserungswürdig!
        lk = euklid(S1, 26)
        while (lk[0]) != 1:
            S1 = int(input("Schlüssel 1 ist invalid, da nicht teilerfremd. Bitte neu eingeben: "))
            lk = euklid(S1, 26)

        S2 = int(input("Und nun der Schlüssel 2  : "))

        G = encrypt(Klartext, S1, S2)
        print ("Und hier ist der Geheimtext : ", G, "\n")
        again = input("Nochmal? ja (j) oder nein (n): ")

    elif choose == "2":
        Geheimtext = str(input("\nBitte einen Text zum entschlüsseln eingeben (Großbuchstaben und ohne Sonderzeichen) :")) # Dieser Text soll schlussendlich entschlüsselt werden
        S1 = int(input("Und jetzt der Schlüssel 1: "))
        S2 = int(input("Und nun der Schlüssel 2  : "))

        K = decrypt(Geheimtext, S1, S2)
        if K == 0:
            again = input("Nochmal? ja (j) oder nein (n): ")
            continue
        print ("Und hier ist der Klartext : ", K, "\n")
        again = input("Nochmal? ja (j) oder nein (n): ")

    else:
        while (choose != "1") and (choose != "2"): #hier muss auch optimiert werden
            choose = input("\nFalsche Eingabe. \nVerschlüsseln (1)\noder Entschlüsseln (2)?: ")
        continue
    if again == "n":
        break