from tkinter import *
from tkinter.ttk import Progressbar

root = Tk()

# Progress bar
progress = IntVar()
progress_bar = Progressbar(root, length=500, maximum=100, variable=progress)
progress_bar.grid(row=0, column=0, padx=20, pady=20)       

# Set duration  
duration = 12

# Calculate correct increment  
increment = 100 / duration

def update_progress():      
    progress.set(progress.get() + increment)     
    if progress.get() < 100:               
        root.after(1000, update_progress) 

# Call to start        
update_progress()

root.mainloop()