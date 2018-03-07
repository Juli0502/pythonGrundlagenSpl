print("Taschenrechner")
zahl1 = input("Bitte die erste Zahl eingeben: ")
zahl2 = input("Bitte die zweite Zahl eingeben:")
summe = int (zahl1) + int (zahl2)

operation = input("+,-,*,/")

if(operation == "+"):
  summe = zahl1 + zahl2
  print("Summe = ", summe)

if (operation == "-"):
  differenz = zahl1 - zahl2
  print("Differenz = ", differenz)
  
if (operation == "*"):
  produkt = zahl1 * zahl2
  print("Produkt = ", produkt)
  
if (operation == ":"):
  quotient =  zahl1 / zahl2
  print("Qutient = ", quotient)