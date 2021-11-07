from tkinter import *

#A simple calculator application


root = Tk()

# This is used when the user presses the = sign , if this is false the ans in the entry is not result
# If it is the result we must remove it while the user is typing another computation

isRes = False

#creating a input field
myInput = Entry(root,bg="white",fg="black",borderwidth=3,width=39)
myInput.grid(row=0,column=0,columnspan=3,padx=10,pady=5)

def buttonFunc(num):
    """Gets the text which is typed by the user and appends it with the expression which is already in input field"""
    #using the global variable
    global isRes

    # If the user presses any symbol i.e he is performing another operation with the result
    # If the user enters a digit he is performing new operation so the input field is cleared
    if((isRes==True and (num!="+" and num!="-" and num!="/" and num!="*" and num!="%")) or myInput.get()=="ERROR"):
        myInput.delete(0,END)   # Deletes the data in the entry 
        
    expression = myInput.get()  #gets the expression till now
    myInput.delete(0,END)       #removes it
    expression+=num             #appends the newly added digit
    myInput.insert(0,expression)    #inserts it in the input field
    isRes=False                 #making the result false 


def buttonClearFunc():
    """clears the input field"""
    myInput.delete(0,END)

def buttonEqualFunc():
    """Evaluated the expression"""

    expression = myInput.get()  #gets the exoression
    myInput.delete(0,END)       #removes the data int the input field

    try:
        result = eval(expression)  # if an exception occurs

    except ZeroDivisionError:
        myInput.insert(0,"ERROR")  #if it is zero division error
    
    except :
        buttonClearFunc()
    
    else: 
        myInput.insert(0,result)  #insert the result
        global isRes
        isRes=True     #make this true to show that = is pressed

    


    


#creating buttons of numbers
button1 = Button(root,text="1",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("1"))
button2 = Button(root,text="2",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("2"))
button3 = Button(root,text="3",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("3"))
button4 = Button(root,text="4",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("4"))
button5 = Button(root,text="5",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("5"))
button6 = Button(root,text="6",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("6"))
button7 = Button(root,text="7",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("7"))
button8 = Button(root,text="8",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("8"))
button9 = Button(root,text="9",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("9"))
button0 = Button(root,text="0",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("0"))
buttonSub = Button(root,text="-",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("-"))
buttonAdd = Button(root,text="+",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("+"))
buttonMul = Button(root,text="*",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("*"))
buttonDiv = Button(root,text="/",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("/"))
buttonMod = Button(root,text="%",bg="white",fg="black",padx=35,pady=20,command=lambda : buttonFunc("%"))
buttonClear = Button(root,text="Clear",bg="white",fg="black",padx=70,pady=20,command=buttonClearFunc)
buttonEqual = Button(root,text="=",bg="white",fg="black",padx=35,pady=20,command=buttonEqualFunc)


#placing them on the screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonSub.grid(row=4,column=1)
buttonAdd.grid(row=4,column=2)

buttonMul.grid(row=5,column=0)
buttonDiv.grid(row=5,column=1)
buttonMod.grid(row=5,column=2)

buttonClear.grid(row=6,column=0,columnspan=2)
buttonEqual.grid(row=6,column=2,columnspan=1)



root.mainloop()