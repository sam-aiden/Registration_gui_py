import tkinter as tk
win = tk.Tk()
win.title("Registration Form")
win.config(bg='lightblue')
win.geometry('700x600')#widthXheight
win.iconbitmap('Anime.ico')
#win.resizable(False,False)

#text_label
Title = tk.Label(win,text='Registration',font=('Times new roman',20,'italic'),fg="black",bg="lightblue",)
Title.pack(padx=5,pady=5)

#Image 
bg=tk.PhotoImage(file='pfp.png')
Img =tk.Label(win,image=bg,bg='lightblue')
Img.pack()

#Tk_varibles
Gen_var =tk.StringVar()
Gen_var.set(None)


#Button functions 
def save_func():
    global name1,age1,gender1,dob1,phone1,address1,email1,password1
    name1 = Name_entry.get()
    age1 = Age_entry.get()
    dob1 = D_O_B_entry.get()
    gender1 = Gen_var.get()
    phone1 = Phone_no_entry.get()
    address1 = Address_entry.get()
    email1 = Email_entry.get()
    password1 = Password_entry.get()
    print("the values are stored in the variable")
    pass

def show_details():
    import tkinter as tk
    root = tk.Toplevel()
    root.title("User Details")
    root.config(bg="lightblue")
    root.geometry('700x600')
    root.iconbitmap('logo.ico')

    #text_label
    Title = tk.Label(root,text='User Details',font=('Times new roman',20,'italic'),fg="black",bg="lightblue")
    Title.pack(padx=5,pady=5)

    #Image 
    bg=tk.PhotoImage(file='profile.png')
    Img =tk.Label(root,image=bg,bg="lightblue")
    Img.pack()

    #Frame 
    frame1 = tk.Frame(root,bg='lightcyan',height=450,width=400)
    frame1.pack()

    #Label 
    name = tk.Label(frame1,text='Name',fg="black",bg="lightblue")
    name.place(relx=0.125,rely=0.022,relheight=0.05,relwidth=0.17)

    Age = tk.Label(frame1,text='Age',fg="black",bg="lightblue")
    Age.place(relx=0.125,rely=0.1,relheight=0.05,relwidth=0.17)

    Gender = tk.Label(frame1,text='Gender',fg="black",bg="lightblue")
    Gender.place(relx=0.125,rely=0.177,relheight=0.05,relwidth=0.17)

    D_O_B = tk.Label(frame1,text='D.O.B',fg="black",bg="lightblue")
    D_O_B.place(relx=0.125,rely=0.25,relheight=0.05,relwidth=0.17)

    Phone_no = tk.Label(frame1,text='Phone_no',fg="black",bg="lightblue")
    Phone_no.place(relx=0.125,rely=0.33,relheight=0.05,relwidth=0.17)

    Address = tk.Label(frame1,text='Address',fg="black",bg="lightblue")
    Address.place(relx=0.125,rely=0.41,relheight=0.05,relwidth=0.17)

    Email = tk.Label(frame1,text='Email',fg="black",bg="lightblue")
    Email.place(relx=0.125,rely=0.48,relheight=0.05,relwidth=0.17)

    Password = tk.Label(frame1,text='Password',fg="black",bg="lightblue")
    Password.place(relx=0.125,rely=0.56,relheight=0.05,relwidth=0.17)

    #label_Label
    Name_label = tk.Label(frame1,text=f'{name1}')
    Name_label.place(relx=0.32,rely=0.022,relheight=0.05,relwidth=0.50)

    Age_label = tk.Label(frame1,text=f'{age1}')
    Age_label.place(relx=0.32,rely=0.1,relheight=0.05,relwidth=0.50)


    Gender_btn =tk.Label(frame1,text=f'{gender1}')                  
    Gender_btn.place(relx=0.32,rely=0.177,relheight=0.05,relwidth=0.50)

    D_O_B_label = tk.Label(frame1,text=f'{dob1}')
    D_O_B_label.place(relx=0.32,rely=0.25,relheight=0.05,relwidth=0.50)

    Phone_no_label = tk.Label(frame1,text=f'{phone1}')
    Phone_no_label.place(relx=0.32,rely=0.33,relheight=0.05,relwidth=0.50)


    Address_label = tk.Label(frame1,text=f'{address1}')
    Address_label.place(relx=0.32,rely=0.41,relheight=0.05,relwidth=0.50)

    Email_label = tk.Label(frame1,text=f'{email1}')
    Email_label.place(relx=0.32,rely=0.48,relheight=0.05,relwidth=0.50)

    Password_label = tk.Label(frame1,text=f'{password1}')
    Password_label.place(relx=0.32,rely=0.56,relheight=0.05,relwidth=0.50)



    root.mainloop()
    pass

#Frame 
frame1 = tk.Frame(win,bg='lightblue',height=450,width=400)
frame1.pack()

#Label 
name = tk.Label(frame1,text='Name',fg="black",bg="lightblue")
name.place(relx=0.125,rely=0.022,relheight=0.05,relwidth=0.17)

Age = tk.Label(frame1,text='Age',fg="black",bg="lightblue")
Age.place(relx=0.125,rely=0.1,relheight=0.05,relwidth=0.17)

Gender = tk.Label(frame1,text='Gender',fg="black",bg="lightblue")
Gender.place(relx=0.125,rely=0.177,relheight=0.05,relwidth=0.17)

D_O_B = tk.Label(frame1,text='D.O.B',fg="black",bg="lightblue")
D_O_B.place(relx=0.125,rely=0.25,relheight=0.05,relwidth=0.17)

Phone_no = tk.Label(frame1,text='Phone_no',fg="black",bg="lightblue")
Phone_no.place(relx=0.125,rely=0.33,relheight=0.05,relwidth=0.17)

Address = tk.Label(frame1,text='Address',fg="black",bg="lightblue")
Address.place(relx=0.125,rely=0.41,relheight=0.05,relwidth=0.17)

Email = tk.Label(frame1,text='Email',fg="black",bg="lightblue")
Email.place(relx=0.125,rely=0.48,relheight=0.05,relwidth=0.17)

Password = tk.Label(frame1,text='Password',fg="black",bg="lightblue")
Password.place(relx=0.125,rely=0.56,relheight=0.05,relwidth=0.17)

#Entry_Label
Name_entry = tk.Entry(frame1)
Name_entry.place(relx=0.32,rely=0.022,relheight=0.05,relwidth=0.37)

Age_entry = tk.Entry(frame1)
Age_entry.place(relx=0.32,rely=0.1,relheight=0.05,relwidth=0.37)

#Gender_entry = tk.Entry(frame1)
#Gender_entry.place(relx=0.32,rely=0.177,relheight=0.05,relwidth=0.37)
Gender_btn =tk.Radiobutton(frame1,text='Male',value="Male",variable=Gen_var)                  
Gender_btn.place(relx=0.32,rely=0.177)

Gender_btn1 =tk.Radiobutton(frame1,text='Female',value="Female",variable=Gen_var)                  
Gender_btn1.place(relx=0.50,rely=0.177)

D_O_B_entry = tk.Entry(frame1)
D_O_B_entry.place(relx=0.32,rely=0.25,relheight=0.05,relwidth=0.37)

Phone_no_entry = tk.Entry(frame1)
Phone_no_entry.place(relx=0.32,rely=0.33,relheight=0.05,relwidth=0.37)

Address_entry = tk.Entry(frame1)
Address_entry.place(relx=0.32,rely=0.41,relheight=0.05,relwidth=0.37)

Email_entry = tk.Entry(frame1)
Email_entry.place(relx=0.32,rely=0.48,relheight=0.05,relwidth=0.37)

Password_entry = tk.Entry(frame1)
Password_entry.place(relx=0.32,rely=0.56,relheight=0.05,relwidth=0.37)

#button 
submit_btn =tk.Button(frame1,text="submit",command=save_func)
submit_btn.place(relx=0.20,rely=0.70)

show_btn =tk.Button(frame1,text="show",command=show_details)
show_btn.place(relx=0.50,rely=0.70)

win.mainloop()