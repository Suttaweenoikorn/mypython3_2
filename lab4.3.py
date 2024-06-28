#ชนิดข้อมูล dictionary
x = {"name": "Suttawee Noikorn", "age":17, "wt":63, "h":173}
print(x)
print("สวัสดี %s" % x["name"])
print("พ.ศ.เกิด %d อายุ %d" % (2567-x["age"], x["age"]))
print("น้ำหนัก %d ส่วนสูง %d" % (x["wt"], x["h"]))

      