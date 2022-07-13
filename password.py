from tkinter import *
from tkinter import messagebox
import random 
import json
window=Tk()
window.config(bg="#5F9EA0",padx=60,pady=60)
window.title("password app")
### Seach Methode
def search():
    thewebsite=website_e.get()
    try :
        with open("passowrd_generator_app\Data.json","r") as file :
            Database=json.load(file)
        email1=Database[thewebsite]["email"]
        pass1=Database[thewebsite]["password"]
    except FileNotFoundError :
        messagebox.showerror(title="Error",message="No Data in File")
    except KeyError :
        messagebox.showerror(title="Error",message="No Data Found1")
    else :
        messagebox.showinfo(title=f"{thewebsite}",message=f"Email :{email1} \npassword : {pass1}")
    
####   password generator ####
def password ():
    passw_e.delete(0,END)
    len_ltr=random.randint(8,10)
    len_nbr=random.randint(2,4)
    len_spc=random.randint(2,4)
    letters=["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "q","r", "s", "t", "u", "v", "w","x", "y", "z"]
    specials=["#","!","&","*","+","%",")","("]
    numbers=["1","2","3","4","5","6","7","8","9"]
    password=[]
    letters1=[random.choice(letters)  for letter  in range(len_ltr) ]
    spc=[random.choice(specials)  for spc  in range(len_spc)] 
    nbr=[random.choice(numbers)  for nbr  in range(len_nbr) ]
    password1=""
    password=letters1 +spc +nbr
    for char in password :
        password1+=char   
    passw_e.insert(0,f"{password1}")  
    
    
###              Save passowrd  ####
def butpass():
    thewebsite=website_e.get()
    theemail=email_e.get()
    thepass=passw_e.get()
    new_data={
        thewebsite:{
        "email":theemail,
        "password":thepass
        }
              }
    if len(thewebsite)==0 or len(thepass)==0 :
            messagebox.showerror(title="nod",message="tbali rak nsit 3fsa ! ")
    else :
        # answr=messagebox.askokcancel(title="Cancel",message="Are you sure you want to continue ? ")    
        # if answr == True : 
            messagebox.showinfo(title="Important",message="Email and password Saved succefully")
            try :
                with open("passowrd_generator_app\Data.json") as file :
                    data=json.load(file)
            except FileNotFoundError :
                with open("passowrd_generator_app\Data.json","w") as file:
                    json.dump(new_data,file,indent=5)
            else:
                data.update(new_data)
                with open("passowrd_generator_app\Data.json","w") as file:
                    json.dump(data,file,indent=5)
            finally :
                website_e.delete(0,END)
                passw_e.delete(0,END)
  
  
## Image 
canvas=Canvas(width=256,height=256,bg="#5F9EA0",highlightthickness=0)
Image=PhotoImage(file="passowrd_generator_app\secure-icon-png-4988.png")
canvas.create_image(128,128,image=Image)
canvas.grid(row=0,column=1)
## website
website=Label(text="Website :",font=("arial",10,"bold"),bg="#5F9EA0")
website.grid(row=1,column=0)
website_e=Entry(text="Website :",width=40)
website_e.grid(row=1,column=1)
website_b=Button(text="Search",width=13,command=search)
website_b.grid(row=1,column=2)

website_e.focus()

##email
email=Label(text="Email/Username :",font=("arial",10,"bold"),bg="#5F9EA0")
email.grid(row=2,column=0)
email_e=Entry(text="Email/Username :",width=60)
email_e.grid(row=2,column=1,columnspan=2)
email_e.insert(0,"Fbekkouche149@gmail.com")
##password
passw=Label(text="Password :",font=("arial",10,"bold"),bg="#5F9EA0")
passw.grid(row=3,column=0)
passw_e=Entry(text="Passowrd :",width=40)
passw_e.grid(row=3,column=1)
passw_b=Button(text="generate Password",command=password)
passw_b.grid(row=3,column=2)
##add
passw1_b=Button(text="Add",font=("arial",10,"bold"),width=45,command=butpass)
passw1_b.grid(row=4,column=1,columnspan=2)
passw1_b=Button(text="Leave",font=("arial",10,"bold"),width=20)
passw1_b.place(x=-60,y=370)




window.mainloop()