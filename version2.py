import Tkinter as tk
from bs4 import BeautifulSoup as bs
import requests
from PIL import ImageTk, Image
import webbrowser
from Tkconstants import *
window=tk.Tk()
window.geometry("600x600")
window.title("Indian Railway Enquery")
window["bg"] = "yellow"

#for new window
def newwin():
    win=tk.Tk()
    win.title("Indian Railway Enquery")
    buttun2=tk.Button(win,text="Back",bg="pink",command=win.destroy)
    buttun2.grid(column=20,row=20)
    #irctc
    
    def bro():
        webbrowser.open('https://www.irctc.co.in/eticketing/loginHome.jsf', new=1)

    buttun3=tk.Button(win,text="GO TO IRCTC WEBSITE",bg="orange",command=bro)
    buttun3.grid(column=19,row=20)
    def main():
        try:
            p=str(entry1.get())
            q=str(entry2.get())
            date=str(entry3.get())
            url="https://www.cleartrip.com/trains/results?from_station="+p+"&to_station="+q+"&class=SL&date="+date
            data=requests.get(url)
            data1=data.text
            soup=bs(data1,'lxml')
            ok=soup.title.string[11:]
            title=tk.Label(win,text=ok,font=("Corbel",12),bg='red')
            title.grid(column=1,row=10)
            par=soup.body.find_all('script')
            dar=par[11].text
            car=dar[30:]
            car1=car.split('}}')
            cata=car1[0]
            city=cata.split('"},"')
            i=13
            try:
                    for ram in city:
                        ras=ram.split(',')
                        ras[15]
                        #number
                        lab1=tk.Label(win,text=ras[1][12:17])
                        lab1.grid(column=0,row=i)
                        #train no.
                        lab2=tk.Label(win,text=ras[2][8:len(ras[2])-1])
                        lab2.grid(column=1,row=i)
                        #departure station
                        lab3=tk.Label(win,text=ras[4][8:len(ras[4])-1])
                        lab3.grid(column=2,row=i)
                        #arrive station
                        lab4=tk.Label(win,text=ras[7][6:len(ras[7])-1])
                        lab4.grid(column=3,row=i)
                        #arrive time
                        lab5=tk.Label(win,text=ras[9][15:20])
                        lab5.grid(column=4,row=i)
                        #depart time
                        lab6=tk.Label(win,text=ras[10][15:20])
                        lab6.grid(column=5,row=i)
                        #distance
                        lab7=tk.Label(win,text=ras[11][11:len(ras[11])])
                        lab7.grid(column=6,row=i)
                        #arrive date
                        lab8=tk.Label(win,text=ras[14][15:len(ras[14])-1])
                        lab8.grid(column=7,row=i)
                        #depart date
                        lab9=tk.Label(win,text=ras[15][15:len(ras[15])-1])
                        lab9.grid(column=8,row=i)
                        #1st
                        st=ras[23][14:len(ras[23])]
                        try:
                            p=int(st)
                            p=st
                        except:
                            p="NO AC"

                        lab10=tk.Label(win,text=p)
                        lab10.grid(column=9,row=i)
                        #2ed
                        st=ras[24]
                        try:
                            p=int(st)
                            p=st
                        except:
                            p="NO 2AC"
                    
                        lab11=tk.Label(win,text=p)
                        lab11.grid(column=10,row=i)
                        #3rd
                        st=ras[25]
                        try:
                            p=int(st)
                            p=st
                        except:
                            p="NO 3AC"
                        lab12=tk.Label(win,text=p)
                        lab12.grid(column=11,row=i)
                        #SL
                        st=ras[26][0:len(ras[26])-1]
                        try:
                            p=int(st)
                            p=st
                        except:
                            p="NO SL"
                        
                        lab13=tk.Label(win,text=p)
                        lab13.grid(column=12,row=i)
                        i=i+1
                        del ras
                    lab1=tk.Label(win,text="Number")
                    lab1.grid(column=0,row=12)
                    lab2=tk.Label(win,text="Train_Name")
                    lab2.grid(column=1,row=12)
                    lab4=tk.Label(win,text="Departure_Station")
                    lab4.grid(column=2,row=12)
                    lab5=tk.Label(win,text="Arrive_Station")
                    lab5.grid(column=3,row=12)
                    lab6=tk.Label(win,text="Arrive_Time")
                    lab6.grid(column=4,row=12)
                    lab7=tk.Label(win,text="Depart_Time")
                    lab7.grid(column=5,row=12)
                    lab8=tk.Label(win,text="Distance")
                    lab8.grid(column=6,row=12)
                    lab9=tk.Label(win,text="Arrive_Date")
                    lab9.grid(column=7,row=12)
                    lab10=tk.Label(win,text="Depart_Date")
                    lab10.grid(column=8,row=12)
                    lab11=tk.Label(win,text="1st_AC")
                    lab11.grid(column=9,row=12)
                    lab12=tk.Label(win,text="2ed_AC")
                    lab12.grid(column=10,row=12)
                    lab13=tk.Label(win,text="3rd_AC")
                    lab13.grid(column=11,row=12)
                    lab14=tk.Label(win,text="SL")
                    lab14.grid(column=12,row=12)
                
                    
            except:
                lab=tk.Label(win,text="'Oops',There is no direct train found\n \n \n")
                lab.grid(column=0,row=12)
        except:
            labc=tk.Label(win,text="'Oops', SOMETHING WENT WRONG")
            labc.grid()

    main()    
# label----
label1=tk.Label(text="WELCOME TO INDIAN RAILWAY",font=("Corbel",15),bg="pink")
label1.grid(column=1,row=0)
label2=tk.Label(text="Enter Departure Station Code",font=("Corbel",10),bg="yellow")
label2.grid(column=0,row=1)
label3=tk.Label(text="Enter   Arrivel   Station  Code",font=("Corbel",10),bg="yellow")
label3.grid(column=0,row=2)
label4=tk.Label(text="Enter Date (Date-Month-Year)",font=("Corbel",10),bg="yellow")
label4.grid(column=0,row=3)
#entry field
entry1=tk.Entry()
entry1.grid(column=1,row=1)
entry2=tk.Entry()
entry2.grid(column=1,row=2)
entry3=tk.Entry()
entry3.grid(column=1,row=3)
#button===
button1=tk.Button(text="Find Trains",bg="green",command=newwin)
button1.grid(column=1,row=8)
button1=tk.Button(text="EXIT",bg="red",command=window.destroy)
button1.grid(column=2,row=8)
####PIL have to download




window.mainloop()
