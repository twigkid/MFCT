#ms familiy terminator
# tgkd 03/03/26

import os

def runterm(): # run the ms fam terminator
    import msfamiliyterminator
    msfamiliyterminator.terminateProc()

if __name__ == "__main__":
    try:
        runterm()
    except ImportError: # catch incase psutil wasnt installed
        os.system("pip install psutil")
        runterm()
