from tkinter import *
from tkinter import messagebox
import ast

    
def main_application():
    def hide_bg_change():
    
        hm_btn.config(bg="blue",fg="white")
        mem_btn.config(bg="blue", fg="white")

    def bg_change(button):
        hide_bg_change()
        current_color = button.cget("bg")
        new_color = 'cyan'  # Adjusted to lowercase 'cyan'
        if current_color != new_color:
            button.config(bg=new_color, fg='black')
        else:
            pass

    def show_page(page_func):
        for widget in main_content_fm.winfo_children():
            widget.destroy()
        page_func()

# Content for home page
    def hm_page():
        hide_bg_change()  # Ensure buttons maintain their original color
        hm_btn.config(bg='cyan', fg='black')
    
        hm_page_fm = Frame(main_content_fm)
        hm_page_content = Frame(hm_page_fm)
        hm_page_text = Label(hm_page_content, text="ako", font=("arial", 25), fg="red")
        hm_page_text.pack()
        hm_page_content.pack()
        hm_page_fm.pack(fill=BOTH, expand=True)

# Content for members page
    def mem_page():
        mem_page_fm = Frame(main_content_fm)
        mem_page_content = Frame(mem_page_fm)
        mem_page_text = Label(mem_page_content, text="ao", font=("arial", 25), fg="red")
        mem_page_text.pack()
        mem_page_content.pack()
        mem_page_fm.pack(fill=BOTH, expand=True)
    
# Function to resize the image without external libraries
    def resize_image(img, width, height):
        return img.subsample(width, height)

    window = Tk()
    window.geometry("800x600")
    window.title("Chorale")

    logo = PhotoImage(file="img/logo.png")
    window.iconphoto(True, logo) 



#This for the icons in the buttons
    orig_img = PhotoImage(file="img/home.png")
    img = resize_image(orig_img, 18, 18)
    orig_img1 = PhotoImage(file="img/group.png")
    img1 = resize_image(orig_img1, 18, 18)
    orig_image_vphs = PhotoImage(file="img/vphs.png")
    img2 = resize_image(orig_image_vphs, 3, 3)
#Menu bar on the left side
    menu_bar = Frame(window, padx=30, bg="blue")
    menu_bar.pack(side="left")
    menu_bar.pack_propagate(False)
    menu_bar.configure(width=300, height=920)

#LOGO
    vphs = Label(menu_bar, bg="darkblue", fg="white", image=img2, compound=LEFT, text="VPHS | CHORALE", font=("bobby jones", 15, "bold"))
    vphs.pack(side=TOP, pady=10)
    vphs.pack(anchor="nw")

# main content
    main_content_fm = Frame(window, highlightbackground="black", highlightthickness=3)
    main_content_fm.pack(fill=BOTH, expand=True, side=LEFT)

# For buttons
    hm_btn = Button(menu_bar, padx=23, text="Schedules", fg="white", font=('Bold', 12), bd=0, bg="blue", image=img, compound=LEFT, command=lambda: (bg_change(hm_btn), show_page(hm_page)))
    hm_btn.place(x=35, y=100)

    mem_btn = Button(menu_bar, padx=23, text="Members", fg="white", font=('Bold', 12), bd=0, bg="blue", image=img1, compound=LEFT, command=lambda: (bg_change(mem_btn), show_page(mem_page)))
    mem_btn.place(x=35, y=150)

    hm_page()
    window.mainloop()
    
def login_window():
    def handle_login():
        username = "username"  # Replace with your username
        password = "password"  # Replace with your password

        entered_username = username_entry.get()
        entered_password = password_entry.get()

        if entered_username == username and entered_password == password:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
            login.destroy()  # Close the login window
            main_application()  # Open the main application window after successful login
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

#Function to resize the image without external libraries
    def resize_image(img, width, height):
        return img.subsample(width, height)

    def username_on_hover(e):
        username_entry.delete(0, "end")

    def username_on_unhover(e):
        username_value = username_entry.get()
        if username_value == "":
            username_entry.insert(0, "Name")

    def password_on_hover(e):
        password_entry.delete(0, "end")

    def password_on_unhover(e):
        password_value = password_entry.get()
        if password_value == "":
            password_entry.insert(0, "Password")
        

  

    login = Tk()
    login.geometry("850x500")
    login.title("Login | Chorale")
    login.resizable(False, False)
    login.configure(bg="white")
    
    orig_img = PhotoImage(file="img/login.png")
    img = resize_image(orig_img, 3,3)
    Label(login, image=img, bg="white").place(x=50, y=50)
    
    login_frame=Frame(login, width=350, height=350, bg="white")
    login_frame.place(x=480, y=70)
    
    signin_heading= Label(login_frame, text="Log In", fg="skyblue", bg="white", font=("Nue Einstellung", 23))
    signin_heading.place(x=100, y=5)
    

    username_entry = Entry(login_frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    username_entry.place(x=30, y=80)
    username_entry.insert(0, "Name")
    Frame(login_frame, width=295, height=2, bg="black").place(x=25, y=107)
    username_entry.bind("<FocusIn>", username_on_hover)
    username_entry.bind("<FocusOut>", username_on_unhover)

    password_entry = Entry(login_frame, width=25, fg="black", border=0, bg="white", font=("", 11))
    password_entry.place(x=30, y=150)
    password_entry.insert(0, "Password")
    Frame(login_frame, width=295, height=2, bg="black").place(x=25, y=177)
    password_entry.bind("<FocusIn>", password_on_hover)
    password_entry.bind("<FocusOut>", password_on_unhover)

    create_button = Button(login_frame, width=39, pady=7, bg="grey", fg="white", border=0, text="Log In", command=handle_login)
    create_button.place(x=33, y=204)

    create_acc = Label(login_frame, text="Don't have an account?", fg="black", bg="white", font=("Nue Einstellung", 9))
    create_acc.place(x=60, y=270)

    signup_btn= Button(login_frame, width=13, text="Create Account", border=0, fg="skyblue", bg="white")
    signup_btn.place(x=190, y=270)
    

    login.mainloop()
    

if __name__ == "__main__":
    login_window()