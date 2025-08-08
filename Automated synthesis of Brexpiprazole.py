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
watson_1=watsonFn()
heidolph_1=heidolphFn()
milliGAT_D=milliGATFn()
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
	global watson_1
	watson_1.watson_init('COM9', 1, frame.lbl_init)
	global heidolph_1
	heidolph_1.heidolph_init('COM10', 1, frame.lbl_init)
	global milliGAT_D
	milliGAT_D.milliGAT_init('COM13', 'D', frame.lbl_init)
	global rotaVap_1
	rotaVap_1.rotaVap_init('1', frame.lbl_init)
#endinit
#cmd
def autoprog_start():
	global valve_1
	global valve_2
	global valve_3
	global valve_4
	global valve_5
	global valve_6
	global valve_7
	global valve_8
	global watson_1
	global heidolph_1
	global milliGAT_D
	global rotaVap_1

	# initialize_valves
	valve_1.valve_go(0.00, "1", lbl_0)
	valve_2.valve_go(0.00, "1", lbl_1)
	valve_3.valve_go(0.00, "1", lbl_2)
	valve_4.valve_go(0.00, "1", lbl_3)
	valve_5.valve_go(0.00, "1", lbl_4)
	valve_6.valve_go(0.00, "1", lbl_5)
	valve_7.valve_go(0.00, "1", lbl_6)
	valve_8.valve_go(0.00, "1", lbl_7)

	# first_step_preparation
	valve_1.valve_go(0.00, "1", lbl_8)
	valve_2.valve_go(0.00, "2", lbl_9)
	valve_3.valve_go(0.00, "2", lbl_10)
	valve_4.valve_go(0.00, "4", lbl_11)
	valve_5.valve_go(0.00, "4", lbl_12)
	valve_6.valve_go(0.00, "1", lbl_13)
	valve_7.valve_go(0.00, "1", lbl_14)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_15)
	milliGAT_D.milliGAT_stoping('D', 6.00, lbl_16)
	
	# first_step_reaction
	# first_step_wash_tubing
	watson_1.watson_pumping('RL', 0.00, 1985.0, lbl_17)
	valve_1.valve_go(0.26, "2", lbl_18) 
	watson_1.watson_pumping('RL', 0.00, 1323.0, lbl_17)
	valve_1.valve_go(1440.00, "1", lbl_19) 
	watson_1.watson_pumping('RL', 5.00, 1.0, lbl_20) 
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_21)
	milliGAT_D.milliGAT_stoping('D', 4.00, lbl_22)
	watson_1.watson_pumping('RL', 0.00, 1323.0, lbl_23)
	valve_4.valve_go(5.00, "3", lbl_24)
	valve_5.valve_go(0.00, "3", lbl_25)
	valve_5.valve_go(0.74, "2", lbl_26)

	# first_step_precipitation
	valve_6.valve_go(0.00, "2", lbl_27)
	valve_7.valve_go(0.00, "5", lbl_28)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_29)
	milliGAT_D.milliGAT_stoping('D', 60.00, lbl_30) 
	valve_6.valve_go(0.00, "2", lbl_31)
	valve_7.valve_go(0.00, "6", lbl_32)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_33)
	milliGAT_D.milliGAT_stoping('D', 80.00, lbl_34) 
	valve_6.valve_go(0.00, "2", lbl_35)
	valve_7.valve_go(0.00, "5", lbl_36)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_37)
	milliGAT_D.milliGAT_stoping('D', 40.00, lbl_38) 
	valve_6.valve_go(0.00, "2", lbl_39)
	valve_7.valve_go(0.00, "6", lbl_40)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_41)
	milliGAT_D.milliGAT_stoping('D', 60.00, lbl_42) 
	watson_1.watson_pumping('RL', 0.00, 1.0, lbl_23)
	
	# first_step_transfer
	valve_6.valve_go(0.00, "2", lbl_43)
	valve_7.valve_go(0.00, "2", lbl_44)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_45)
	milliGAT_D.milliGAT_stoping('D', 5.00, lbl_46)
	valve_6.valve_go(0.00, "2", lbl_47)
	valve_7.valve_go(0.00, "7", lbl_48)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_49)
	milliGAT_D.milliGAT_stoping('D', 8.00, lbl_50) 
	valve_6.valve_go(0.00, "2", lbl_43)
	valve_7.valve_go(0.00, "2", lbl_44)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_45)
	milliGAT_D.milliGAT_stoping('D', 2.00, lbl_46)
	valve_6.valve_go(0.00, "2", lbl_47)
	valve_7.valve_go(0.00, "7", lbl_48)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_49)
	milliGAT_D.milliGAT_stoping('D', 4.00, lbl_50)
	
	# second_step_reaction
	# second_step_wash_tubing
	valve_1.valve_go(0.00, "1", lbl_52)
	valve_2.valve_go(0.00, "3", lbl_53)
	valve_3.valve_go(0.00, "3", lbl_54)
	valve_4.valve_go(0.00, "4", lbl_55)
	valve_5.valve_go(0.00, "4", lbl_56)
	valve_6.valve_go(0.00, "3", lbl_57)
	valve_7.valve_go(0.00, "2", lbl_58)
	valve_8.valve_go(0.00, "4", lbl_59)
	watson_1.watson_pumping('RL', 0.00, 1985.0, lbl_60)
	valve_1.valve_go(0.26, "2", lbl_61)
	watson_1.watson_pumping('RL', 0.00, 1323.0, lbl_23)
	valve_1.valve_go(150.00, "1", lbl_62) 
	watson_1.watson_pumping('RL', 5.00, 1.0, lbl_63)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_64)
	milliGAT_D.milliGAT_stoping('D', 4.00, lbl_65)
	watson_1.watson_pumping('RL', 0.00, 1323.0, lbl_66)
	valve_4.valve_go(5.00, "3", lbl_67)
	valve_5.valve_go(0.00, "3", lbl_68)
	valve_5.valve_go(0.74, "2", lbl_69)
	
	# rotary_evaporation
	valve_8.valve_go(0.00, "3", lbl_70)
	rotaVap_1.Global_status(True, 0.00, lbl_71)
	rotaVap_1.rotation_speed(80, True, 0.00,  lbl_72)
	rotaVap_1.vacuum_P(100, True, 0.00,  lbl_73)
	rotaVap_1.heating(40, True, lbl_74)
	rotaVap_1.lift_height(220, lbl_75)
	rotaVap_1.rotation_speed(0, True, 1200.00,  lbl_76) 
	rotaVap_1.vacuum_P(1000, True, 0.00,  lbl_77)
	rotaVap_1.heating(70, True, lbl_78)
	rotaVap_1.lift_height(0, lbl_79)
	valve_8.valve_go(0.00, "2", lbl_80)
	
	# second_step_quench
	valve_6.valve_go(0.00, "4", lbl_81)
	valve_7.valve_go(0.00, "4", lbl_82)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_84)
	valve_6.valve_go(10.00, "4", lbl_85)
	valve_7.valve_go(0.00, "5", lbl_86)
	rotaVap_1.rotation_speed(40, True, 0.00,  lbl_83)
	milliGAT_D.milliGAT_stoping('D', 10.00, lbl_87)
	valve_6.valve_go(30.00, "4", lbl_88)
	valve_7.valve_go(0.00, "6", lbl_89)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_90)
	milliGAT_D.milliGAT_stoping('D', 40.00, lbl_91)
	
	# second_step_precipitation
	valve_6.valve_go(0.00, "4", lbl_100)
	valve_7.valve_go(0.00, "3", lbl_101)
	rotaVap_1.lift_height(220, lbl_102)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_103)
	milliGAT_D.milliGAT_stoping('D', 1.0, lbl_104) 
	valve_6.valve_go(4.00, "4", lbl_105)      
	valve_7.valve_go(0.00, "6", lbl_106)
	rotaVap_1.lift_height(0, lbl_102)
	rotaVap_1.rotation_speed(0, True, 600.00,  lbl_76) 
	milliGAT_D.milliGAT_pumping('D', 20.00, -25000.00, lbl_107) 
	milliGAT_D.milliGAT_stoping('D', 5.00, lbl_108)
	
	# second_step_transfer
	rotaVap_1.rotation_speed(50, True, 0.00,  lbl_83) 
	rotaVap_1.lift_height(220, lbl_102)
	valve_6.valve_go(0.00, "4", lbl_109)
	valve_7.valve_go(0.00, "3", lbl_110)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_111)
	milliGAT_D.milliGAT_stoping('D', 6.00, lbl_112)
	valve_6.valve_go(0.00, "4", lbl_113)
	valve_7.valve_go(0.00, "8", lbl_114)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_116)
	milliGAT_D.milliGAT_stoping('D', 12.00, lbl_117) 
	valve_6.valve_go(0.00, "4", lbl_109)
	valve_7.valve_go(0.00, "3", lbl_110)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_111)
	milliGAT_D.milliGAT_stoping('D', 1.00, lbl_112)
	valve_6.valve_go(0.00, "4", lbl_113)
	valve_7.valve_go(0.00, "8", lbl_114)
	rotaVap_1.rotation_speed(0, True, 0.00,  lbl_115)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_116)
	milliGAT_D.milliGAT_stoping('D', 3.00, lbl_117)
	rotaVap_1.lift_height(0, lbl_102)
	rotaVap_1.heating(20, True, lbl_74)

	# third_step_preparation
	valve_1.valve_go(0.00, "1", lbl_118)
	valve_2.valve_go(0.00, "4", lbl_119)
	valve_3.valve_go(0.00, "2", lbl_120)
	valve_4.valve_go(0.00, "4", lbl_121)
	valve_5.valve_go(0.00, "4", lbl_122)
	valve_6.valve_go(0.00, "5", lbl_123)
	valve_7.valve_go(0.00, "3", lbl_124)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_116)
	valve_7.valve_go(0.20, "5", lbl_124)
	milliGAT_D.milliGAT_stoping('D', 7.80, lbl_117)
	heidolph_1.heidolph_rotating(0.00, 800.000000, lbl_125)
	heidolph_1.heidolph_heating(0.00, 80.000000, lbl_126)

	# third_step_reaction
	# third_step_wash_tubing
	watson_1.watson_pumping('RL', 0.00, 1985.0, lbl_127)
	valve_1.valve_go(0.26, "2", lbl_128)  #time
	watson_1.watson_pumping('RL', 0.00, 1323.0, lbl_23)
	valve_1.valve_go(600.00, "1", lbl_129)  #time
	watson_1.watson_pumping('RL', 5.00, 1.0, lbl_130)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_131)
	milliGAT_D.milliGAT_stoping('D', 4.00, lbl_132)
	watson_1.watson_pumping('RL', 0.00, 1323.0, lbl_133)
	heidolph_1.heidolph_heating(0.00, 25.000000, lbl_134)
	watson_1.watson_pumping('RL', 5.74, 1.0, lbl_135)
	
	# third_step_precipitation
	valve_6.valve_go(0.00, "2", lbl_123)
	valve_7.valve_go(0.00, "5", lbl_124)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_107)
	milliGAT_D.milliGAT_stoping('D', 10.00, lbl_132)
	valve_6.valve_go(0.00, "2", lbl_123)
	valve_7.valve_go(0.00, "6", lbl_124)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_107)
	milliGAT_D.milliGAT_stoping('D', 30.00, lbl_132)
	valve_6.valve_go(0.00, "2", lbl_123)
	valve_7.valve_go(0.00, "5", lbl_124)
	milliGAT_D.milliGAT_pumping('D', 0.00, 25000.00, lbl_107)
	milliGAT_D.milliGAT_stoping('D', 10.00, lbl_132)
	valve_6.valve_go(0.00, "2", lbl_123)
	valve_7.valve_go(0.00, "6", lbl_124)
	milliGAT_D.milliGAT_pumping('D', 0.00, -25000.00, lbl_107)
	milliGAT_D.milliGAT_stoping('D', 20.00, lbl_132)
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
	watson_1.close()
	heidolph_1.close()
	milliGAT_D.close("D")
	rotaVap_1.close()
#endabort
#label
lbl_0 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 1 goes to position 1, total time usage 0.00', anchor = 'w', justify = tk.LEFT)
lbl_0.pack()
lbl_1 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 2 goes to position 1, total time usage 0.00', anchor = 'w', justify = tk.LEFT)
lbl_1.pack()
lbl_2 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 3 goes to position 1, total time usage 0.00', anchor = 'w', justify = tk.LEFT)
lbl_2.pack()
lbl_3 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 4 goes to position 1, total time usage 0.00', anchor = 'w', justify = tk.LEFT)
lbl_3.pack()
lbl_4 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 5 goes to position 1, total time usage 0.00', anchor = 'w', justify = tk.LEFT)
lbl_4.pack()
lbl_5 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 6 goes to position 1, total time usage 0.00', anchor = 'w', justify = tk.LEFT)
lbl_5.pack()
lbl_6 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 1, total time usage 0.00', anchor = 'w', justify = tk.LEFT)
lbl_6.pack()
lbl_7 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 8 goes to position 1, total time usage 0.00', anchor = 'w', justify = tk.LEFT)
lbl_7.pack()
lbl_8 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 1 goes to position 1, total time usage 0.10', anchor = 'w', justify = tk.LEFT)
lbl_8.pack()
lbl_9 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 2 goes to position 2, total time usage 0.10', anchor = 'w', justify = tk.LEFT)
lbl_9.pack()
lbl_10 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 3 goes to position 2, total time usage 0.10', anchor = 'w', justify = tk.LEFT)
lbl_10.pack()
lbl_11 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 4 goes to position 4, total time usage 0.10', anchor = 'w', justify = tk.LEFT)
lbl_11.pack()
lbl_12 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 5 goes to position 4, total time usage 0.10', anchor = 'w', justify = tk.LEFT)
lbl_12.pack()
lbl_13 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 6 goes to position 1, total time usage 0.10', anchor = 'w', justify = tk.LEFT)
lbl_13.pack()
lbl_14 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 1, total time usage 0.10', anchor = 'w', justify = tk.LEFT)
lbl_14.pack()
lbl_15 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at 25000 ul/min, total time usage 0.20 min', anchor = 'w', justify = tk.LEFT)
lbl_15.pack()
lbl_16 = tk.Label(fr_cmdInt, width = 75, text = 'After 8.00 min, MilliGAT D stops, total time usage 8.20', anchor = 'w', justify = tk.LEFT)
lbl_16.pack()
lbl_17 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Watson Marlow 1 direction RL pumps at 1323.0 RPM, total time usage 8.30', anchor = 'w', justify = tk.LEFT)
lbl_17.pack()
lbl_18 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.42 min, Valve 1 goes to position 2, total time usage 8.72', anchor = 'w', justify = tk.LEFT)
lbl_18.pack()
lbl_19 = tk.Label(fr_cmdInt, width = 75, text = 'After 1200.00 min, Valve 1 goes to position 1, total time usage 1208.72', anchor = 'w', justify = tk.LEFT)
lbl_19.pack()
lbl_20 = tk.Label(fr_cmdInt, width = 75, text = 'After 5.00 min, Watson Marlow 1 direction RL pumps at 1.0 RPM, total time usage 1213.72', anchor = 'w', justify = tk.LEFT)
lbl_20.pack()
lbl_21 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at 25000 ul/min, total time usage 1213.82 min', anchor = 'w', justify = tk.LEFT)
lbl_21.pack()
lbl_22 = tk.Label(fr_cmdInt, width = 75, text = 'After 2.00 min, MilliGAT D stops, total time usage 1215.82', anchor = 'w', justify = tk.LEFT)
lbl_22.pack()
lbl_23 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Watson Marlow 1 direction RL pumps at 1323.0 RPM, total time usage 1215.92', anchor = 'w', justify = tk.LEFT)
lbl_23.pack()
lbl_24 = tk.Label(fr_cmdInt, width = 75, text = 'After 5.00 min, Valve 4 goes to position 3, total time usage 1220.92', anchor = 'w', justify = tk.LEFT)
lbl_24.pack()
lbl_25 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 5 goes to position 3, total time usage 1220.92', anchor = 'w', justify = tk.LEFT)
lbl_25.pack()
lbl_26 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.30 min, Valve 5 goes to position 2, total time usage 1221.22', anchor = 'w', justify = tk.LEFT)
lbl_26.pack()
lbl_27 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 2, total time usage 1221.32', anchor = 'w', justify = tk.LEFT)
lbl_27.pack()
lbl_28 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 5, total time usage 1221.32', anchor = 'w', justify = tk.LEFT)
lbl_28.pack()
lbl_29 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at 25000 ul/min, total time usage 1221.42 min', anchor = 'w', justify = tk.LEFT)
lbl_29.pack()
lbl_30 = tk.Label(fr_cmdInt, width = 75, text = 'After 30.00 min, MilliGAT D stops, total time usage 1251.42', anchor = 'w', justify = tk.LEFT)
lbl_30.pack()
lbl_31 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 2, total time usage 1251.52', anchor = 'w', justify = tk.LEFT)
lbl_31.pack()
lbl_32 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 6, total time usage 1251.52', anchor = 'w', justify = tk.LEFT)
lbl_32.pack()
lbl_33 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at -25000 ul/min, total time usage 1251.62 min', anchor = 'w', justify = tk.LEFT)
lbl_33.pack()
lbl_34 = tk.Label(fr_cmdInt, width = 75, text = 'After 40.00 min, MilliGAT D stops, total time usage 1291.62', anchor = 'w', justify = tk.LEFT)
lbl_34.pack()
lbl_35 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 2, total time usage 1291.72', anchor = 'w', justify = tk.LEFT)
lbl_35.pack()
lbl_36 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 5, total time usage 1291.72', anchor = 'w', justify = tk.LEFT)
lbl_36.pack()
lbl_37 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at 25000 ul/min, total time usage 1291.82 min', anchor = 'w', justify = tk.LEFT)
lbl_37.pack()
lbl_38 = tk.Label(fr_cmdInt, width = 75, text = 'After 30.00 min, MilliGAT D stops, total time usage 1321.82', anchor = 'w', justify = tk.LEFT)
lbl_38.pack()
lbl_39 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 2, total time usage 1321.92', anchor = 'w', justify = tk.LEFT)
lbl_39.pack()
lbl_40 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 6, total time usage 1321.92', anchor = 'w', justify = tk.LEFT)
lbl_40.pack()
lbl_41 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at -25000 ul/min, total time usage 1322.02 min', anchor = 'w', justify = tk.LEFT)
lbl_41.pack()
lbl_42 = tk.Label(fr_cmdInt, width = 75, text = 'After 40.00 min, MilliGAT D stops, total time usage 1362.02', anchor = 'w', justify = tk.LEFT)
lbl_42.pack()
lbl_43 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 2, total time usage 1362.12', anchor = 'w', justify = tk.LEFT)
lbl_43.pack()
lbl_44 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 2, total time usage 1362.12', anchor = 'w', justify = tk.LEFT)
lbl_44.pack()
lbl_45 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at 25000 ul/min, total time usage 1362.22 min', anchor = 'w', justify = tk.LEFT)
lbl_45.pack()
lbl_46 = tk.Label(fr_cmdInt, width = 75, text = 'After 8.00 min, MilliGAT D stops, total time usage 1370.22', anchor = 'w', justify = tk.LEFT)
lbl_46.pack()
lbl_47 = tk.Label(fr_cmdInt, width = 75, text = 'After 5.00 min, Valve 6 goes to position 2, total time usage 1375.22', anchor = 'w', justify = tk.LEFT)
lbl_47.pack()
lbl_48 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 7, total time usage 1375.22', anchor = 'w', justify = tk.LEFT)
lbl_48.pack()
lbl_49 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at -25000 ul/min, total time usage 1375.32 min', anchor = 'w', justify = tk.LEFT)
lbl_49.pack()
lbl_50 = tk.Label(fr_cmdInt, width = 75, text = 'After 16.00 min, MilliGAT D stops, total time usage 1391.32', anchor = 'w', justify = tk.LEFT)
lbl_50.pack()
lbl_51 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Watson Marlow 1 direction RL pumps at 1.0 RPM, total time usage 1391.42', anchor = 'w', justify = tk.LEFT)
lbl_51.pack()
lbl_52 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 1 goes to position 1, total time usage 1391.52', anchor = 'w', justify = tk.LEFT)
lbl_52.pack()
lbl_53 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 2 goes to position 3, total time usage 1391.52', anchor = 'w', justify = tk.LEFT)
lbl_53.pack()
lbl_54 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 3 goes to position 3, total time usage 1391.52', anchor = 'w', justify = tk.LEFT)
lbl_54.pack()
lbl_55 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 4 goes to position 4, total time usage 1391.52', anchor = 'w', justify = tk.LEFT)
lbl_55.pack()
lbl_56 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 5 goes to position 4, total time usage 1391.52', anchor = 'w', justify = tk.LEFT)
lbl_56.pack()
lbl_57 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 6 goes to position 3, total time usage 1391.52', anchor = 'w', justify = tk.LEFT)
lbl_57.pack()
lbl_58 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 2, total time usage 1391.52', anchor = 'w', justify = tk.LEFT)
lbl_58.pack()
lbl_59 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 8 goes to position 4, total time usage 1391.52', anchor = 'w', justify = tk.LEFT)
lbl_59.pack()
lbl_60 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Watson Marlow 1 direction RL pumps at 1323.0 RPM, total time usage 1391.62', anchor = 'w', justify = tk.LEFT)
lbl_60.pack()
lbl_61 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.42 min, Valve 1 goes to position 2, total time usage 1392.04', anchor = 'w', justify = tk.LEFT)
lbl_61.pack()
lbl_62 = tk.Label(fr_cmdInt, width = 75, text = 'After 240.00 min, Valve 1 goes to position 1, total time usage 1632.04', anchor = 'w', justify = tk.LEFT)
lbl_62.pack()
lbl_63 = tk.Label(fr_cmdInt, width = 75, text = 'After 5.00 min, Watson Marlow 1 direction RL pumps at 1.0 RPM, total time usage 1637.04', anchor = 'w', justify = tk.LEFT)
lbl_63.pack()
lbl_64 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at 25000 ul/min, total time usage 1637.14 min', anchor = 'w', justify = tk.LEFT)
lbl_64.pack()
lbl_65 = tk.Label(fr_cmdInt, width = 75, text = 'After 2.00 min, MilliGAT D stops, total time usage 1639.14', anchor = 'w', justify = tk.LEFT)
lbl_65.pack()
lbl_66 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Watson Marlow 1 direction RL pumps at 1323.0 RPM, total time usage 1639.24', anchor = 'w', justify = tk.LEFT)
lbl_66.pack()
lbl_67 = tk.Label(fr_cmdInt, width = 75, text = 'After 5.00 min, Valve 4 goes to position 3, total time usage 1644.24', anchor = 'w', justify = tk.LEFT)
lbl_67.pack()
lbl_68 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 5 goes to position 3, total time usage 1644.24', anchor = 'w', justify = tk.LEFT)
lbl_68.pack()
lbl_69 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.30 min, Valve 5 goes to position 2, total time usage 1644.54', anchor = 'w', justify = tk.LEFT)
lbl_69.pack()
lbl_70 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 8 goes to position 3, total time usage 1644.64', anchor = 'w', justify = tk.LEFT)
lbl_70.pack()
lbl_71 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Globalstatus start, total time usage 1644.64', anchor = 'w', justify = tk.LEFT)
lbl_71.pack()
lbl_72 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, rotary vaporator start to rotate at 50 rpm, total time usage 1644.74', anchor = 'w', justify = tk.LEFT)
lbl_72.pack()
lbl_73 = tk.Label(fr_cmdInt, width = 75, text = 'Rotary vaporator start to vacuum at 125 mbar, stop after 0.00 min, total time usage 1644.74', anchor = 'w', justify = tk.LEFT)
lbl_73.pack()
lbl_74 = tk.Label(fr_cmdInt, width = 75, text = 'adjust temperature to 40 ', anchor = 'w', justify = tk.LEFT)
lbl_74.pack()
lbl_75 = tk.Label(fr_cmdInt, width = 75, text = 'Lift flask for 220 mm', anchor = 'w', justify = tk.LEFT)
lbl_75.pack()
lbl_76 = tk.Label(fr_cmdInt, width = 75, text = 'After 20.00 min, rotary vaporator start to rotate at 0 rpm, total time usage 1664.74', anchor = 'w', justify = tk.LEFT)
lbl_76.pack()
lbl_77 = tk.Label(fr_cmdInt, width = 75, text = 'Rotary vaporator start to vacuum at 1000 mbar, stop after 0.00 min, total time usage 1664.74', anchor = 'w', justify = tk.LEFT)
lbl_77.pack()
lbl_78 = tk.Label(fr_cmdInt, width = 75, text = 'adjust temperature to 60 ', anchor = 'w', justify = tk.LEFT)
lbl_78.pack()
lbl_79 = tk.Label(fr_cmdInt, width = 75, text = 'Lift flask for 0 mm', anchor = 'w', justify = tk.LEFT)
lbl_79.pack()
lbl_80 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 8 goes to position 2, total time usage 1664.74', anchor = 'w', justify = tk.LEFT)
lbl_80.pack()
lbl_81 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 4, total time usage 1664.84', anchor = 'w', justify = tk.LEFT)
lbl_81.pack()
lbl_82 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 4, total time usage 1664.84', anchor = 'w', justify = tk.LEFT)
lbl_82.pack()
lbl_83 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, rotary vaporator start to rotate at 50 rpm, total time usage 1664.84', anchor = 'w', justify = tk.LEFT)
lbl_83.pack()
lbl_84 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at 25000 ul/min, total time usage 1664.94 min', anchor = 'w', justify = tk.LEFT)
lbl_84.pack()
lbl_85 = tk.Label(fr_cmdInt, width = 75, text = 'After 10.00 min, Valve 6 goes to position 4, total time usage 1674.94', anchor = 'w', justify = tk.LEFT)
lbl_85.pack()
lbl_86 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 5, total time usage 1674.94', anchor = 'w', justify = tk.LEFT)
lbl_86.pack()
lbl_87 = tk.Label(fr_cmdInt, width = 75, text = 'After 20.00 min, MilliGAT D stops, total time usage 1694.94', anchor = 'w', justify = tk.LEFT)
lbl_87.pack()
lbl_88 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 4, total time usage 1695.04', anchor = 'w', justify = tk.LEFT)
lbl_88.pack()
lbl_89 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 6, total time usage 1695.04', anchor = 'w', justify = tk.LEFT)
lbl_89.pack()
lbl_90 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at -25000 ul/min, total time usage 1695.14 min', anchor = 'w', justify = tk.LEFT)
lbl_90.pack()
lbl_91 = tk.Label(fr_cmdInt, width = 75, text = 'After 40.00 min, MilliGAT D stops, total time usage 1735.14', anchor = 'w', justify = tk.LEFT)
lbl_91.pack()
lbl_92 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 4, total time usage 1735.24', anchor = 'w', justify = tk.LEFT)
lbl_92.pack()
lbl_93 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 5, total time usage 1735.24', anchor = 'w', justify = tk.LEFT)
lbl_93.pack()
lbl_94 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at 25000 ul/min, total time usage 1735.34 min', anchor = 'w', justify = tk.LEFT)
lbl_94.pack()
lbl_95 = tk.Label(fr_cmdInt, width = 75, text = 'After 20.00 min, MilliGAT D stops, total time usage 1755.34', anchor = 'w', justify = tk.LEFT)
lbl_95.pack()
lbl_96 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 4, total time usage 1755.44', anchor = 'w', justify = tk.LEFT)
lbl_96.pack()
lbl_97 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 6, total time usage 1755.44', anchor = 'w', justify = tk.LEFT)
lbl_97.pack()
lbl_98 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at -25000 ul/min, total time usage 1755.54 min', anchor = 'w', justify = tk.LEFT)
lbl_98.pack()
lbl_99 = tk.Label(fr_cmdInt, width = 75, text = 'After 40.00 min, MilliGAT D stops, total time usage 1795.54', anchor = 'w', justify = tk.LEFT)
lbl_99.pack()
lbl_100 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 4, total time usage 1795.64', anchor = 'w', justify = tk.LEFT)
lbl_100.pack()
lbl_101 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 1, total time usage 1795.64', anchor = 'w', justify = tk.LEFT)
lbl_101.pack()
lbl_102 = tk.Label(fr_cmdInt, width = 75, text = 'Lift flask for 220 mm', anchor = 'w', justify = tk.LEFT)
lbl_102.pack()
lbl_103 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at 25000 ul/min, total time usage 1795.74 min', anchor = 'w', justify = tk.LEFT)
lbl_103.pack()
lbl_104 = tk.Label(fr_cmdInt, width = 75, text = 'After 6.00 min, MilliGAT D stops, total time usage 1801.74', anchor = 'w', justify = tk.LEFT)
lbl_104.pack()
lbl_105 = tk.Label(fr_cmdInt, width = 75, text = 'After 5.00 min, Valve 6 goes to position 4, total time usage 1806.74', anchor = 'w', justify = tk.LEFT)
lbl_105.pack()
lbl_106 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 8, total time usage 1806.74', anchor = 'w', justify = tk.LEFT)
lbl_106.pack()
lbl_107 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at -25000 ul/min, total time usage 1806.84 min', anchor = 'w', justify = tk.LEFT)
lbl_107.pack()
lbl_108 = tk.Label(fr_cmdInt, width = 75, text = 'After 8.00 min, MilliGAT D stops, total time usage 1814.84', anchor = 'w', justify = tk.LEFT)
lbl_108.pack()
lbl_109 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 4, total time usage 1814.94', anchor = 'w', justify = tk.LEFT)
lbl_109.pack()
lbl_110 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 1, total time usage 1814.94', anchor = 'w', justify = tk.LEFT)
lbl_110.pack()
lbl_111 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at 25000 ul/min, total time usage 1815.04 min', anchor = 'w', justify = tk.LEFT)
lbl_111.pack()
lbl_112 = tk.Label(fr_cmdInt, width = 75, text = 'After 2.00 min, MilliGAT D stops, total time usage 1817.04', anchor = 'w', justify = tk.LEFT)
lbl_112.pack()
lbl_113 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 6 goes to position 4, total time usage 1817.14', anchor = 'w', justify = tk.LEFT)
lbl_113.pack()
lbl_114 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 8, total time usage 1817.14', anchor = 'w', justify = tk.LEFT)
lbl_114.pack()
lbl_115 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, rotary vaporator start to rotate at 0 rpm, total time usage 1817.14', anchor = 'w', justify = tk.LEFT)
lbl_115.pack()
lbl_116 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at -25000 ul/min, total time usage 1817.24 min', anchor = 'w', justify = tk.LEFT)
lbl_116.pack()
lbl_117 = tk.Label(fr_cmdInt, width = 75, text = 'After 6.00 min, MilliGAT D stops, total time usage 1823.24', anchor = 'w', justify = tk.LEFT)
lbl_117.pack()
lbl_118 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Valve 1 goes to position 1, total time usage 1823.34', anchor = 'w', justify = tk.LEFT)
lbl_118.pack()
lbl_119 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 2 goes to position 4, total time usage 1823.34', anchor = 'w', justify = tk.LEFT)
lbl_119.pack()
lbl_120 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 3 goes to position 4, total time usage 1823.34', anchor = 'w', justify = tk.LEFT)
lbl_120.pack()
lbl_121 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 4 goes to position 4, total time usage 1823.34', anchor = 'w', justify = tk.LEFT)
lbl_121.pack()
lbl_122 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 5 goes to position 4, total time usage 1823.34', anchor = 'w', justify = tk.LEFT)
lbl_122.pack()
lbl_123 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 6 goes to position 5, total time usage 1823.34', anchor = 'w', justify = tk.LEFT)
lbl_123.pack()
lbl_124 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Valve 7 goes to position 1, total time usage 1823.34', anchor = 'w', justify = tk.LEFT)
lbl_124.pack()
lbl_125 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Heidolph 1 rotates at 500 rpm, total time usage 1823.34', anchor = 'w', justify = tk.LEFT)
lbl_125.pack()
lbl_126 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.00 min, Heidolph 1 heats to 85 degree Celsius, total time usage 1823.34', anchor = 'w', justify = tk.LEFT)
lbl_126.pack()
lbl_127 = tk.Label(fr_cmdInt, width = 75, text = 'After 15.00 min, Watson Marlow 1 direction RL pumps at 1323.0 RPM, total time usage 1838.34', anchor = 'w', justify = tk.LEFT)
lbl_127.pack()
lbl_128 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.42 min, Valve 1 goes to position 2, total time usage 1838.76', anchor = 'w', justify = tk.LEFT)
lbl_128.pack()
lbl_129 = tk.Label(fr_cmdInt, width = 75, text = 'After 1200.00 min, Valve 1 goes to position 1, total time usage 3038.76', anchor = 'w', justify = tk.LEFT)
lbl_129.pack()
lbl_130 = tk.Label(fr_cmdInt, width = 75, text = 'After 5.00 min, Watson Marlow 1 direction RL pumps at 1.0 RPM, total time usage 3043.76', anchor = 'w', justify = tk.LEFT)
lbl_130.pack()
lbl_131 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, MilliGAT D pumps at 25000 ul/min, total time usage 3043.86 min', anchor = 'w', justify = tk.LEFT)
lbl_131.pack()
lbl_132 = tk.Label(fr_cmdInt, width = 75, text = 'After 2.00 min, MilliGAT D stops, total time usage 3045.86', anchor = 'w', justify = tk.LEFT)
lbl_132.pack()
lbl_133 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Watson Marlow 1 direction RL pumps at 1323.0 RPM, total time usage 3045.96', anchor = 'w', justify = tk.LEFT)
lbl_133.pack()
lbl_134 = tk.Label(fr_cmdInt, width = 75, text = 'After 0.10 min, Heidolph 1 heats to 25 degree Celsius, total time usage 3046.06', anchor = 'w', justify = tk.LEFT)
lbl_134.pack()
lbl_135 = tk.Label(fr_cmdInt, width = 75, text = 'After 5.00 min, Watson Marlow 1 direction RL pumps at 1.0 RPM, total time usage 3051.06', anchor = 'w', justify = tk.LEFT)
lbl_135.pack()
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
8
0
0
1200
5
0
2
0
5
0
0
0
0
0
30
0
0
0
40
0
0
0
30
0
0
0
40
0
0
0
8
5
0
0
16
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
240
5
0
2
0
5
0
0
0
0
0
0
20
0
0
0
0
0
0
10
0
20
0
0
0
40
0
0
0
20
0
0
0
40
0
0
0
6
5
0
0
8
0
0
0
2
0
0
0
0
6
0
0
0
0
0
0
0
0
0
15
0
1200
5
0
2
0
0
5
#endtimeline
frame.btn_start['command']=lambda:threading.Thread(target=autoprog_start, name='StartThread').start()
frame.btn_abort['command']=lambda:threading.Thread(target=autoprog_abort, name='StartThread').start()
frame.btn_init['command']=lambda:threading.Thread(target=autoprog_init, name='StartThread').start()
frame.window.mainloop()
