import tkinter as tk

class LoginWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.attempts = 0
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Login")
        self.pack()

        # Username label and entry
        self.username_label = tk.Label(self, text="Username")
        self.username_label.grid()
        self.username_entry = tk.Entry(self)
        self.username_entry.grid()

        # Password label and entry
        self.password_label = tk.Label(self, text="Password")
        self.password_label.grid()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid()

        # Login button
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.grid()

        #Details
        self.secret_txt = tk.Text(self, width=35, height=5, wrap=tk.WORD)
        self.secret_txt.grid(row=5, column=0, columnspan=2, sticky=tk.W)

    def login(self):
        message = ""
        # Check the credentials
        if self.username_entry.get() == "user" and self.password_entry.get() == "pass":
            # If the credentials are correct, open a new window
            self.master.withdraw()
            new_window = tk.Toplevel(self.master)
            new_window.title("Welcome!")
            tk.Label(new_window, text="Welcome!").grid()

        else:
            # If the credentials are incorrect, increment the attempts counter
            self.attempts += 1
            if self.attempts >= 3:
                # If there have been 3 or more failed attempts, exit the program
                self.master.quit()
            else:
                # Otherwise, display an error message
                message = "Error: " + "Incorrect username or password."
                self.secret_txt.delete(0.0, tk.END)
                self.secret_txt.insert(0.0, message)


root = tk.Tk()
root.geometry("200x85")
app = LoginWindow(master=root)
app.mainloop()
