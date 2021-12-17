import tkinter as tk
import os

uid = os.getuid()

if uid != 0 :
    print('You must be root')
    exit()

win = tk.Tk()
win.title('KAL1T00lz')
win.minsize(height=300,width=300)
win.configure(bg='lightblue')
win.resizable(False,False)


def aircrack():
    os.system("xterm -e sudo apt install -y airckrack-ng")

def burpsuite():
    os.system("sudo xterm -e wget https://github.com/K4L1T00lz/Burpinstall/releases/download/burpsuite/burpsuite.sh && sudo bash burpsuite.sh")

def crackmapexec():
    os.system("sudo xterm -e sudo pip install pipx && sudo xterm -e pipx ensurepath && sudo xterm -e pipx install crackmapexec")

def hydra():
    os.system("xterm -e sudo apt install -y hydra")

def john():
    os.system("xterm -e sudo apt install -y john")

def metasploit():
    os.system("xterm -e curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && xterm -e ./msfinstall")

def nmap():
    os.system("xterm -e wget https://nmap.org/dist/nmap-7.92-1.x86_64.rpm && sudo xterm -e sudo alien -v nmap-7.92-1.x86_64.rpm && sudo xterm -e sudo dpkg --install nmap_7.92-2_amd64.deb ")

def airgeddon():
    os.system("xterm -e wget https://raw.githubusercontent.com/K4L1T00lz/airgeddoninstall/main/airgeddoninstall.sh && sudo chmod +x airgeddoninstall.sh && sudo xterm -e sudo bash airgeddoninstall.sh ")

def sqlmap():
    os.system("xterm -e wget https://raw.githubusercontent.com/K4L1T00lz/sqlmapinstall/main/sqlmapinstall.sh && sudo chmod +x sqlmapinstall.sh && sudo xterm -e sudo bash sqlmapinstall.sh")

def wireshark():
    os.system("xterm -e sudo apt install wireshark")

def nikto():
    os.system("xterm -e wget https://raw.githubusercontent.com/K4L1T00lz/niktoinstall/main/niktoinstall.sh && sudo chmod +x niktoinstall.sh && sudo bash niktoinstall.sh")

def hashcat():
    os.system("xterm -e sudo apt install -y hashcat")

def seclists():
    os.system("xterm -e sudo git clone --depth 1 https://github.com/danielmiessler/SecLists.git /seclists")

def bully():
    os.system("xterm -e sudo apt install bully")

def bettercap():
    os.system("xterm -e go get -u github.com/bettercap/bettercap && sudo mv go/bin/bettercap /usr/bin/bettercap")


bt1 = tk.Button(text='Airckrack-ng',bg='#189AB4',command = lambda : aircrack(),height=4,width=10).grid(column=1,row=1)

bt2 = tk.Button(text='Burpsuite',bg='#189AB4',command = lambda : burpsuite(),height=4,width=10).grid(column=2,row=1)

bt3 = tk.Button(text='Crackmapexec',bg='#189AB4',command = lambda : crackmapexec(),height=4,width=10).grid(column=3,row=1)

bt4 = tk.Button(text='Hydra',bg='#189AB4',command = lambda : hydra(),height=4,width=10).grid(column=3,row=3)

bt5 = tk.Button(text='John',bg='#189AB4',command = lambda : john(),height=4,width=10).grid(column=1,row=4)

bt6 = tk.Button(text='Metasploit',bg='#189AB4',command = lambda : metasploit(),height=4,width=10).grid(column=2,row=4)

bt7 = tk.Button(text='Nmap',bg='#189AB4',command = lambda : nmap(),height=4,width=10).grid(column=3,row=4)

bt8 = tk.Button(text='Airgeddon',bg='#189AB4',command = lambda : airgeddon(),height=4,width=10).grid(column=1,row=5)

bt9 = tk.Button(text='SqlMap',bg='#189AB4',command = lambda : sqlmap(),height=4,width=10).grid(column=2,row=5)

bt10 = tk.Button(text='Wireshark',bg='#189AB4',command = lambda : wireshark(),height=4,width=10).grid(column=3,row=5)

bt11 = tk.Button(text='Nikto',bg='#189AB4',command = lambda : nikto(),height=4,width=10).grid(column=1,row=6)

bt12 = tk.Button(text='Hashcat',bg='#189AB4',command = lambda : hashcat(),height=4,width=10).grid(column=2,row=6)

bt13 = tk.Button(text='Seclists',bg='#189AB4',command = lambda : seclists(),height=4,width=10).grid(column=3,row=6)

bt14 = tk.Button(text='Bullly',bg='#189AB4',command = lambda : bully(),height=4,width=10).grid(column=2,row=3)

bt15 = tk.Button(text='Bettercap',bg='#189AB4',command = lambda : bettercap(),height=4,width=10).grid(column=1,row=3)

win.mainloop()