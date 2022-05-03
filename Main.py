import random
import pickle
from tkinter import *
from tkinter.ttk import * #progressbar
import csv


klasse1 =["abed efternavn", "benjamin", "christian", "salih", "laura", "emilie", "thor", "Mark", "kalja", "patrick"]
klasse2 =['abed', 'benjamin', 'christian', 'salih', 'laura', 'emilie', 'thor', 'Mark', 'kalja', 'patrick']
random.shuffle(klasse1)

groups = [[]]
Valg = input("hvor mange deltagere?")

if len(klasse1) >4 :
    length = len(klasse1)
    middle_index = length // 3
    Gruppe1 = klasse1[:middle_index]
    Gruppe2 = klasse1[middle_index:]

print(Gruppe1)
print(Gruppe2)
print(len(klasse1))

random.shuffle(klasse1)
print(klasse1)
filename = 'names.csv'

class mainWindow:
    def __init__(self):
        self.fodboldtur = {}

        with open('names.csv') as File:  # åbner filen for at procces den
            plots = csv.reader(File)
            next(plots)  # skipper headeren i csv filen

        def afslut():  # giver afslut en funktion som man kan køre i koden
            outfile = open(filename, 'wb')  # python åbner filen
            pickle.dump(self.fodboldtur, outfile)  # python gemmer filen
            outfile.close()  # python lukker filen
            print("Programmet er afsluttet!")

        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        # Progress bar widget
        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")

        self.progressLabel = Label(self.root, textvariable=self.progressLabelText)
        self.progressLabel.pack()
        self.progress = Progressbar(self.root, orient=HORIZONTAL,
                                    length=250, mode='determinate')
        self.progress['value'] = self.total / self.target * 100
        # print(self.progress['length'])
        # print(self.progress['value'])
        # BUTTONS
        self.progress.pack(padx=20)


