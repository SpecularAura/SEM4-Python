import tkinter as tk

class LoginWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.userList = {}
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

        # Add User Button
        self.add_user_button = tk.Button(self, text="New User", command=self.newuser)
        self.add_user_button.grid()

        #Details
        self.secret_txt = tk.Text(self, width=35, height=5, wrap=tk.WORD)
        self.secret_txt.grid(row=6, column=0, columnspan=2, sticky=tk.W)
    def newuser(self):
        # self.master.withdraw()
        new_window = tk.Toplevel(self.master)
        new_window.title("Welcome!")
        
        # Username label and entry
        self.new_username_label = tk.Label(new_window, text="Username")
        self.new_username_label.grid()
        self.new_username_entry = tk.Entry(new_window)
        self.new_username_entry.grid()

        # Password label and entry
        self.new_password_label = tk.Label(new_window, text="Password")
        self.new_password_label.grid()
        self.new_password_entry = tk.Entry(new_window, show="*")
        self.new_password_entry.grid()

        # Login button
        self.new_login_button = tk.Button(new_window, text="Create User", command=lambda: self.createUser(new_window))
        self.new_login_button.grid()

    def createUser(self, new_window):
        with open(r'userdata.txt', "a") as file1:
            username = self.new_username_entry.get()
            password = self.new_password_entry.get()
            if self.validCredentials(username, password):
                file1.write(f'{username}:{password},')
        new_window.withdraw()

    # Checks if the new user 
    def validCredentials(username, password):
        if password.length < 8: 
            return False
        return True 

    def isValidUser(self, entered_user_name, entered_pasword):
        with open(r'userdata.txt', 'r') as file1:
            for line in file1:
                for user in line.split(','):
                    print(user)
                    username, password = user.split(':')
                    if username == entered_user_name and password == entered_pasword:
                        return True
        return False


    def login(self):
        message = ""
        # Check the credentials
        # if self.username_entry.get() == "user" and self.password_entry.get() == "pass":
        if self.isValidUser(self.username_entry.get(), self.password_entry.get()):
            # If the credentials are correct, open a new window
            self.master.destroy()
            new_window = tk.Tk()
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
root.geometry("360x360")
app = LoginWindow(master=root)
app.mainloop()