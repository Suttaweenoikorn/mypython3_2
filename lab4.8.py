def bmi(kg, cm):
    bmi = kg/(cm/100)**2
    return bmi

def compare(bmi):
    if bmi < 18.50:
        print("น้ำหนักน้อย")
    elif bmi >= 18.50 and bmi<= 22.90:
        print("ปกติ")
    elif bmi >= 23 and bmi <= 24.90:
        print("ท้วม")
    elif bmi >= 25 and bmi <= 29.90:
        print("อ้วน")
    else:
        print("อ้วนมาก")
        
   
    
kg = int(input("kg = "))
cm = int(input("cm = " ))
print("ค่า bmi = %.2f" % bmi(kg, cm))
compare(bmi(kg, cm))
