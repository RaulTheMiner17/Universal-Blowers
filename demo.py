import tkinter as tk
import mysql.connector

# Create a connection to the database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="universal_blowers"
)

# Create a cursor to execute database queries
cursor = db.cursor()

# Create the login window
class LoginWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Query the database for the user with the given username and password
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            self.master.switch_frame(BuyingWindow)
        else:
            tk.messagebox.showerror("Error", "Invalid username or password")

# Create the buying window
class BuyingWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.machine_label = tk.Label(self, text="Machine Name")
        self.machine_label.pack()

        self.machine_entry = tk.Entry(self)
        self.machine_entry.pack()

        self.quantity_label = tk.Label(self, text="Quantity")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack()

        self.buy_button = tk.Button(self, text="Buy", command=self.buy)
        self.buy_button.pack()

    def buy(self):
        machine_name = self.machine_entry.get()
        quantity = int(self.quantity_entry.get())

        # Insert the purchase into the database
        cursor.execute("INSERT INTO purchases (machine_name, quantity) VALUES (%s, %s)", (machine_name, quantity))
        db.commit()

        tk.messagebox.showinfo("Success", "Purchase made successfully")

# Create the main application window
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Industrial Machine Store")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginWindow, BuyingWindow):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.switch_frame(LoginWindow)

    def switch_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

# Start the application
app = App()
app.mainloop()

# Close the database connection
db.close()
