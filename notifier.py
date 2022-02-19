# ================================ my notifier desktop ============
from plyer import notification
from tkinter import *
from tkinter import messagebox
import time
# creat the window app
app = Tk()
app.title("baalidev Notifier")
app.geometry("500x350")
app.config(bg='#d1d1d1')

# lable and input 1
title = Label(app, text="Title to notify",font=("Verdana", 16),fg="#000", bg='#d1d1d1')
title.place(x=15, y=10)
title_input = Entry(app,width=30,font=("Verdana", 16) , borderwidth=3, relief="flat")
title_input.place(x=15 ,y=50)

# lable and input 2
msg = Label(app, text="Display Message",font=("Verdana", 16),fg="#000", bg='#d1d1d1')
msg.place(x=15, y=100)
msg_input = Entry(app,width=30,font=("Verdana", 16) , borderwidth=3, relief="flat" )
msg_input.place(x=15 ,y=150)

# lable and input 3
set = Label(app, text="Set Time",font=("Verdana", 16),fg="#000", bg='#d1d1d1')
set.place(x=15, y=200)
set_input = Entry(app,width=5,font=("Verdana", 16) , borderwidth=3, relief="flat" )
set_input.place(x=120 ,y=200)
min = Label(app, text="Min",font=("Verdana", 16),fg="#000",bg='#d1d1d1')
min.place(x=200, y=200)

def doIt():
    get_title = title_input.get()
    get_msg = msg_input.get()
    get_min = set_input.get()
    if get_title == "" or get_msg == "" or get_min == "":
        messagebox.showerror("Alert!!", "All The Input Are Required")
    else:
        get_min_int = int(float(get_min))
        min_to_sec = get_min_int * 60
        messagebox.showinfo("notifier set", "set Notification?")
        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message= get_msg,
                            app_name='notifier',
                            app_icon='Paomedia-Small-N-Flat-Bell.ico',
                            timeout=10)
# button
btn = Button(app, text="submit",command=doIt, borderwidth=0,
                bg="#D50",fg="black",font=("Verdana", 16),
                pady=5, padx=10)
btn.place(x=15, y=250)
app.mainloop()
