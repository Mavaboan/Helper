# Input, specifikt hvkellige forbrug

inkomst = int(input("Hvor meget tjener du om måneden efter skat?"))

husleje = int(input("Hvor meget bruger du på husleje/betaling på dit hus?"))

mad = int(input("Hvor meget bruger du på mad om måneden?"))

utility = int(input("Hvor meget bruger du på el, vand, internet etc om måneden?"))

underholdning = int(input("Hvor meget bruger du på underholdning om måneden?"))

tøj = int(input("Hvor meget bruger du på tøj om måneden?"))

opsparing = int(input("Hvor meget bruger du på din opsparing om måneden?"))

forsikring = int(input("Hvor meget bruger du på forsikringer om måneden?"))

transport = int(input("Hvor meget bruger du på transport om måneden?"))

andet = int(input("Hvor meget bruger du på andre ting om måneden?"))

# Sammenligner inkomst med forbrug
if (int(husleje) > (int(inkomst) * float(0.35))):
    print("Du bruger mange penge på dit hus, overvej at finde et billigere sted at bo")

if
