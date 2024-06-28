#โปรแกรมหาพื้นที่สามเหลี่ยม
def Triangle(base, height):
    area = 1/2*base*height
    #print("พื้นที่สามเหลี่ยม %d" % area)
    return area 

b = int(input("รับค่าฐาน "))
h = int(input("รับค่าสูง "))
print("พื้นที่สามเหลี่ยม %d" % Triangle(2,3))
Triangle(5,10)
Triangle(2,3)






