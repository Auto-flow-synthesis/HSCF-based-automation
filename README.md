1.	Overview
Auto-flow-synthesis is a Python-based graphical software platform developed for controlling and orchestrating automated multistep chemical synthesis systems.
The software provides a graphical user interface (GUI) for: configuring experimental parameters, executing predefined synthesis workflows, and controlling laboratory hardware devices, including pumps, valves, rotary evaporators, and relay modules.
This software is designed for academic research use in flow chemistry, reaction automation, and self-driving laboratory systems.

2.	System requirements
All software dependencies and operating systems
	Operating system: Windows 10 (64-bit)
	Python: 3.10
	Required Python packages: mttkinter, pyserial, numpy, pandas, matplotlib, tkinter
Versions of the software have been tested on
	Windows 10 (64-bit) with Python 3.10
Non-standard hardware
	The software is designed to control laboratory automation hardware, For detailed information, see Supplementary Information Section 6

3.	Installation guide
Instructions
	Install Python 3.10 (64-bit)
	Download this repository and extract it to a local folder
	Install required Python packages
	Connect the hardware devices
	Open Windows Device Manager and check the assigned COM port numbers for each connected device, (e.g., COM1, COM2).
	Configure the corresponding COM port numbers in the software GUI or python file to match the device settings.
Typical install time on a "normal" desktop computer
	Approximately 10 minutes on a standard desktop computer with an existing Python installation.

4.	Demo (Valve)
Instructions to run on data
	Connect the valve to the computer via the serial interface
	Open Windows Device Manager and set the COM port of the valve device to *COM1*
	Run the python file “demo_valve.py”
	Click “Initialize” to establish the connection with the valve
	After successful connection, click “Start” to begin the demo
Expected output
	The valve is successfully connected and initialized
	After 1 minute, the valve switches from channel 1 (initial position) to channel 2
Expected run time for demo on a "normal" desktop computer
	Approximately 1–2 minutes

5.	Instructions for Use
How to run the software on your data
	Connect all required hardware devices (e.g., pumps, valves, rotary evaporator, relay modules) to the computer.
	Configure the COM port for each device in Windows Device Manager.
	Run the corresponding automated synthesis workflow, for example: Automated synthesis of Esonarimod.py
	Click Initialize to establish connections with all devices
	After successful initialization, click Start to begin the automated synthesis workflow

6.	License
This project is covered under the Apache 2.0 License.
