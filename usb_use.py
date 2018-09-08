import usb.core
import usb.backend.libusb1
import os
import sys
import subprocess

class USB():
    def __init__(self):
        print("Init class")

    def calculate(self, a, b):
        wynik = a + b
        print(wynik)

    def check_modules(self, backend=usb.backend.libusb1):
        print("Checking USB module")
        """dev = usb.core.find(find_all=True, backend=usb.backend.libusb1)
        a = next(dev)
        print(a)"""
        description_of_usb_devices = subprocess.check_output(['powershell.exe',' gwmi Win32_USBControllerDevice |%{[wmi]($_.Dependent)} | Sort Description | ft Description -auto'], shell=True)
        serial_numbers_of_usb_devices = subprocess.check_output(['powershell.exe',' gwmi Win32_USBControllerDevice |%{[wmi]($_.Dependent)} | Sort DeviceID | ft DeviceID -auto'], shell=True)
        usb_devices = [description_of_usb_devices.decode("cp437"), serial_numbers_of_usb_devices.decode("cp437")]
        print(usb_devices[0])
        print(usb_devices[1])