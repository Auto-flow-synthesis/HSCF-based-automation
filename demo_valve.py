from mttkinter import mtTkinter as tk
from tkinter import ttk
from interfaceFn import *
from heidolphFn import *
from milliGATFn import *
from valveFn import *
from sf10Fn import *
from asiapumpFn import *
from oushishengFn import *
from watsonFn import *
from rotaVapFn import *
from relayFn import *
import time
import threading
frame = InterfaceFn()
fr_cmdInt = frame.fr_cmdInt
#parameter
valve_1=valveFn()
#endparameter
#init
def autoprog_init():
	global valve_1
	valve_1.valve_init('COM1', 1, frame.lbl_init)
	# valve_1.lbl_valve_sta = lbl_valve_1_sta
#endinit
#cmd
def autoprog_start():
	global valve_1
	valve_1.valve_go(1.00, "2", lbl_0)
	autoprog_abort()
#endcmd
#abort
def autoprog_abort():
	valve_1.close()
#endabort
#label
lbl_0 = tk.Label(fr_cmdInt, width = 75, text = 'After 1.00 min, Valve 1 goes to position 2, total time usage 1.00', anchor = 'w', justify = tk.LEFT)
lbl_0.pack()
#endlabel
#timeline
1
#endtimeline
frame.btn_start['command']=lambda:threading.Thread(target=autoprog_start, name='StartThread').start()
frame.btn_abort['command']=lambda:threading.Thread(target=autoprog_abort, name='StartThread').start()
frame.btn_init['command']=lambda:threading.Thread(target=autoprog_init, name='StartThread').start()
frame.window.mainloop()
