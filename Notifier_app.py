from tkinter import *
from  PIL import Image,ImageTk
from tkinter import messagebox
from plyer import notification
import time

t=Tk()
t.title("Notifier-App")
t.geometry("700x500")
img=Image.open("combined.png.png")
tkimage=ImageTk.PhotoImage(img)

#get details
def get_details():
    get_title=title.get()
    get_msg=msg.get()
    get_time=time1.get()

    if get_title =="" or get_msg=="" or get_time=="":
        messagebox.showerror("Alert",'All fields are mandatory')

    else:
        int_time=int (float(get_time))
        min_to_sec=int_time*60
        messagebox.showinfo("Notifier set","Set notification")
        t.destroy()


        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon="icon.ico.ico",
                            timeout=10)

img_label=Label(t,image=tkimage).grid()

#label1
t_label=Label(t,text="Title To Notify",font=("poppins",10))
t_label.place(x=12,y=120)

#entry1

title=Entry(t,width="25",font=("poppins",13))
title.place(x=123,y=120)

#label2
m_label=Label(t,text="Display Message",font=("poppins",10))
m_label.place(x=12,y=160)

#entry2
msg=Entry(t,width="40",font=("poppins",13))
msg.place(x=123,y=160,height=30)


#label3
time_label=Label(t,text="Set Time",font=("poppins",10))
time_label.place(x=12,y=200)

#entry3
time1=Entry(t,width="5",font=("poppins",13))
time1.place(x=123,y=200)

#label4
time_min_label=Label(t,text="",font=("poppins",10))
time_min_label.place(x=175,y=180)

#button
but=Button(t,text="SET NOTIFICATION",font=("poppins",10,'bold'),fg="#ffffff",bg="#528DFF",width=20,relief="raised",
           command=get_details)
but.place(x=170,y=250)

t.resizable(0,0)
t.mainloop()