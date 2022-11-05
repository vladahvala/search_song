from tkinter import *
from sql_interface import DbChinook
from logic import Search_engine

class Window(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pos = self.center_() #розміщення вікна по центру екрана
        self.geometry('850x570' + pos)

        self.db = DbChinook()
        self.engine = Search_engine(self.db)

        self.create_widgets()
        
    def create_widgets(self):
        #створення таблиці grid
        self.columnconfigure(tuple(range(10)), weight=1)
        self.rowconfigure(tuple(range(10)), weight=1)

        #створення загальної Frame
        all = Frame(self, width=100, height=50, borderwidth=1, relief=SOLID)
        all.grid(row=0,column=0)

        #LEFT
        #--------------------------------------------------------------
        #створення верхньої лівої Frame
        left_top_frame = Frame(all, width=120, height=110)
        left_top_frame.grid(row=0,column=0)

        #створення Labels для назви
        enter_lb = Label(left_top_frame, text = "Введіть назву пісні:", font=('Arial',10), fg="black").pack(side='top', anchor='sw', ipadx=40, pady=10)

        #створення поля вводу Entry
        self.input_var = StringVar()
        self.entry = Entry(left_top_frame, width=51, relief = 'solid', textvariable=self.input_var).pack(side='left', anchor='nw', pady=10)

        #створення нижньої лівої Frame
        left_bottom_frame = Frame(all, width=100, height=50)
        left_bottom_frame.grid(row=1, column=0, rowspan=8,  sticky="N", padx = 30, pady=30)

        #створення 2 смуг прокручування Scrollbar
        self.scroll_v =Scrollbar(left_bottom_frame, relief = 'solid', orient=VERTICAL)
        self.scroll_v.pack(side='right', fill=Y)
        self.scroll_h =Scrollbar(left_bottom_frame, relief = 'solid', orient=HORIZONTAL)
        self.scroll_h.pack(side='bottom', fill=X)

        #створення Listbox
        self.list_box = Listbox(left_bottom_frame, xscrollcommand=self.scroll_h.set, yscrollcommand=self.scroll_v.set, 
                                 height=16, width=26, relief = 'solid', font=("Arial", 15), selectmode=SINGLE)
        self.list_box.pack()
        self.list_box.bind('<<ListboxSelect>>', self.click_track)
        
        #конфігурація Scrollbars
        self.list_box.config(yscrollcommand= self.scroll_v.set)
        self.list_box.config(xscrollcommand= self.scroll_h.set)
        self.scroll_v.config(command= self.list_box.yview)
        self.scroll_h.config(command= self.list_box.xview)
        #--------------------------------------------------------------


        #RIGHT
        #--------------------------------------------------------------
        #створення верхньої правої Frame
        right_top_frame = Frame(all, width=100, height=50)
        right_top_frame.grid(row=0,column=1, sticky="W")

        #створення Button-search
        self.button = Button(right_top_frame, width=5, height=2, text="search", font="Arial 10", bg="#99ff33", 
                                relief="raised", command=self.search_track).pack(padx=30)

        #створення Frame для сортування
        right_sort_frame = Frame(all, width=100, height=50)
        right_sort_frame.grid(row=0,column=1, sticky="NW", pady=10, padx=120)

        #створення Radiobutton
        self.var_name = StringVar()
        self.var_name.set("name")  
        R1 = Radiobutton(right_sort_frame, text="за назвою",
                    value="name",
                    variable=self.var_name)
        R1.pack(side='bottom')
        R2 = Radiobutton(right_sort_frame, text="за автором",
                    value="artist",
                    variable=self.var_name)
        R2.pack(side='bottom')
        R3 = Radiobutton(right_sort_frame, text="за жанром",
                    value="genre",
                    variable=self.var_name)
        R3.pack(side='bottom')

        #створення Frame для інформації
        info_frame = Frame(all, width=90, height=100, borderwidth=1, relief=SOLID)
        info_frame.grid(row=1, column=1, rowspan=10, sticky="NW", pady=30, padx =30)

        #створення Labels для пісень
        self.song_name = Label(info_frame, text = "Назва обраної пісні", font="Arial 10", width=50, height=2, fg="black",)
        self.song_name.pack()
        self.artist = Label(info_frame, text = "Автор", width=40, height=3, fg="black", borderwidth=1, relief=SOLID)
        self.artist.pack()
        self.album = Label(info_frame, text = "Назва альбому", width=40, height=3, fg="black", borderwidth=1, relief=SOLID)
        self.album.pack(pady=10)
        self.length = Label(info_frame, text = "Тривалість", width=40, height=3, fg="black", borderwidth=1, relief=SOLID)
        self.length.pack()
        self.label6 = Label(info_frame, width=20, height=11).pack(pady=3)
        #--------------------------------------------------------------

    def search_track(self):
        """Пошук треків за назвою треку, або за автором
        або за жанром, в залежності від обраного режиму 
        radiobutton
        """
        self.list_box.delete(0,END) #очищення Listbox
        text = self.input_var.get() #текст із Entry
        if self.var_name.get() == "name": #заповнення Listbox треками за введеним параметром
            for row in self.engine.select_name_tracks(text):
                self.list_box.insert(END, row[0])
        elif self.var_name.get() == "artist":  
            for row in self.engine.select_artist(text):
                self.list_box.insert(END, row[0])
        elif self.var_name.get() == "genre":
            for row in self.engine.select_genre(text):
                self.list_box.insert(END, row[0])
    
    def click_track(self, event):
        """Добуває детальну інформацію про обраний 
        трек і вводить її у відповідні Labels
        """
        widget = event.widget
        selection = widget.curselection() #обираємо елемент із Listbox
        if selection:
            song = widget.get(selection[0])  
            self.song_name.config(text = self.engine.select_name_tracks(song)[0][0]) 
            self.artist.config(text = self.engine.select_name_tracks(song)[0][1])
            self.album.config(text = self.engine.select_name_tracks(song)[0][2])
            millisec = int(self.engine.select_name_tracks(song)[0][3])
            self.length.config(text = str(int(millisec/60000)) + " хв " + str(int((millisec%60000)/1000)) + " сек") #вивід трека у хв і сек        
        
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