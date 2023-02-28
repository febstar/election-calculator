from tkinter import *
from tkinter import messagebox

States = ["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno",
          "Cross River",
          "Delta",
          "Ebonyi",
          "Edo",
          "Ekiti",
          "Enugu",
          "FCT - Abuja",
          "Gombe",
          "Imo",
          "Jigawa",
          "Kaduna",
          "Kano",
          "Katsina",
          "Kebbi",
          "Kogi",
          "Kwara",
          "Lagos",
          "Nasarawa",
          "Niger",
          "Ogun",
          "Ondo",
          "Osun",
          "Oyo",
          "Plateau",
          "Rivers",
          "Sokoto",
          "Taraba",
          "Yobe",
          "Zamfara"]
window = Tk()
window.title("Election Tracker")
LP = Label(text="Labour Party")
LP.grid(column=1, row=0)
LP.config(padx=2, pady=2)
APC = Label(text="All Progressive Congress")
APC.config(padx=2, pady=2)
APC.grid(column=2, row=0)
PDP = Label(text="People's Democratic Party")
PDP.config(padx=2, pady=2)
PDP.grid(column=3, row=0)
n = 0
LP_list = []
APC_list = []
PDP_list = []
for state in States:
    n +=1
    display = Label(text=f"{state}")
    display.grid(column=0, row=1 + n)
    entry1 = Entry()
    entry1.insert(END,0)
    entry1.grid(column=1, row=1 + n)
    entry2 = Entry()
    entry2.insert(END, 0)
    entry2.grid(column=2, row=1 + n)
    entry3 = Entry()
    entry3.insert(END, 0)
    entry3.grid(column=3, row=1 + n)
    LP_list.append(entry1)
    APC_list.append(entry2)
    PDP_list.append(entry3)

def calculate():
    l = 0
    c = 0
    p = 0
    for a in LP_list:
        i = a.get()
        l += int(i)
    for a in APC_list:
        i = a.get()
        c += int(i)
    for a in PDP_list:
        i = a.get()
        p += int(i)

    messagebox.showinfo(title="FINAL RESULTS!", message=f"Labour Party: {l} | All Progressive Congress: {c} | People's Democratic Party: {p}")

do = Button(text="Calculate", command=calculate)
do.grid(column=6,row=14)


window.mainloop()