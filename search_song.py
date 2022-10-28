from tkinter import *

class Window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        pos = self.center_() #розміщення вікна по центру екрана
        self.geometry('760x600' + pos)

        #створення таблиці grid
        self.columnconfigure(tuple(range(10)), weight=1)
        self.rowconfigure(tuple(range(10)), weight=1)

        #створення загальної Frame
        self.all = Frame(self, width=100, height=50, borderwidth=1, relief=SOLID)
        self.all.grid(row=0,column=0)

        #LEFT
        #--------------------------------------------------------------
        #створення верхньої лівої Frame
        self.left_top_frame = Frame(self.all, width=120, height=110)
        self.left_top_frame.grid(row=0,column=0)

        #створення Labels для назви
        self.label1 = Label(self.left_top_frame, text = "Title", font=('Arial',10), fg="black").pack(side='top', anchor='sw', ipadx=40, pady=10)

        #створення поля вводу Entry
        self.entry_name = Entry(self.left_top_frame, width=54, relief = 'solid').pack(side='left', anchor='nw', pady=10)

        #створення нижньої лівої Frame
        self.left_bottom_frame = Frame(self.all, width=100, height=50)
        self.left_bottom_frame.grid(row=1, column=0, rowspan=8,  sticky="N", padx = 30, pady=30)

        #створення 2 смуг прокручування Scrollbar
        self.scroll_v =Scrollbar(self.left_bottom_frame, relief = 'solid', orient=VERTICAL)
        self.scroll_v.pack(side='right')
        self.scroll_h =Scrollbar(self.left_bottom_frame, relief = 'solid', orient=HORIZONTAL)
        self.scroll_h.pack(side='bottom')

        #створення Listbox
        self.list_box = Listbox(self.left_bottom_frame, xscrollcommand=self.scroll_h.set, yscrollcommand=self.scroll_v.set, 
                                 height=16, width=26, relief = 'solid', font=("Arial", 16), selectmode=MULTIPLE)
        self.list_box.pack()
        
        #конфігурація Scrollbars
        self.list_box.config(yscrollcommand= self.scroll_v.set)
        self.list_box.config(xscrollcommand= self.scroll_h.set)
        self.scroll_v.config(command= self.list_box.yview)
        self.scroll_h.config(command= self.list_box.xview)
        #--------------------------------------------------------------


        #RIGHT
        #--------------------------------------------------------------
        #створення верхньої правої Frame
        self.right_top_frame = Frame(self.all, width=100, height=50)
        self.right_top_frame.grid(row=0,column=1, sticky="W")

        #створення Button-search
        self.button = Button(self.right_top_frame, width=5, height=2, text="search", font="Arial 10", bg="#99ff33", 
                                relief="raised").pack(padx=30)

        #створення Frame для сортування
        self.right_sort_frame = Frame(self.all, width=100, height=50)
        self.right_sort_frame.grid(row=0,column=1, sticky="NW", pady=10, padx=120)

        #створення Radiobutton
        self.var_name = StringVar()
        self.var_name.set("none")  
        Radiobutton(self.right_sort_frame, text="за назвою",
                    value="name",
                    variable=self.var_name).pack(side='bottom')
        Radiobutton(self.right_sort_frame, text="за автором",
                    value="artist",
                    variable=self.var_name).pack(side='bottom')
        Radiobutton(self.right_sort_frame, text="за жанром",
                    value="genre",
                    variable=self.var_name).pack(side='bottom')

        #створення Frame для інформації
        self.info_frame = Frame(self.all, width=90, height=100, borderwidth=1, relief=SOLID)
        self.info_frame.grid(row=1, column=1, rowspan=10, sticky="NW", pady=30, padx =30)

        #створення Labels для пісень
        self.label2 = Label(self.info_frame, text = "Назва обраної пісні", font="Arial 11", width=30, height=3, fg="black",).pack(expand=1)
        self.label3 = Label(self.info_frame, text = "Автор", width=20, height=3, fg="black", borderwidth=1, relief=SOLID).pack()
        self.label4 = Label(self.info_frame, text = "Назва альбому", width=20, height=3, fg="black", borderwidth=1, relief=SOLID).pack(pady=10)
        self.label5 = Label(self.info_frame, text = "Тривалість", width=20, height=3, fg="black", borderwidth=1, relief=SOLID).pack()
        #self.label5 = Label(self.info_frame, width=20, height=11).pack(pady=3)
        #--------------------------------------------------------------
        
    #розміщення вікна по центру екрана
    def center_(self):
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()
        posW = int(self.winfo_screenwidth()/2 - windowWidth/2)        
        posH = int(self.winfo_screenheight()/2 - windowHeight/2)
        return ("+{}+{}".format(posW, posH))

if __name__ == "__main__":
    root = Window()
    root.mainloop()