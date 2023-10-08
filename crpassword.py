import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    password_length = 12  # You can change this to your desired password length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)  # Clear the previous password
    password_entry.insert(0, password)

# Function to accept the generated password
def accept_password():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}\nPassword: {password}")

# Function to reset the username and password fields
def reset_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

# Generate password button
generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.pack()

# Accept button
accept_button = tk.Button(root, text="Accept", command=accept_password)
accept_button.pack()

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.pack()

root.mainloop()