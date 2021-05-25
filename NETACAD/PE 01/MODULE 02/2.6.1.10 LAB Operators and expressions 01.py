"""Your task is to complete the code in order to evaluate the following expression:"""

from tkinter import *
window = Tk()
window.title('Add Image')
window = Canvas(window, width = 200, height = 200)
window.pack()
image = PhotoImage(file = 'D:\\GANI\\SMA\\MAPEL\\KELAS X\\INFORMATIKA PAK SOPAN\\PYTHON\\NETACAD\\PE 01\\MODULE 02\\2.6.1.10 LAB Operators and expressions 02.PNG')
window.create_image(0, 0, anchor = NW, image = image)

"""The result should be assigned to y. Be careful - watch the operators and keep their priorities in mind. Don't hesitate to use as many parentheses as you need.

You can use additional variables to shorten the expression (but it's not necessary). Test your code carefully."""

x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)