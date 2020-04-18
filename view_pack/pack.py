'''Example of how to use the pack() method to create a GUI layout'''
# import tkinter and all its functions
from tkinter import * 
 
root = Tk() # create root window
root.title("Basic GUI Layout with Pack")
root.maxsize(900, 600) 
root.config(bg="skyblue")
 
# Create left and right frames
left_frame = Frame(root, width=200, height=400, bg='grey')
left_frame.pack(side='left', fill='both', padx=10, pady=5, expand=True)
 
right_frame = Frame(root, width=650, height=400, bg='grey')
right_frame.pack(side='right', fill='both', padx=10, pady=5, expand=True)
 
# Create frames and labels in left_frame
Label(left_frame, text="Original Image").pack(side='top', padx=5, pady=5)
 
image = PhotoImage()
original_image = image.subsample(3,3)
Label(left_frame, image=original_image).pack(fill='both', padx=5, pady=5)
 
#large_image = original_image.subsample(2,2)
Label(right_frame, image=image).pack(fill='both', padx=5, pady=5)
 
tool_bar = Frame(left_frame, width=90, height=185, bg='lightgrey')
tool_bar.pack(side='left', fill='both', padx=5, pady=5, expand=True)
 
filter_bar = Frame(left_frame, width=90, height=185, bg='lightgrey')
filter_bar.pack(side='right', fill='both', padx=5, pady=5, expand=True)
 
def clicked():
    '''if button is clicked, display message'''
    print("Clicked.")
 
# Example labels that serve as placeholders for other widgets 
Label(tool_bar, text="Tools", relief=RAISED).pack(anchor='n', padx=5, pady=3, ipadx=10)
Label(filter_bar, text="Filters", relief=RAISED).pack(anchor='n', padx=5, pady=3, ipadx=10)
 
# For now, when the buttons are clicked, they only call the clicked() method. We will add functionality later.
Button(tool_bar, text="Select", command=clicked).pack(padx=5, pady=5)
Button(tool_bar, text="Crop", command=clicked).pack(padx=5, pady=5)
Button(tool_bar, text="Rotate &amp; Flip", command=clicked).pack(padx=5, pady=5)
Button(tool_bar, text="Resize", command=clicked).pack(padx=5, pady=5)
Button(filter_bar, text="Black &amp; White", command=clicked).pack(padx=5, pady=5)
 
root.mainloop()