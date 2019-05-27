"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
#   make the details of the selected rows appear in the entry fields
    titleEnt.delete(0, END)
    titleEnt.insert(END, (selected_tuple[1]))
    authorEnt.delete(0, END)
    authorEnt.insert(END, (selected_tuple[2]))
    yearEnt.delete(0, END)
    yearEnt.insert(END, (selected_tuple[3]))
    isbnEnt.delete(0, END)
    isbnEnt.insert(END, (selected_tuple[4]))


def view_command():
    listbox.delete(0, END)
    for row in backend.view():
        listbox.insert(END, row)


def search_command():
    listbox.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        listbox.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    listbox.delete(0, END)
    listbox.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()


window = Tk()
window.wm_title("BookStore")

title = Label(window, text="Title")
title.grid(row=0, column=0)

author = Label(window, text="Author")
author.grid(row=0, column=2)

year = Label(window, text="Year")
year.grid(row=1, column=0)

isbn = Label(window, text="ISBN")
isbn.grid(row=1, column=2)

title_text = StringVar()
titleEnt = Entry(window, textvariable=title_text)
titleEnt.grid(row=0, column=1)

author_text = StringVar()
authorEnt = Entry(window, textvariable=author_text)
authorEnt.grid(row=0, column=3)

year_text = StringVar()
yearEnt = Entry(window, textvariable=year_text)
yearEnt.grid(row=1, column=1)

isbn_text = StringVar()
isbnEnt = Entry(window, textvariable=isbn_text)
isbnEnt.grid(row=1, column=3)

listbox = Listbox(window, height=6, width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
