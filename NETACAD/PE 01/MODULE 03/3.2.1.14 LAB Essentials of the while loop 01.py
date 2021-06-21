"""Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

The figure illustrates the rule used by the builders:"""

from tkinter import *
window = Tk()
window.title('Add Image')
window = Canvas(window, width = 300, height = 300)
window.pack()
image = PhotoImage(file = 'D:\\GANI\\SMA\\MAPEL\\KELAS X\\INFORMATIKA PAK SOPAN\\PYTHON\\NETACAD\\PE 01\\MODULE 03\\3.2.1.14 LAB Essentials of the while loop 02.PNG')
window.create_image(0, 0, anchor = NW, image = image)

"""Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

Test your code using the data we've provided."""

blocks = int(input("Enter the number of blocks: "))

height = 0
in_layer = 1
while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1

print("The height of the pyramid:", height)

'''
In layer 1,tingginya 1,blok dikurangi 1
In layer 2,tingginya 2,blok dikurangi 2
'''