import tkinter as tkinter
from Voroni import Voronoi


class MainWindow:
    RADIUS = 3

    LOCK_FLAG = False

    def __init__(self, master):
        self.account = 0
        self.master = master
        self.master.title("Mini-Project 2 - Voronoi")
        self.tab=[]

        self.frmMain = tkinter.Frame(self.master, relief=tkinter.RAISED, borderwidth=1)
        self.frmMain.pack(fill=tkinter.BOTH, expand=1)

        self.w = tkinter.Canvas(self.frmMain, width=1000, height=1000)
        self.w.config(background='black')
        self.w.bind('<Double-1>', self.onDoubleClick)
        self.w.pack()

        self.frmButton = tkinter.Frame(self.master)
        self.frmButton.pack()

        self.btnCalculate = tkinter.Button(self.frmButton, text='Calculate', width=46, command=self.onClickCalculate)
        self.btnCalculate.pack(side=tkinter.LEFT)

        self.btnJD = tkinter.Button(self.frmButton, text='Next', width=47, command=self.onClickJD)
        self.btnJD.pack(side=tkinter.LEFT)

        self.btnClear = tkinter.Button(self.frmButton, text='Clear', width=46, command=self.onClickClear)
        self.btnClear.pack(side=tkinter.LEFT)


    def onClickCalculate(self):
        # jeden blok kodu nalezy odkreskowac

        #dodawanie punktów reczenie

        if not self.LOCK_FLAG:
            self.LOCK_FLAG = True

            pObj = self.w.find_all()
            points = []
            for p in pObj:
                coord = self.w.coords(p)
                points.append((coord[0] + self.RADIUS, coord[1] + self.RADIUS))

            vp = Voronoi(points)
            vp.process()
            lines = vp.get_output()
            self.drawLinesOnCanvas(lines)
            self.tab = lines
            print(lines)


    def onClickClear(self):
        self.LOCK_FLAG = False
        self.w.delete(tkinter.ALL)
        self.account=0
        self.tab=[]

    def onDoubleClick(self, event):
        if not self.LOCK_FLAG:
            self.w.create_oval(event.x - self.RADIUS, event.y - self.RADIUS, event.x + self.RADIUS,
                               event.y + self.RADIUS, fill="white")

    def onClickJD(self):
        if self.account>=len(self.tab):
            return
        else:
            l = self.tab[self.account]
            self.w.create_line(l[0], l[1], l[2], l[3], fill='yellow')
            self.account += 1

    def drawLinesOnCanvas(self, lines):
        tiu=['red','yellow','green','orange','purple','blue']
        for l in lines:
            y=0
            self.w.create_line(l[0], l[1], l[2], l[3], fill=tiu[int(y)])


def main():
    root = tkinter.Tk()
    app = MainWindow(root)
    root.mainloop()

main()
