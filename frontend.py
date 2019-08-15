from tkinter import *
from backend import Database

database = Database("books.db")

def get_selected_row(event):
    global selected_tuple
    if list1.curselection(): #if this isnt empty do the following
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])


def view_command():
    list1.delete(0,END)
    for rows in database.view():
        list1.insert(END, rows)

def search_command():
    list1.delete(0,END)
    for rows in database.search(e1.get(),e2.get(),e3.get(),e4.get()):
        list1.insert(END,rows)

def add_command():
    database.insert(e1.get(),e2.get(),e3.get(),e4.get())
    list1.delete(0,END)
    list1.insert(END,(e1.get(),e2.get(),e3.get(),e4.get()))

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], e1.get(),e2.get(),e3.get(),e4.get())
    view_command()

window = Tk()
window.wm_title("Bookstore")

l1 = Label(window,text = "Title")
l1.grid(row = 0, column = 0)

#title
e1 = Entry(window)
e1.grid(row = 0, column = 1)

l2 = Label(window,text = "Author")
l2.grid(row = 0, column = 2)

#author
e2 = Entry(window)
e2.grid(row = 0, column = 3)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

#year
e3 = Entry(window)
e3.grid(row = 1, column = 1)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

#isbn
e4 = Entry(window)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, width = 35, height = 6)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

sb1.configure(command = list1.yview)
list1.configure(yscrollcommand= sb1.set)

list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window, text = "View All", width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search Entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add Entry", width = 12, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)



window.mainloop()
