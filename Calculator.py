from tkinter import*

def buttonClick(numbers):
    global operator
    operator = operator + str (numbers)
    calInput.set (operator)

def buttonClearDisplay():
    global operator
    operator = ""
    calInput.set ("")

def buttonEqualsDisplay():
    global operator
    total =  str (eval (operator))
    calInput.set (total)
    operator = ""

calculator = Tk()
calculator.title("My Calculator")
operator = ""
calInput = StringVar()

txtDisplay = Entry(calculator , font= ('arial',20,'bold'), textvariable =calInput, bd = 30, insertwidth =4, bg= "powder blue", justify = 'right').grid(columnspan = 4)

button7 = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="7",bg= "powder blue", command = lambda:buttonClick(7)).grid(row = 1 ,column =0)
button8 = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="8",bg= "powder blue", command = lambda:buttonClick(8)).grid(row = 1 ,column =1)
button9 = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="9",bg= "powder blue", command = lambda:buttonClick(9)).grid(row = 1 ,column =2)
buttonPlus = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="+",bg= "blue", command = lambda:buttonClick("+")).grid(row = 1 ,column =3)

button4 = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="4",bg= "powder blue", command = lambda:buttonClick(4)).grid(row = 2 ,column =0)
button5 = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="5",bg= "powder blue", command = lambda:buttonClick(5)).grid(row = 2 ,column =1)
button6 = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="6",bg= "powder blue", command = lambda:buttonClick(6)).grid(row = 2 ,column =2)
buttonMinus = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="-",bg= "blue", command = lambda:buttonClick("-")).grid(row = 2 ,column =3)

button1 = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="1",bg= "powder blue", command = lambda:buttonClick(1)).grid(row = 3 ,column =0)
button2 = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="2",bg= "powder blue", command = lambda:buttonClick(2)).grid(row = 3 ,column =1)
button3 = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="3",bg= "powder blue", command = lambda:buttonClick(3)).grid(row = 3 ,column =2)
buttonCross = Button (calculator, padx =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="x",bg= "blue", command = lambda:buttonClick("*")).grid(row = 3 ,column =3)

button0 = Button (calculator, padx =16, pady =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="0",bg= "powder blue", command = lambda:buttonClick(0)).grid(row = 4 ,column =0)
buttonC = Button (calculator, padx =16, pady =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="C",bg= "powder blue",command = buttonClearDisplay).grid(row = 4 ,column =1)
buttonEqual = Button (calculator, padx =16, pady =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="=",bg= "powder blue",command = buttonEqualsDisplay).grid(row = 4 ,column =2)
buttonSlash = Button (calculator, padx =16, pady =16,bd =8, fg ="navy blue", font =('arial',20,'bold'),
                  text ="÷",bg= "blue", command = lambda:buttonClick("/")).grid(row = 4 ,column =3)

calculator.mainloop()
