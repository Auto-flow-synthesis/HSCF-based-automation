import requests
from requests.auth import HTTPBasicAuth
import traceback
import tkinter as tk
import urllib3
import time
import os
from tkinter import messagebox
import pyvisa

class rotaVapFn:
    # urllib3.disable_warnings()
    def __init__(self):
        self.BASE_URL = "https://169.254.73.96/api/v1"
        self.USERNAME = "rw"
        self.PASSWORD = "ckUNAUNN"
        self.auth = (self.USERNAME, self.PASSWORD)
        self.session = requests.Session()
        self.rootcert = 'path/to/root.crt'
        self.info_endpoint = self.BASE_URL + "/info"

        # Set username and password
        self.session.auth = ('rw', 'ckUNAUNN')
        
        # Disable the certificate
        if os.path.isfile(self.rootcert):
            self.session.verify = self.rootcert
        else:
            self.session.verify = False
    
    #initiate and check connection status
    def rotavap_init(self, num, lbl_init):
        lbl_init["text"] += "Connect to RotaVap %d successfully\n" %num
        # urllib3.disable_warnings()
        url = f"{self.BASE_URL}/settings"
        #initialize the HTTP connection
        
        self.session.get(url)

        # Verify instruments
        info_resp = self.session.get(self.info_endpoint)
        if info_resp.status_code != 200:
            raise Exception("Unexpected status code when getting device info", info_resp.status_code)
        info_msg = info_resp.json()
        system_name = info_msg["systemName"]
        print(f"Connected to {system_name}")
        if info_msg["systemClass"] != "Rotavapor":
            raise Exception(f"This is not a Rotavapor")

    # Adjust temperature
    def heating(self, tarTemp, status, lbl):
        try:
            url = f"{self.BASE_URL}/process"
            payload = {
                'heating':{
                "set": tarTemp,
                "running": status
                }}
            self.session.put(url, json=payload)
            # response = requests.post(url, json=payload, auth=HTTPBasicAuth(USERNAME, PASSWORD))
            # return response.json()
        except:
            tk.messagebox.showinfo("Warning", traceback.format_exc())


    # Adjust speed
    def rotation_speed(self, rotSpeed, status, waitTime, lbl):
        time.sleep(waitTime)
        try:
            url = f"{self.BASE_URL}/process"
            payload = {
                'rotation':{
                "set": rotSpeed,
                "running": status
            }}

            self.session.put(url, json=payload)
            # response = requests.post(url, json=payload, auth=HTTPBasicAuth(USERNAME, PASSWORD))
            # return response.json()
        except:
            print("Warning", traceback.format_exc())

    def lift_height(self, lHeight, lbl):
        
        try:
            url = f"{self.BASE_URL}/process"
            payload = {
                'lift':{
                "set": lHeight}
            }
            self.session.put(url, json=payload)

        except:
            tk.messagebox.showinfo("Warning", traceback.format_exc())

    def vacuum_P(self, pressure, valve_status,waitTime, lbl):
        url = f"{self.BASE_URL}/process"
        payload = {
            'vacuum':{
            "set": pressure,
            "aerateValveOpen": valve_status,
            "aerateValvePulse": False
        }}
        
        self.session.put(url, json=payload)
        time.sleep(waitTime)
        # response = requests.post(url, json=payload, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        # return response.json()

    def Global_status(self, status, waitTime, lbl):
        time.sleep(waitTime)
        url = f"{self.BASE_URL}/process"
        payload = {
            'globalStatus':{
            "running": status
        }}
        self.session.put(url, json=payload)

    def close(self):
        self.rotation_speed(0, False,0)
        self.vacuum_P(1000, False,0)
        #stop pumping and rotation

if __name__ == "__main__":
    rotavap_1=rotaVapFn()
    rotavap_1.lift_height(0)
    # rotavap_1.vacuum_P(500, False, False)
    # rotavap_1.rotation_speed(100, False, 1)
    # rotavap_1.heating(50, True)
    # rotavap_1.global_status(True)
    # rotavap_1.rotation_speed(0, False, 0)
    


