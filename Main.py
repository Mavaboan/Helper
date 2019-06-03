# Input, specifikt inkomst og forbrug

inkomst = int(input("Hvor meget tjener du om måneden efter skat?"))

husleje = int(input("Hvor meget bruger du på husleje/betaling på dit hus?"))

mad = int(input("Hvor meget bruger du på mad om måneden?"))

underholdning = int(input("Hvor meget bruger du på underholdning om måneden?"))

tøj = int(input("Hvor meget bruger du på tøj om måneden?"))

opsparing = int(input("Hvor meget bruger du på din opsparing om måneden?"))

forsikring = int(input("Hvor meget bruger du på forsikringer om måneden?"))

transport = int(input("Hvor meget bruger du på transport om måneden?"))

andet = int(input("Hvor meget bruger du på andre ting om måneden?"))

# Sammenligner inkomst med forbrug
if (int(husleje) > (int(inkomst) * float(0.35))):
    print("Du bruger mange penge på dit hus, overvej at finde et billigere sted at bo")

if (mad > (inkomst * 0.20)):
    print("Du bruger mange penge på mad, overvej at bruge mindre")

if (underholdning > (inkomst * 0.1)):
    print("Du bruger mange penge på underholdning, overvej at bruge mindre")

if (tøj > (inkomst * 0.15)):
    print("Du bruger mange penge på tøj, overvej at bruge mindre")

if (opsparing > (inkomst * 0.15)):
    print("Du sender mange penge til din opsaring, du kan sagtens sende minder uden at have problemer.")

if (forsikring > (inkomst * 0.20)):
    print("Du bruger mange penge på din forsikring, prøv at se om du kan finde billigere forsikringer")

if (transport > (inkomst * 0.15)):
    print("Du bruger mange penge på transport, overvej at cykle eller finde en anden måde at få billigere transport")

if (andet > (inkomst * 0.2)):
    print("Du bruger mange penge på diverse andre ting, overvej at nedskærre dit forbrug")
