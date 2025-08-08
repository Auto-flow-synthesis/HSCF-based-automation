from mttkinter import mtTkinter as tk
from tkinter import ttk
from interfaceFn import *
from heidolphFn import *
from milliGATFn import *
from valveFn import *
from sf10Fn import *
# from asiapumpFn import *
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
valve_2=valveFn()
valve_3=valveFn()
valve_4=valveFn()
valve_5=valveFn()
valve_6=valveFn()
valve_7=valveFn()
valve_8=valveFn()
valve_9=valveFn()
valve_10=valveFn()
valve_11=valveFn()
valve_12=valveFn()
valve_13=valveFn()
valve_14=valveFn()
valve_15=valveFn()
valve_16=valveFn()
valve_17=valveFn()
valve_18=valveFn()
valve_19=valveFn()
relay_1=relayFn()
watson_1=watsonFn()
watson_2=watsonFn()
watson_3=watsonFn()
oushisheng_1=oushishengFn()
sf10_1=sf10Fn()
milliGAT_S=milliGATFn()
milliGAT_E=milliGATFn()
milliGAT_C=milliGATFn()
milliGAT_M=milliGATFn()
milliGAT_D=milliGATFn()
milliGAT_U=milliGATFn()
rotaVap_1=rotaVapFn()
#endparameter
#init
def autoprog_init():
	global valve_1
	valve_1.valve_init('COM1', 1, frame.lbl_init)
	global valve_2
	valve_2.valve_init('COM2', 2, frame.lbl_init)
	global valve_3
	valve_3.valve_init('COM3', 3, frame.lbl_init)
	global valve_4
	valve_4.valve_init('COM4', 4, frame.lbl_init)
	global valve_5
	valve_5.valve_init('COM5', 5, frame.lbl_init)
	global valve_6
	valve_6.valve_init('COM6', 6, frame.lbl_init)
	global valve_7
	valve_7.valve_init('COM7', 7, frame.lbl_init)
	global valve_8
	valve_8.valve_init('COM8', 8, frame.lbl_init)
	global valve_9
	valve_9.valve_init('COM9', 9, frame.lbl_init)
	global valve_10
	valve_10.valve_init('COM10', 10, frame.lbl_init)
	global valve_11
	valve_11.valve_init('COM11', 11, frame.lbl_init)
	global valve_12
	valve_12.valve_init('COM12', 12, frame.lbl_init)
	global valve_13
	valve_13.valve_init('COM13', 13, frame.lbl_init)
	global valve_14
	valve_14.valve_init('COM14', 14, frame.lbl_init)
	global valve_15
	valve_15.valve_init('COM15', 15, frame.lbl_init)
	global valve_16
	valve_16.valve_init('COM16', 16, frame.lbl_init)
	global valve_17
	valve_17.valve_init('COM25', 17, frame.lbl_init)
	global valve_18
	valve_18.valve_init('COM26', 18, frame.lbl_init)
	global valve_19
	valve_19.valve_init('COM28', 19, frame.lbl_init)
	global relay_1
	relay_1.relay_init('COM29', 1, frame.lbl_init)
	global watson_1
	watson_1.watson_init('COM17', 1, frame.lbl_init)
	global watson_2
	watson_2.watson_init('COM18', 2, frame.lbl_init)
	global watson_3
	watson_3.watson_init('COM19', 3, frame.lbl_init)
	global oushisheng_1
	oushisheng_1.oushisheng_init('COM20', 1, frame.lbl_init)
	global sf10_1
	sf10_1.sf10_init('COM30', 1, frame.lbl_init)
	global milliGAT_S
	milliGAT_S.milliGAT_init('COM27', 'S', frame.lbl_init)
	global milliGAT_E
	milliGAT_E.milliGAT_init('COM21', 'E', frame.lbl_init)
	global milliGAT_C
	milliGAT_C.milliGAT_init('COM23', 'C', frame.lbl_init)
	global milliGAT_M
	milliGAT_M.milliGAT_init('COM23', 'M', frame.lbl_init)
	global milliGAT_D
	milliGAT_D.milliGAT_init('COM22', 'D', frame.lbl_init)
	global milliGAT_U
	milliGAT_U.milliGAT_init('COM24', 'U', frame.lbl_init)
	global rotaVap_1
	rotaVap_1.rotaVap_init('1', frame.lbl_init)
#endinit

# cmd for global initialize
def initialize_valves():
	valve_1.valve_go(0.005, "1", lbl_0)
	valve_2.valve_go(0.005, "1", lbl_0)
	valve_3.valve_go(0.005, "1", lbl_0)
	valve_4.valve_go(0.005, "1", lbl_0)
	valve_5.valve_go(0.005, "1", lbl_0)
	valve_6.valve_go(0.005, "1", lbl_0)
	valve_7.valve_go(0.005, "2", lbl_0)
	valve_8.valve_go(0.005, "1", lbl_0)
	valve_9.valve_go(0.005, "1", lbl_0)
	valve_10.valve_go(0.005, "1", lbl_0)
	valve_11.valve_go(0.005, "1", lbl_0)
	valve_12.valve_go(0.005, "1", lbl_0)
	valve_13.valve_go(0.005, "1", lbl_0)
	valve_14.valve_go(0.005, "1", lbl_0)
	valve_15.valve_go(0.005, "1", lbl_0)
	valve_16.valve_go(0.005, "1", lbl_0)
	valve_17.valve_go(0.005, "1", lbl_0)
	valve_18.valve_go(0.005, "2", lbl_0)
	valve_19.valve_go(0.005, "1", lbl_0)
def initialize_milliGAT():
	milliGAT_S.milliGAT_pumping('S', 0.005, 0.00, lbl_1)
	milliGAT_S.milliGAT_stoping('S', 0.005, lbl_1)
	milliGAT_E.milliGAT_pumping('E', 0.005, 0.00, lbl_1)
	milliGAT_E.milliGAT_stoping('E', 0.005, lbl_1)
	milliGAT_C.milliGAT_pumping('C', 0.005, 0.00, lbl_1)
	milliGAT_C.milliGAT_stoping('C', 0.005, lbl_1)
	milliGAT_M.milliGAT_pumping('M', 0.005, 0.00, lbl_1)
	milliGAT_M.milliGAT_stoping('M', 0.005, lbl_1)
	milliGAT_D.milliGAT_pumping('D', 0.005, 0.00, lbl_1)
	milliGAT_D.milliGAT_stoping('D', 0.005, lbl_1)
	milliGAT_U.milliGAT_pumping('U', 0.005, 0.00, lbl_1)
	milliGAT_U.milliGAT_stoping('U', 0.005, lbl_1)

# cmd for global operation	
def rotaVao_10min_200to75mbar():   
	valve_8.valve_go(0.00, "4", lbl_2)
	valve_9.valve_go(0.00, "4", lbl_2)
	valve_10.valve_go(0.00, "8", lbl_2)
	valve_19.valve_go(0.00, "2", lbl_2)
	rotaVap_1.Global_status(True, 0.00, lbl_2)
	rotaVap_1.lift_height(220, lbl_2)
	rotaVap_1.heating(50, True, lbl_2)
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_2)
	rotaVap_1.vacuum_P(75, True, 0.00,  lbl_2)
	valve_10.valve_go(8.00, "9", lbl_2)
	valve_10.valve_go(2.00, "7", lbl_2)
	valve_19.valve_go(0.00, "1", lbl_2)
	rotaVap_1.Global_status(False, 0.00, lbl_2)
	rotaVap_1.heating(20, True, lbl_2)
def rotaVao_20min_200to75mbar():    
	valve_8.valve_go(0.00, "4", lbl_3)
	valve_9.valve_go(0.00, "4", lbl_3)
	valve_10.valve_go(0.00, "8", lbl_3)
	valve_19.valve_go(0.00, "2", lbl_3)
	rotaVap_1.Global_status(True, 0.00, lbl_3)
	rotaVap_1.lift_height(220, lbl_3)
	rotaVap_1.heating(50, True, lbl_3)
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_3)
	rotaVap_1.vacuum_P(75, True, 0.00,  lbl_3)
	valve_10.valve_go(10.00, "9", lbl_3)
	valve_10.valve_go(10.00, "7", lbl_3)
	valve_19.valve_go(0.00, "1", lbl_3)
	rotaVap_1.Global_status(False, 0.00, lbl_3)
	rotaVap_1.heating(20, True, lbl_3)
def rotaVap_colletion():   
	valve_8.valve_go(0.00, "1", lbl_4)
	valve_9.valve_go(0.00, "1", lbl_4)
	rotaVap_1.rotation_speed(80, True, 0.00,  lbl_4)
	watson_3.watson_pumping('RL', 0.00, 1000.0, lbl_4)
	watson_3.watson_pumping('RL', 0.30, 1.0, lbl_4)
	rotaVap_1.rotation_speed(00, True, 0.00,  lbl_4)

	valve_8.valve_go(0.00, "4", lbl_4)
	valve_9.valve_go(0.00, "4", lbl_4)
	valve_10.valve_go(0.00, "8", lbl_4)
	valve_19.valve_go(0.00, "2", lbl_4)
	rotaVap_1.Global_status(True, 0.00, lbl_4)
	rotaVap_1.heating(50, True, lbl_4)
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_4)
	rotaVap_1.vacuum_P(300, True, 0.00,  lbl_4)
	valve_10.valve_go(4.70, "7", lbl_4)
	valve_19.valve_go(0.00, "1", lbl_4)
	rotaVap_1.Global_status(False, 0.00, lbl_4)
	rotaVap_1.heating(20, True, lbl_4)
def rotaVap_wash_Acetone3():   
	rotaVap_1.rotation_speed(80, True, 0.00,  lbl_5)
	watson_3.watson_pumping('RL', 0.00, 1000.0, lbl_5)
	# round 1    # time 2.3 min
	valve_8.valve_go(0.00, "1", lbl_5)
	valve_9.valve_go(0.00, "1", lbl_5)
	valve_8.valve_go(0.30, "4", lbl_5)
	valve_9.valve_go(0.00, "1", lbl_5)
	valve_8.valve_go(1.00, "2", lbl_5)
	valve_9.valve_go(0.00, "2", lbl_5)
	valve_19.valve_go(0.00, "2", lbl_5)
	valve_8.valve_go(1.00, "1", lbl_5)
	valve_9.valve_go(0.00, "1", lbl_5)
	# round 2    # time 2.3 min
	valve_8.valve_go(0.00, "1", lbl_5)
	valve_9.valve_go(0.00, "1", lbl_5)
	valve_8.valve_go(0.30, "4", lbl_5)
	valve_9.valve_go(0.00, "1", lbl_5)
	valve_8.valve_go(1.00, "2", lbl_5)
	valve_9.valve_go(0.00, "2", lbl_5)
	valve_19.valve_go(0.00, "2", lbl_5)
	valve_8.valve_go(1.00, "1", lbl_5)
	valve_9.valve_go(0.00, "1", lbl_5)
	# round 3    # time 2.4 min
	valve_8.valve_go(0.00, "1", lbl_5)
	valve_9.valve_go(0.00, "1", lbl_5)
	valve_8.valve_go(0.40, "4", lbl_5)
	valve_9.valve_go(0.00, "1", lbl_5)
	valve_8.valve_go(1.00, "2", lbl_5)
	valve_9.valve_go(0.00, "2", lbl_5)
	valve_19.valve_go(0.00, "2", lbl_5)
	valve_8.valve_go(1.00, "1", lbl_5)
	valve_9.valve_go(0.00, "1", lbl_5)
	# round x    # time 5 min
	valve_8.valve_go(0.00, "3", lbl_5)
	valve_9.valve_go(0.00, "2", lbl_5)
	watson_3.watson_pumping('RL', 5.00, 1.0, lbl_5)
	rotaVap_1.rotation_speed(0, True, 0.00,  lbl_5)
	# rotoVap for 2 min
	valve_8.valve_go(0.00, "4", lbl_5)
	valve_9.valve_go(0.00, "4", lbl_5)
	valve_10.valve_go(0.00, "8", lbl_5)
	valve_19.valve_go(0.00, "2", lbl_5)
	rotaVap_1.Global_status(True, 0.00, lbl_5)
	rotaVap_1.heating(50, True, lbl_5)
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_5)
	rotaVap_1.vacuum_P(50, True, 0.00,  lbl_5)
	valve_10.valve_go(2.00, "7", lbl_5)
	valve_19.valve_go(0.00, "1", lbl_5)
	rotaVap_1.Global_status(False, 0.00, lbl_5)
	rotaVap_1.heating(20, True, lbl_5)
def rotaVap_wash_Acetone1():    
	rotaVap_1.rotation_speed(80, True, 0.00,  lbl_6)
	watson_3.watson_pumping('RL', 0.00, 1000.0, lbl_6)
	# round 1    # time 2.3 min
	valve_8.valve_go(0.00, "1", lbl_6)
	valve_9.valve_go(0.00, "1", lbl_6)
	valve_8.valve_go(0.30, "4", lbl_6)
	valve_9.valve_go(0.00, "1", lbl_6)
	valve_8.valve_go(1.00, "2", lbl_6)
	valve_9.valve_go(0.00, "2", lbl_6)
	valve_19.valve_go(0.00, "2", lbl_6)
	valve_8.valve_go(1.00, "1", lbl_6)
	valve_9.valve_go(0.00, "1", lbl_6)
	# round x    # time 5 min
	valve_8.valve_go(0.00, "3", lbl_6)
	valve_9.valve_go(0.00, "2", lbl_6)
	watson_3.watson_pumping('RL', 5.00, 1.0, lbl_6)
	rotaVap_1.rotation_speed(0, True, 0.00,  lbl_6)
	# rotoVap for 2 min
	valve_8.valve_go(0.00, "4", lbl_6)
	valve_9.valve_go(0.00, "4", lbl_6)
	valve_10.valve_go(0.00, "8", lbl_6)
	valve_19.valve_go(0.00, "2", lbl_6)
	rotaVap_1.Global_status(True, 0.00, lbl_6)
	rotaVap_1.heating(50, True, lbl_6)
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_6)
	rotaVap_1.vacuum_P(50, True, 0.00,  lbl_6)
	valve_10.valve_go(2.00, "7", lbl_6)
	valve_19.valve_go(0.00, "1", lbl_6)
	rotaVap_1.Global_status(False, 0.00, lbl_6)
	rotaVap_1.heating(20, True, lbl_6)
def rotaVap_move_waste():   
	valve_8.valve_go(0.00, "3", lbl_7)
	valve_9.valve_go(0.00, "2", lbl_7)
	watson_3.watson_pumping('RL', 0.00, 1000.0, lbl_7)
	watson_3.watson_pumping('RL', 5.00, 1.0, lbl_7)

# cmd for reaction step 1
def first_step_preparation():   
	valve_1.valve_go(0.00, "1", lbl_8)
	valve_2.valve_go(0.00, "1", lbl_8)
	milliGAT_S.milliGAT_pumping('S', 0.00, 10000.00, lbl_8)
	valve_1.valve_go(3.00, "2", lbl_8)  
	valve_1.valve_go(3.00, "3", lbl_8)  
	valve_1.valve_go(5.00, "4", lbl_8) 
	valve_1.valve_go(1.50, "5", lbl_8)  
	milliGAT_S.milliGAT_stoping('S', 0.50, lbl_8)  
def first_step_reaction():                            
	valve_3.valve_go(0.00, "2", lbl_9)
	watson_1.watson_pumping('RL', 0.00, 1000.0, lbl_9)
	valve_3.valve_go(659.00, "1", lbl_9)    # reaction time
	watson_1.watson_pumping('RL', 2.00, 1.0, lbl_9)
def first_step_wash_tubing():    
	valve_1.valve_go(0.00, "5", lbl_10)
	valve_2.valve_go(0.00, "1", lbl_10)
	milliGAT_S.milliGAT_pumping('S', 0.00, 10000.00, lbl_10)
	milliGAT_S.milliGAT_stoping('S', 5.00, lbl_10)    
	valve_3.valve_go(0.00, "2", lbl_10)
	watson_1.watson_pumping('RL', 0.00, 1000.0, lbl_10)
	valve_3.valve_go(1.00, "1", lbl_10)
	watson_1.watson_pumping('RL', 5.00, 1.0, lbl_10)
def first_step_filtration():    
	valve_1.valve_go(0.00, "7", lbl_11)
	valve_2.valve_go(0.00, "2", lbl_11)
	milliGAT_S.milliGAT_pumping('S', 0.00, -10000.00, lbl_11)
	milliGAT_S.milliGAT_stoping('S', 20.00, lbl_11)    
def first_step_wash_filtration():   
	valve_1.valve_go(0.00, "5", lbl_12)
	valve_2.valve_go(0.00, "2", lbl_12)
	milliGAT_S.milliGAT_pumping('S', 0.00, 10000.00, lbl_12)
	milliGAT_S.milliGAT_stoping('S', 5.00, lbl_12)
	valve_1.valve_go(0.00, "7", lbl_12)
	valve_2.valve_go(0.00, "2", lbl_12)
	milliGAT_S.milliGAT_pumping('S', 0.00, -10000.00, lbl_12)
	milliGAT_S.milliGAT_stoping('S', 10.00, lbl_12) 
def first_step_final_cleaning():  
	# wash with Acetone
	valve_1.valve_go(0.00, "6", lbl_13)
	valve_2.valve_go(0.00, "2", lbl_13)
	milliGAT_S.milliGAT_pumping('S', 0.00, 10000.00, lbl_13)
	milliGAT_S.milliGAT_stoping('S', 4.00, lbl_13)
	valve_1.valve_go(0.00, "8", lbl_13)
	valve_2.valve_go(0.00, "2", lbl_13)
	milliGAT_S.milliGAT_pumping('S', 0.00, -10000.00, lbl_13)
	milliGAT_S.milliGAT_stoping('S', 6.00, lbl_13)
	# wash with Acetone
	valve_1.valve_go(0.00, "6", lbl_13)
	valve_2.valve_go(0.00, "2", lbl_13)
	milliGAT_S.milliGAT_pumping('S', 0.00, 10000.00, lbl_13)
	milliGAT_S.milliGAT_stoping('S', 4.00, lbl_13)
	valve_1.valve_go(0.00, "8", lbl_13)
	valve_2.valve_go(0.00, "2", lbl_13)
	milliGAT_S.milliGAT_pumping('S', 0.00, -10000.00, lbl_13)
	milliGAT_S.milliGAT_stoping('S', 6.00, lbl_13)
	# wash with EtOAc		
	valve_1.valve_go(0.00, "5", lbl_13)
	valve_2.valve_go(0.00, "2", lbl_13)
	milliGAT_S.milliGAT_pumping('S', 0.00, 10000.00, lbl_13)
	milliGAT_S.milliGAT_stoping('S', 4.00, lbl_13)
	valve_1.valve_go(0.00, "8", lbl_13)
	valve_2.valve_go(0.00, "2", lbl_13)
	milliGAT_S.milliGAT_pumping('S', 0.00, -10000.00, lbl_13)
	milliGAT_S.milliGAT_stoping('S', 8.00, lbl_13)

# cmd for reaction step 2
def second_step_preparation():  
	valve_4.valve_go(0.00, "1", lbl_14)
	valve_5.valve_go(0.00, "1", lbl_14)
	milliGAT_E.milliGAT_pumping('E', 0.00, 10000.00, lbl_14)
	valve_4.valve_go(1.50, "2", lbl_14) 
	valve_4.valve_go(2.00, "3", lbl_14) 
	milliGAT_E.milliGAT_stoping('E', 0.50, lbl_14) 
def second_step_reaction():   
	valve_6.valve_go(0.00, "2", lbl_15)
	watson_2.watson_pumping('RL', 0.00, 1000.0, lbl_15)
	valve_6.valve_go(141.0, "1", lbl_15)    # reaction time 141 min
	watson_2.watson_pumping('RL', 2.00, 1.0, lbl_15)
def second_step_wash_tubing():   
	valve_4.valve_go(0.00, "3", lbl_16)
	valve_5.valve_go(0.00, "1", lbl_16)
	milliGAT_E.milliGAT_pumping('E', 0.00, 25000.00, lbl_16)
	milliGAT_E.milliGAT_stoping('E', 2.00, lbl_16)  
	valve_6.valve_go(0.00, "2", lbl_16)
	watson_2.watson_pumping('RL', 0.00, 1000.0, lbl_16)
	valve_6.valve_go(1.00, "1", lbl_16)
	watson_2.watson_pumping('RL', 5.00, 1.0, lbl_16)
def second_step_filtration():  
	valve_4.valve_go(0.00, "6", lbl_17)
	valve_5.valve_go(0.00, "2", lbl_17)
	valve_10.valve_go(0.00, "1", lbl_17)
	milliGAT_E.milliGAT_pumping('E', 0.00, -25000.00, lbl_17)
	milliGAT_E.milliGAT_stoping('E', 15.00, lbl_17)
def second_step_wash_filtration():   
	valve_4.valve_go(0.00, "3", lbl_18)
	valve_5.valve_go(0.00, "2", lbl_18)
	milliGAT_E.milliGAT_pumping('E', 0.00, 25000.00, lbl_18)
	milliGAT_E.milliGAT_stoping('E', 4.00, lbl_18)
	valve_4.valve_go(0.00, "6", lbl_18)
	valve_5.valve_go(0.00, "2", lbl_18)
	valve_10.valve_go(0.00, "1", lbl_18)
	milliGAT_E.milliGAT_pumping('E', 0.00, -25000.00, lbl_18)
	milliGAT_E.milliGAT_stoping('E', 6.00, lbl_18)
def second_step_final_cleaning(): 
 	# wash with H2O
	valve_4.valve_go(0.00, "7", lbl_19)
	valve_5.valve_go(0.00, "2", lbl_19)
	milliGAT_E.milliGAT_pumping('E', 0.00, 25000.00, lbl_19)
	milliGAT_E.milliGAT_stoping('E', 4.00, lbl_19)    
	valve_4.valve_go(0.00, "8", lbl_19)
	valve_5.valve_go(0.00, "2", lbl_19)
	milliGAT_E.milliGAT_pumping('E', 0.00, -25000.00, lbl_19)
	milliGAT_E.milliGAT_stoping('E', 8.00, lbl_19)   
	# wash with Acetone
	valve_4.valve_go(0.00, "5", lbl_19)
	valve_5.valve_go(0.00, "2", lbl_19)
	milliGAT_E.milliGAT_pumping('E', 0.00, 25000.00, lbl_19)
	milliGAT_E.milliGAT_stoping('E', 4.00, lbl_19)    
	valve_4.valve_go(0.00, "8", lbl_19)
	valve_5.valve_go(0.00, "2", lbl_19)
	milliGAT_E.milliGAT_pumping('E', 0.00, -25000.00, lbl_19)
	milliGAT_E.milliGAT_stoping('E', 8.00, lbl_19)   
	# wash with EtOAc		
	valve_4.valve_go(0.00, "3", lbl_19)
	valve_5.valve_go(0.00, "2", lbl_19)
	milliGAT_E.milliGAT_pumping('E', 0.00, 25000.00, lbl_19)
	milliGAT_E.milliGAT_stoping('E', 4.00, lbl_19)    
	valve_4.valve_go(0.00, "8", lbl_19)
	valve_5.valve_go(0.00, "2", lbl_19)
	milliGAT_E.milliGAT_pumping('E', 0.00, -25000.00, lbl_19)
	milliGAT_E.milliGAT_stoping('E', 8.00, lbl_19)
def second_step_recrystallization():    # time 64 min
	# wash with Hex round 1 
	valve_4.valve_go(0.00, "6", lbl_20)
	valve_5.valve_go(0.00, "4", lbl_20)
	valve_10.valve_go(0.00, "1", lbl_20)
	milliGAT_E.milliGAT_pumping('E', 0.00, -25000.00, lbl_20)
	rotaVap_1.lift_height(220, lbl_20)
	rotaVap_1.heating(60, True, lbl_20)
	rotaVap_1.rotation_speed(100, True, 0.00,  lbl_20)
	milliGAT_E.milliGAT_stoping('E', 12.00, lbl_20)
	valve_4.valve_go(5.00, "6", lbl_20)
	valve_5.valve_go(0.00, "3", lbl_20)
	valve_7.valve_go(0.00, "1", lbl_20)
	valve_10.valve_go(0.00, "1", lbl_20)
	milliGAT_E.milliGAT_pumping('E', 0.00, 25000.00, lbl_20)
	milliGAT_E.milliGAT_stoping('E', 16.00, lbl_20)
	# wash with Hex round 2
	valve_4.valve_go(0.00, "6", lbl_20)
	valve_5.valve_go(0.00, "4", lbl_20)
	valve_10.valve_go(0.00, "1", lbl_20)
	milliGAT_E.milliGAT_pumping('E', 0.00, -25000.00, lbl_20)
	milliGAT_E.milliGAT_stoping('E', 2.00, lbl_20)
	valve_4.valve_go(5.00, "6", lbl_20)
	valve_5.valve_go(0.00, "3", lbl_20)
	valve_10.valve_go(0.00, "1", lbl_20)
	rotaVap_1.rotation_speed(0, True, 0.00,  lbl_20)
	milliGAT_E.milliGAT_pumping('E', 0.00, 25000.00, lbl_20)
	milliGAT_E.milliGAT_stoping('E', 4.00, lbl_20)
	# rotaVap stop work
	rotaVap_1.lift_height(0, lbl_20)
	rotaVap_1.heating(20, True, lbl_20)
	# move waste
	valve_4.valve_go(0.00, "8", lbl_20)
	valve_5.valve_go(0.00, "3", lbl_20)
	milliGAT_E.milliGAT_pumping('E', 0.00, -25000.00, lbl_20)
	milliGAT_E.milliGAT_stoping('E', 20.00, lbl_20)
	# stop cooling
	valve_7.valve_go(0.00, "2", lbl_20) 
def second_step_dissolve_product():  
	valve_4.valve_go(0.00, "4", lbl_21)
	valve_5.valve_go(0.00, "3", lbl_21)
	milliGAT_E.milliGAT_pumping('E', 0.00, 25000.00, lbl_21)
	milliGAT_E.milliGAT_stoping('E', 16.00, lbl_21) 

# cmd for reaction step 3
def third_step_reaction_and_separation():  
	valve_10.valve_go(0.00, "2", lbl_22)
	valve_11.valve_go(0.00, "1", lbl_22)
	valve_12.valve_go(0.00, "1", lbl_22)
	milliGAT_C.milliGAT_pumping('C', 0.00, 30000.00, lbl_22) 
	milliGAT_M.milliGAT_pumping('M', 0.00, 5000.00, lbl_22) 
	milliGAT_D.milliGAT_pumping('D', 0.00, 10000.00, lbl_22) 
	
	valve_11.valve_go(65.00, "2", lbl_22) 
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_22) 
	milliGAT_M.milliGAT_stoping('M', 1.00, lbl_22)  
	milliGAT_C.milliGAT_stoping('C', 3.00, lbl_22)  
	milliGAT_D.milliGAT_stoping('D', 0.00, lbl_22)  
def third_step_transfer_for_FC():  
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_23)
	rotaVap_1.lift_height(220, lbl_23)
	rotaVap_1.heating(60, True, lbl_23)
	# round 1    # time 13 min
	valve_10.valve_go(0.00, "3", lbl_23)
	valve_11.valve_go(0.00, "4", lbl_23)
	valve_12.valve_go(0.00, "2", lbl_23)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_23)
	milliGAT_D.milliGAT_stoping('D', 2.00, lbl_23) 
	valve_10.valve_go(5.00, "3", lbl_23)
	valve_11.valve_go(0.00, "3", lbl_23)
	valve_12.valve_go(0.00, "2", lbl_23)
	valve_13.valve_go(0.00, "1", lbl_23)
	valve_17.valve_go(0.00, "4", lbl_23)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_23)
	milliGAT_D.milliGAT_stoping('D', 6.00, lbl_23)
	# round 2    # time 9 min
	valve_10.valve_go(0.00, "3", lbl_23)
	valve_11.valve_go(0.00, "4", lbl_23)
	valve_12.valve_go(0.00, "2", lbl_23)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_23)
	milliGAT_D.milliGAT_stoping('D', 1.00, lbl_23) 
	valve_10.valve_go(5.00, "3", lbl_23)
	valve_11.valve_go(0.00, "3", lbl_23)
	valve_12.valve_go(0.00, "2", lbl_23)
	valve_13.valve_go(0.00, "1", lbl_23)
	valve_17.valve_go(0.00, "4", lbl_23)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_23)
	milliGAT_D.milliGAT_stoping('D', 3.00, lbl_23) 
	# round 3    # time 4 min
	valve_10.valve_go(0.00, "3", lbl_23)
	valve_11.valve_go(0.00, "4", lbl_23)
	valve_12.valve_go(0.00, "2", lbl_23)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_23)
	milliGAT_D.milliGAT_stoping('D', 1.00, lbl_23) 
	valve_10.valve_go(0.00, "3", lbl_23)
	valve_11.valve_go(0.00, "3", lbl_23)
	valve_12.valve_go(0.00, "2", lbl_23)
	valve_13.valve_go(0.00, "1", lbl_23)
	valve_17.valve_go(0.00, "4", lbl_23)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_23)
	milliGAT_D.milliGAT_stoping('D', 3.00, lbl_23) 
	
	rotaVap_1.rotation_speed(0, True, 0.00,  lbl_23)
	rotaVap_1.lift_height(0, lbl_23)
	rotaVap_1.heating(20, True, lbl_23)
def third_step_FC_purge():   
	valve_17.valve_go(0.00, "4", lbl_24)
	valve_13.valve_go(0.00, "3", lbl_24)
	valve_13.valve_go(0.85, "2", lbl_24)
	valve_13.valve_go(0.15, "1", lbl_24)
def third_step_FC():  
	valve_10.valve_go(0.00, "4", lbl_25)
	valve_11.valve_go(0.00, "3", lbl_25)
	valve_12.valve_go(0.00, "3", lbl_25)
	valve_13.valve_go(0.00, "1", lbl_25)
	valve_17.valve_go(0.00, "1", lbl_25)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_25)
	milliGAT_D.milliGAT_stoping('D', 20.00, lbl_25)  
	valve_13.valve_go(0.00, "3", lbl_25)
	valve_13.valve_go(3.60, "2", lbl_25)
	valve_13.valve_go(0.40, "1", lbl_25)
def third_step_clean_colum(): 
	# round 1 EtOAc    # time 3 min
	valve_10.valve_go(0.00, "4", lbl_26)
	valve_11.valve_go(0.00, "3", lbl_26)
	valve_12.valve_go(0.00, "5", lbl_26)
	valve_13.valve_go(0.00, "1", lbl_26)
	valve_17.valve_go(0.00, "4", lbl_26)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_26)
	milliGAT_D.milliGAT_stoping('D', 2.00, lbl_26) 
	valve_13.valve_go(0.00, "3", lbl_26)
	valve_13.valve_go(0.85, "2", lbl_26)
	valve_13.valve_go(0.15, "1", lbl_26)
	# round 2 EtOAc    # time 3 min
	valve_10.valve_go(0.00, "4", lbl_26)
	valve_11.valve_go(0.00, "3", lbl_26)
	valve_12.valve_go(0.00, "5", lbl_26)
	valve_13.valve_go(0.00, "1", lbl_26)
	valve_17.valve_go(0.00, "4", lbl_26)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_26)
	milliGAT_D.milliGAT_stoping('D', 2.00, lbl_26) 
	valve_13.valve_go(0.00, "3", lbl_26)
	valve_13.valve_go(0.85, "2", lbl_26)
	valve_13.valve_go(0.15, "1", lbl_26)
	# round 3 EtOAc    # time 3 min
	valve_10.valve_go(0.00, "4", lbl_26)
	valve_11.valve_go(0.00, "3", lbl_26)
	valve_12.valve_go(0.00, "5", lbl_26)
	valve_13.valve_go(0.00, "1", lbl_26)
	valve_17.valve_go(0.00, "4", lbl_26)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_26)
	milliGAT_D.milliGAT_stoping('D', 2.00, lbl_26) 
	valve_13.valve_go(0.00, "3", lbl_26)
	valve_13.valve_go(0.85, "2", lbl_26)
	valve_13.valve_go(0.15, "1", lbl_26)
	# round 4 Hexane    # time 3 min
	valve_10.valve_go(0.00, "4", lbl_26)
	valve_11.valve_go(0.00, "3", lbl_26)
	valve_12.valve_go(0.00, "4", lbl_26)
	valve_13.valve_go(0.00, "1", lbl_26)
	valve_17.valve_go(0.00, "4", lbl_26)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_26)
	milliGAT_D.milliGAT_stoping('D', 2.00, lbl_26) 
	valve_13.valve_go(0.00, "3", lbl_26)
	valve_13.valve_go(0.85, "2", lbl_26)
	valve_13.valve_go(0.15, "1", lbl_26)
	# round 5 Hexane    # time 3 min
	valve_10.valve_go(0.00, "4", lbl_26)
	valve_11.valve_go(0.00, "3", lbl_26)
	valve_12.valve_go(0.00, "4", lbl_26)
	valve_13.valve_go(0.00, "1", lbl_26)
	valve_17.valve_go(0.00, "4", lbl_26)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_26)
	milliGAT_D.milliGAT_stoping('D', 2.00, lbl_26)  
	valve_13.valve_go(0.00, "3", lbl_26)
	valve_13.valve_go(0.85, "2", lbl_26)
	valve_13.valve_go(0.15, "1", lbl_26)
def third_step_dissolve_product():  
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_27)
	# round 1    # time 28 min
	valve_10.valve_go(0.00, "3", lbl_27)
	valve_11.valve_go(0.00, "5", lbl_27)
	valve_12.valve_go(0.00, "2", lbl_27)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_27)
	milliGAT_D.milliGAT_stoping('D', 12.00, lbl_27)  
	valve_10.valve_go(0.00, "3", lbl_27)
	valve_11.valve_go(0.00, "6", lbl_27)
	valve_12.valve_go(0.00, "2", lbl_27)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_27)
	milliGAT_D.milliGAT_stoping('D', 16.00, lbl_27)  
	# round 2    # time 20 min
	valve_10.valve_go(0.00, "3", lbl_27)
	valve_11.valve_go(0.00, "5", lbl_27)
	valve_12.valve_go(0.00, "2", lbl_27)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_27)
	milliGAT_D.milliGAT_stoping('D', 8.00, lbl_27) 
	valve_10.valve_go(0.00, "3", lbl_27)
	valve_11.valve_go(0.00, "6", lbl_27)
	valve_12.valve_go(0.00, "2", lbl_27)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_27)
	milliGAT_D.milliGAT_stoping('D', 12.00, lbl_27)  
	# round 3    # time 12 min
	valve_10.valve_go(0.00, "3", lbl_27)
	valve_11.valve_go(0.00, "5", lbl_27)
	valve_12.valve_go(0.00, "2", lbl_27)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_27)
	milliGAT_D.milliGAT_stoping('D', 4.00, lbl_27) 
	valve_10.valve_go(0.00, "3", lbl_27)
	valve_11.valve_go(0.00, "6", lbl_27)
	valve_12.valve_go(0.00, "2", lbl_27)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_27)
	milliGAT_D.milliGAT_stoping('D', 8.00, lbl_27)  
	# stop rotovap
	rotaVap_1.rotation_speed(0, True, 0.00,  lbl_27)

# cmd for reaction step 4
def fourth_step_preparation():   
	# puge Argon
	valve_16.valve_go(0.00, "1", lbl_28)
	valve_18.valve_go(0.00, "2", lbl_28)
	# chemical transfer   
	valve_14.valve_go(0.00, "1", lbl_28)
	valve_15.valve_go(0.00, "1", lbl_28)
	milliGAT_U.milliGAT_pumping('U', 0.00, 10000.00, lbl_28)
	valve_14.valve_go(1.00, "2", lbl_28) 
	valve_14.valve_go(2.00, "3", lbl_28)
	milliGAT_U.milliGAT_stoping('U', 2.0, lbl_28) 
	# stop puge Argon
	valve_16.valve_go(0.00, "2", lbl_28)
	valve_18.valve_go(0.00, "1", lbl_28)
def fourth_step_reaction():
	relay_1.relay_go(0.00, 1, "1", lbl_29)
	valve_16.valve_go(0.00, "2", lbl_29)
	valve_18.valve_go(0.00, "1", lbl_29)
	oushisheng_1.oushisheng_pumping('1', 0.00, 100.0, lbl_29)
	sf10_1.sf10_pumping('SF10', 0.00, 100.0, lbl_29)
	valve_16.valve_go(1345.00, "1", lbl_29)  # reaction time 24h
	valve_18.valve_go(0.00, "1", lbl_29)
	valve_16.valve_go(10.00, "1", lbl_29) 
	valve_18.valve_go(0.00, "2", lbl_29)
	valve_16.valve_go(10.00, "2", lbl_29)
	valve_18.valve_go(0.00, "1", lbl_29)
	oushisheng_1.oushisheng_pumping('1', 0.00, 100.0, lbl_29)
	sf10_1.sf10_pumping('SF10', 0.00, 100.0, lbl_29)
	relay_1.relay_go(0.00, 1, "1", lbl_29)
# cmd for reaction
def reaction_1():
	first_step_preparation() 
	first_step_reaction() 
	first_step_wash_tubing()
	first_step_filtration()
	first_step_wash_filtration() 
	first_step_final_cleaning() 
def reaction_2():
	second_step_preparation() 
	second_step_reaction()
	second_step_wash_tubing() 
	second_step_filtration()
	second_step_wash_filtration() 
	rotaVao_20min_200to75mbar() 
	rotaVap_colletion() 
	second_step_recrystallization() 
	second_step_final_cleaning() 
	rotaVap_wash_Acetone3() 
	second_step_dissolve_product() 
def reaction_3():
	third_step_reaction_and_separation()
	rotaVao_20min_200to75mbar() 
	rotaVap_colletion() 
	third_step_transfer_for_FC() 
	rotaVap_wash_Acetone1() 
	third_step_FC_purge()
	third_step_FC() 
	rotaVao_10min_200to75mbar() 
	rotaVap_move_waste()
	third_step_FC() 
	rotaVao_10min_200to75mbar() 
	rotaVap_move_waste() 
	third_step_FC()
	rotaVao_10min_200to75mbar() 
	rotaVap_move_waste()
	third_step_FC() 
	rotaVao_20min_200to75mbar()
	rotaVap_move_waste() 
	rotaVap_colletion()
def reaction_4():
	fourth_step_preparation()
	fourth_step_reaction()
def reaction_1_to_3():
	reaction_1()
	reaction_2()
	reaction_3()
def reaction_4_and_1_to_3():
	thread1 = threading.Thread(target=reaction_1_to_3)
	thread2 = threading.Thread(target=reaction_4)
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()

# cmd for start
def autoprog_start():
	global valve_1
	global valve_2
	global valve_3
	global valve_4
	global valve_5
	global valve_6
	global valve_7
	global valve_8
	global valve_9
	global valve_10
	global valve_11
	global valve_12
	global valve_13
	global valve_14
	global valve_15
	global valve_16
	global valve_17
	global valve_18
	global valve_19
	global relay_1
	global watson_1
	global watson_2
	global watson_3
	global oushisheng_1
	global sf10_1
	global milliGAT_S
	global milliGAT_E
	global milliGAT_C
	global milliGAT_M
	global milliGAT_D
	global milliGAT_U

	initialize_valves()
	initialize_milliGAT()
	
	reaction_1()
	reaction_2()
	reaction_3()
	third_step_dissolve_product()
	rotaVap_wash_Acetone1()
	reaction_4_and_1_to_3()
	third_step_dissolve_product()
	rotaVap_wash_Acetone1()
	reaction_4()

	autoprog_abort()
#endcmd
#abort
def autoprog_abort():
	valve_1.close()
	valve_2.close()
	valve_3.close()
	valve_4.close()
	valve_5.close()
	valve_6.close()
	valve_7.close()
	valve_8.close()
	valve_9.close()
	valve_10.close()
	valve_11.close()
	valve_12.close()
	valve_13.close()
	valve_14.close()
	valve_15.close()
	valve_16.close()
	valve_17.close()
	valve_18.close()
	valve_19.close()
	relay_1.close()	
	watson_1.close()
	watson_2.close()
	watson_3.close()
	oushisheng_1.close()
	sf10_1.close()
	milliGAT_S.close('S')
	milliGAT_E.close('E')
	milliGAT_C.close('C')
	milliGAT_M.close('M')
	milliGAT_D.close('D')
	milliGAT_U.close('U')
	rotaVap_1.close()

#endabort
#label
lbl_0 = tk.Label(fr_cmdInt, width = 75, text = 'initialize_valves', anchor = 'w', justify = tk.LEFT)
lbl_0.pack()
lbl_1 = tk.Label(fr_cmdInt, width = 75, text = 'initialize_milliGAT', anchor = 'w', justify = tk.LEFT)
lbl_1.pack()
lbl_2 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVao_10min_200to75mbar', anchor = 'w', justify = tk.LEFT)
lbl_2.pack()
lbl_3 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVao_20min_200to75mbar', anchor = 'w', justify = tk.LEFT)
lbl_3.pack()
lbl_4 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVap_colletion', anchor = 'w', justify = tk.LEFT)
lbl_4.pack()
lbl_5 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVap_wash_Acetone3', anchor = 'w', justify = tk.LEFT)
lbl_5.pack()
lbl_6 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVap_wash_Acetone1', anchor = 'w', justify = tk.LEFT)
lbl_6.pack()
lbl_7 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVap_move_waste', anchor = 'w', justify = tk.LEFT)
lbl_7.pack()

lbl_8 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_preparation', anchor = 'w', justify = tk.LEFT)
lbl_8.pack()
lbl_9 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_reaction', anchor = 'w', justify = tk.LEFT)
lbl_9.pack()
lbl_10 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_wash_tubing', anchor = 'w', justify = tk.LEFT)
lbl_10.pack()
lbl_11 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_filtration', anchor = 'w', justify = tk.LEFT)
lbl_11.pack()
lbl_12 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_wash_filtration', anchor = 'w', justify = tk.LEFT)
lbl_12.pack()
lbl_13 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_final_cleaning', anchor = 'w', justify = tk.LEFT)
lbl_13.pack()
lbl_14 = tk.Label(fr_cmdInt, width = 75, text = 'second_step_preparation', anchor = 'w', justify = tk.LEFT)
lbl_14.pack()
lbl_15 = tk.Label(fr_cmdInt, width = 75, text = 'second_step_reaction', anchor = 'w', justify = tk.LEFT)
lbl_15.pack()
lbl_16 = tk.Label(fr_cmdInt, width = 75, text = 'second_step_wash_tubing', anchor = 'w', justify = tk.LEFT)
lbl_16.pack()
lbl_17 = tk.Label(fr_cmdInt, width = 75, text = 'second_step_filtration', anchor = 'w', justify = tk.LEFT)
lbl_17.pack()
lbl_18 = tk.Label(fr_cmdInt, width = 75, text = 'second_step_wash_filtration', anchor = 'w', justify = tk.LEFT)
lbl_18.pack()
lbl_19 = tk.Label(fr_cmdInt, width = 75, text = 'second_step_final_cleaning', anchor = 'w', justify = tk.LEFT)
lbl_19.pack()
lbl_20 = tk.Label(fr_cmdInt, width = 75, text = 'second_step_recrystallization', anchor = 'w', justify = tk.LEFT)
lbl_20.pack()
lbl_21 = tk.Label(fr_cmdInt, width = 75, text = 'second_step_dissolve_product', anchor = 'w', justify = tk.LEFT)
lbl_21.pack()

lbl_22 = tk.Label(fr_cmdInt, width = 75, text = 'third_step_reaction_and_separation', anchor = 'w', justify = tk.LEFT)
lbl_22.pack()
lbl_23 = tk.Label(fr_cmdInt, width = 75, text = 'third_step_transfer_for_FC', anchor = 'w', justify = tk.LEFT)
lbl_23.pack()
lbl_24 = tk.Label(fr_cmdInt, width = 75, text = 'third_step_FC_purge', anchor = 'w', justify = tk.LEFT)
lbl_24.pack()
lbl_25 = tk.Label(fr_cmdInt, width = 75, text = 'third_step_FC', anchor = 'w', justify = tk.LEFT)
lbl_25.pack()
lbl_26 = tk.Label(fr_cmdInt, width = 75, text = 'third_step_clean_colum', anchor = 'w', justify = tk.LEFT)
lbl_26.pack()
lbl_27 = tk.Label(fr_cmdInt, width = 75, text = 'third_step_dissolve_product', anchor = 'w', justify = tk.LEFT)
lbl_27.pack()

lbl_28 = tk.Label(fr_cmdInt, width = 75, text = 'fourth_step_preparation', anchor = 'w', justify = tk.LEFT)
lbl_28.pack()
lbl_29 = tk.Label(fr_cmdInt, width = 75, text = 'fourth_step_reaction', anchor = 'w', justify = tk.LEFT)
lbl_29.pack()
#endlabel
#timeline
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
#endtimeline
frame.btn_start['command']=lambda:threading.Thread(target=autoprog_start, name='StartThread').start()
frame.btn_abort['command']=lambda:threading.Thread(target=autoprog_abort, name='StartThread').start()
frame.btn_init['command']=lambda:threading.Thread(target=autoprog_init, name='StartThread').start()
frame.window.mainloop()
