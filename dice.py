#Import section
import tkinter as tk
import random
from PIL import ImageTk, Image


#main window
window = tk.Tk()
window.geometry('500x300')
window.title('Dado')
window.config(bg='black')


#Different images from the possible sides of the dice
dice = ['dot1.png', 'dot2.png', 'dot3.png', 'dot4.png', 'dot5.png', 'dot6.png']
dice_picture = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#Creates a label for the image
image_label = tk.Label(window, image = dice_picture)
image_label.image = dice_picture
image_label.pack(expand=True)

#Creates function rolling_dice, that uses module random to select a random choice of the differente sides of the dice
def rolling_dice():
    dice_picture2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    image_label.configure(image=dice_picture2)
    # keep a reference
    image_label.image = dice_picture2


#Creates button. Command uses function rolling_dice()
photo = ImageTk.PhotoImage(file = 'roll_.png')
button = tk.Button(window, image = photo, fg = 'cyan',height = 50, width = 200, command = rolling_dice).pack(ipadx=5,
    ipady=5)


window.mainloop()
