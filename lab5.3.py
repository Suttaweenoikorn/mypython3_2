def fa(c):
    fa = (9/5)*c+32
    return fa

def ke(c):
    ke = c+273.15
    return ke

Cel = int(input("Celcius : "))
print("fa : %.2f" % fa(Cel))
print("ke : %.2f" % ke(Cel))

