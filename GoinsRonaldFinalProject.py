"""

Author:  R. Landon Goins
Date written: 7/16/2023
Assignment:   Final Project
Short Desc:  GUI ktinker program in which their are 3 weapons to choose from to go against the computer.
             It plays much like a game of rock paper scissors.

"""

#importing Ktinker as well as PIL for images
from tkinter import *
from PIL import Image, ImageTk
from random import randint
import tkinter as tk



#creating first window and setting parameters
root = Tk()
root.geometry("600x500")
root.title("The Field of Battle")
#Changing background to black color
root.config(bg="black")

#creating second window and setting parameters
root2 = Tk()
root2.geometry("500x200")
root2.title("The Officers Table")
#Changing background to black color
root2.config(bg="black") 


#creating the first frame
firstframe = Frame(root)
firstframe.pack()

#creating second frame
secondframe = Frame(root)
secondframe.pack()

#starting class
class BattleApp:
    

    #creating the first frame
    firstframe = Frame(root)
    firstframe.pack()


    secondframe = Frame(root)
    secondframe.pack(side = BOTTOM)
    
    # 0 = Bow
    # 1 = Shield
    # 2 = Lance


    #defining the function of the bow & arrow option button  
    def play_bow():
        pick_num = randint(0,2)
        if pick_num == 2:
            Label(firstframe, text = "You have bested the enemy from a distance!").grid(row=1)
            image = Image.open("bow.png")   #Opening pil image
            image = image.resize((300, 200))  # Adjust the image size
            photo = ImageTk.PhotoImage(image)
            image_label =Label(root, image=photo)
            image_label.image = photo
            image_label.place(x=150, y=50)
            print("You have bested the enemy from a distance!")
        elif pick_num == 1:
            Label(firstframe, text = "The enemy had blocked your arrows with their shield! Try again!").grid(row=1)
            image = Image.open("shield.png")  #Opening pil image
            image = image.resize((300, 200))  # Adjust the image size
            photo = ImageTk.PhotoImage(image)
            image_label =Label(root, image=photo)
            image_label.image = photo
            image_label.place(x=150, y=50)
            print("The enemy had blocked your arrows with their shield! Try again!")
        else:
            Label(firstframe, text = "The enemy also used a bow. The game is a draw!").grid(row=1)
            image = Image.open("black.png")   #Opening pil image
            image = image.resize((300, 200))  # Adjust the image size
            photo = ImageTk.PhotoImage(image)
            image_label =Label(root, image=photo)
            image_label.image = photo
            image_label.place(x=150, y=50)
     
     
            
    #defining the function of the shield option button  
    def play_shield():
        pick_num = randint(0,2)
        if pick_num == 2:
            Label(firstframe, text = "The enemy has shattered your shield! You have lost, try again!").grid(row=1)
            image = Image.open("lance.png")   #Opening pil image
            image = image.resize((300, 200))  # Adjust the image size
            photo = ImageTk.PhotoImage(image)
            image_label =Label(root, image=photo)
            image_label.image = photo
            image_label.place(x=150, y=50)
            print("The enemy has shattered your shield! You have lost, try again!")
        elif pick_num == 1:
            Label(firstframe, text ="The enemy also chose a shield. The game is a draw!").grid(row=1)
            image = Image.open("black.png")   #Opening pil image
            image = image.resize((300, 200))  # Adjust the image size
            photo = ImageTk.PhotoImage(image)
            image_label =Label(root, image=photo)
            image_label.image = photo
            image_label.place(x=150, y=50)
        else:
            Label(firstframe, text = "You have blocked the enemy arrows! Victory!").grid(row=1)
            image = Image.open("shield.png")   #Opening pil image
            image = image.resize((300, 200))  # Adjust the image size
            photo = ImageTk.PhotoImage(image)
            image_label =Label(root, image=photo)
            image_label.image = photo
            image_label.place(x=150, y=50)
            print("You have blocked the enemy arrows! Victory!")
            
            
    #defining the function of the lance option button      
    def play_lance():
        pick_num = randint(0,2)
        if pick_num == 2:
            Label(firstframe, text = "The enemy also used their lance! The game is a draw, try again!").grid(row=1)
            image = Image.open("black.png")   #Opening pil image
            image = image.resize((300, 200))  # Adjust the image size
            photo = ImageTk.PhotoImage(image)
            image_label =Label(root, image=photo)
            image_label.image = photo
            image_label.place(x=150, y=50)
        elif pick_num == 1:
            Label(firstframe, text="You shattered the enemy shields with your lance! Victory!").grid(row=1)
            image = Image.open("lance.png")   #Opening pil image
            image = image.resize((300, 200))  # Adjust the image size
            photo = ImageTk.PhotoImage(image)
            image_label =tk.Label(root, image=photo)
            image_label.image = photo
            image_label.place(x=150, y=50)
            print("You shattered the enemy shields with your lance! Victory!")
        else:
            Label(firstframe, text="The enemy has bested you from a distance with arrows, try again!").grid(row=1)
            image = Image.open("bow.png")   #Opening pil image
            image = image.resize((300, 200))  # Adjust the image size
            photo = ImageTk.PhotoImage(image)
            image_label =Label(root, image=photo)
            image_label.image = photo
            image_label.place(x=150, y=50)
            print("The enemy has bested you from a distance with arrows, try again!")

    #creating labels for game instructions
    Label(secondframe, text="In this game of battle you must beat the computer by choosing the right tool!", fg ='red').grid()
    Label(secondframe, text="The bow will beat the lance, the shield will beat the bow, and the lance will beat the shield.", fg ='red').grid()



    #creating button for each battle method and calling back to functions set above
    myButton = Button(root2, text="Bow & Arrow", command=play_bow)
    myButton.pack(pady=10)


    myButton = Button(root2, text="Shield", command=play_shield)
    myButton.pack(pady=15)



    myButton = Button(root2, text="Lance", command=play_lance)
    myButton.pack(pady=19)

    #creating exit button 
    exitbutton = Button(root2, text ='Exit', fg ='red', command=root.destroy)
    exitbutton.pack()



root.mainloop()

