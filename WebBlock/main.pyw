from tkinter import *
from tkinter import ttk
from datetime import datetime as df
import threading # to start the blocker function as a parallel process to prevent the tkinter window from freezing
import blocker

# link addition function
def add_link():
    """ adds website links to the websites.txt
    """
    with open("websites.txt", "r+") as website_loc:
        content = website_loc.readlines()
        print(content)
        if Addlink.get() != " ":
            if (Addlink.get() + "z") in content:
                pass
            else: 
                website_loc.write(Addlink.get() + "\n")
        else:
            pass
    window.destroy()
    mainWindow()
        
# link removing functions
def existing_links():
    """ Fetches the existing links from the websites.txt file and stores them in content
    """
    with open("websites.txt", "r+") as website_loc:
        content = website_loc.readlines()
        return content

def remove_selected_link():
    """ removes the link selected from the combobox
    """
    with open("websites.txt", "r+") as file:
        websites = file.readlines()
    for website in websites:
        if website[:-1] == Removelink.get()[:-1]:
            websites.remove(website)
    with open("websites.txt", "r+") as file:
        for website in websites:
            file.write(website)
            file.truncate()
    window.destroy()
    mainWindow()
            
#initiating blocker
def run_blocker():
    """ The name says all, It initiates the blocker
    """
    blocker.status = True
    Statuslabel.config(text = "Status: Blocking")
    blocker.blocker(Starttime.get(), Stoptime.get())

#stopping the script
def stop_blocker():
    """ Stops the blocker by changing the status to False 
    """
    blocker.status = False
    window.destroy()

def mainWindow():
    global window, Addlink, Removelink, Statuslabel, Starttime, Stoptime
    window = Tk()

    window.title("Blocker")
    window.resizable(False, False)

    #Link addition feild
    Add = Label(window, text = "Add link")
    Add.grid(row = 0, column = 0)

    #Link addition feild
    Addlink = StringVar()
    Addfeild = Entry(window, textvar = Addlink)
    Addfeild.grid(row = 0, column = 1)

    #Link addition button
    Addbutton = Button(window, text = "Add", width = 10,command = add_link)
    Addbutton.grid(row = 0, column = 3)

    #Link removal label
    Remove = Label(window, text = "Remove link")
    Remove.grid(row = 1, column = 0)

    #Link removal combobox
    Removelink = StringVar()
    Linkchoosen = ttk.Combobox(window, width = 17, textvariable = Removelink)
    Linkchoosen["values"] = tuple(existing_links())
    Linkchoosen.grid(row = 1, column = 1)
    Linkchoosen.current()

    #Link removal button
    Removebutton = Button(window, text = "Remove", width = 10, command = remove_selected_link)
    Removebutton.grid(row = 1, column = 3)

    
    #start stop timings (24 hours)
    Starttiming = Label(window, text = "Start time")
    Starttiming.grid(row = 2, column = 0)

    Starttime = IntVar()
    Starttimechoosen = ttk.Combobox(window, width = 17, textvariable = Starttime)
    Starttimechoosen["values"] = tuple([i for i in range(0,24)])
    Starttimechoosen.grid(row = 2, column = 1)
    Starttimechoosen.current()

    Stoptiming = Label(window, text = "Stop time")
    Stoptiming.grid(row = 2, column = 2)

    Stoptime = IntVar()
    Stoptimechoosen = ttk.Combobox(window, width = 17, textvariable = Stoptime)
    Stoptimechoosen["values"] = tuple([i for i in range(0,24)])
    Stoptimechoosen.grid(row = 2, column = 3)
    Stoptimechoosen.current()

    #Start and Stop buttons
    Startbutton = Button(window, text = "Start", width = 10, command = threading.Thread(target=run_blocker).start)
    Startbutton.grid(row = 4, column = 1)
    
    Stopbutton = Button(window, text = "Stop", width = 10, command = stop_blocker)
    Stopbutton.grid(row = 4, column = 2)
    
    #Status bar
    Statuslabel = Label(window, text = "Status: Ready", bd = 1, relief = SUNKEN, anchor = W)
    Statuslabel.grid(row = 4, column = 0)

    #spacing, to create space between the feilds and the button
    Button1 = Label(window, text = " ")
    Button1.grid(row = 3, column = 1)

    Button2 = Label(window, text = " ")
    Button2.grid(row = 3, column = 2)

    window.mainloop()
    
mainWindow()