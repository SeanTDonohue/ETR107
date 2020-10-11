# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:28:37 2020

@author: stimo
"""
from tkinter import Tk, Label
import tkinter as tk

window = Tk()
example = Label(window, text = "WOW! This is Fun!")
example.pack()

button = tk.Button(window, text = "DO NOT PRESS", bd = "5", bg= "red", fg= "white",  command = window.destroy)
button.pack(side = "top")

window.mainloop()

