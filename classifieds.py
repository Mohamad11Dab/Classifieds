
from sys import exit as abort

# A function for opening a web document given its URL.

from urllib.request import urlopen

# Some standard Tkinter functions.  
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression. 
from re import *

# A function for displaying a web document in the host
# operating system's default web browser 
from webbrowser import open as urldisplay

# All the standard SQLite functions.
from sqlite3 import *


def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (NOT RELIABLE OR RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                               'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                               'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            print("Warning - Request does not reveal client's true identity.")
            print("          This is both unreliable and unethical!")
            print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError:
        print("Download error - Cannot find document at URL '" + url + "'\n")
        return None
    except HTTPError:
        print("Download error - Access denied to document at URL '" + url + "'\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to download " + \
              "the document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError:
        print("Download error - Unable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
   
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("Download error - Unable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents


from re import findall

url1 = ""
web_document1 = ""
item_locanto = []
price_locanto = []

url2 = ""
web_document2 = ""
item_old = []
price_old = []

url3 = ""
web_document3 = ""
item_amazon = []
price_amazon = []
#Set a function 
def Get_locanto():
    global url1# Set Global Variable inside function
    global web_document1
    global item_locanto
    global price_locanto
    url1=' https://www.locanto.com.au/Accessories-Jewellery/420/ '#url for locanto(Jewellery) web document
    web_document1=download(url1,incognito=True)# download the document
    item_locanto=findall('<a class=".*" href=".*">(.*)<div class=".*"><s',web_document1)#regex to extract names of most recent items(Jewellery) listed in Locanto
    price_locanto=findall('<div class="bp_ad__price">([A-Za-z 0-9 -/./$]+)</div>',web_document1)#regex to extract prices of most recent item(Jewellery) listed in Locanto

def Get_old():
    global url2
    global web_document2
    global item_old
    global price_old
    url2='http://www.vintagemachinery.org/classifieds/ads.aspx'#url for Vintage Machinery(Machines) web document
    web_document2=download(url2,incognito=True)#download document 
    item_old=findall('<a id=".*" href=".*" style=".*">(.*)</a>',web_document2)#regex to extract names of most recent items(Machines) listed in Vintage Machinery
    price_old=findall('<span id=".*Price">(.*)</span>',web_document2)#regex to extract prices of most recent items(Machines) listed in Vintage Machinery

def Get_amazon():
    global url3
    global web_document3
    global item_amazon
    global price_amazon
    url3='https://www.amazon.com.au/gp/bestsellers/videogames/'#url for Amazon(video games) web document
    web_document3=download(url3,incognito=True)#download document 
    item_amazon=findall('<div class=".*" aria-hidden=".*" data-rows=".*">\n(.*)',web_document3)#regex to extract name of most recent items(video games) listed in amazon
    price_amazon=findall('<span class=.* >(.*)</span></span></a>',web_document3)#regex to extract prices of most recent items (video games) listed in amazon

def Show_detail():
    if Label_ad.get()==1:
        urldisplay('https://www.locanto.com.au/Accessories-Jewellery/420/') # to open the web page of locanto(Jewellery)  
    elif Label_ad.get()==2:
        urldisplay(url2) #to open web page of Vintage Machinery(Machines)
    elif Label_ad.get()==3:
        urldisplay(url3)#To open web page of Amazon(Video games )
        
 # Set a function to clear the inputs of texts and entries       
def clear_texts():
    description.delete("1.0","end")
    price.delete("1.0","end")
    Source.delete("0","end")
    URL.delete("0","end")
    
 # Set a function to when selecting the recent items without selecting the category   
def no_category():
    description.insert(END,'Please Select Category')
    price.insert(END,'$__.__')
    Source.insert(0,'Source:No item selected')
    URL.insert(0,'URL:No Item selected')
    
 # Set function to when we select the most recent item   
def display_latest():
    clear_texts()#clear text first
    try:#to aviod any errors concerning lose of internet connection 
        if Label_ad.get()==1:#if we select Jewllery at Locanto
         Get_locanto()
         description.insert(END,item_locanto[0])#insert the very first most recent item name found in the list extracted from regex in the description widget
         price.insert(END,price_locanto[0])# insert the very first most recent item price found in the list extracted from regex in the price widget 
        elif Label_ad.get()==2:#if we select Machines at Vintage Machinery
         Get_old()
         description.insert(END,item_old[1])
         price.insert(END,price_old[0])
        elif Label_ad.get()==3:#if we select Video games at Amazon
         Get_amazon()
         description.insert(END,item_amazon[0])
         price.insert(END,price_amazon[0])
        else:#if no category is selected 
         no_category() 
    except:#display the following instead of displaying an error in the shell window
        description.insert(END,'No Item Description Available')
        price.insert(END,'$_.__')

    if Label_ad.get()==1:
        Source.insert(0,'Source:Locanto')#insert the source in the source widget(in this case locanto)
        URL.insert(0,'URL:'+url1)#insert the url for the category chosen (in this case url for locanto)
    elif Label_ad.get()==2:
        Source.insert(0,'Source:Vintage Machinery')
        URL.insert(0,'URL:'+url2)

    elif Label_ad.get()==3:
        Source.insert(0,'Source:Amazon')
        URL.insert(0,'URL:'+url3)


        
        
     
def display_second():
    clear_texts()
    try:
        if Label_ad.get()==1:
         Get_locanto()
         description.insert(END,item_locanto[1])##insert the very second most recent item name found in the list extracted from regex in the description widget
         price.insert(END,price_locanto[1])#insert the very second most recent item price found in the list extracted from regex in the price widget
        elif Label_ad.get()==2:
         Get_old()
         description.insert(END,item_old[2])
         price.insert(END,price_old[1])
        elif Label_ad.get()==3:
         Get_amazon()
         description.insert(END,item_amazon[1])
         price.insert(END,price_amazon[1])
        else:
         no_category()
    except:
        description.insert(END,'No Item Description Available')
        price.insert(END,'$_.__')

    if Label_ad.get()==1:
        Source.insert(0,'Source:Locanto')
        URL.insert(0,'URL:'+url1)
    elif Label_ad.get()==2:
        Source.insert(0,'Source:Vintage Machinery')
        URL.insert(0,'URL:'+url2)

    elif Label_ad.get()==3:
        Source.insert(0,'Source:Amazon')
        URL.insert(0,'URL:'+url3)
 
def display_third():
    clear_texts()
    try:
        if Label_ad.get()==1:
         Get_locanto()
         description.insert(END,item_locanto[2])#insert the very third most recent item name found in the list extracted from regex in the description widget
         price.insert(END,price_locanto[2])#insert the very third most recent item price found in the list extracted from regex in the price widget
        elif Label_ad.get()==2:
         Get_old()
         description.insert(END,item_old[3])
         price.insert(END,price_old[2])
        elif Label_ad.get()==3:
         Get_amazon()
         description.insert(END,item_amazon[2])
         price.insert(END,price_amazon[2])
        else:
         no_category()
    except:
        description.insert(END,'No Item Description Available')
        price.insert(END,'$_.__')

    if Label_ad.get()==1:
        Source.insert(0,'Source:Locanto')
        URL.insert(0,'URL:'+url1)
    elif Label_ad.get()==2:
        Source.insert(0,'Source:Vintage Machinery')
        URL.insert(0,'URL:'+url2)

    elif Label_ad.get()==3:
        Source.insert(0,'Source:Amazon')
        URL.insert(0,'URL:'+url3)
        
#set function for the save selection button
def save_selection():
    connection=connect(database='classifieds.db')#connect with the database
    classifieds_db=connection.cursor()#get a pointer into the database 
    sourceget= Source.get()
    sourcesplit = sourceget.split(":")# select the source 
    priceget= price.get('1.0',END)#sleect the price
    descriptionget= description.get('1.0',END)#select the description
    classifieds_db.execute('UPDATE current_selection SET Source="'+ sourcesplit[1] +'",Price="'+ priceget +'",Description="'+ descriptionget +'"')#execute them in the database
    connection.commit()
    classifieds_db.close()
    connection.close()
  
    
     
     






#Create The GUI Window
base_window=Tk()
#Give a window Name
base_window.title('Buy Cart for Online Shopping')
#Set a background color for the GUI
base_window['bg']='light Blue'
#Set Size for the Window
base_window.geometry('600x800')
#Add Image to the GUI
pop_image= PhotoImage(file='Best.png')
base_image=Label(base_window,image =pop_image)
base_image.grid(row=0,column=0,rowspan=2,columnspan=10)

#Add widget for the classified ads
#Create a Label Frame
Category=LabelFrame(base_window,text='Category',fg='green',font=('Arial',15,'bold'),bg='light blue')
Label_ad=IntVar()#Set a variable
#Create Radiobuttons
Ad1=Radiobutton(Category,text='Jewellery @Locanto',font=('Times',15),variable=Label_ad,value=1,bg='light blue',width=30)#Set values for the variable so that only one
Ad2=Radiobutton(Category,text='Machines @ Vintage Machinery',font=('Times',15),variable=Label_ad,value=2,bg='light blue',width=30)#at a time can be clicked
Ad3=Radiobutton(Category,text='Video Games @ Amazon Best Sellers',font=('Times',15),variable=Label_ad,value=3,bg='light blue',width=30)
#Placing them in the frame according to rows and columns
Ad1.grid(row=1,column=1)
Ad2.grid(row=2,column=1)
Ad3.grid(row=3,column=1)
#Placing the frame in the GUI
Category.grid(row=3,column=0,columnspan=6)



#Add widget for What items to be selected
Item=LabelFrame(base_window,text='Item',fg='green',font=('Arial',15,'bold'),bg='light blue',height=50)
#Creating buttons that can be clicked one at a time
Latest=Button(Item,text='Latest',font=('Times',15,),activeforeground='Green',command=display_latest,fg='blue',bg='light blue',activebackground='Yellow',width=16)
Second=Button(Item,text='Second',font=('Times',15,),activeforeground='Green',command=display_second,fg='blue',bg='light blue',activebackground='Yellow',width=16)
Third=Button(Item,text='Third',font=('Times',15,),activeforeground='Green',command=display_third,fg='blue',bg='light blue',activebackground='Yellow',width=16)
#Placing the buttons in the frame according to rows and columns
Latest.grid(row=1,column=1)
Second.grid(row=2,column=1)
Third.grid(row=3,column=1)
#Placing the Frame in the GUI
Item.grid(row=3,column=6,columnspan=3,ipadx=15)



Options=LabelFrame(base_window,text='Options',fg='green',font=('Arial',15,'bold'),bg='light blue')
#Create a button that dispalys the details of the selected item one clicked
show=Button(Options,text='Show Details',font=('Times',15),command=Show_detail,activeforeground='Green',fg='blue',bg='light blue',activebackground='Yellow',width=20,)
show.grid(row=0,column=0)
#Option to save selection once clicked
Save=Button(Options,text='Save Selection',command=save_selection,width=15,font=('Times',15),bg='light blue')
Save.grid(row=0,column=1)


Options.grid(row=4,column=0,columnspan=10,ipadx=60)

Selection=LabelFrame(base_window,text='Selection',fg='green',font=('Arial',15,'bold'),bg='light blue')
#price of the Item
price=Text(Selection,font=('Times',30),height=2,width=10,fg='blue',bg='light green',wrap=WORD)
price.insert(END,'$00.00')
price.grid(row=0,column=0,rowspan=2,columnspan=2)
#Description of the item
description=Text(Selection,font=('Times',20),width=25,height=1,fg='blue',bg='light green',wrap=WORD)
description.insert(END,'Description of selected item')
description.grid(row=0,column=2,rowspan=4,columnspan=2,ipady=30)
#Name of the classified site
var=StringVar()
Source=Entry(Selection,textvariable=var,font=('Times',15),width=56,fg='blue',bg='light green')
Source.insert(0,'Source:Name of classified ad site')
Source.grid(row=6,column=0,columnspan=4)
#The adress where the item should be sent to
URL=Entry(Selection,font=('Times',15),width=56,fg='blue',bg='light green')
URL.insert(0,'URL:Adress where item is listed')
URL.grid(row=7,column=0,columnspan=4)


Selection.grid(row=5,column=0,columnspan=10,rowspan=4,ipadx=10) 

base_window.mainloop()
