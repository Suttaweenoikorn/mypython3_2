def showme():
    name = E1.get()
    price = E2.get()
    print(name)
    print(price)


import tkinter as tk
app = tk.Tk()
app.geometry("500x300") #กำหนดขนาด
app.title('เขียนโดย suttawee')
L1 = tk.Label(text="ยินดีเข้าสู่ Python")
L2 = tk.Label(text="โดย ศุทธวีร์ น้อยกรณ์")
L3 = tk.Label(text="กรอกชื่อสินค้า: ")
E1 = tk.Entry()
L4 = tk.Label(text="ราคาสินค้า: ")
E2 = tk.Entry()
B1 = tk.Button(text="ตกลง", command= showme)
#label.pack()
#label.grid(row=0, column=5)
L1.place(x=50, y=10)
L2.place(x=50, y =40)
L3.place(x=20, y=70)
E1.place(x=100, y=70)
L4.place(x=20, y=100)
E2.place(x=100, y=100)
B1.place(x=200, y=130)