#ezcite python gui
from tkinter import * 
import tkinter as tk  
from tkinter import messagebox
import webbrowser 
import os
from playsound import playsound
import pyglet




 
#Define GUI size and window title
window = tk.Tk()
window.configure(background='aqua')
window.title('ezCite Ver.1.0.0a')  
cwd_icon = os.getcwd() + r'\assets\images\appicon.png'
cwd_bt = os.getcwd() + r'\assets\images\button_help-faq.png'
cwd_bt1 = os.getcwd() + r'\assets\images\button_about-the-devs.png'
cwd_bt2 = os.getcwd() + r'\assets\images\button_settings.png'
cwd_bt3 = os.getcwd() + r'\assets\images\button_mla-website-citation.png'
cwd_bt4 = os.getcwd() + r'\assets\images\button_mla-book-citation.png'
cwd_bt5 = os.getcwd() + r'\assets\images\button_apa-website-citation.png'
cwd_bt6 = os.getcwd() + r'\assets\images\button_apa-book-citation.png'
cwd_submit = os.getcwd() + r'\assets\images\button_submit.png'
cwd_sound = os.getcwd() + r'\assets\images\button_sound.png'
cwd_creds = os.getcwd() + r'\assets\images\button_credits.png'
cwd_music = os.getcwd() + r'\assets\images\button_music.png'
cwd_credits = os.getcwd() + r'\scrtext.py'


cwdbtclick1 = os.getcwd() + r'\assets\sound\b_click_variation1.wav'
def bt1():
   playsound(cwdbtclick1)

cwdfont1 = os.getcwd() + r'\assets\fonts\Ubuntu-Regular.ttf'
pyglet.font.add_file(cwdfont1)
ubuntu = pyglet.font.load('Ubuntu Regular')


window.geometry('800x830')  
window.minsize(800, 830)
window.maxsize(800, 830)

#APP ICON
p1 = PhotoImage(file = cwd_icon)
window.iconphoto(False, p1) 


#Titles
title = tk.Label(window, text='ezCite - The Ultimate Citation Generator', bg='aqua', font=('Ubuntu Regular', 20), width=40, height=3)
title.pack()    



#Button 1 (HELP)
def helpec():
   bt1()
   webbrowser.open('https://leodeng.gitbook.io/ecwiki/getting-started/installation/installation-video')

click_btn= PhotoImage(file=cwd_bt)

b1 = tk.Button(image=click_btn, command = helpec, borderwidth=0, bg='#00FFFF', activebackground='#00FFFF')
b1.pack(pady=10)


#Button 2 (About)
def abec():
   bt1()
   messagebox.showinfo( "About the Devs (VERY JUICY STUFF hAhAh)", "Leo: Hello Stranger! \n(Or maybe friend in this situation, ok if u know me dont look haha) \nI'm Leo! One of the developers of ezCite,\na 12 year old developer that likes to code(lol)\nI admire Linus Torvalds and also like to use ubuntu/fedora.\nI mainly code in: Python, HTML, Markdown, and CSS(a little)\n\n\n\n\nAllen:")

click_btn1= PhotoImage(file=cwd_bt1)

b2 = tk.Button(image=click_btn1, command = abec, borderwidth=0, bg='#00FFFF', activebackground='#00FFFF')
b2.pack(pady=10)

#Settings function buttons
click_btn_sound= PhotoImage(file=cwd_sound)
click_btn_creds= PhotoImage(file=cwd_creds)
click_btn_music= PhotoImage(file=cwd_music)

#Button 3 (Settings)
def s():
   bt1()
   def soundprefs():
      pass
   def musicprefs():
      pass
   def showcredits():
      from scrtext import credsmusic
   pref = Toplevel(window)
   pref.title("ezCite Ver.1.0.0a - Settings")
   pref.geometry("800x600")
   pref.configure(background='aqua')
   Label(pref,text ="ezCite Preferences", bg='aqua', font=('Ubuntu Regular', 20), width=40, height=3).pack()

   sound = Button(pref, image=click_btn_sound, command=soundprefs, borderwidth=0, bg='#00FFFF', activebackground='#00FFFF')
   sound.pack(pady=15)

   creds = Button(pref, image=click_btn_creds, command=showcredits, borderwidth=0, bg='#00FFFF', activebackground='#00FFFF')
   creds.pack(pady=15)

   music = Button(pref, image=click_btn_music, command=musicprefs, borderwidth=0, bg='#00FFFF', activebackground='#00FFFF')
   music.pack(pady=15)

   
click_btn2= PhotoImage(file=cwd_bt2)

b2 = tk.Button(image=click_btn2, command = s, borderwidth=0, bg='#00FFFF', activebackground='#00FFFF')
b2.pack(pady=10)


#SUBMIT BUTTON
click_btn_submit= PhotoImage(file=cwd_submit)

#Button 4 (MLA 8 Website Citation)
def mla8web():
   bt1()
   mla8webwin = Toplevel(window)
   mla8webwin.title("ezCite Ver.1.0.0a - MLA 8 Website Citation")
   mla8webwin.geometry("800x600")
   mla8webwin.configure(background='aqua')
   Label(mla8webwin,text ="ezCite - MLA 8 Website Citation Generator", bg='aqua', font=('Ubuntu Regular', 20), width=40, height=3).pack()
   Label(mla8webwin, text = 'Website (JSTOR is not supported)', bg='aqua', font=('Ubuntu Regular', 15)).pack()
   
   entrymla8web = Entry(mla8webwin, font=('Ubuntu Regular',11)).pack(ipadx= 250)
   def process_mla8_web_req():
      input = entrymla8web.get("1.0",END)
      print(input)

   submit = Button(mla8webwin, image=click_btn_submit, command=process_mla8_web_req, borderwidth=0, bg='#00FFFF', activebackground='#00FFFF')
   submit.pack(pady=15)
   label=Label(mla8webwin, text="", font=("Comic Sans MS"))
   label.pack()

   

click_btn3= PhotoImage(file=cwd_bt3)

b2 = tk.Button(image=click_btn3, command = mla8web, borderwidth=0, bg='#00FFFF', activebackground='#00FFFF')
b2.pack(pady=10)



#Button 5 (MLA 8 Book Citation)
def mla8book():
   bt1()
   pass
   
click_btn4= PhotoImage(file=cwd_bt4)

b2 = tk.Button(image=click_btn4, command = mla8book, borderwidth=0, bg='#00FFFF', activebackground='#00FFFF')
b2.pack(pady=10)




#Button 6 (APA 7 Website Citation)
def apa7web():
   bt1()
   pass
   
click_btn5= PhotoImage(file=cwd_bt5)

b2 = tk.Button(image=click_btn5, command = apa7web, borderwidth=0, bg='#00FFFF', activebackground='#00FFFF')
b2.pack(pady=10)



#Button 7 (APA 7 Book Citation)
def apa7book():
   bt1()
   pass
   
click_btn6= PhotoImage(file=cwd_bt6)

b2 = tk.Button(image=click_btn6, command = apa7book, borderwidth=0, bg='#00FFFF', activebackground='#00FFFF')
b2.pack(pady=10)




  

window.mainloop()