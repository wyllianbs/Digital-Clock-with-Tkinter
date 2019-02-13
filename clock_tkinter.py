#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Relógio Digital
Prof. Wyllian B. da Silva
'''

import time

try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

def mostra(tempo1=''):
	tempo2 = time.strftime('%H:%M:%S')
	if tempo2 != tempo1:
		tempo1 = tempo2
		relogio.config(text=tempo2)
		relogio.after(500, mostra)

if __name__ == '__main__':
	mestre = tk.Tk()
	mestre.title('Relógio Digital'.decode('utf-8'))
	relogio = tk.Label(mestre, font=('Helvetica', 150, 'bold'), bg='#ffeab4')
	relogio.pack(fill='both', expand=1)
	mestre.geometry('810x200+0+0')
	mostra()
	mestre.mainloop()
