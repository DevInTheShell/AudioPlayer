# -*- coding: utf-8 -*-

from tkinter import *

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        
        self.seekbar = Scale(self, orient = "horizontal", length = 435)
        self.seekbar.grid(row = 0, column = 0, columnspan = 5, pady = 5)
        
        self.time = Label(self, text = "00:00:00")
        self.time.grid(row = 0, column = 5, sticky = S, pady = 5)
        
        self.previous = Button(self, text = "Previous", width = 10)
        self.previous.grid(row = 1, column = 0, padx = 5)
        
        self.play = Button(self, text = "Play", width = 10)
        self.play.grid(row = 1, column = 1, padx = 5)
        
        self.pause = Button(self, text = "Pause", width = 10)
        self.pause.grid(row = 1, column = 2, padx = 5)
        
        self.stop = Button(self, text = "Stop", width = 10)
        self.stop.grid(row = 1, column = 3, padx = 5)
        
        self.next = Button(self, text = "Next", width = 10)
        self.next.grid(row = 1, column = 4, padx = 5)
        
        self.eject = Button(self, text = "Eject", width = 10)
        self.eject.grid(row = 1, column = 5, padx = 5)
        
        self.playlist = Listbox(self, width = 88, height = 20)
        self.playlist.grid(row = 2, column = 0, columnspan = 6, pady = 5)
        self.playlist.insert(END, " 1. Various Artist - Track 1")
        self.playlist.insert(END, " 2. Various Artist - Track 2")
        self.playlist.insert(END, " 3. Various Artist - Track 3")

if __name__ == "__main__":
    root = Tk()
    root.title("Audio Player")
    root.resizable(0, 0)
    app = Application(root)
    app.mainloop()
    root.destroy()