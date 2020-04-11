import tkinter as tk




window = tk.Tk() 

window.title("SAIL") 

window.geometry("375x200") 

instructions = tk.Label(window, text = "Type in the colour"
						"of the words, and not the word text!", 
									font = ('Helvetica', 12)) 
instructions.pack() 

window.update()

instructions['text'] = "asdasd"

window.update()
