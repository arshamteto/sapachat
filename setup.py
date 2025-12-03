import os,time,sys,platform, urllib.request
systemguess = platform.system().lower()
syst = ["Linux","windows","Darwin(mac)"]
allowed = " ".join(syst) 
root = None
listener = None
limit = None
url = "https://raw.githubusercontent.com/arshamteto/sapa/refs/heads/main/bin.py" #bin
url2 = "https://raw.githubusercontent.com/arshamteto/sapa/refs/heads/main/start.py" #start
current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "bin.py")

current_folder2 = os.path.dirname(os.path.abspath(__file__))
file_path2 = os.path.join(current_folder, "start.py")
os.system('cls' if os.name == 'nt' else 'clear')
print("Running setup.py ...")
time.sleep(1)
def keyexit():
    system = platform.system().lower()
    print("Press any key to exit...")
    if system == "windows":
        import msvcrt
        msvcrt.getch()
    else:
        import tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
packages = [
    "Pillow"
]
time.sleep(2)
print("Downloading files...")


with urllib.request.urlopen(url2) as response:
    data2 = response.read()

with open(file_path2, "wb") as f:
    f.write(data2)
    print("downloaded start.py")
    time.sleep(1)
with urllib.request.urlopen(url) as response:
    data = response.read()
with open(file_path, "wb") as f:
    f.write(data)
    print("downloaded bin.py")
    time.sleep(1)
time.sleep(2)
print("done.")
time.sleep(1)
print("No Error Found.")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.6)
def wininstall():
    print
    pip_cmd = "pip"
    print(f"[+] Using: {pip_cmd}")
    for pkg in packages:
        print(f"[+] Installing {pkg} ...")
        os.system(f"{pip_cmd} install {pkg}")
        print("[+] Installation complete!")
        time.sleep(1)
        time.sleep(1)
def linuxinstall_def():
    print
    pip_cmd = "pip3"
    print(f"[+] Using: {pip_cmd}")
    for pkg in packages:
        print(f"[+] Installing {pkg} ...")
        os.system(f"{pip_cmd} install {pkg}")
        print("[+] Installation complete!")
        time.sleep(1)
        time.sleep(1)
        
        
def linuxinstall_venv():
    os.system("python3 -m venv venv")
    print("installed venv.")
    time.sleep(1)
    os.system("source vevn/bin/activate")
    time.sleep(1)
    print("venv activated.")
    time.sleep(1)
    pip_cmd = "pip3"
    print(f"[+] Using: {pip_cmd}")
    for pkg in packages:
        print(f"[+] Installing {pkg} ...")
        os.system(f"{pip_cmd} install {pkg}")
        print("[+] Installation complete!")
        time.sleep(1)
        time.sleep(1)
    
    
menutext = f'''sapa is only enabled on {allowed}
 this os is {systemguess}, | if not, choose your os.

                    1   =   WINDOWS
                    2   =   LINUX
                    3   =   macOS
    
'''
print(menutext)
oschoise = input("|> : ")
while True:
    if oschoise == '1':
        root = False
        break
    elif oschoise == '2':
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("are you okay with 'pip3' installing or you need venv?    1 = venv / 2 = not venv, install defualt ")
        askver = input("|> : ")
        if askver == '1':
            root = None
            break
        elif askver == '2':
            root = True
            break
        else:
            print("wrong input")
            time.sleep(1)
            continue
    elif oschoise == '3':
        root = False
        break
    else:
        print("wrong input. try again")
        time.sleep(1)
        continue
if root is False:
    wininstall()
elif root is True:
    linuxinstall_def()
elif root is None:
    linuxinstall_venv()

print()
print("you can run  'bin.py --help'   or   'start.py' (recommended)")
print()
time.sleep(3)
keyexit()