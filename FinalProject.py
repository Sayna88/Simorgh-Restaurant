from tkinter import*
from tkinter.ttk import Treeview
from FinalProjectsevis import Services

s=[]
mony=0
global oldName
services=Services("RestaurantOrder")

pishghazaList = [{"name":"soup jo","price":100000},{"name":"soup reshte","price":120000},{"name":"ash reshte","price":150000},{"name":"ash dogh","price":150000},{"name":"ash ghalamkar","price":150000},{"name":"ash torsh","price":150000},{"name":"french friz","price":90000},{"name":"salad sezar","price":120000},{"name":"salad sezar ba morgh gril","price":130000},{"name":"salad sezar ba morgh sokhary","price":150000},{"name":"salad shirazi","price":85000},{"name":"salad makarony","price":125000}]
ghazayeasliiList = [{"name":"pizza makhsos","price":180000},{"name":"pizza peperonii","price":150000},{"name":"pizza gosht va gharch","price":190000},{"name":"pizza vegan","price":200000},{"name":"chelo kabab","price":200000},{"name":"chelo gosht","price":200000},{"name":"chelo joje","price":200000},{"name":"pasta","price":120000},{"name":"morgh sokhary","price":150000},{"name":"morgh gril","price":120000}]
dessertList = [{"name":"jelly","price":120000},{"name":"bastany ba mivehay ostovaei","price":200000},{"name":"bastany","price":150000},{"name":"reshte khoshkar","price":180000},{"name":"jellebastany","price":250000},{"name":"majon","price":230000},{"name":"chizcake vanil","price":100000},{"name":"chizcake shocolat","price":105000},{"name":"chizcake capochino","price":100000},{"name":"chizcake totfarangii","price":100000},{"name":"cake vanil","price":110000},{"name":"cake shokolat","price":115000},{"name":"cake totfarangii","price":110000}]

#------------function--------

def updateOrder():
    global oldName
    try:
        focusItem=setorderTreeView.focus()
        focusWrk=setorderTreeView.item(focusItem)
        pishghazaWidget.Entry.insert(0,focusWrk["values"][0])
        ghazayeasliiWidget.Entry.insert(0,focusWrk["values"][1])
        desserWidget.Entry.insert(0,focusWrk["values"][2])
        oldName = focusWrk["values"][0]
    except Exception as e:
        print(e)

def deleteOrder():
    try:
        focusItem=setorderTreeView.focus()
        focusWrk=setorderTreeView.item(focusItem)
        services.deleteorder(focusWrk["values"][0])
    except Exception:
        print(Exception)
    finally:
        fetchData()

def doneOrder():
    try:
        focusItem=setorderTreeView.focus()
        focusWrk=setorderTreeView.item(focusItem)
        services.getDoneorders(focusWrk["values"][0])
    except Exception:
        print(Exception)
    finally:
        fetchData()

def updateData():
    try:
        newOrderData={
            "pishghaza"   :pishghazaWidget.Entry.get(),
            "ghazayeaslii":ghazayeasliiWidget.Entry.get(),
            "desser"      :desserWidget.Entry.get(),
        }
        services.updateorder(oldName,newOrderData)
    except Exception:
        print("Error in setData function")
    finally:
        pishghazaWidget.Entry.delete(0,"end")
        ghazayeasliiWidget.Entry.delete(0,"end")
        desserWidget.Entry.delete(0,"end")
        fetchData()

def setData():
    global oldName
    try:
        pishghaza = pishghazaWidget.Entry.get()
        ghazayeaslii = ghazayeasliiWidget.Entry.get()
        dessert = desserWidget.Entry.get()
        
        pishghaza_price = 0
        ghazayeaslii_price = 0
        dessert_price = 0

        for item in pishghazaList:
            if item["name"] == pishghaza:
                pishghaza_price = item["price"]
                break

        for item in ghazayeasliiList:
            if item["name"] == ghazayeaslii:
                ghazayeaslii_price = item["price"]
                break

        for item in dessertList:
            if item["name"] == dessert:
                dessert_price = item["price"]
                break

        total_price = pishghaza_price + ghazayeaslii_price + dessert_price
        orderData = {
            "pishghaza": pishghaza,
            "ghazayeaslii": ghazayeaslii,
            "desser": dessert,
            "price": total_price
            }
        services.setorder(orderData)
    except Exception as e:
        print("Error in setData function:",e)
    finally:
        pishghazaWidget.Entry.delete(0, "end")
        ghazayeasliiWidget.Entry.delete(0, "end")
        desserWidget.Entry.delete(0, "end")
        fetchData()

def showWorks(ListOforder):
    for item in setorderTreeView.get_children():
        setorderTreeView.delete(item)

    for work in ListOforder:
        setorderTreeView.insert("","end",values=list(work.values()))

def fetchData():
    try:
        orderList = services.getAllorders()
        showWorks(orderList)
    except:
        print("Error in fetchData function")

def muneButton():
    menu_window = Toplevel(root)
    menu_window.title("Menu")
    menu_window.geometry("700x900")
    menu_window.config(bg="skyblue")
    pishghazaTitle=Label(menu_window, text="---- Pishghaza ----")
    pishghazaTitle.pack(pady=10)
    pishghazaListbox=Listbox(menu_window,width=50,height=10)
    pishghazaListbox.pack(pady=10)
    for item in pishghazaList:
        pishghazaListbox.insert(END,f"{item['name']} ====> {item['price']}")

    ghazayeasliiTitle=Label(menu_window, text="---- Ghazaye Aslii ----")
    ghazayeasliiTitle.pack(pady=10)
    ghazayeasliiListbox=Listbox(menu_window,width=50,height=10)
    ghazayeasliiListbox.pack(pady=10)

    for item in ghazayeasliiList:
        ghazayeasliiListbox.insert(END,f"{item['name']} ====> {item['price']}")

    dessertTitle=Label(menu_window, text="----Dessert----")
    dessertTitle.pack(pady=10)
    dessertListbox=Listbox(menu_window,width=50,height=15)
    dessertListbox.pack(pady=10)

    for item in dessertList:
        dessertListbox.insert(END,f"{item['name']} ====> {item['price']}")

class EntryWidget():
    def __init__(self,name,parent):
        self.name = name
        self.label = Label(parent,text=name)
        self.Entry = Entry(parent)
    def packWidget(self):
        self.label.pack(ipadx=10,ipady=10,pady=10)
        self.Entry.pack(ipadx=10,ipady=10)

#------------root------------

root=Tk()
root.geometry("1100x600+200+50")
root.title("Simorgh Restaurant☺")
root.config(bg="skyblue")

root.rowconfigure(0,weight=10)
root.rowconfigure(1,weight=10)
root.rowconfigure(2,weight=80)
root.columnconfigure(0,weight=50)
root.columnconfigure(1,weight=50)

#------------widgets---------

welcomLabel=Label(root,text=" Welcome To Simorgh Restaurant ☺",bg="skyblue")
welcomLabel.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)

#------------frames----------

setOrderFrame=LabelFrame(root,text="Set Order",bg="#d8aeff")
showOrderFrame=LabelFrame(root,text="Show Order",bg="#faaeff")

#------------framegrids------

setOrderFrame.grid(row=2,column=0,sticky="nsew",padx=10,pady=10)
showOrderFrame.grid(row=2,column=1,sticky="nsew",padx=10,pady=10)

#------------widgets---------

menubutton=Button(root,text="Menu",bg="#fc8b3d",width=7,height=2,command=muneButton)
menubutton.grid(row=1,column=0,padx=10,pady=10)

#------------entrys----------

pishghazaWidget=EntryWidget("Pishghaza",setOrderFrame)
ghazayeasliiWidget=EntryWidget("Ghazayeaslii",setOrderFrame)
desserWidget=EntryWidget("Dessert",setOrderFrame)

#------------entryspack------

pishghazaWidget.packWidget()
ghazayeasliiWidget.packWidget()
desserWidget.packWidget()

#------------setOPframe------

setorderOPframe=Frame(setOrderFrame)
setorderOPframe.pack(side="bottom")

#------------buttons---------

setButton=Button(setorderOPframe,text="Set",bg="#a7ff83",command=setData,width=5,height=1)
updateButton=Button(setorderOPframe,text="Update",bg="#83ffec",command=updateData)

#------------buttonspack-----

setButton.pack(side="left",ipadx=5,ipady=5,padx=5,pady=5)
updateButton.pack(side="right",ipadx=5,ipady=5,padx=5,pady=5)

#------------showOPframe-----

showOrderOPframe=Frame(showOrderFrame)
showOrderOPframe.pack(side="bottom")

#------------buttons2--------

deleteorderButton=Button(showOrderOPframe,text="delete",command=deleteOrder,bg="#ff3030")
updateorderButton= Button(showOrderOPframe,text="update",command=updateOrder,bg="#80bcff")
doneorderButton=Button(showOrderOPframe,text="Done",command=doneOrder,bg="#13ff00")

#------------buttons2pack----

deleteorderButton.pack(side="left",ipadx=5,ipady=5,padx=5, pady=5)
updateorderButton.pack(side="right",ipadx=5,ipady=5,padx=5, pady=5)
doneorderButton.pack(side="right",ipadx=5,ipady=5,padx=5, pady=5)

#------------headers---------

myHeaders = ["Pishghaza", "Ghazayeaslii", "Dessert", "Price"]
setorderTreeView = Treeview(showOrderFrame, columns=myHeaders)

setorderTreeView.column('#0', width=0, stretch="No")
setorderTreeView.column("Pishghaza", width=120, anchor="w")
setorderTreeView.column("Ghazayeaslii", width=90, anchor='center')
setorderTreeView.column("Dessert", width=120, anchor='center')
setorderTreeView.column("Price", width=90, anchor='center')
setorderTreeView.heading("Pishghaza", text="Pishghaza")
setorderTreeView.heading("Ghazayeaslii", text="Ghazayeaslii")
setorderTreeView.heading("Dessert", text="Dessert")
setorderTreeView.heading("Price", text="Price")

setorderTreeView.pack()

fetchData()

#------------end-------------

root.mainloop()