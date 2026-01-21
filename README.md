# Auto-flow-synthesis

## 1. Overview
**Auto-flow-synthesis** is a Python-based graphical software platform developed for controlling and orchestrating automated multistep chemical synthesis systems.

The software provides a graphical user interface (GUI) for:
* **Configuring** experimental parameters.
* **Executing** predefined synthesis workflows.
* **Controlling** laboratory hardware devices, including pumps, valves, rotary evaporators, and relay modules.

This software is designed for academic research use in flow chemistry, reaction automation, and self-driving laboratory systems.

---

## 2. System Requirements

### Operating System & Environment
* **Operating System:** Windows 10 (64-bit)
* **Python Version:** 3.10
* **Required Python Packages:** 
    * `matplotlib`
    * `mttkinter`
    * `numpy`
    * `pandas`
    * `pandastable`
    * `pyserial`
    * `pyvisa`
    

### Tested Configurations
* The software has been tested on **Windows 10 (64-bit)** with **Python 3.10**.

### Non-standard Hardware
* The software is specifically designed to control laboratory automation hardware. For detailed hardware specifications and setup, please refer to **Supplementary Information Section 6**.

---

## 3. Installation Guide

### Instructions
1.  **Install Python:** Ensure Python 3.10 (64-bit) is installed on your system.
2.  **Download Repository:** Download this repository and extract the files to a local folder.
3.  **Install Dependencies:** Run the following command to install the required packages:
    ```bash
    pip install mttkinter pyserial numpy pandas matplotlib
    ```
4.  **Hardware Connection:** Connect all laboratory hardware devices to your computer.
5.  **COM Port Configuration:** * Open **Windows Device Manager**.
    * Identify and note the assigned COM port numbers (e.g., `COM1`, `COM2`) for each device.
    * Configure these COM port numbers in the software GUI or the corresponding Python configuration file.

### Typical Install Time
* Approximately **10 minutes** on a standard desktop computer with an existing Python installation.

---

## 4. Demo (Valve Control)

### Instructions to Run
1.  Connect the valve to the computer via the serial interface.
2.  In **Windows Device Manager**, ensure the valve's COM port is set to `COM1`.
3.  Execute the demo script:
    ```bash
    python demo_valve.py
    ```
4.  Click the **"Initialize"** button in the GUI to establish a connection.
5.  Once connected, click **"Start"** to begin the demo.

### Expected Output
* The GUI confirms the valve is successfully connected and initialized.
* After **1 minute**, the valve physically switches from **Channel 1** (initial position) to **Channel 2**.

### Expected Run Time
* Approximately **1–2 minutes**.

---

## 5. Instructions for Use

### Running Automated Workflows
1.  **Hardware Setup:** Connect all required devices (pumps, valves, rotary evaporator, relay modules).
2.  **Port Mapping:** Ensure all COM ports are correctly configured in Windows Device Manager and the software settings.
3.  **Launch Workflow:** Run the specific automated synthesis script, for example:
    ```bash
    python "Automated synthesis of Esonarimod.py"
    ```
4.  **Initialization:** Click **Initialize** to establish communication with all hardware.
5.  **Execution:** After successful initialization, click **Start** to begin the automated synthesis process.

---

## 6. License
This project is licensed under the **Apache 2.0 License**.
