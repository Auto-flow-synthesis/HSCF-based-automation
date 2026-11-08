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
* **Operating System:** Windows 11 22H2 (64-bit; build 22621)
* **Python Version:** 3.8.6 (64-bit)
* **Python Dependencies:** The complete list of 29 installed packages and their exact versions is provided in [requirements.txt](requirements.txt).

### Main Python Packages

| Package | Version |
| --- | --- |
| `matplotlib` | `3.7.5` |
| `mttkinter` | `0.6.1` |
| `numpy` | `1.24.4` |
| `pandas` | `2.0.3` |
| `pandastable` | `0.13.1` |
| `pyserial` | `3.5` |
| `PyVISA` | `1.14.1` |
| `requests` | `2.32.3` |
| `urllib3` | `2.2.2` |

### Non-standard Hardware
* The software is specifically designed to control laboratory automation hardware. For detailed hardware specifications and setup, please refer to **Supplementary Information Section 6**.
* Detailed descriptions of the device-control functions, parameter definitions, and GUI operation are provided in **Supplementary Section 7, Table S19, and Figs. S66–S67**. The device-specific COM port assignments and rotary-evaporator network addresses are listed in **Table S21** for brexpiprazole, **Table S24** for esonarimod, and **Table S28** for benzoxazinone derivatives.

---

## 3. Installation Guide

### Instructions
1.  **Install Python:** Ensure Python 3.8.6 (64-bit) is installed and selected in your terminal.
2.  **Download Repository:** Download this repository and extract the files to a local folder.
3.  **Install Dependencies:** Open a terminal in the repository folder and run the following command to install the recorded package versions:
    ```powershell
    python -m pip install -r requirements.txt
    ```
4.  **Hardware Connection:** Connect all laboratory hardware devices to your computer.
5.  **COM Port Configuration:**
    * Open **Windows Device Manager**.
    * Identify and note the assigned COM port numbers (e.g., `COM1`, `COM2`) for each device.
    * Configure these COM port numbers in the workflow editor or in `autoprog_init()` of the selected synthesis script.
6.  **Rotary Evaporator Configuration:** Set `self.BASE_URL` in `rotaVapFn.py` to the network address of the connected instrument. Configure the instrument-specific username and password using the Windows user environment variables `HSCF_ROTAVAP_USERNAME` and `HSCF_ROTAVAP_PASSWORD`. Restart the terminal after setting these variables so that the program can read them.

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
* After **1 minute**, the script sends a command selecting valve **position 2** and then closes the connection. Confirm the physical valve position; the script does not set an initial position of 1.

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