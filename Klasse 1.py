# importing tkinter module
from tkinter import *
from PIL import ImageTk,Image #image stuff - install package: Pillow
#import tkinter as Tkinter
import random
import csv

class Klasse1:


    def __init__(self):
        self.root = Tk()
        self.klasse=[]

        with open('names.csv') as File:  # åbner filen for at procces den
            names = csv.reader(File)
            next(names)  # skipper headeren i csv filen
            for row in names:
               # print(row)
                splitnavn=row[0].split(';')
               # print(splitnavn)
                self.klasse.append(f"{splitnavn[0]} {splitnavn[1]}")
           # print(self.klasse)

        self.maxAntalGrupper = len(self.klasse)//2
        print(self.maxAntalGrupper)
        self.maxGruppeDeltagere = len(self.klasse)-2

        self.maxTal = max(self.maxAntalGrupper,self.maxGruppeDeltagere)


        velkomst = Label(self.root, text="Velkommen til GUI")
        velkomst.pack(pady=10)

        self.stateselector = StringVar()
        self.R1 = Radiobutton(self.root, text="Gruppestørrelse", value=0, var=self.stateselector, command = lambda:(self.antalDropdown.config(state='active')))
        self.R2 = Radiobutton(self.root, text="Antal Grupper", value=1, var=self.stateselector,command = lambda:(self.antalDropdown.config(state='active')))

        self.antalValgVar = StringVar(self.root)
        self.antalValgVar.set("Vælg antal")
        self.antalDropdown = OptionMenu(self.root, self.antalValgVar, *list(range(self.maxTal))[1:])
        self.antalDropdown.config(state='disabled')
       # self.antalDropdown.configure(self.root,self.antalValgVar, *list(range(self.maxAntalGrupper))[1:])
        self.R1.pack()
        self.R2.pack()

        self.antalDropdown.pack()

        mainloop()



    def dataReadout(self, frame):
        # returns Dict of row and column
        pass
if __name__ == '__main__':
    main = Klasse1()
