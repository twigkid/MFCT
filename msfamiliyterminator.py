import psutil
from time import sleep

msFamilyProc = { # all processes to look for
    "wpcMon.exe",
}

def getProc(): # returns all running processes with their pid [0] and their name [1]
    allProc = []
    procList = psutil.process_iter()
    for proc in procList:
        allProc.append(proc)
    
    return allProc

def terminateProc(): # searches through all processes and kills all ms familiy related processes from a list
    allProc = getProc()
    killed = False
    while True:
        for proc in allProc:
            procName = str.lower(proc.name())
            if procName in msFamilyProc:
                proc.kill()
                killed = True
                print(f"killed: {procName}")
        
        if not killed:
            sleep(0.5)
        else:
            break    

    print("terminate sequence complete")
    
