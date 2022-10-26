#ezcitev1
# By Leodeng


import requests
from bs4 import BeautifulSoup
import os
from datetime import date
import csv
import pygame
from pygame import mixer
import time
import subprocess

pygame.mixer.init()
pygame.mixer.music.load("ezs.mp3")

 
today = date.today()

while True:
    os.system("clear")
    print("""                                                                                                  
                                             CCCCCCCCCCCCC  iiii          tttt                              
                                          CCC::::::::::::C i::::i      ttt:::t                              
                                        CC:::::::::::::::C  iiii       t:::::t                              
                                       C:::::CCCCCCCC::::C             t:::::t                              
    eeeeeeeeeeee    zzzzzzzzzzzzzzzzz C:::::C       CCCCCCiiiiiiittttttt:::::ttttttt        eeeeeeeeeeee    
  ee::::::::::::ee  z:::::::::::::::zC:::::C              i:::::it:::::::::::::::::t      ee::::::::::::ee  
 e::::::eeeee:::::eez::::::::::::::z C:::::C               i::::it:::::::::::::::::t     e::::::eeeee:::::ee
e::::::e     e:::::ezzzzzzzz::::::z  C:::::C               i::::itttttt:::::::tttttt    e::::::e     e:::::e
e:::::::eeeee::::::e      z::::::z   C:::::C               i::::i      t:::::t          e:::::::eeeee::::::e
e:::::::::::::::::e      z::::::z    C:::::C               i::::i      t:::::t          e:::::::::::::::::e 
e::::::eeeeeeeeeee      z::::::z     C:::::C               i::::i      t:::::t          e::::::eeeeeeeeeee  
e:::::::e              z::::::z       C:::::C       CCCCCC i::::i      t:::::t    tttttte:::::::e           
e::::::::e            z::::::zzzzzzzz  C:::::CCCCCCCC::::Ci::::::i     t::::::tttt:::::te::::::::e          
 e::::::::eeeeeeee   z::::::::::::::z   CC:::::::::::::::Ci::::::i     tt::::::::::::::t e::::::::eeeeeeee  
  ee:::::::::::::e  z:::::::::::::::z     CCC::::::::::::Ci::::::i       tt:::::::::::tt  ee:::::::::::::e  
    eeeeeeeeeeeeee  zzzzzzzzzzzzzzzzz        CCCCCCCCCCCCCiiiiiiii         ttttttttttt      eeeeeeeeeeeeee                                                                                               
                                                             
                                                             
                        1111111                000000000     
                       1::::::1              00:::::::::00   
                      1:::::::1            00:::::::::::::00 
                      111:::::1           0:::::::000:::::::0
vvvvvvv           vvvvvvv1::::1           0::::::0   0::::::0
 v:::::v         v:::::v 1::::1           0:::::0     0:::::0
  v:::::v       v:::::v  1::::1           0:::::0     0:::::0
   v:::::v     v:::::v   1::::l           0:::::0 000 0:::::0
    v:::::v   v:::::v    1::::l           0:::::0 000 0:::::0
     v:::::v v:::::v     1::::l           0:::::0     0:::::0
      v:::::v:::::v      1::::l           0:::::0     0:::::0
       v:::::::::v       1::::l           0::::::0   0::::::0
        v:::::::v     111::::::111        0:::::::000:::::::0
         v:::::v      1::::::::::1 ......  00:::::::::::::00 
          v:::v       1::::::::::1 .::::.    00:::::::::00   
           vvv        111111111111 ......      000000000     
    """
    )
    print("ezCite v1.0 Main Menu:\n\n")
    print("1. MLA 8 Citation (Website)\n")
    print("2. MLA 8 Citation (Book)\n")
    print("3. APA 7 Citation (Website)\n")
    print("4. APA 7 Citation (Book)\n")


    i = input("Your Choice: ")

    if i == "1":
        os.system("clear")
        mla8web = input("Enter Website Address:")
        url = mla8web
        print("\n\n")
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for title in soup.find_all('title'):
            title.get_text()
        websitetitle = title.get_text()
        link = mla8web
        citedate = today.strftime("%d %b. %Y.")
        mla8_webcite_result = websitetitle + ". " + link + ". " + "Accessed " + citedate
        print(mla8_webcite_result)
        input("\n\nPress Enter To Go Back...")

    if i == "2":
        os.system("clear")
        mla8book = input("Enter Book ISBN Number (Please ONLY Enter a book with an isbn-13 number):")
        isbn1 = "https://www.isbnsearcher.com/books/" + mla8book
        reqs = requests.get(isbn1)


        soup = BeautifulSoup(reqs.text, 'lxml')

        for heading in soup.find_all(["h1"]):
            heading.text.strip()
            booktitlemla = heading.text.strip()

        #Converting the HTML content to a Soup object
        html_soup_object = BeautifulSoup(reqs.text, 'html.parser')

        

        bookpub = html_soup_object.find_all(class_="text-success")
        for publisher in bookpub:
            if "publisher" in str(publisher):
                publisher.text.strip()
                bookpublishermla = publisher.text.strip()

        

        year = html_soup_object.find_all(class_="col-8 col-sm-9 mb-1")
        for pubyear in year:
            if "-" in str(pubyear):
                pubyear.text.strip()
                yearmla = pubyear.text.strip()


        #Finding all the elements by using class name called "text-success"
        author = html_soup_object.find_all(class_="text-success")
        for author in author:
            if "author" in str(author):
                author.text.strip()
                author = author.text.strip()


            citedatebookmla8 = today.strftime("%d %b. %Y.")
            mla8_bookcite_result = bookpublishermla + yearmla
            print(mla8_bookcite_result)
            input("\n\nPress Enter To Go Back...")



                


        input("\n\nPress Enter To Go Back...")



    if i == "3":
        os.system("clear")
        apa7web = input("Enter Website Address:")
        url = apa7web
        print("\n\n")
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for title in soup.find_all('title'):
            title.get_text()
        websitetitle = title.get_text()
        link = apa7web
        citedateapa = today.strftime("%b %d, %Y,")
        apa7web_webcite_result = "(n.d.). " + websitetitle + " Retrieved " + citedateapa + " from " + link 
        print(apa7web_webcite_result)
        input("\n\nPress Enter To Go Back...")


    if i == "4":
        os.system("clear")
        apa7book = input("Enter Book ISBN Number:")

    if i == "magicDJleo":
        os.system("clear")
        print("""
 _____ _            __  __             _        ____      _   _               
|_   _| |__   ___  |  \/  | __ _  __ _(_) ___  |  _ \    | | | |    ___  ___  
  | | | '_ \ / _ \ | |\/| |/ _` |/ _` | |/ __| | | | |_  | | | |   / _ \/ _ \ 
  | | | | | |  __/ | |  | | (_| | (_| | | (__  | |_| | |_| | | |__|  __/ (_) |
  |_| |_| |_|\___| |_|  |_|\__,_|\__, |_|\___| |____/ \___/  |_____\___|\___/ 
                                 |___/                                        
        \n\n"""
        )
        print("""
         _   _                 ____  _             _                 
        | \ | | _____      __ |  _ \| | __ _ _   _(_)_ __   __ _   _ 
 _____  |  \| |/ _ \ \ /\ / / | |_) | |/ _` | | | | | '_ \ / _` | (_)
|_____| | |\  | (_) \ V  V /  |  __/| | (_| | |_| | | | | | (_| |  _ 
        |_| \_|\___/ \_/\_/   |_|   |_|\__,_|\__, |_|_| |_|\__, | (_)
                                             |___/         |___/     
        \n"""
        )
        print("""
 _   _   _        _____      ____ _ _____           ___         ____ 
| |_| | | | ___  | ____|____/ ___(_)_   _|__   ___ / _ \ _ __  / ___|
| __| |_| |/ _ \ |  _| |_  / |   | | | |/ _ \ / __| | | | '_ \| |  _ 
| |_|  _  |  __/ | |___ / /| |___| | | |  __/ \__ \ |_| | | | | |_| |
 \__|_| |_|\___| |_____/___|\____|_| |_|\___| |___/\___/|_| |_|\____|
                                                                     
        \n"""
        )
        pygame.mixer.music.play()
        while True:
            os.system("clear")
            mdlps = input("\n\nType 's' to end this wonderfullll music......\n(IF YOU STOP MUSIC, I'LL FIND YOUR HOUSE AND PUT A Bigggg SPEAKER THERE AND PLAY MY EZCITE MUSIC FOREVER!!!! lol ;3)\n\n'p' to pause music...........\n\nand 'r' to resume MuSic.......\n")
            if mdlps == "s":
                pygame.mixer.music.stop()
                break
            if mdlps == "p":
                pygame.mixer.music.pause()
            if mdlps == "r":
                pygame.mixer.music.unpause()
        input("\n\nPress Enter To Go Back...")


    if i == "d0nutboi":
        subprocess.call(["python3", "d0nut.py"])
        input("Press ENTER to quit")
        time.sleep(1)
        continue








