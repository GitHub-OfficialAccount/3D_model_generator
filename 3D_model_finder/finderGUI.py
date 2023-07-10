import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
from finder import *

# Function to handle button click event
def search():
    global result
    global var
    keyword = keyword_entry.get()
    page = page_entry.get()
    if not keyword:
        messagebox.showwarning("Warning!", "Keyword is empty!")
    else:
        print("Keyword:", keyword)
        print("Page:", page)
        data = fetch_data(generate_url(action="search", keyword=keyword, page=page)) 
        result = data_converter(data) #clean data
        result = multiple_files_indicator(result) #indicates whether the number of parts a 3D model has

        download_images(result)

        show(master=root,result=result)
        # var.set(1)
        return result

def exit_program():
    root.quit()
    root.destroy()

def show(master, result):
    global root2

    def exit_program2():
        root2.quit()
        root2.destroy()

    try:
        if root2:
            root2.quit()
            root2.destroy()
    except: #root 2 not defined
        pass

    root2 = tk.Toplevel(master)
    root2.title("Search Results")

    # Create a list of image paths and label texts
    image_paths = [get_image_url_from_index(result,i) for i in range(len(result))]
    label_texts = [result[i]['name']+f"({result[i]['parts']} parts)" for i in range(len(result))]

    # Create a list of PhotoImage objects from the image paths
    images = []
    for path in image_paths:
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        images.append(photo)
    # #######
    # for i in range(len(images)):
    #     print(images[i])

    # Create three rows for displaying images and labels
    labels = []

    for i in range(3):
        for j in range(4):
            index = i*4 + j  
        
            frame = tk.Frame(root2)
            frame.grid(row=i, column=j, padx=10, pady=10)

            # Create label
            image_label = tk.Label(frame, image=images[index])
            image_label.pack(side="top")

            text_label = tk.Label(frame, text=label_texts[index])   
            text_label.pack(side="top")
            
            # Add to list of labels
            labels.append(image_label)
            
    def image_clicked(event):
        index = labels.index(event.widget)
        ans = messagebox.askokcancel("Confirm", f"Proceed with Image {index+1}?")
        if ans:
            print(f"Image {index+1} selected")
            download_file_from_index(result,index)
            exit_program2()
            
    # Bind click to all labels    
    for label in labels: 
        label.bind("<Button-1>", image_clicked)

    root2.mainloop()


# Create the main window
root = tk.Tk()
root.title("Search Interface")

# Create the 'Keyword' label and textbox
keyword_label = tk.Label(root, text="Keyword:")
keyword_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
keyword_entry = tk.Entry(root)
keyword_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Create the 'Page' label and textbox
page_label = tk.Label(root, text="Page:")
page_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
page_entry = tk.Entry(root)        
page_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Create the Submit button
submit_button = tk.Button(root, text="Search", command=search)  
submit_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# #wait for search to be pressed
# var = tk.IntVar()
# submit_button.wait_variable(var)

# Run the main loop
root.mainloop()