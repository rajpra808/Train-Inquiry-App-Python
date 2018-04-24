import Tkinter as tk
from bs4 import BeautifulSoup as bs
import requests

window=tk.Tk()
window.geometry("1300x800")
# define function
def main():
    p=str(entry1.get())
    q=str(entry2.get())
    date=str(entry3.get())
    url="https://www.cleartrip.com/trains/results?from_station="+p+"&to_station="+q+"&class=SL&date="+date
    data=requests.get(url)
    data1=data.text
    soup=bs(data1,'lxml')
    ok=soup.title.string[11:]
    title=tk.Label(window,text=ok,font=("Corbel",12),bg='red')
    title.grid(column=1,row=10)
    par=soup.body.find_all('script',type="text/javascript")
    dar=par[2].text
    car=dar[30:]
    car1=car.split('}}')
    cata=car1[0]
    city=cata.split('"},"')
    i=13
    try:
            for ram in city:
                ras=ram.split(',')
                ras[15]
                lab1=tk.Label(text=ras[1][12:17])
                lab1.grid(column=0,row=i)
                lab2=tk.Label(text=ras[2][8:len(ras[2])-1])
                lab2.grid(column=1,row=i)
                lab3=tk.Label(text=ras[4][8:len(ras[4])-1])
                lab3.grid(column=2,row=i)
                lab4=tk.Label(text=ras[7][6:len(ras[7])-1])
                lab4.grid(column=3,row=i)
                lab5=tk.Label(text=ras[9][15:20])
                lab5.grid(column=4,row=i)
                lab6=tk.Label(text=ras[10][15:20])
                lab6.grid(column=5,row=i)
                lab7=tk.Label(text=ras[11][11:len(ras[11])])
                lab7.grid(column=6,row=i)
                lab8=tk.Label(text=ras[14][15:len(ras[14])-1])
                lab8.grid(column=7,row=i)
                lab9=tk.Label(text=ras[15][15:len(ras[15])-1])
                lab9.grid(column=8,row=i)
                lab10=tk.Label(text=ras[23][14:len(ras[23])])
                lab10.grid(column=9,row=i)
                lab11=tk.Label(text=ras[24])
                lab11.grid(column=10,row=i)
                lab12=tk.Label(text=ras[25])
                lab12.grid(column=11,row=i)
                lab13=tk.Label(text=ras[26][0:len(ras[26])-1])
                lab13.grid(column=12,row=i)
                i=i+1
                del ras
            lab1=tk.Label(text="Number")
            lab1.grid(column=0,row=12)
            lab2=tk.Label(text="Train_Name")
            lab2.grid(column=1,row=12)
            lab4=tk.Label(text="Departure_Station")
            lab4.grid(column=2,row=12)
            lab5=tk.Label(text="Arrive_Station")
            lab5.grid(column=3,row=12)
            lab6=tk.Label(text="Arrive_Time")
            lab6.grid(column=4,row=12)
            lab7=tk.Label(text="Depart_Time")
            lab7.grid(column=5,row=12)
            lab8=tk.Label(text="Distance")
            lab8.grid(column=6,row=12)
            lab9=tk.Label(text="Arrive_Date")
            lab9.grid(column=7,row=12)
            lab10=tk.Label(text="Depart_Date")
            lab10.grid(column=8,row=12)
            lab11=tk.Label(text="1st_AC")
            lab11.grid(column=9,row=12)
            lab12=tk.Label(text="2ed_AC")
            lab12.grid(column=10,row=12)
            lab13=tk.Label(text="3rd_AC")
            lab13.grid(column=11,row=12)
            lab14=tk.Label(text="SL")
            lab14.grid(column=12,row=12)
            button = Tkinter.Button(frame,text="Exit",command=tk.destroy)
            button.pack(side=BOTTOM)

            
    except:
        lab=tk.Label(text="'Oops',There is no direct train found\n \n \n")
        lab.grid(column=0,row=12)
        button = tk.Button(window,text="Exit",command=tk.destroy)
        button.pack(side=BOTTOM)

  

     
window.title("Indian Railway Enquery")
# label----
label1=tk.Label(text="WELCOME TO INDIAN RAILWAY",font=("Corbel",15),bg="pink")
label1.grid(column=1,row=0)
label2=tk.Label(text="Enter Departure Station Code",font=("Corbel",10))
label2.grid(column=0,row=1)
label3=tk.Label(text="Enter   Arrivel   Station  Code",font=("Corbel",10))
label3.grid(column=0,row=2)
label4=tk.Label(text="Enter Date (Date-Month-Year)",font=("Corbel",10))
label4.grid(column=0,row=3)
#entry field
entry1=tk.Entry()
entry1.grid(column=1,row=1)
entry2=tk.Entry()
entry2.grid(column=1,row=2)
entry3=tk.Entry()
entry3.grid(column=1,row=3)
#button===
button1=tk.Button(text="Find Trains",bg="green",command=main)
button1.grid(column=1,row=8)


window.mainloop()
