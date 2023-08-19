import tkinter as tk

numbers = [1,2,3,4,5,6,7,8,9,0]

class GUI:
    def __init__(self) -> None:
        self.expression = ""
        
        self.root = tk.Tk()
        
        self.root.title("ND's Calculator")
        self.root.geometry("350x340")
        self.root.resizable(0, 0)
        
        self.label = tk.Label(self.root, text="Try it Out", font=("Calibri Bold", 18))
        self.label.pack(pady=10)
        
        self.frame1 = tk.Frame(self.root)
        
        self.input_text = tk.StringVar()
        self.textbox = tk.Entry(self.frame1, font=("Arial", 18), textvariable=self.input_text, justify="right")
        self.textbox.pack(fill="x", ipady=10)
        
        self.frame1.pack(fill="x")
        
        self.frame2 = tk.Frame(self.root)
        
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)
        self.frame2.columnconfigure(2, weight=1)
        self.frame2.columnconfigure(3, weight=1)
        
        
        self.load_buttons()    
        
        
        self.frame2.pack(fill="x")

        self.root.mainloop()
    
    def load_buttons(self):
        
        # Up Top
        backButton = tk.Button(self.root, text="\u2190", font=("Arial", 18), bg="#ddd" , border = 1, command=self.backButton)
        backButton.place(x=300, y= 0, height=56, width=55)
        
        # ROW 1
        btn1 = tk.Button(self.frame2, text="1", font=("Arial", 18), command=self.btn1_click)
        btn1.grid(row=1, column=0, sticky="nsew")

        btn2 = tk.Button(self.frame2, text="2", font=("Arial", 18), command=self.btn2_click)
        btn2.grid(row=1, column=1, sticky="nsew")

        btn3 = tk.Button(self.frame2, text="3", font=("Arial", 18), command=self.btn3_click)
        btn3.grid(row=1, column=2, sticky="nsew")
        
        btnPlus = tk.Button(self.frame2, text="+", font=("Arial", 18), background="#ddd", command=self.btnAdd_click)
        btnPlus.grid(row=1, column=3, sticky="nsew")

        # ROW 2
        btn4 = tk.Button(self.frame2, text="4", font=("Arial", 18), command=self.btn4_click)
        btn4.grid(row=2, column=0, sticky="nsew")

        btn5 = tk.Button(self.frame2, text="5", font=("Arial", 18), command=self.btn5_click)
        btn5.grid(row=2, column=1, sticky="nsew")

        btn6 = tk.Button(self.frame2, text="6", font=("Arial", 18), command=self.btn6_click)
        btn6.grid(row=2, column=2, sticky="nsew")
        
        btnMinus = tk.Button(self.frame2, text="-", font=("Arial", 18), background="#ddd", command=self.btnSub_click)
        btnMinus.grid(row=2, column=3, sticky="nsew")

        # ROW 3
        btn7 = tk.Button(self.frame2, text="7", font=("Arial", 18), command=self.btn7_click)
        btn7.grid(row=3, column=0, sticky="nsew")

        btn8 = tk.Button(self.frame2, text="8", font=("Arial", 18), command=self.btn8_click)
        btn8.grid(row=3, column=1, sticky="nsew")

        btn9 = tk.Button(self.frame2, text="9", font=("Arial", 18), command=self.btn9_click)
        btn9.grid(row=3, column=2, sticky="nsew")

        btnMulti = tk.Button(self.frame2, text="*", font=("Arial", 18), background="#ddd", command=self.btnMul_click)
        btnMulti.grid(row=3, column=3, sticky="nsew")

        # ROW 0
        
        btn12 = tk.Button(self.frame2, text="C", font=("Arial", 18), background="#ddd", command=self.btn_clear)
        btn12.grid(row=0, column=0, sticky="nsew", columnspan=3)
        
        btnDivide = tk.Button(self.frame2, text="/", font=("Arial", 18), background="#ddd", command=self.btnDiv_click)
        btnDivide.grid(row=0, column=3, sticky="nsew")         

        
        # ROW 4
        
        btn10 = tk.Button(self.frame2, text=".", font=("Arial", 18), command=self.btnDot_click)
        btn10.grid(row=4, column=0, sticky="nsew")
        
        btn11 = tk.Button(self.frame2, text="0", font=("Arial", 18), command=self.btn0_click)
        btn11.grid(row=4, column=1, sticky="nsew") 
              
        btnEquals = tk.Button(self.frame2, text="=", font=("Arial", 18), background="#ddd", command=self.btn_equal)
        btnEquals.grid(row=4, column=2, sticky="nsew", columnspan=2)   


    def btn_clear(self):
        self.expression = ""
        self.input_text.set(self.expression)
        

    def btn_equal(self):
        try:
            result = str(eval(self.expression)) 
            self.expression = ""
            self.input_text.set(result)
        except:
            raise Exception("INVLAID COMMAND")
        
        
    def btn1_click(self):
        self.expression += "1"
        self.input_text.set(self.expression)

    def btn2_click(self):
        self.expression += "2"
        self.input_text.set(self.expression)

    def btn3_click(self):
        self.expression += "3"
        self.input_text.set(self.expression)

    def btn4_click(self):
        self.expression += "4"
        self.input_text.set(self.expression)

    def btn5_click(self):
        self.expression += "5"
        self.input_text.set(self.expression)

    def btn6_click(self):
        self.expression += "6"
        self.input_text.set(self.expression)

    def btn7_click(self):
        self.expression += "7"
        self.input_text.set(self.expression)

    def btn8_click(self):
        self.expression += "8"
        self.input_text.set(self.expression)

    def btn9_click(self):
        self.expression += "9"
        self.input_text.set(self.expression)

    def btn0_click(self):
        self.expression += "0"
        self.input_text.set(self.expression)

    def btnAdd_click(self):
        self.expression += "+"
        self.input_text.set(self.expression)

    def btnSub_click(self):
        self.expression += "-"
        self.input_text.set(self.expression)

    def btnMul_click(self):
        self.expression += "*"
        self.input_text.set(self.expression)

    def btnDiv_click(self):
        self.expression += "/"
        self.input_text.set(self.expression)
        
    def btnDot_click(self):
        self.expression += "."
        self.input_text.set(self.expression)

    def backButton(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)            
    
    
GUI()    
