# Roll-the-dice

A simple dice roller application using Python and Tkinter. This application displays a GUI with a single button to roll the dice.

**Requirements**
Python 3.x, Tkinter, Pillow (PIL)

**Usage**
To run the application, simply run the following command in the terminal/command prompt:

**Description**
This application uses the Tkinter library to create a GUI window, and the Pillow (PIL) library to display the images of the different sides of the dice. When the button is clicked, the rolling_dice function is called, which uses the random module to randomly select an image of a dice side, and display it in the GUI window.
The different sides of the dice are stored as image files in the same directory as the code. The name of these image files are stored in the dice list, and the ImageTk.PhotoImage method from the PIL library is used to open the image files and display them in the GUI window.

