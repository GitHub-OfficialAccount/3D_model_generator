from tkinter import *  

root = Tk()  

# Left side  
left_frame = Frame(root)  
left_frame.pack(side=LEFT)   

textbox = Entry(left_frame, width=30)  
textbox.pack()   

generate_button = Button(left_frame, text="Generate")  
generate_button.pack()

advanced_options_button = Button(left_frame, text="Advanced Options  ▼")  
advanced_options_button.pack()  

option1_entry = Entry(left_frame, width=30)  
option1_label = Label(left_frame, text="Option 1: ") 

option2_entry = Entry(left_frame, width=30)
option2_label = Label(left_frame, text="Option 2: ")       

options_showing = False  

def show_hide_options(): 
    global options_showing
    if not options_showing: 
        option1_label.pack()
        option1_entry.pack() 
        option2_label.pack()
        option2_entry.pack()         
        advanced_options_button.config(text="Advanced Options  ▲")
        options_showing = True
    else:         
        option1_label.forget()
        option1_entry.forget()
        option2_label.forget()
        option2_entry.forget()
        advanced_options_button.config(text="Advanced Options  ▼ ")
        options_showing = False

advanced_options_button.config(command=show_hide_options)  

# Right side
right_frame = Frame(root, width=200, height=200)  
right_frame.pack(side=RIGHT, padx=20, pady=20)  

box = Canvas(right_frame, width=200, height=200)  
box.pack()  

confirm_button = Button(right_frame, text="Confirm")  
confirm_button.pack()   

root.mainloop()