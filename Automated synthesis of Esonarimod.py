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
relay_1=relayFn()
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
milliGAT_A=milliGATFn()
milliGAT_E=milliGATFn()
watson_1=watsonFn()
watson_2=watsonFn()
watson_3=watsonFn()
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
	global relay_1
	relay_1.relay_init('COM17', 1, frame.lbl_init)
	global milliGAT_A
	milliGAT_A.milliGAT_init('COM12', 'A', frame.lbl_init)
	global milliGAT_E
	milliGAT_E.milliGAT_init('COM13', 'E', frame.lbl_init)
	global watson_1
	watson_1.watson_init('COM14', 1, frame.lbl_init)
	global watson_2
	watson_2.watson_init('COM15', 2, frame.lbl_init)
	global watson_3
	watson_3.watson_init('COM16', 3, frame.lbl_init)
	global rotaVap_1
	rotaVap_1.rotaVap_init('1', frame.lbl_init)

# cmd for global initialize
def initialize_valves():
	valve_1.valve_go(0.005, "1", lbl_0)
	valve_2.valve_go(0.005, "1", lbl_0)
	valve_3.valve_go(0.005, "1", lbl_0)
	valve_4.valve_go(0.005, "1", lbl_0)
	valve_5.valve_go(0.005, "1", lbl_0)
	valve_6.valve_go(0.005, "1", lbl_0)
	valve_7.valve_go(0.005, "1", lbl_0)
	valve_8.valve_go(0.005, "1", lbl_0)
	valve_9.valve_go(0.005, "1", lbl_0)
	valve_10.valve_go(0.005, "1", lbl_0)
	valve_11.valve_go(0.005, "1", lbl_0)
def initialize_milliGAT():
	milliGAT_A.milliGAT_pumping('A', 0.005, 10000.00, lbl_1)
	milliGAT_A.milliGAT_stoping('A', 0.005, lbl_1)
	milliGAT_E.milliGAT_pumping('E', 0.005, 10000.00, lbl_1)
	milliGAT_E.milliGAT_stoping('E', 0.005, lbl_1)
	
# cmd for global operation	
def rotaVao_20min_200to75mbar():
	valve_9.valve_go(0.00, "4", lbl_2)
	valve_10.valve_go(0.00, "4", lbl_2)
	valve_11.valve_go(0.00, "2", lbl_2)
	rotaVap_1.Global_status(True, 0.00, lbl_2)
	rotaVap_1.lift_height(220, lbl_2)
	rotaVap_1.heating(50, True, lbl_2)
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_2)
	rotaVap_1.vacuum_P(75, True, 0.00,  lbl_2)
	valve_8.valve_go(0.00, "8", lbl_2)
	valve_8.valve_go(10.00, "7", lbl_2)
	valve_8.valve_go(10.00, "6", lbl_2)
	valve_11.valve_go(0.00, "1", lbl_2)
	rotaVap_1.Global_status(False, 0.00, lbl_2)
	rotaVap_1.heating(20, True, lbl_2)
def rotaVao_10min_200to75mbar():
	valve_9.valve_go(0.00, "4", lbl_3)
	valve_10.valve_go(0.00, "4", lbl_3)
	valve_11.valve_go(0.00, "2", lbl_3)
	rotaVap_1.Global_status(True, 0.00, lbl_3)
	rotaVap_1.lift_height(220, lbl_3)
	rotaVap_1.heating(50, True, lbl_3)
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_3)
	rotaVap_1.vacuum_P(75, True, 0.00,  lbl_3)
	valve_8.valve_go(0.00, "8", lbl_3)
	valve_8.valve_go(5.00, "7", lbl_3)
	valve_8.valve_go(5.00, "6", lbl_3)
	valve_11.valve_go(0.00, "1", lbl_3)
	rotaVap_1.Global_status(False, 0.00, lbl_3)
	rotaVap_1.heating(20, True, lbl_3)
def rotaVap_colletion():
	valve_9.valve_go(0.00, "1", lbl_4)
	valve_10.valve_go(0.00, "1", lbl_4)
	rotaVap_1.rotation_speed(80, True, 0.00,  lbl_4)
	watson_3.watson_pumping('RL', 0.00, 1000.0, lbl_4)
	watson_3.watson_pumping('RL', 0.30, 1.0, lbl_4)
	rotaVap_1.rotation_speed(00, True, 0.00,  lbl_4)
	valve_9.valve_go(0.00, "4", lbl_4)
	valve_10.valve_go(0.00, "4", lbl_4)
	valve_11.valve_go(0.00, "2", lbl_4)
	rotaVap_1.Global_status(True, 0.00, lbl_4)
	rotaVap_1.heating(50, True, lbl_4)
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_4)
	rotaVap_1.vacuum_P(250, True, 0.00,  lbl_4)
	valve_8.valve_go(0.00, "8", lbl_4)
	valve_8.valve_go(4.70, "6", lbl_4)
	valve_11.valve_go(0.00, "1", lbl_4)
	rotaVap_1.Global_status(False, 0.00, lbl_4)
	rotaVap_1.heating(20, True, lbl_4)
def rotaVap_wash_Acetone3():
	rotaVap_1.rotation_speed(80, True, 0.00,  lbl_5)
	watson_3.watson_pumping('RL', 0.00, 1000.0, lbl_5)
	# round 1    # time 2.3 min
	valve_9.valve_go(0.00, "1", lbl_5)
	valve_10.valve_go(0.00, "1", lbl_5)
	valve_9.valve_go(0.30, "4", lbl_5)
	valve_10.valve_go(0.00, "1", lbl_5)
	valve_9.valve_go(1.00, "2", lbl_5)
	valve_10.valve_go(0.00, "2", lbl_5)
	valve_11.valve_go(0.00, "2", lbl_5)
	valve_9.valve_go(1.00, "1", lbl_5)
	valve_10.valve_go(0.00, "1", lbl_5)
	# round 2    # time 2.3 min
	valve_9.valve_go(0.00, "1", lbl_5)
	valve_10.valve_go(0.00, "1", lbl_5)
	valve_9.valve_go(0.30, "4", lbl_5)
	valve_10.valve_go(0.00, "1", lbl_5)
	valve_9.valve_go(1.00, "2", lbl_5)
	valve_10.valve_go(0.00, "2", lbl_5)
	valve_11.valve_go(0.00, "2", lbl_5)
	valve_9.valve_go(1.00, "1", lbl_5)
	valve_10.valve_go(0.00, "1", lbl_5)
	# round 3    # time 2.4 min
	valve_9.valve_go(0.00, "1", lbl_5)
	valve_10.valve_go(0.00, "1", lbl_5)
	valve_9.valve_go(0.30, "4", lbl_5)
	valve_10.valve_go(0.00, "1", lbl_5)
	valve_9.valve_go(1.00, "2", lbl_5)
	valve_10.valve_go(0.00, "2", lbl_5)
	valve_11.valve_go(0.00, "2", lbl_5)
	valve_9.valve_go(1.00, "1", lbl_5)
	valve_10.valve_go(0.00, "1", lbl_5)
	# round x    # time 5 min
	valve_9.valve_go(0.00, "3", lbl_5)
	valve_10.valve_go(0.00, "2", lbl_5)
	watson_3.watson_pumping('RL', 5.00, 1.0, lbl_5)
	rotaVap_1.rotation_speed(0, True, 0.00,  lbl_5)
	# rotoVap for 2 min
	valve_9.valve_go(0.00, "4", lbl_5)
	valve_10.valve_go(0.00, "4", lbl_5)
	valve_11.valve_go(0.00, "2", lbl_5)
	valve_8.valve_go(0.00, "8", lbl_5)
	rotaVap_1.Global_status(True, 0.00, lbl_5)
	rotaVap_1.heating(50, True, lbl_5)
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_5)
	rotaVap_1.vacuum_P(50, True, 0.00,  lbl_5)
	valve_8.valve_go(2.00, "6", lbl_5)
	valve_11.valve_go(0.00, "1", lbl_5)
	rotaVap_1.Global_status(False, 0.00, lbl_5)
	rotaVap_1.heating(20, True, lbl_5)
def rotaVap_wash_Acetone1():
	rotaVap_1.rotation_speed(80, True, 0.00,  lbl_6)
	watson_3.watson_pumping('RL', 0.00, 1000.0, lbl_6)
	# round 1    # time 2.3 min
	valve_9.valve_go(0.00, "1", lbl_6)
	valve_10.valve_go(0.00, "1", lbl_6)
	valve_9.valve_go(0.30, "4", lbl_6)
	valve_10.valve_go(0.00, "1", lbl_6)
	valve_9.valve_go(1.00, "2", lbl_6)
	valve_10.valve_go(0.00, "2", lbl_6)
	valve_11.valve_go(0.00, "2", lbl_6)
	valve_9.valve_go(1.00, "1", lbl_6)
	valve_10.valve_go(0.00, "1", lbl_6)
	# round x    # time 5 min
	valve_9.valve_go(0.00, "3", lbl_6)
	valve_10.valve_go(0.00, "2", lbl_6)
	watson_3.watson_pumping('RL', 5.00, 1.0, lbl_6)
	rotaVap_1.rotation_speed(0, True, 0.00,  lbl_6)
	# rotoVap for 2 min
	valve_9.valve_go(0.00, "4", lbl_6)
	valve_10.valve_go(0.00, "4", lbl_6)
	valve_11.valve_go(0.00, "2", lbl_6)
	valve_8.valve_go(0.00, "8", lbl_6)
	rotaVap_1.Global_status(True, 0.00, lbl_6)
	rotaVap_1.heating(50, True, lbl_6)
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_6)
	rotaVap_1.vacuum_P(50, True, 0.00,  lbl_6)
	valve_8.valve_go(2.00, "6", lbl_6)
	valve_11.valve_go(0.00, "1", lbl_6)
	rotaVap_1.Global_status(False, 0.00, lbl_6)
	rotaVap_1.heating(20, True, lbl_6)
def rotaVap_move_waste():
	valve_9.valve_go(0.00, "3", lbl_7)
	valve_10.valve_go(0.00, "2", lbl_7)
	watson_3.watson_pumping('RL', 0.00, 1000.0, lbl_7)
	watson_3.watson_pumping('RL', 5.00, 1.0, lbl_7)
def rotaVap_drying():
	valve_9.valve_go(0.00, "4", lbl_8)
	valve_10.valve_go(0.00, "4", lbl_8)
	valve_11.valve_go(0.00, "2", lbl_8)
	rotaVap_1.Global_status(True, 0.00, lbl_8)
	rotaVap_1.lift_height(220, lbl_8)
	rotaVap_1.heating(50, True, lbl_8)
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_8)
	rotaVap_1.vacuum_P(10, True, 0.00,  lbl_8)
	valve_8.valve_go(0.00, "7", lbl_8)
	rotaVap_1.Global_status(False, 600.00, lbl_8)
	rotaVap_1.heating(20, True, lbl_8)

# cmd for reaction step 1	
def first_step_preparation():
	valve_1.valve_go(0.00, "1", lbl_9)
	valve_2.valve_go(0.00, "1", lbl_9)
	milliGAT_A.milliGAT_pumping('A', 0.00, 25000.00, lbl_9)
	valve_1.valve_go(3.00, "2", lbl_9)
	valve_1.valve_go(3.00, "3", lbl_9)
	milliGAT_A.milliGAT_stoping('A', 0.40, lbl_9)
def first_step_reaction():
	watson_1.watson_pumping('RL', 0.00, 1000.0, lbl_10)
	valve_3.valve_go(0.00, "2", lbl_10)
	valve_3.valve_go(120.00, "1", lbl_10)    # Reaction time 120 min
	watson_1.watson_pumping('RL', 2.00, 1.0, lbl_10)
def first_step_wash_tubing():
	# round 1
	valve_1.valve_go(0.00, "4", lbl_11)
	valve_2.valve_go(0.00, "1", lbl_11)
	milliGAT_A.milliGAT_pumping('A', 0.00, 25000.00, lbl_11)
	milliGAT_A.milliGAT_stoping('A', 4.00, lbl_11)
	watson_1.watson_pumping('RL', 0.00, 1000.0, lbl_11)
	valve_3.valve_go(0.00, "2", lbl_11)
	valve_3.valve_go(1.00, "1", lbl_11)
	watson_1.watson_pumping('RL', 2.00, 1.0, lbl_11)
	# round 2
	valve_1.valve_go(0.00, "4", lbl_11)
	valve_2.valve_go(0.00, "1", lbl_11)
	milliGAT_A.milliGAT_pumping('A', 0.00, 25000.00, lbl_11)
	milliGAT_A.milliGAT_stoping('A', 2.00, lbl_11)
	watson_1.watson_pumping('RL', 0.00, 1000.0, lbl_11)
	valve_3.valve_go(0.00, "2", lbl_11)
	valve_3.valve_go(1.00, "1", lbl_11)
	watson_1.watson_pumping('RL', 2.00, 1.0, lbl_11)
def first_step_liquid_liquid_separation():
	# round 1
	valve_1.valve_go(0.00, "5", lbl_12)
	valve_2.valve_go(0.00, "2", lbl_12)
	milliGAT_A.milliGAT_pumping('A', 0.00, 25000.00, lbl_12)
	milliGAT_A.milliGAT_stoping('A', 4.00, lbl_12)
	valve_1.valve_go(0.00, "8", lbl_12)
	valve_2.valve_go(0.00, "2", lbl_12)
	valve_8.valve_go(0.00, "1", lbl_12)
	milliGAT_A.milliGAT_pumping('A', 0.00, -25000.00, lbl_12)
	milliGAT_A.milliGAT_stoping('A', 20.00, lbl_12)
	# round 2
	valve_1.valve_go(0.00, "4", lbl_12)
	valve_2.valve_go(0.00, "2", lbl_12)
	milliGAT_A.milliGAT_pumping('A', 0.00, 25000.00, lbl_12)
	valve_1.valve_go(2.00, "5", lbl_12)
	valve_2.valve_go(0.00, "2", lbl_12)
	milliGAT_A.milliGAT_stoping('A', 2.00, lbl_12)
	valve_1.valve_go(0.00, "8", lbl_12)
	valve_2.valve_go(0.00, "2", lbl_12)
	valve_8.valve_go(0.00, "1", lbl_12)
	milliGAT_A.milliGAT_pumping('A', 0.00, -25000.00, lbl_12)
	milliGAT_A.milliGAT_stoping('A', 5.00, lbl_12) 
def first_step_precipitation():
	# start rotation and heating
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_13)
	rotaVap_1.lift_height(220, lbl_13)
	rotaVap_1.heating(60, True, lbl_13)
	# add EtOAc
	valve_1.valve_go(0.00, "4", lbl_13)
	valve_2.valve_go(0.00, "3", lbl_13)
	valve_8.valve_go(0.00, "3", lbl_13)
	milliGAT_A.milliGAT_pumping('A', 0.00, 15000.00, lbl_13)
	milliGAT_A.milliGAT_stoping('A', 1.00, lbl_13) 
	# after 5 min stop heating
	rotaVap_1.rotation_speed(50, True, 300.00, lbl_13) 
	rotaVap_1.lift_height(0, lbl_13)
	rotaVap_1.heating(20, True, lbl_13)
	# add Hexane
	valve_1.valve_go(0.00, "6", lbl_13)
	valve_2.valve_go(0.00, "3", lbl_13)
	valve_8.valve_go(0.00, "3", lbl_13)
	milliGAT_A.milliGAT_pumping('A', 0.00, 25000.00, lbl_13)
	milliGAT_A.milliGAT_stoping('A', 20.00, lbl_13)
	# stop rotation
	rotaVap_1.rotation_speed(0, True, 0.00,  lbl_13) 
	rotaVap_1.lift_height(0, lbl_13)
	rotaVap_1.heating(20, True, lbl_13)
	# move to waste
	valve_1.valve_go(0.00, "14", lbl_13)
	valve_2.valve_go(0.00, "3", lbl_13)
	valve_8.valve_go(0.00, "3", lbl_13)
	milliGAT_A.milliGAT_pumping('A', 0.00, -25000.00, lbl_13)
	milliGAT_A.milliGAT_stoping('A', 25.00, lbl_13)
def first_step_dissolve_product():
	# start rotation and heating
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_14)
	rotaVap_1.lift_height(220, lbl_14)
	rotaVap_1.heating(60, True, lbl_14)
	# add MeCN round 1
	valve_1.valve_go(0.00, "7", lbl_14)
	valve_2.valve_go(0.00, "3", lbl_14)
	valve_8.valve_go(0.00, "3", lbl_14)
	milliGAT_A.milliGAT_pumping('A', 0.00, 25000.00, lbl_14)
	milliGAT_A.milliGAT_stoping('A', 8.00, lbl_14) 
	# move MeCN round 1
	valve_1.valve_go(0.00, "10", lbl_14)
	valve_2.valve_go(0.00, "3", lbl_14)
	valve_8.valve_go(0.00, "3", lbl_14)
	milliGAT_A.milliGAT_pumping('A', 0.00, -25000.00, lbl_14)
	milliGAT_A.milliGAT_stoping('A', 12.00, lbl_14)
	# add MeCN round 2
	valve_1.valve_go(0.00, "7", lbl_14)
	valve_2.valve_go(0.00, "3", lbl_14)
	valve_8.valve_go(0.00, "3", lbl_14)
	milliGAT_A.milliGAT_pumping('A', 0.00, 25000.00, lbl_14)
	milliGAT_A.milliGAT_stoping('A', 4.00, lbl_14) 
	# move MeCN round 2
	valve_1.valve_go(0.00, "10", lbl_14)
	valve_2.valve_go(0.00, "3", lbl_14)
	valve_8.valve_go(0.00, "3", lbl_14)
	milliGAT_A.milliGAT_pumping('A', 0.00, -25000.00, lbl_14)
	milliGAT_A.milliGAT_stoping('A', 6.00, lbl_14) 
	# add MeCN round 3
	valve_1.valve_go(0.00, "7", lbl_14)
	valve_2.valve_go(0.00, "3", lbl_14)
	valve_8.valve_go(0.00, "3", lbl_14)
	milliGAT_A.milliGAT_pumping('A', 0.00, 25000.00, lbl_14)
	milliGAT_A.milliGAT_stoping('A', 4.00, lbl_14)
	# move MeCN round 3
	valve_1.valve_go(0.00, "10", lbl_14)
	valve_2.valve_go(0.00, "3", lbl_14)
	valve_8.valve_go(0.00, "3", lbl_14)
	milliGAT_A.milliGAT_pumping('A', 0.00, -25000.00, lbl_14)
	milliGAT_A.milliGAT_stoping('A', 6.00, lbl_14)
	# stop rotation and heating
	rotaVap_1.rotation_speed(0, True, 0.00,  lbl_14)
	rotaVap_1.lift_height(0, lbl_14)
	rotaVap_1.heating(20, True, lbl_14)

# cmd for reaction step 2	
def second_step_purge_argon():
	valve_7.valve_go(0.00, "2", lbl_15)
	valve_6.valve_go(0.00, "1", lbl_15)
	valve_6.valve_go(3.00, "2", lbl_15)
	valve_7.valve_go(3.00, "1", lbl_15)
def second_step_preparation():
	valve_4.valve_go(0.00, "1", lbl_16)
	valve_5.valve_go(0.00, "1", lbl_16)
	milliGAT_E.milliGAT_pumping('E', 0.00, 25000.00, lbl_16)
	valve_4.valve_go(3.00, "2", lbl_16)
	valve_4.valve_go(3.00, "3", lbl_16)
	milliGAT_E.milliGAT_stoping('E', 0.40, lbl_16)
def second_step_reaction():
	relay_1.relay_go(0.00, 1, "1", lbl_17)
	watson_2.watson_pumping('RL', 0.00, 1000.0, lbl_17)
	valve_6.valve_go(0.00, "2", lbl_17)
	valve_6.valve_go(1440.00, "1", lbl_17)
	watson_2.watson_pumping('RL', 2.00, 1.0, lbl_17)
	relay_1.relay_go(0.00, 1, "0", lbl_17)

# cmd for reaction
def reaction_1():
	first_step_preparation()
	first_step_reaction()
	first_step_wash_tubing()
	first_step_liquid_liquid_separation()
	rotaVao_20min_200to75mbar()
	rotaVap_colletion()
	first_step_precipitation()
	rotaVap_colletion()
	rotaVap_drying()
def reaction_2():
	second_step_purge_argon()
	second_step_preparation()
	second_step_reaction()
def reaction_1_and_2():
	thread1 = threading.Thread(target=reaction_1)
	thread2 = threading.Thread(target=reaction_2)
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()

#endinit
#cmd
def autoprog_start():
	global rotaVap_1
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
	global relay_1
	global milliGAT_A
	global milliGAT_E
	global watson_1
	global watson_2
	global watson_3

	initialize_valves()
	initialize_milliGAT()
	
	reaction_1()
	first_step_dissolve_product()
	rotaVap_wash_Acetone3()
	reaction_1_and_2()
	first_step_dissolve_product()
	rotaVap_wash_Acetone3()
	reaction_2()

	autoprog_abort()
#endcmd
#abort
def autoprog_abort():
	rotaVap_1.close()
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
	milliGAT_A.close("A")
	milliGAT_E.close("E")
	watson_1.close()
	watson_2.close()
	watson_3.close()
	relay_1.close()
#endabort
#label
lbl_0 = tk.Label(fr_cmdInt, width = 75, text = 'initialize_valves', anchor = 'w', justify = tk.LEFT)
lbl_0.pack()
lbl_1 = tk.Label(fr_cmdInt, width = 75, text = 'initialize_milliGAT', anchor = 'w', justify = tk.LEFT)
lbl_1.pack()
lbl_2 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVao_20min_200to75mbar', anchor = 'w', justify = tk.LEFT)
lbl_2.pack()
lbl_3 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVao_10min_200to75mbar', anchor = 'w', justify = tk.LEFT)
lbl_3.pack()
lbl_4 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVap_colletion', anchor = 'w', justify = tk.LEFT)
lbl_4.pack()
lbl_5 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVap_wash_Acetone3', anchor = 'w', justify = tk.LEFT)
lbl_5.pack()
lbl_6 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVap_wash_Acetone1', anchor = 'w', justify = tk.LEFT)
lbl_6.pack()
lbl_7 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVap_move_waste', anchor = 'w', justify = tk.LEFT)
lbl_7.pack()
lbl_8 = tk.Label(fr_cmdInt, width = 75, text = 'rotaVap_drying', anchor = 'w', justify = tk.LEFT)
lbl_8.pack()
lbl_9 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_preparation', anchor = 'w', justify = tk.LEFT)
lbl_9.pack()
lbl_10 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_reaction', anchor = 'w', justify = tk.LEFT)
lbl_10.pack()
lbl_11 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_wash_tubing', anchor = 'w', justify = tk.LEFT)
lbl_11.pack()
lbl_12 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_liquid_liquid_separation', anchor = 'w', justify = tk.LEFT)
lbl_12.pack()
lbl_13 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_precipitation', anchor = 'w', justify = tk.LEFT)
lbl_13.pack()
lbl_14 = tk.Label(fr_cmdInt, width = 75, text = 'first_step_dissolve_product', anchor = 'w', justify = tk.LEFT)
lbl_14.pack()
lbl_15 = tk.Label(fr_cmdInt, width = 75, text = 'second_step_purge_argon', anchor = 'w', justify = tk.LEFT)
lbl_15.pack()
lbl_16 = tk.Label(fr_cmdInt, width = 75, text = 'second_step_preparation', anchor = 'w', justify = tk.LEFT)
lbl_16.pack()
lbl_17 = tk.Label(fr_cmdInt, width = 75, text = 'second_step_reaction', anchor = 'w', justify = tk.LEFT)
lbl_17.pack()
#endlabel
#timeline
0
#endtimeline
frame.btn_start['command']=lambda:threading.Thread(target=autoprog_start, name='StartThread').start()
frame.btn_abort['command']=lambda:threading.Thread(target=autoprog_abort, name='StartThread').start()
frame.btn_init['command']=lambda:threading.Thread(target=autoprog_init, name='StartThread').start()
frame.window.mainloop()
