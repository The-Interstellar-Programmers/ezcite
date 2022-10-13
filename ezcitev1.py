#ezcitev1
# By Leodeng


import requests
from bs4 import BeautifulSoup
import os
import time
import datetime
from datetime import date
 
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
        mla8book = input("Enter Book ISBN Number:")
        isbn1 = "https://www.isbnsearcher.com/books/" + mla8book
        reqs = requests.get(isbn1)
        soup = BeautifulSoup(reqs.text, 'lxml')
        for heading in soup.find_all(["h1"]):
            heading.text.strip()
        soup = BeautifulSoup(reqs.text, 'html.parser')
        author = soup.find_all ('text-success')
        bookname = heading.text.strip()
        print(author)
    
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







