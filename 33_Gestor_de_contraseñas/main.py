from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- GENERADOR DE CONTRASEÑAS ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    x="".join(password_list)
    password_entry.insert(0,x)
    pyperclip.copy(x)

# ---------------------------- GUARDAR CONTRASEÑA ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    
    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Complete toda la información") 

    else:  
        is_ok=messagebox.askokcancel(title="Confirmación",message=f"Ingresaste los siguientes datos: \n Website: {website} \n Email: {email} \n Password: {password}\n ¿Son correctos?")

        if is_ok:
            with open("passwords.txt","a") as passwords:
                passwords.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0,END)       

# ---------------------------- DISEÑO UI ------------------------------- #
window = Tk()
window.title("Administrador de Contraseñas")
window.config(padx=50, pady=50) # Aumenté un poco el padding para que respire

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0,"youremail@gmail.com")
email_entry.focus()

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")
password_entry.focus()

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()