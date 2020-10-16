from tkinter import *
from get_train_set import *
from datetime import *

counter = 0

week = int ( datetime.today().isocalendar() [1] )


def update (a,b):
    global counter
    
    if b == 'x':
        b = 0
        a = week
        counter = 0
    else:
        counter += b
        a += counter
   
    train_set = get_train_set(a)
    
    txtLbl1.configure (text = train_set[0])
    txtLbl2.configure (text = train_set[2])
    txtLbl3.configure (text = train_set[4])

    img1.configure (file = train_set[1])
    img2.configure (file = train_set[3])
    img3.configure (file = train_set[5])

    curr_week.configure (text = str(a) +'th week')

   

window = Tk()

window.geometry('435x250')
window.title ('Training schedule')
window.configure(background = 'White')
window.resizable  (0,0)


day1 = Label (window, text = 'MON', font = ('Arial', 20), bg = 'White')
day2 = Label (window, text = 'WED',font = ('Arial', 20), bg = 'White')
day3 = Label (window, text = 'FRI', font = ('Arial', 20),bg = 'White')


img1 = PhotoImage (file = 'default.png', width = 100, height = 100)
img2 = PhotoImage (file = 'default.png', width = 100, height = 100)
img3 = PhotoImage (file = 'default.png', width = 100, height = 100)

imgLbl1 = Label (window, image = img1)
imgLbl2 = Label (window, image = img2)
imgLbl3 = Label (window, image = img3)

txtLbl1 = Label (window, font = ('Arial', 12), bg = 'White')
txtLbl2 = Label (window, font = ('Arial', 12), bg = 'White')
txtLbl3 = Label (window, font = ('Arial', 12), bg = 'White')

img_home = PhotoImage (file = 'home (3).gif')
btn_home = Button (window, image = img_home,  relief = 'ridge', command = lambda: update(week,'x'))

img_next = PhotoImage (file = 'next.gif')
btn_next = Button (window, image = img_next, relief = 'ridge', command = lambda: update (week,1))

img_prev = PhotoImage (file = 'prev.gif')
btn_prev = Button (window, image = img_prev, relief = 'ridge', command = lambda: update (week,-1))

curr_week = Label (window, text = str(week) + 'th week', font = ('Arial', 15),bg = 'White')

day1.place (x = 30, y = 10)
day2.place (x = 180, y = 10)
day3.place (x = 345, y = 10)

imgLbl1.place (x = 10, y = 50)
imgLbl2.place (x = 160, y = 50)
imgLbl3.place (x = 320, y = 50)

txtLbl1.place (x = 35, y = 160)
txtLbl2.place (x = 200, y = 160)
txtLbl3.place (x = 345, y = 160)

can = Canvas (window, width = 435, height = 2, bg = '#4286f4')
can.create_line (0,0, 435, 0, width = 2, fill = '#4286f4')

can.place (x = 0, y = 185)

btn_home.place (x = 15, y = 200)
btn_prev.place (x = 335, y = 200)
btn_next.place (x = 381, y = 200)

curr_week.place (x = 160, y = 190)


update(week,0)

window.mainloop()
