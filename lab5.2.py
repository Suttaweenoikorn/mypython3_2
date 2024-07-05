def abc(num):
    sum = 0
    for i in range(num):
        price = int(input("รับราคาสินค้า %d " % (i+1)))
        sum += price
    return sum

def tax(sum):
    vat = sum*7/100
    return vat

def total(a, b, c):
    t = (a - c)+b
    return t

def disc(c):
    c = sum*5/100
    return c

num = int(input("จำนวนสินค้า "))
sum = abc(num)
print("ราคารวม %.2f" % sum)
print("ภาษี %.2f" % disc(sum))
print("รวมเป็นเงินทั้งสิ้น %.2f" % total(sum, tax(sum), disc(sum)))
