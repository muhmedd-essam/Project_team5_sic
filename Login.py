def books(self):
    with open('books_data.json', 'r') as file:
        users = json.load(file)

    newWindow = Toplevel(self.shop)
    newWindow.title("Online Shopping")
    newWindow.geometry("800x600+280+50")
    newWindow.iconbitmap('supermarkets.ico')
    Label(newWindow, text='Books', fg='gold', bg='black', font=('tajawal', 16, 'bold')).pack(fill=tk.X)
    Fab = tk.Frame(newWindow, height=800, bg='darkblue')
    Fab.pack(fill=tk.X)

    with open('books_data.json', 'r') as file:
        users = json.load(file)

    positions = [(20, 270), (180, 270), (340, 270), (500, 270), (660, 270)]

    varBooks = [IntVar() for _ in range(5)]

    entries = []

    for i in range(len(users)):
        self.book_label = Label(Fab, text=users[i]['text'], fg='gold', bg='darkblue', font=('tajawal', 16, 'bold'))
        self.book_label.place(x=users[i]['x'], y=positions[i][1])

        book_entry = Entry(Fab, textvariable=varBooks[i], width=18, justify='center')
        book_entry.place(x=users[i]['x'] + 5, y=positions[i][1] + 40)

        entries.append(book_entry)



    def changebooks():
        newWindow = Toplevel(self.shop)
        newWindow.title("Edit Books")
        newWindow.geometry("400x300+400+200")
        newWindow.iconbitmap('supermarkets.ico')

        varOldName = StringVar()
        varNewName = StringVar()

        book_label = Label(newWindow, text="Book Name you need to change it:", font=('tajawal', 12, 'bold'))
        book_label.pack(pady=10)

        book_entry = Entry(newWindow, textvariable=varOldName, width=30)
        book_entry.pack()

        book_label = Label(newWindow, text="New Book Name:", font=('tajawal', 12, 'bold'))
        book_label.pack(pady=10)

        newname = Entry(newWindow, textvariable=varNewName, width=30)
        newname.pack()

        add_button = Button(newWindow, text="add Book",
                            command=lambda: change_book(varOldName.get(), varNewName.get))
        add_button.pack(pady=10)

        back_button = Button(newWindow, text="Back", command=newWindow.destroy)
        back_button.pack(pady=10)

    def change_book(old_name, new_name):
        with open('books_data.json', 'r') as file:
            users = json.load(file)
        for user in users:
            if user['text'] == old_name:
                user['text'] = new_name
                with open('books_data.json', 'w') as file:
                    json.dump(users, file)
                messagebox.showinfo("Success", "The book has been changed.")
                newWindow.destroy()
                self.books()
                return
        messagebox.showinfo("Error", "The book was not found.")



    add_button = Button(Fab, text="Edit Books", command=change_book)
    add_button.place(x=0, y=530)