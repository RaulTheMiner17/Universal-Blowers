import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, parent, on_login):
        super().__init__(parent)
        self.on_login = on_login
        
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()
        
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "admin123":
            self.on_login()
        else:
            tk.messagebox.showerror("Login Error", "Invalid username or password.")
    
class BuyMachinePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.machine_label = tk.Label(self, text="Choose a machine to buy:")
        self.machine_label.pack()
        
        self.machine_listbox = tk.Listbox(self)
        self.machine_listbox.insert(1, "Lathe Machine")
        self.machine_listbox.insert(2, "Drilling Machine")
        self.machine_listbox.insert(3, "Milling Machine")
        self.machine_listbox.pack()
        
        self.buy_button = tk.Button(self, text="Buy Machine", command=self.buy_machine)
        self.buy_button.pack()
    
    def buy_machine(self):
        selected_machine = self.machine_listbox.get(tk.ACTIVE)
        tk.messagebox.showinfo("Success", f"You have bought a {selected_machine}.")
        

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Industrial Machine Store")
        self.geometry("400x300")
        
        self.login_page = LoginPage(self, self.show_buy_machine_page)
        self.login_page.pack(expand=True)
        
    def show_buy_machine_page(self):
        self.login_page.pack_forget()
        self.buy_machine_page = BuyMachinePage(self)
        self.buy_machine_page.pack(expand=True)

#if __name__ == "__main__":
app = MainWindow()
app.mainloop()
