import tkinter
import time
import serial


class relayFn:

    relay = serial.Serial
    
    lbl_relay_sta = tkinter.Label
    
    status = {1: False, 2: False, 3: False, 4: False}

    def relay_init(self, COM, num, lbl_init, baudrate=9600, timeout=1):
        """Initialize relay connection"""
        try:
            self.relay = serial.Serial(
                port=COM,
                baudrate=baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=timeout
            )
            lbl_init["text"] += "Connect to Relay %d successfully\n" % num
            
        except:
            lbl_init["text"] += "Fail to find Relay %d \n" % num

    def relay_lbl_update(self, value, lbl):
        """Update relay label with timestamp and color"""
        lbl["text"] = time.strftime("%Y-%m-%d %H:%M:%S\n\t", time.localtime()) + lbl["text"]
        
        if value:
            lbl.configure(bg="#B0C4DE")  # Light blue for success
        else:
            lbl.configure(bg="red")      # Red for failure

    def relay_go(self, timeEntry, relay_num, state, lbl):
        """
        Control single relay after time delay
        timeEntry: delay time in minutes
        relay_num: relay number (1-4)
        state: True (ON) or False (OFF)
        lbl: label to update
        """
        try:
            # Wait for specified time
            time.sleep(timeEntry * 60)
            state = True if state == "1" else False
            # Send relay command
            relay_byte = relay_num.to_bytes(1, 'big')
            state_byte = b'\x01' if state else b'\x00'
            checksum = 0xA0 + relay_num + (1 if state else 0)
            checksum_byte = checksum.to_bytes(1, 'big')
            command = b'\xA0' + relay_byte + state_byte + checksum_byte
            
            self.relay.write(command)
            time.sleep(0.1)
            
            # Update status
            self.status[relay_num] = state
            
            # Update GUI
            self.relay_lbl_update(True, lbl)
            state_text = "ON" if state else "OFF"
            self.lbl_relay_sta["text"] = ("Current Relay %d: %s" % (relay_num, state_text))
            
        except:
            self.relay_lbl_update(False, lbl)

    def relay_set_single(self, relay_num, state):
        """
        Set single relay immediately without delay
        relay_num: 1-4
        state: True (ON) or False (OFF)
        """
        try:
            relay_byte = relay_num.to_bytes(1, 'big')
            state_byte = b'\x01' if state else b'\x00'
            checksum = 0xA0 + relay_num + (1 if state else 0)
            checksum_byte = checksum.to_bytes(1, 'big')
            command = b'\xA0' + relay_byte + state_byte + checksum_byte
            
            self.relay.write(command)
            time.sleep(0.1)
            self.status[relay_num] = state
            return True
            
        except:
            return False

    def relay_set_all(self, state):
        """
        Set all relays to same state
        state: True (ON) or False (OFF)
        """
        success = True
        for relay_num in range(1, 5):
            if not self.relay_set_single(relay_num, state):
                success = False
        return success

    def write(self, cmd):
        self.relay.write(cmd)

    def read(self):
        return self.relay.read()

    def close(self):
        if self.relay and self.relay.is_open:
            self.relay.close()

# # Initialize
# relay_controller = relayFn()
# relay_controller.relay_init('COM3', 1, init_label)

# # Control with delay (like valve_go)
# relay_controller.relay_go(2, 1, True, status_label)  # Turn ON relay 1 after 2 minutes

# # Immediate control
# relay_controller.relay_set_single(2, False)  # Turn OFF relay 2 immediately

# # Control all relays
# relay_controller.relay_set_all(True)  # Turn ON all relays