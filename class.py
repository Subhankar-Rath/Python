from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Student Form")

# Correct icon loading
icon_path = r"D:\PlacementML\pixel2.ico"   # change if your folder is different
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

root.geometry('500x500+0+0')
root.configure(background="#0D0070")

# Load image
img = Image.open("star.png")
resize_img = img.resize((100, 70))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root, image=img, bg="#003870")
img_label.pack(pady=10, padx=20)

# Title label
text_label = Label(root, text="Giet Bucks",
                   font=('Arial', 18, 'bold'),
                   bg="#220070",
                   fg='white')
text_label.pack(pady=10, padx=20)

# Email
email_label = Label(root, text="Email",
                    font=('Arial', 18, 'bold'),
                    bg="#003870",
                    fg='white')
email_label.pack(pady=(20, 5))

email_entry = Entry(root, font=('Arial', 18),
                    fg='white', bg='grey')
email_entry.pack(pady=(5, 10))

# Password
password_label = Label(root, text="Password",
                       font=('Arial', 18, 'bold'),
                       bg="#003870",
                       fg='white')
password_label.pack(pady=(20, 5))

password_entry = Entry(root, font=('Arial', 18),
                       fg='white', bg='grey',
                       show="*")
password_entry.pack(pady=(5, 10))

# Login button
login_btn = Button(root, text="Login",
                   font=('Arial', 18, 'bold'),
                   bg="#CB4814",
                   fg='white')
login_btn.pack(pady=(10, 10))

root.mainloop()
