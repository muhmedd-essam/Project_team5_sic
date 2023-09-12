import tkinter as tk
import json
from tkinter import messagebox
import webbrowser
from tkinter import *
from ADMIN_LOGIN import adminLoginApp


class LoginApplication:
    def __init__(self, shop):
        self.shop = shop

        self.shop.title("Online Shopping")
        self.shop.geometry("800x600+280+50")
        self.shop.resizable(False, False)
        self.shop.iconbitmap('supermarkets.ico')
        self.shop.title_label = tk.Label(self.shop, text='Store Online', fg='gold', bg='black',
                                         font=('tajawal', 16, 'bold'))
        self.shop.title_label.pack(fill=tk.X)

        self.F1 = Frame(shop, width=800, height=400, bg='black')
        self.F1.place(x=0, y=367)
        self.Photo = PhotoImage(file="2.png")
        self.imo = tk.Label(image=self.Photo)
        self.imo.place(x=0, y=30)

        self.email_label = tk.Label(self.F1, text="Email:", fg='gold', bg='black',
                                         font=('tajawal', 16, 'bold'))
        self.email_label.place(x=370, y=10)
        self.email_entry = tk.Entry(self.F1)
        self.email_entry.place(x=340, y=40)

        self.password_label = tk.Label(self.F1, text="Password:", fg='gold', bg='black',
                                         font=('tajawal', 16, 'bold'))
        self.password_label.place(x=350, y=60)
        self.password_entry = tk.Entry(self.F1, show="*")
        self.password_entry.place(x=340, y=90)

        self.login_button = tk.Button(self.F1, text="Login", command=self.login, width=26, fg='black', bg='#DBA901',
                                      font=('tajawal', 16, 'bold'))
        self.login_button.place(x=230, y=120)

        self.register_button = tk.Button(self.F1, text="Register", command=self.open_register_window, width=26, fg='black', bg='#DBA901',
                                      font=('tajawal', 16, 'bold'))
        self.register_button.place(x=230, y=180)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Load user data from JSON file
        with open('users.json', 'r') as file:
            users = json.load(file)

        for i in range(len(users)):
            if email in users and users[email]["password"] == password:
                name = users[email]["name"]
                messagebox.showinfo("Login Successful", f"Welcome {name}!")
                self.shop.destroy()
                home_app = homeApplication(tk.Tk())
                break
            elif email == "admin@gmail.com" and password == "1234":
                messagebox.showinfo("Login Successful", "Welcome Admin!")
                self.shop.destroy()
                adminLoginApp(tk.Tk())
                tk.mainloop()

                break
            else:
                messagebox.showerror("Login Failed", "Invalid email or password.")
                break


    def open_register_window(self):
        self.shop.destroy()
        register_app = RegisterApplication(tk.Tk())

class RegisterApplication:
    def __init__(self, shop):
        self.shop = shop

        self.shop.title("Online Shopping")
        self.shop.geometry("800x660+280+50")
        self.shop.resizable(False, False)
        self.shop.iconbitmap('supermarkets.ico')
        self.shop.title_label = tk.Label(self.shop, text='Store Online', fg='gold', bg='black',
                                         font=('tajawal', 16, 'bold'))
        self.shop.title_label.pack(fill=tk.X)

        self.F1 = Frame(shop, width=800, height=400, bg='black')
        self.F1.place(x=0, y=367)
        self.Photo = PhotoImage(file="2.png")
        self.imo = tk.Label(image=self.Photo)
        self.imo.place(x=0, y=30)

        self.email_label = tk.Label(self.F1, text="Email:", fg='gold', bg='black',
                                         font=('tajawal', 16, 'bold'))
        self.email_label.place(x=370, y=10)
        self.email_entry = tk.Entry(self.F1)
        self.email_entry.place(x=340, y=40)

        self.name_label = tk.Label(self.F1, text="Name:", fg='gold', bg='black',
                                         font=('tajawal', 16, 'bold'))
        self.name_label.place(x=370, y=60)
        self.name_entry = tk.Entry(self.F1)
        self.name_entry.place(x=340, y=90)

        self.password_label = tk.Label(self.F1, text="Password:", fg='gold', bg='black',
                                         font=('tajawal', 16, 'bold'))
        self.password_label.place(x=350, y=110)
        self.password_entry = tk.Entry(self.F1, show="*")
        self.password_entry.place(x=340,y=140)

        self.age_label = tk.Label(self.F1, text="Age:", fg='gold', bg='black',
                                         font=('tajawal', 16, 'bold'))
        self.age_label.place(x=380, y= 160)
        self.age_entry = tk.Entry(self.F1)
        self.age_entry.place(x=340, y= 190)

        self.register_button = tk.Button(self.F1, text="Register", command=self.register, width=26, fg='black', bg='#DBA901',
                                      font=('tajawal', 16, 'bold'))
        self.register_button.place(x=230, y=220)

    def register(self):
        email = self.email_entry.get()
        name = self.name_entry.get()
        password = self.password_entry.get()
        age = self.age_entry.get()

        try:
            with open('users.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        # Add new user data
        users[email] = {
            "name": name,
            "password": password,
            "age": age
        }

        # Save updated user data to JSON file
        with open('users.json', 'w') as file:
            json.dump(users, file)

        messagebox.showinfo("Registration Successful", "Registration completed successfully.")
        self.shop.destroy()
        login_app = LoginApplication(tk.Tk())








class homeApplication:
    def __init__(self, shop):
        self.shop = shop

        self.shop.title("Online Shopping")
        self.shop.geometry("800x600+280+50")
        self.shop.resizable(False, False)
        self.shop.iconbitmap('supermarkets.ico')
        self.shop.title_label = tk.Label(self.shop, text='Store Online', fg='gold', bg='black',
                                         font=('tajawal', 16, 'bold'))
        self.shop.title_label.pack(fill=tk.X)

        self.F1 = Frame(shop, width=800, height=400, bg='black')
        self.F1.place(x=0, y=367)

        self.button_books = tk.Button(self.F1, text='Books', width=26, fg='black', bg='#DBA901',
                                      font=('tajawal', 16, 'bold'), command=self.books)
        self.button_books.place(x=20, y=10)
        self.button_Electronics = tk.Button(self.F1, text='Electronics', width=26, fg='black', bg='#DBA901',
                                            font=('tajawal', 16, 'bold'), command=self.Electronics)
        self.button_Electronics.place(x=440, y=10)
        self.button_Fashion = tk.Button(self.F1, text='Fashion', width=26, fg='black', bg='#DBA901',
                                        font=('tajawal', 16, 'bold'), command=self.Fashion)
        self.button_Fashion.place(x=20, y=80)
        self.button_Sports = tk.Button(self.F1, text='Sports', width=26, fg='black', bg='#DBA901',
                                       font=('tajawal', 16, 'bold'), command=self.Sports)
        self.button_Sports.place(x=440, y=80)

        self.buttons = [
            ("Books"),
            ("Electronics"),
            ("Fashion"),
            ("Sports")
        ]
        self.change = tk.Button(text='Change sort, Ascending/descending', width=30, fg='black', bg='#DBA901',
                                font=('tajawal', 16, 'bold'), command=self.toggle_sort)
        self.change.place(x=220, y=550)
        self.sort_ascending = True

        self.create_buttons()

        self.Photo = PhotoImage(file="2.png")
        self.imo = tk.Label(image=self.Photo)
        self.imo.place(x=0, y=30)
        self.logout_button = tk.Button( text="Logout", width=10, fg='black', bg='#DBA901',
                                font=('tajawal', 16, 'bold') ,command=self.logout)
        self.logout_button.place(x=10, y=550)

    def logout(self):
        self.shop.destroy()
        login_app = LoginApplication(tk.Tk())

    def books(self):
        with open('books_data.json', 'r') as file:
            users = json.load(file)

        def addToCard():
            newWindow = Toplevel(self.shop)
            newWindow.title("Online Shopping")
            newWindow.geometry("800x600+280+50")
            newWindow.iconbitmap('supermarkets.ico')
            Label(newWindow,text='cart', fg='gold', bg='black',
                  font=('tajawal', 16, 'bold')).pack(fill=tk.X)
            Fab3 = tk.Frame(newWindow, height=800, bg='darkblue')
            Fab3.pack(fill=tk.X)
            back_button = tk.Button(Fab3, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                    command=self.back_to_home)
            back_button.place(x=20, y=20)

            list = [varBook1.get(), varBook2.get(), varBook3.get(), varBook4.get(), varBook5.get()]


            positions = [(20, 200), (180, 200), (340, 200), (500, 200), (660, 200)]
            label_list = []

            for i in range(len(list)):
                if list[i] != 0:
                    mytext = users[i]['text']
                    cart = Label(Fab3, text=mytext, font=('Helvetica 20 bold'), bg='darkblue', fg='gold')
                    cart.place(x=positions[i][0], y=positions[i][1])
                    label_list.append(cart)

            ul = 'https://wa.me/01128828067?text=i want to bay book 1'

            def open():
                webbrowser.open_new(ul)

            pay_button = tk.Button(Fab3, text='Go to pay by vodafone cash', width=30, fg='black', bg='#DBA901',
                                   font=('tajawal', 16, 'bold'),
                                   command=open)
            pay_button.place(x=220, y=400)

            ul2 = 'https://www.facebook.com/LifeMakersEGY'

            def open2():
                webbrowser.open_new(ul2)

            pay_button = tk.Button(Fab3, text='to connect with us', width=20, fg='black', bg='#DBA901',
                                   font=('tajawal', 16, 'bold'),
                                   command=open2)
            pay_button.place(x=50, y=500)

            def destroyy():
                for label in label_list:
                    label.destroy()

            back_button = tk.Button(Fab3, text='Remove from cart', width=30, fg='black', bg='#DBA901',
                                    font=('tajawal', 16, 'bold'),
                                    command=destroyy)
            back_button.place(x=220, y=300)
        def calculate_total():
            totalBook1Ent = int(varBook1.get()) * 50
            totalBook2Ent = int(varBook2.get()) * 90
            totalBook3Ent = int(varBook3.get()) * 90
            totalBook4Ent = int(varBook4.get()) * 90
            totalBook5Ent = int(varBook5.get()) * 90
            totalBookPrice = float(totalBook1Ent + totalBook2Ent + totalBook3Ent + totalBook4Ent + totalBook5Ent)
            varPrice.set(str(totalBookPrice) + "$")

        def search_book():
            global mid
            search_text = search_entry.get()
            with open('books_data.json', 'r') as file:
                users = json.load(file)


            low = 0
            high = len(users) -1
            found = False

            while low <= high:
                mid = (low + high) // 2
                book = users[mid]['text']

                if search_text == book:
                    found = True
                    break
                elif search_text < book:
                    high = mid - 1
                else:
                    low = mid + 1



            if found:
                book_label = Label(Fab, text=users[mid]['text'] + ' ✓', fg='gold', bg='darkblue',
                                   font=('tajawal', 16, 'bold'))
                book_label.place(x=users[mid]['x'], y=positions[mid][1])
            else:
                messagebox.showinfo("Not Found", "The book was not found.")






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







        search_label = tk.Label(Fab, text="Search for Item:", bg='darkblue', fg='gold',
                                font=('tajawal', 16, 'bold'))
        search_label.place(x=70, y=460)

        search_entry = tk.Entry(Fab, width=18, justify='center')
        search_entry.place(x=250, y=466)

        boAddToCard = Button(Fab, text='add to card', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                             command=addToCard)
        boAddToCard.place(x=25, y=350)

        back_button = tk.Button(Fab, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                command=self.back_to_home)
        back_button.place(x=20, y=20)

        search = Button(Fab,text='search', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                        command=search_book)
        search.place(x=170, y=490)

        varBook1 = IntVar()
        varBook2 = IntVar()
        varBook3 = IntVar()
        varBook4 = IntVar()
        varBook5 = IntVar()

        varPrice = StringVar()

        book1ent = Entry(Fab, textvariable=varBook1, width=18, justify='center')
        book1ent.place(x=25, y=310)

        book2ent = Entry(Fab, textvariable=varBook2, width=18, justify='center')
        book2ent.place(x=185, y=310)

        book3ent = Entry(Fab, textvariable=varBook3, width=18, justify='center')
        book3ent.place(x=345, y=310)

        book4ent = Entry(Fab, textvariable=varBook4, width=18, justify='center')
        book4ent.place(x=505, y=310)

        book5ent = Entry(Fab, textvariable=varBook5, width=18, justify='center')
        book5ent.place(x=665, y=310)

        priceBooks = Label(Fab, text='Price:', fg='gold', bg='darkblue', font=('tajawal', 16, 'bold'))
        priceBooks.place(x=505, y=460)

        bookprice = Entry(Fab, textvariable=varPrice, width=18, justify='center')
        bookprice.place(x=585, y=466)

        totalprice = Button(Fab, text='Calc', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                            command=calculate_total)
        totalprice.place(x=570, y=490)






    def Electronics(self):
        with open('Elctronics_data.json', 'r') as file:
            users = json.load(file)

        def addToCard():
            newWindow = Toplevel(self.shop)
            newWindow.title("Online Shopping")
            newWindow.geometry("800x600+280+50")
            newWindow.iconbitmap('supermarkets.ico')
            Label(newWindow, text='cart', fg='gold', bg='black',
                  font=('tajawal', 16, 'bold')).pack(fill=tk.X)
            Fab3 = tk.Frame(newWindow, height=800, bg='darkblue')
            Fab3.pack(fill=tk.X)
            back_button = tk.Button(Fab3, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                    command=self.back_to_home)
            back_button.place(x=20, y=20)

            list = [varBook1.get(), varBook2.get(), varBook3.get(), varBook4.get(), varBook5.get()]


            positions = [(20, 200), (180, 200), (340, 200), (500, 200), (660, 200)]
            label_list = []

            for i in range(len(list)):
                if list[i] != 0:
                    mytext = users[i]['text']
                    cart = Label(Fab3, text=mytext, font=('Helvetica 20 bold'), bg='darkblue', fg='gold')
                    cart.place(x=positions[i][0], y=positions[i][1])
                    label_list.append(cart)

            ul = 'https://wa.me/01128828067?text=i want to bay book 1'

            def open():
                webbrowser.open_new(ul)

            pay_button = tk.Button(Fab3, text='Go to pay by vodafone cash', width=30, fg='black', bg='#DBA901',
                                   font=('tajawal', 16, 'bold'),
                                   command=open)
            pay_button.place(x=220, y=400)

            ul2 = 'https://www.facebook.com/LifeMakersEGY'

            def open2():
                webbrowser.open_new(ul2)

            pay_button = tk.Button(Fab3, text='to connect with us', width=20, fg='black', bg='#DBA901',
                                   font=('tajawal', 16, 'bold'),
                                   command=open2)
            pay_button.place(x=50, y=500)

            def destroyy():
                for label in label_list:
                    label.destroy()

            back_button = tk.Button(Fab3, text='Remove from cart', width=30, fg='black', bg='#DBA901',
                                    font=('tajawal', 16, 'bold'),
                                    command=destroyy)
            back_button.place(x=220, y=300)

        def calculate_total():
            totalBook1Ent = int(varBook1.get()) * 50
            totalBook2Ent = int(varBook2.get()) * 90
            totalBook3Ent = int(varBook3.get()) * 90
            totalBook4Ent = int(varBook4.get()) * 90
            totalBook5Ent = int(varBook5.get()) * 90
            totalBookPrice = float(totalBook1Ent + totalBook2Ent + totalBook3Ent + totalBook4Ent + totalBook5Ent)
            varPrice.set(str(totalBookPrice) + "$")

        def search_book():
            global mid
            search_text = search_entry.get()
            with open('Elctronics_data.json', 'r') as file:
                users = json.load(file)


            low = 0
            high = len(users) - 1
            found = False

            while low <= high:
                mid = (low + high) // 2
                book = users[mid]['text']

                if search_text == book:
                    found = True
                    break
                elif search_text < book:
                    high = mid - 1
                else:
                    low = mid + 1

            if found:
                book_label = Label(Fab, text=users[mid]['text'] + ' ✓', fg='gold', bg='darkblue',
                                   font=('tajawal', 16, 'bold'))
                book_label.place(x=users[mid]['x'], y=positions[mid][1])
            else:
                messagebox.showinfo("Not Found", "The book was not found.")

        newWindow = Toplevel(self.shop)
        newWindow.title("Online Shopping")
        newWindow.geometry("800x600+280+50")
        newWindow.iconbitmap('supermarkets.ico')
        Label(newWindow, text='Books', fg='gold', bg='black', font=('tajawal', 16, 'bold')).pack(fill=tk.X)
        Fab = tk.Frame(newWindow, height=800, bg='darkblue')
        Fab.pack(fill=tk.X)


        with open('Elctronics_data.json', 'r') as file:
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


        search_label = tk.Label(Fab, text="Search for Item:", bg='darkblue', fg='gold',
                                font=('tajawal', 16, 'bold'))
        search_label.place(x=70, y=460)

        search_entry = tk.Entry(Fab, width=18, justify='center')
        search_entry.place(x=250, y=466)

        boAddToCard = Button(Fab, text='add to card', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                             command=addToCard)
        boAddToCard.place(x=25, y=350)

        back_button = tk.Button(Fab, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                command=self.back_to_home)
        back_button.place(x=20, y=20)

        search = Button(Fab, text='search', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                        command=search_book)
        search.place(x=170, y=490)

        varBook1 = IntVar()
        varBook2 = IntVar()
        varBook3 = IntVar()
        varBook4 = IntVar()
        varBook5 = IntVar()

        varPrice = StringVar()

        book1ent = Entry(Fab, textvariable=varBook1, width=18, justify='center')
        book1ent.place(x=25, y=310)

        book2ent = Entry(Fab, textvariable=varBook2, width=18, justify='center')
        book2ent.place(x=185, y=310)

        book3ent = Entry(Fab, textvariable=varBook3, width=18, justify='center')
        book3ent.place(x=345, y=310)

        book4ent = Entry(Fab, textvariable=varBook4, width=18, justify='center')
        book4ent.place(x=505, y=310)

        book5ent = Entry(Fab, textvariable=varBook5, width=18, justify='center')
        book5ent.place(x=665, y=310)

        priceBooks = Label(Fab, text='Price:', fg='gold', bg='darkblue', font=('tajawal', 16, 'bold'))
        priceBooks.place(x=505, y=460)

        bookprice = Entry(Fab, textvariable=varPrice, width=18, justify='center')
        bookprice.place(x=585, y=466)

        totalprice = Button(Fab, text='Calc', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                            command=calculate_total)
        totalprice.place(x=570, y=490)



    def Fashion(self):
        with open('Fashion.json', 'r') as file:
            users = json.load(file)

        def addToCard():
            newWindow = Toplevel(self.shop)
            newWindow.title("Online Shopping")
            newWindow.geometry("800x600+280+50")
            newWindow.iconbitmap('supermarkets.ico')
            Label(newWindow, text='cart', fg='gold', bg='black',
                  font=('tajawal', 16, 'bold')).pack(fill=tk.X)
            Fab3 = tk.Frame(newWindow, height=800, bg='darkblue')
            Fab3.pack(fill=tk.X)
            back_button = tk.Button(Fab3, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                    command=self.back_to_home)
            back_button.place(x=20, y=20)

            list = [varBook1.get(), varBook2.get(), varBook3.get(), varBook4.get(), varBook5.get()]


            positions = [(20, 200), (180, 200), (340, 200), (500, 200), (660, 200)]
            label_list = []

            for i in range(len(list)):
                if list[i] != 0:
                    mytext = users[i]['text']
                    cart = Label(Fab3, text=mytext, font=('Helvetica 20 bold'), bg='darkblue', fg='gold')
                    cart.place(x=positions[i][0], y=positions[i][1])
                    label_list.append(cart)

            ul = 'https://wa.me/01128828067?text=i want to bay book 1'

            def open():
                webbrowser.open_new(ul)

            pay_button = tk.Button(Fab3, text='Go to pay by vodafone cash', width=30, fg='black', bg='#DBA901',
                                   font=('tajawal', 16, 'bold'),
                                   command=open)
            pay_button.place(x=220, y=400)

            ul2 = 'https://www.facebook.com/LifeMakersEGY'

            def open2():
                webbrowser.open_new(ul2)

            pay_button = tk.Button(Fab3, text='to connect with us', width=20, fg='black', bg='#DBA901',
                                   font=('tajawal', 16, 'bold'),
                                   command=open2)
            pay_button.place(x=50, y=500)

            def destroyy():
                for label in label_list:
                    label.destroy()

            back_button = tk.Button(Fab3, text='Remove from cart', width=30, fg='black', bg='#DBA901',
                                    font=('tajawal', 16, 'bold'),
                                    command=destroyy)
            back_button.place(x=220, y=300)

        def calculate_total():
            totalBook1Ent = int(varBook1.get()) * 50
            totalBook2Ent = int(varBook2.get()) * 90
            totalBook3Ent = int(varBook3.get()) * 90
            totalBook4Ent = int(varBook4.get()) * 90
            totalBook5Ent = int(varBook5.get()) * 90
            totalBookPrice = float(totalBook1Ent + totalBook2Ent + totalBook3Ent + totalBook4Ent + totalBook5Ent)
            varPrice.set(str(totalBookPrice) + "$")

        def search_book():
            global mid
            search_text = search_entry.get()
            with open('Fashion.json', 'r') as file:
                users = json.load(file)


            low = 0
            high = len(users) - 1
            found = False

            while low <= high:
                mid = (low + high) // 2
                book = users[mid]['text']

                if search_text == book:
                    found = True
                    break
                elif search_text < book:
                    high = mid - 1
                else:
                    low = mid + 1

            if found:
                book_label = Label(Fab, text=users[mid]['text'] + ' ✓', fg='gold', bg='darkblue',
                                   font=('tajawal', 16, 'bold'))
                book_label.place(x=users[mid]['x'], y=positions[mid][1])
            else:
                messagebox.showinfo("Not Found", "The book was not found.")

        newWindow = Toplevel(self.shop)
        newWindow.title("Online Shopping")
        newWindow.geometry("800x600+280+50")
        newWindow.iconbitmap('supermarkets.ico')
        Label(newWindow, text='Books', fg='gold', bg='black', font=('tajawal', 16, 'bold')).pack(fill=tk.X)
        Fab = tk.Frame(newWindow, height=800, bg='darkblue')
        Fab.pack(fill=tk.X)


        with open('Fashion.json', 'r') as file:
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


        search_label = tk.Label(Fab, text="Search for Item:", bg='darkblue', fg='gold',
                                font=('tajawal', 16, 'bold'))
        search_label.place(x=70, y=460)

        search_entry = tk.Entry(Fab, width=18, justify='center')
        search_entry.place(x=250, y=466)

        boAddToCard = Button(Fab, text='add to card', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                             command=addToCard)
        boAddToCard.place(x=25, y=350)

        back_button = tk.Button(Fab, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                command=self.back_to_home)
        back_button.place(x=20, y=20)

        search = Button(Fab, text='search', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                        command=search_book)
        search.place(x=170, y=490)

        varBook1 = IntVar()
        varBook2 = IntVar()
        varBook3 = IntVar()
        varBook4 = IntVar()
        varBook5 = IntVar()

        varPrice = StringVar()

        book1ent = Entry(Fab, textvariable=varBook1, width=18, justify='center')
        book1ent.place(x=25, y=310)

        book2ent = Entry(Fab, textvariable=varBook2, width=18, justify='center')
        book2ent.place(x=185, y=310)

        book3ent = Entry(Fab, textvariable=varBook3, width=18, justify='center')
        book3ent.place(x=345, y=310)

        book4ent = Entry(Fab, textvariable=varBook4, width=18, justify='center')
        book4ent.place(x=505, y=310)

        book5ent = Entry(Fab, textvariable=varBook5, width=18, justify='center')
        book5ent.place(x=665, y=310)

        priceBooks = Label(Fab, text='Price:', fg='gold', bg='darkblue', font=('tajawal', 16, 'bold'))
        priceBooks.place(x=505, y=460)

        bookprice = Entry(Fab, textvariable=varPrice, width=18, justify='center')
        bookprice.place(x=585, y=466)

        totalprice = Button(Fab, text='Calc', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                            command=calculate_total)
        totalprice.place(x=570, y=490)



    def Sports(self):
        with open('Sport.json', 'r') as file:
            users = json.load(file)

        def addToCard():
            newWindow = Toplevel(self.shop)
            newWindow.title("Online Shopping")
            newWindow.geometry("800x600+280+50")
            newWindow.iconbitmap('supermarkets.ico')
            Label(newWindow, text='cart', fg='gold', bg='black',
                  font=('tajawal', 16, 'bold')).pack(fill=tk.X)
            Fab3 = tk.Frame(newWindow, height=800, bg='darkblue')
            Fab3.pack(fill=tk.X)
            back_button = tk.Button(Fab3, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                    command=self.back_to_home)
            back_button.place(x=20, y=20)

            list = [varBook1.get(), varBook2.get(), varBook3.get(), varBook4.get(), varBook5.get()]


            positions = [(20, 200), (180, 200), (340, 200), (500, 200), (660, 200)]
            label_list = []

            for i in range(len(list)):
                if list[i] != 0:
                    mytext = users[i]['text']
                    cart = Label(Fab3, text=mytext, font=('Helvetica 20 bold'), bg='darkblue', fg='gold')
                    cart.place(x=positions[i][0], y=positions[i][1])
                    label_list.append(cart)

            ul = 'https://wa.me/01128828067?text=i want to bay book 1'

            def open():
                webbrowser.open_new(ul)

            pay_button = tk.Button(Fab3, text='Go to pay by vodafone cash', width=30, fg='black', bg='#DBA901',
                                   font=('tajawal', 16, 'bold'),
                                   command=open)
            pay_button.place(x=220, y=400)

            ul2 = 'https://www.facebook.com/LifeMakersEGY'

            def open2():
                webbrowser.open_new(ul2)

            pay_button = tk.Button(Fab3, text='to connect with us', width=20, fg='black', bg='#DBA901',
                                   font=('tajawal', 16, 'bold'),
                                   command=open2)
            pay_button.place(x=50, y=500)

            def destroyy():
                for label in label_list:
                    label.destroy()

            back_button = tk.Button(Fab3, text='Remove from cart', width=30, fg='black', bg='#DBA901',
                                    font=('tajawal', 16, 'bold'),
                                    command=destroyy)
            back_button.place(x=220, y=300)

        def calculate_total():
            totalBook1Ent = int(varBook1.get()) * 50
            totalBook2Ent = int(varBook2.get()) * 90
            totalBook3Ent = int(varBook3.get()) * 90
            totalBook4Ent = int(varBook4.get()) * 90
            totalBook5Ent = int(varBook5.get()) * 90
            totalBookPrice = float(totalBook1Ent + totalBook2Ent + totalBook3Ent + totalBook4Ent + totalBook5Ent)
            varPrice.set(str(totalBookPrice) + "$")

        def search_book():
            global mid
            search_text = search_entry.get()
            with open('Sport.json', 'r') as file:
                users = json.load(file)


            low = 0
            high = len(users) - 1
            found = False

            while low <= high:
                mid = (low + high) // 2
                book = users[mid]['text']

                if search_text == book:
                    found = True
                    break
                elif search_text < book:
                    high = mid - 1
                else:
                    low = mid + 1

            if found:
                book_label = Label(Fab, text=users[mid]['text'] + ' ✓', fg='gold', bg='darkblue',
                                   font=('tajawal', 16, 'bold'))
                book_label.place(x=users[mid]['x'], y=positions[mid][1])
            else:
                messagebox.showinfo("Not Found", "The book was not found.")

        newWindow = Toplevel(self.shop)
        newWindow.title("Online Shopping")
        newWindow.geometry("800x600+280+50")
        newWindow.iconbitmap('supermarkets.ico')
        Label(newWindow, text='Books', fg='gold', bg='black', font=('tajawal', 16, 'bold')).pack(fill=tk.X)
        Fab = tk.Frame(newWindow, height=800, bg='darkblue')
        Fab.pack(fill=tk.X)


        with open('Sport.json', 'r') as file:
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


        search_label = tk.Label(Fab, text="Search for Item:", bg='darkblue', fg='gold',
                                font=('tajawal', 16, 'bold'))
        search_label.place(x=70, y=460)

        search_entry = tk.Entry(Fab, width=18, justify='center')
        search_entry.place(x=250, y=466)

        boAddToCard = Button(Fab, text='add to card', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                             command=addToCard)
        boAddToCard.place(x=25, y=350)

        back_button = tk.Button(Fab, text='Back', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                                command=self.back_to_home)
        back_button.place(x=20, y=20)

        search = Button(Fab, text='search', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                        command=search_book)
        search.place(x=170, y=490)

        varBook1 = IntVar()
        varBook2 = IntVar()
        varBook3 = IntVar()
        varBook4 = IntVar()
        varBook5 = IntVar()

        varPrice = StringVar()

        book1ent = Entry(Fab, textvariable=varBook1, width=18, justify='center')
        book1ent.place(x=25, y=310)

        book2ent = Entry(Fab, textvariable=varBook2, width=18, justify='center')
        book2ent.place(x=185, y=310)

        book3ent = Entry(Fab, textvariable=varBook3, width=18, justify='center')
        book3ent.place(x=345, y=310)

        book4ent = Entry(Fab, textvariable=varBook4, width=18, justify='center')
        book4ent.place(x=505, y=310)

        book5ent = Entry(Fab, textvariable=varBook5, width=18, justify='center')
        book5ent.place(x=665, y=310)

        priceBooks = Label(Fab, text='Price:', fg='gold', bg='darkblue', font=('tajawal', 16, 'bold'))
        priceBooks.place(x=505, y=460)

        bookprice = Entry(Fab, textvariable=varPrice, width=18, justify='center')
        bookprice.place(x=585, y=466)

        totalprice = Button(Fab, text='Calc', width=10, fg='black', bg='#DBA901', font=('tajawal', 16, 'bold'),
                            command=calculate_total)
        totalprice.place(x=570, y=490)



    def create_buttons(self):
        # حذف Buttons الحالية
        for button in self.F1.winfo_children():
            button.destroy()

        # ترتيب buttons بناء على الترتيب المحدد
        if self.sort_ascending:
            sorted_buttons = self.sort_ascending_custom(self.buttons, key=lambda x: x[0])  # ترتيب تصاعدي
        else:
            sorted_buttons = self.sort_descending_custom(self.buttons, key=lambda x: x[0])  # ترتيب تنازلي

        button_list = [(20, 10), (440, 10), (20, 80), (440, 80)]

        for i in range(len(button_list)):
            x, y = button_list[i]
            button_text = sorted_buttons[i]
            button = tk.Button(self.F1, text=button_text, width=26, fg='black', bg='#DBA901',
                               font=('tajawal', 16, 'bold'))
            button.place(x=x, y=y)
            if button_text == "Books":
                button.configure(command=self.books)
            elif button_text == "Electronics":
                button.configure(command=self.Electronics)
            elif button_text == "Fashion":
                button.configure(command=self.Fashion)
            elif button_text == "Sports":
                button.configure(command=self.Sports)
    def sort_ascending_custom(self, arr, key=lambda x: x):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if key(arr[j]) > key(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def sort_descending_custom(self, arr, key=lambda x: x):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if key(arr[j]) < key(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def toggle_sort(self):
        self.sort_ascending = not self.sort_ascending
        self.create_buttons()

    def back_to_home(self):
        self.shop.deiconify()

        # إظهار النافذة الأصلية






login_app = LoginApplication(tk.Tk())
tk.mainloop()

# shop = Tk()
# ob = homeApplication(shop)
# shop.mainloop()
