

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
import pydicom 
import pillow_heif 
import numpy as np
import pylab
from tkinter import messagebox

def browse():
    global img,filename
    filename = filedialog.askopenfilename(title = "Select a File",
             initialdir='C:\\',
             filetypes = [('All Files',"*.*"), 
             ('PNG files',"*.png"),
             ('JPG files',"*.jpg"),
             ('HEIC files',"*.heic"),
             ('DCM files',"*.dcm")])#selecting a file from the system
    filename=filename.lower()
    my_str.set(filename)
    if filename[-4:] == 'heic':
        img= pillow_heif.read_heif(filename) #path to file
    elif filename[-3:] == 'dcm':  
        img= pydicom.dcmread(filename) #path to file
    else:
        img = Image.open(filename)#opening the selected file


def png_to_jpg():
    global img
    if filename[-3:]=='png':
        #Python tkinter messagebox askquestion 
        ask = messagebox.askquestion("Please Confirm", "Are you sure want to convert?")
        if ask =='yes':
            export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg',
                                filetypes=[("jpg file", ".jpg")])#choosing the path and changing extension to jpg


             # some minor case, resulting jpg file is larger one, should meet your expectation
             # in most case, resulting jpg file is resized small one
            if img.mode != "RGB":
                img = img.convert("RGB")
                img.save(export_file_path)
                succ_msg="Succesfully Converted! ",export_file_path
                msg_str.set(succ_msg)

            else:
                img.save(export_file_path)
                succ_msg="Succesfully Converted! ",export_file_path
                msg_str.set(succ_msg)
        else:
            succ_msg= "Sorry, You have Canceled!"
            msg_str.set(succ_msg)
    else:
        messagebox.showwarning('Error', 'Sorry, You have not selected .png file!')




def dcm_to_png():
    global img
    #Python tkinter messagebox askquestion
    if filename[-3:]=='dcm':
        ask = messagebox.askquestion("Please Confirm", "Are you sure want to convert?")
        if ask =='yes':
            new_image = img.pixel_array.astype(float)
            #print(new_image)
            scaled_image = (np.maximum(new_image, 0) / new_image.max()) * 255.0
            #print(scaled_image)
            scaled_image = np.uint8(scaled_image)
            final_image = Image.fromarray(scaled_image)
            #final_image.save('image.png')
            export_file_path = filedialog.asksaveasfilename(defaultextension='.png',
                                     filetypes=[("png file", ".png")])#choosing the path and changing extension to png 
            final_image.save(export_file_path)#saving the file on desired path
            succ_msg="Succesfully Converted! ",export_file_path
            msg_str.set(succ_msg)
            
        else:
            succ_msg= "Sorry, You have Canceled!"
            msg_str.set(succ_msg)
        
    else:
        messagebox.showwarning('Error', 'Sorry, You have not selected .dcm file!')


#function to change from heic to jpeg
def heic_to_jpeg():
    global img
    if filename[-4:]=='heic':
        #Python tkinter messagebox askquestion 
        ask = messagebox.askquestion("Please Confirm", "Are you sure want to convert?")
        if ask =='yes':    
            image = Image.frombytes(
            img.mode,
            img.size,
            img.data,
            "raw")
            #final_image.save('image.png')
            export_file_path = filedialog.asksaveasfilename(defaultextension='.jpeg',
                                        filetypes=[("jpeg file", ".jpeg")])#choosing the path and changing extension to png 
            image.save(export_file_path)#saving the file on desired path
            succ_msg="Succesfully Converted! ",export_file_path
            msg_str.set(succ_msg)
        else:
            succ_msg= "Sorry, You have Canceled!"
            msg_str.set(succ_msg)            
    else:
        messagebox.showwarning('Error', 'Sorry, You have not selected .heic file!')


#function to change from jpg to png
def jpg_to_png():
    global img
    if filename[-3:]=='jpg':
        #Python tkinter messagebox askquestion 
        ask = messagebox.askquestion("Please Confirm", "Are you sure want to convert?")
        if ask =='yes':
            export_file_path = filedialog.asksaveasfilename(defaultextension='.png',
                                        filetypes=[("png file", ".png")])#choosing the path and changing extension to jpg 
            img.save(export_file_path)#saving the file on desired path
            succ_msg="Succesfully Converted! ",export_file_path
            msg_str.set(succ_msg)
            
        else:
            succ_msg= "Sorry, You have Canceled!"
            msg_str.set(succ_msg)               
    else:
        messagebox.showwarning('Error', 'Sorry, You have not selected .jpg file!')


def donothing():
   x = 0
def programmer():
    messagebox.showinfo('Information', 'Md. Ripon Miah, JE(IT), Tangail PBS, Email:ripon2488@gmail.com, Mobile:01732119556')

def helpmenu():
    messagebox.showinfo('How To..', 'Browse Image and Open ')


# ## Creating the GUI Window:


#creating window
root = Tk()
my_str = tk.StringVar()
msg_str= tk.StringVar()
root.geometry('600x250')#geometry of window
root.minsize(600,250) # fixed size
root.maxsize(600,250) # fixed size

menubar = Menu(root)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=programmer)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.title('Image Format Converter -Ripon')#title for window

Label(root,text='Image Format Converter',font='arial 15').place(x=200,y=10)

Label(root,textvariable=my_str,fg='blue',wraplength=600 ).place(relx=0.5, rely=0.4, anchor=CENTER)
Label(root,textvariable=msg_str,fg='blue',wraplength=500 ).place(relx=0.5, rely=0.7, anchor=CENTER)


# - Tk() – We generated a window called root with the Tk() technique.
# - geometry() – The size of the window is specified by this function.
# - title() – provides the newly formed window a title
# - Label() – Label is a Gui widget that is typically used to show text on the window. This adds a label to the project's GUI window. A label's color, font, size, height, and width may all be changed. This Label() method was used to show text in this case.
# - place() – The place() method aids in the presentation of widgets on the window. We may give the x and y coordinates of a widget and position it using the place() method.

# ## Creating Button in GUI



Button(root,text = 'Browse an Image',command=browse,fg='blue',font='arial 10').place(x=250,y=60)#creating button


# - Button() – This aids in the creation of a button on the window. command=browse indicates that the browse function will be invoked whenever this button is pressed. Similarly to the label, we may select the color, font, background color, foreground color, and so on of a button here.


Button(root,text='PNG To JPG',command=png_to_jpg,fg='red',font='arial 10').place(x=100,y=130)
Button(root,text='DCM To PNG',command=dcm_to_png,fg='red',font='arial 10').place(x=200,y=130)
Button(root,text='HEIC To JPEG',command=heic_to_jpeg,fg='red',font='arial 10').place(x=300,y=130)
Button(root,text='JPG To PNG',command=jpg_to_png,fg='red',font='arial 10').place(x=410,y=130)


root.mainloop()





