import sys

operacije = ["+","-","*","/"]
operacija = input("Unesite operaciju: ")


if len(operacija) < 1:
    print("Greska: Niste uneli operaciju")
    sys.exit()
elif len(operacija) > 1:
    print("Greska: Uneli ste vise operacija")
    sys.exit()
if not operacija in operacije:
    print("Greska: Uneli ste pogresnu operaciju")
    sys.exit()

if operacija == operacije[0]:
    sabirak = float(input("Unesite prvi sabirak: "))
    sabirak2 = float(input("Unesite drugi sabirak: "))
    zbir = sabirak + sabirak2
    print("Zbir je ", zbir)


if operacija == operacije[1]:
    umanjenik = float(input("Unesite umanjenik: "))
    umanjilac = float(input("Unesite umanjilac: "))
    razlika = umanjenik - umanjilac
    print("Razlika je ", razlika)

if operacija == operacije[2]:
    prviCinilac = float(input("Unesite prvi cinilac: "))
    drugiCinilac = float(input("Unesite drugi cinilac: "))
    proizvod = prviCinilac * drugiCinilac
    print("Proizvod je ", proizvod)

if operacija == operacije[3]:
    deljenik = float(input("Unesite deljenik: "))
    delilac = float(input("Unesite delilac: "))
    kolicnik = deljenik / delilac
    print("Kolicnik je ", kolicnik)   
